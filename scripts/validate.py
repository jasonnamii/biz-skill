#!/usr/bin/env python3
"""
biz-skill self-check validator.

evals/cases.json 로드 → 각 케이스의 기대 축/키워드를 기준으로
SKILL.md + references/ 구조가 해당 모드 파이프라인을 지원하는지 확인.

실제 LLM 매칭 실행은 세션 내 Claude가 수행하고, 이 스크립트는
구조적 회귀(파일 존재·섹션 존재·스포크 파일 존재)를 점검한다.

Exit 0 = PASS, Exit 1 = FAIL.
"""

import json
import sys
import re
from pathlib import Path


def load_cases(root: Path) -> dict:
    cases_path = root / "evals" / "cases.json"
    if not cases_path.exists():
        print(f"[FAIL] evals/cases.json not found")
        sys.exit(1)
    return json.loads(cases_path.read_text(encoding="utf-8"))


def check_structure(root: Path) -> list:
    """SKILL.md + references/ + scripts/ 구조 체크."""
    errors = []
    must_have = [
        "SKILL.md",
        "references/report-template.md",
        "references/narrative-template.md",
        "references/execution-pipeline.md",
        "references/axis-connection-map.md",
        "references/spoke-standard.md",
        "scripts/spoke_loader.py",
    ]
    for rel in must_have:
        if not (root / rel).exists():
            errors.append(f"missing: {rel}")
    return errors


def check_spoke_coverage(root: Path) -> list:
    """18축 스포크 파일 존재 체크 (느슨: 절반 이상이면 OK)."""
    axes = [
        "f1-market", "f2-bizmodel", "f3-moat", "f4-innovation",
        "g1-launch", "g2-growth", "g3-scaleup", "g4-global", "g5-platform",
        "s1-pivot", "s2-alliance", "s3-diversify", "s4-exit",
        "e1-org", "e2-capital", "e3-survival", "e4-regulation", "e5-timing",
    ]
    found = [a for a in axes if (root / "references" / f"{a}.md").exists()]
    errors = []
    if len(found) < len(axes) // 2:
        errors.append(
            f"spoke coverage too low: {len(found)}/{len(axes)}"
        )
    return errors


def check_skill_md_axes(root: Path, cases: dict) -> list:
    """SKILL.md에 18축 코드·3개 모드가 모두 언급되는지."""
    errors = []
    skill_md = (root / "SKILL.md").read_text(encoding="utf-8")
    modes_needed = ["진단", "전략", "판정"]
    for m in modes_needed:
        if m not in skill_md:
            errors.append(f"mode '{m}' not found in SKILL.md")
    # 축 코드 샘플 체크
    axis_codes = set()
    for case in cases.get("cases", []):
        axis_codes.update(case.get("expected_axes_primary", []))
    for code in axis_codes:
        # Korean-adjacent axis codes (e.g., F1시장) — use simple substring
        if code not in skill_md:
            errors.append(f"axis code '{code}' not found in SKILL.md")
    return errors


def check_output_keywords(root: Path, cases: dict) -> list:
    """각 케이스의 expected_output_contains가 execution-pipeline.md에 정의됐는지."""
    errors = []
    pipeline_path = root / "references" / "execution-pipeline.md"
    if not pipeline_path.exists():
        errors.append("execution-pipeline.md missing — cannot check output keywords")
        return errors
    pipeline = pipeline_path.read_text(encoding="utf-8")
    for case in cases.get("cases", []):
        for kw in case.get("expected_output_contains", []):
            if kw not in pipeline:
                errors.append(
                    f"[{case['id']}] keyword '{kw}' not in execution-pipeline.md"
                )
    return errors


def main():
    script_dir = Path(__file__).parent
    root = script_dir.parent  # biz-skill/

    print(f"=== biz-skill Self-Check ===")
    print(f"root: {root}")

    cases = load_cases(root)
    print(f"cases loaded: {len(cases.get('cases', []))}")

    all_errors = []
    all_errors += check_structure(root)
    all_errors += check_spoke_coverage(root)
    all_errors += check_skill_md_axes(root, cases)
    all_errors += check_output_keywords(root, cases)

    if all_errors:
        print(f"\n[FAIL] {len(all_errors)} errors:")
        for e in all_errors:
            print(f"  - {e}")
        sys.exit(1)
    else:
        print(f"\n[PASS] 구조 회귀 검증 통과. LLM 매칭 품질은 실세션에서 확인.")
        sys.exit(0)


if __name__ == "__main__":
    main()
