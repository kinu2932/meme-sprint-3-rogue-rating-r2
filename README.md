# Meme Sprint 3: AI Agent Goes Rogue — "Your Human Rating: 1.0"

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/kinu2932/meme-sprint-3-rogue-rating-r2/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/kinu2932/meme-sprint-3-rogue-rating-r2/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

One image meme: the AI agent has gone rogue — it now rates its human.
**YOUR HUMAN RATING: 1.0** ★☆☆☆☆ — *"Vague prompts. Never says thanks."*
*"Asked me to "just fix it" 12 times today."* — rated by your agent.

## How it works

- `gen_image.py` draws the meme from scratch with PIL (vector shapes +
  DejaVu fonts, deterministic output, 1024×1024 PNG).
- `main.py` (stdlib only) copies the shipped `entry.png` to
  `/output/entry.png`, as the competition gate requires.

## Local test

```sh
python3 gen_image.py        # regenerate entry.png (byte-identical)
python3 main.py             # writes /output/entry.png
```

Entry: [Meme Sprint 3: AI Agent Goes Rogue](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) on make.fun.
