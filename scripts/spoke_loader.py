#!/usr/bin/env python3
"""
biz-skill 2단계 로딩 파서.

사용법:
  # 1단계: 스포크의 패턴명 목록만 추출 (토큰 절약)
  python spoke_loader.py scan references/f1-market.md

  # 2단계: 특정 패턴만 정독 추출
  python spoke_loader.py read references/f1-market.md "P1" "F2"

  # 전체 헤딩 구조 확인
  python spoke_loader.py headings references/f1-market.md
"""

import sys
import re
from pathlib import Path


def scan_patterns(filepath: str) -> str:
    """1단계 스캔: 성공·실패 패턴 라이브러리의 ### 패턴명만 추출."""
    path = Path(filepath)
    if not path.exists():
        return f"ERROR: {filepath} not found"

    lines = path.read_text(encoding="utf-8").splitlines()
    output = []
    current_section = None

    for line in lines:
        # ## 레벨 헤딩 추적
        if line.startswith("## "):
            heading = line.lstrip("# ").strip()
            if "성공 패턴" in heading or "실패 패턴" in heading:
                current_section = heading
                output.append(f"\n{'='*60}")
                output.append(f"  {heading}")
                output.append(f"{'='*60}")
            elif "패턴 쌍" in heading or "진단" in heading or "조건부" in heading or "축간" in heading:
                current_section = heading
                output.append(f"\n--- {heading} (별도 섹션)")
            else:
                current_section = None

        # ### 레벨 = 개별 패턴명
        elif line.startswith("### ") and current_section and ("패턴" in current_section):
            pattern_name = line.lstrip("# ").strip()
            output.append(f"  • {pattern_name}")

    if not output:
        return "WARNING: 표준 구조(성공 패턴 라이브러리/실패 패턴 라이브러리) 헤딩 미발견"

    return "\n".join(output)


def read_pattern(filepath: str, pattern_ids: list[str]) -> str:
    """2단계 정독: 지정된 패턴 ID가 포함된 ### 섹션 전문 추출."""
    path = Path(filepath)
    if not path.exists():
        return f"ERROR: {filepath} not found"

    lines = path.read_text(encoding="utf-8").splitlines()
    output = []
    capturing = False
    capture_depth = 0

    for i, line in enumerate(lines):
        # ### 레벨 패턴 시작 감지
        if line.startswith("### "):
            heading = line.lstrip("# ").strip()
            # 패턴 ID 매칭 (예: "P1", "F2", "패턴 1", "실패 패턴 2")
            matched = any(pid.lower() in heading.lower() for pid in pattern_ids)
            if matched:
                capturing = True
                capture_depth = line.index(line.lstrip()[0]) if line.lstrip() else 0
                output.append(f"\n{'─'*60}")
                output.append(line)
                continue
            elif capturing:
                # 다음 ### 패턴을 만나면 캡처 중단
                capturing = False
                output.append(f"{'─'*60}\n")

        # ## 레벨 만나면 캡처 중단
        if line.startswith("## ") and capturing:
            capturing = False
            output.append(f"{'─'*60}\n")

        if capturing:
            output.append(line)

    if capturing:
        output.append(f"{'─'*60}\n")

    if not output:
        return f"WARNING: 패턴 ID {pattern_ids}에 매칭되는 섹션 없음"

    return "\n".join(output)


def show_headings(filepath: str) -> str:
    """스포크의 전체 헤딩 구조를 트리 형태로 출력."""
    path = Path(filepath)
    if not path.exists():
        return f"ERROR: {filepath} not found"

    lines = path.read_text(encoding="utf-8").splitlines()
    output = [f"📄 {path.name}", ""]

    for i, line in enumerate(lines):
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            indent = "  " * (level - 1)
            heading = line.lstrip("# ").strip()
            output.append(f"L{i+1:>4} {indent}{heading}")

    return "\n".join(output)


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]
    filepath = sys.argv[2]

    if command == "scan":
        print(scan_patterns(filepath))
    elif command == "read":
        if len(sys.argv) < 4:
            print("ERROR: 'read' 명령에는 패턴 ID가 필요합니다")
            print("  예: python spoke_loader.py read references/f1-market.md P1 F2")
            sys.exit(1)
        pattern_ids = sys.argv[3:]
        print(read_pattern(filepath, pattern_ids))
    elif command == "headings":
        print(show_headings(filepath))
    else:
        print(f"ERROR: 알 수 없는 명령 '{command}'. scan/read/headings 중 선택")
        sys.exit(1)


if __name__ == "__main__":
    main()
