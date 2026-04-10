# biz-skill

> 🇰🇷 [한국어 README](./README.ko.md)

**Business strategy diagnosis engine with 18-axis pattern matching — diagnose and design strategies using success and failure counter-examples.**

## Prerequisites

- **Claude Cowork or Claude Code** environment

## Goal

Business strategy shouldn't be generic. Biz-Skill diagnoses your actual business situation across 18 axes — Foundation, Growth, Strategy, and Execution — then matches patterns against known success and failure cases. Every recommendation pairs with a counter-example. Output is narrative, context-driven, and evidence-based.

## When & How to Use

Provide your business context: what you're trying to achieve, current situation, market, team, constraints. The skill maps across 18 axes and matches against proven success patterns and failure modes, with counter-examples showing risk scenarios.

## Use Cases

| Scenario | Prompt | What Happens |
|---|---|---|
| Revenue plateau | `"biz-skill: stuck at $5M ARR, keep vertical or expand horizontal?"` | 18-axis diagnosis→success pattern→failure counter-example + recommendation |
| GTM pivot | `"biz-skill: shift from direct sales to product-led growth"` | Foundation/Growth/Strategy diagnosis→success pattern (Figma)→failure counter-example |
| Pricing strategy | `"biz-skill: raise price 30% or add enterprise tier?"` | Diagnosis on pricing + positioning→success pattern→failure counter |

## Key Features

- 18-axis diagnostic framework: Foundation (4), Growth (5), Strategy (4), Execution (5)
- Pattern matching against known success and failure cases
- Mandatory control group comparison — always shows both sides
- Narrative and context-driven output tailored to your situation
- Works across industries and company stages

## Works With

- **[research-frame](https://github.com/jasonnamii/research-frame)** — deeper axis investigation
- **[financial-model](https://github.com/jasonnamii/financial-model)** — validates recommendations with numbers
- **[bp-guide](https://github.com/jasonnamii/bp-guide)** — structures diagnosis for investors
- **[hit-skill](https://github.com/jasonnamii/hit-skill)** — designs human-behavior elements within strategies

## Installation

```bash
git clone https://github.com/jasonnamii/biz-skill.git ~/.claude/skills/biz-skill
```

## Update

```bash
cd ~/.claude/skills/biz-skill && git pull
```

Skills placed in `~/.claude/skills/` are automatically available in Claude Code and Cowork sessions.

## Part of Cowork Skills

This is one of 25+ custom skills. See the full catalog: [github.com/jasonnamii/cowork-skills](https://github.com/jasonnamii/cowork-skills)

## License

MIT License — feel free to use, modify, and share.
