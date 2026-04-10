# 사업 전략 패턴 매칭 엔진

> 🇺🇸 [English README](./README.md)

**18축 패턴 매칭 기반 사업 전략 진단 엔진 — 성공 및 실패 대조사례로 전략 진단 및 설계.**

## 사전 요구사항

- **Claude Cowork 또는 Claude Code** 환경

## 목적

사업 전략은 일반적이면 안 됩니다. Biz-Skill은 실제 사업 상황을 18축(기반, 성장, 전략, 실행) 전반에 진단한 후 알려진 성공 및 실패 사례와 매칭시킵니다. 모든 권장사항은 대조사례와 함께 제시됩니다. 산출물은 서사적, 맥락 중심적, 증거 기반입니다.

## 사용 시점 및 방법

사업 맥락을 제공하세요: 달성하려는 목표, 현재 상황, 시장, 팀, 제약 조건. 스킬은 18축 전반을 매핑하고 증명된 성공 패턴 및 실패 모드와 매칭시키며, 위험 시나리오를 보여주는 대조사례를 함께 제시합니다.

## 사용 예시

| 상황 | 프롬프트 | 결과 |
|---|---|---|
| 매출 정체 | `"biz-skill: $5M ARR에서 정체. 수직 통합할지 수평 확장할지?"` | 18축 진단→성공 패턴→실패 대조사례 + 권장사항 |
| GTM 변경 | `"biz-skill: 직접 판매에서 제품 주도 성장으로 전환"` | 기반/성장/전략 진단→성공 패턴 (Figma)→실패 대조사례 |
| 가격 전략 | `"biz-skill: 가격 30% 인상 vs 엔터프라이즈 계층 추가?"` | 가격+포지셔닝 진단→성공 패턴→실패 대조사례 |

## 핵심 기능

- 18축 진단 프레임워크: 기반 (4), 성장 (5), 전략 (4), 실행 (5)
- 알려진 성공 및 실패 사례 패턴 매칭
- 필수 대조군 비교 — 항상 양쪽 제시
- 상황에 맞춘 서사적이고 맥락 중심적 산출물
- 산업 및 회사 단계 전반 적용

## 연관 스킬

- **[research-frame](https://github.com/jasonnamii/research-frame)** — 축 심화 조사
- **[financial-model](https://github.com/jasonnamii/financial-model)** — 숫자로 권장사항 검증
- **[bp-guide](https://github.com/jasonnamii/bp-guide)** — 투자자 대상 진단 구조화
- **[hit-skill](https://github.com/jasonnamii/hit-skill)** — 전략 내 인간 행동 요소 설계

## 설치

```bash
git clone https://github.com/jasonnamii/biz-skill.git ~/.claude/skills/biz-skill
```

## 업데이트

```bash
cd ~/.claude/skills/biz-skill && git pull
```

`~/.claude/skills/`에 배치된 스킬은 Claude Code 및 Cowork 세션에서 자동으로 사용할 수 있습니다.

## Cowork 스킬 생태계

25개 이상의 커스텀 스킬 중 하나입니다. 전체 카탈로그: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## 라이선스

MIT 라이선스 — 자유롭게 사용, 수정, 공유하세요.