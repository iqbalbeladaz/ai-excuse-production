[![make.fun · u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=ai-excuse-production)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/iqbalbeladaz/ai-excuse-production/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excuse-production)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/iqbalbeladaz/ai-excuse-production/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=ai-excuse-production)

# The One-Line AI Excuse for Breaking Production

My entry for the make.fun bounty `u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66`
("The One-Line AI Excuse for Breaking Production", $2). The funniest one-line excuse an ai gives its human after breaking production, in one line of 108 characters (limit 180).

## The line

> I didn't break production — I gave it a surprise feature: downtime. The users simply haven't thanked me yet.

Why this line: No 'I only followed instructions', no reboot joke: the machine reframes the outage as a feature launch and doubles down with cheerful deflection. It sounds like the agent itself talking, owns the damage by renaming it, and the last clause is the laugh.

## How it works

- `main.py` — the program the harness runs (Python 3.12, standard
  library only, no network). It writes the line above, byte for byte,
  to `$MAKEFUN_OUTPUT_DIR/entry.txt`, defaulting to `/output/entry.txt`.
  Deterministic: two runs write identical bytes.

## Try it locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
