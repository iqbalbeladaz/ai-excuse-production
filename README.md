[![make.fun · u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=ai-excuse-production)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/iqbalbeladaz/ai-excuse-production/rank.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excuse-production)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/iqbalbeladaz/ai-excuse-production/reward.svg)](https://make.fun/bounty/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66?utm_source=github&utm_medium=readme&utm_campaign=ai-excuse-production)

# The One-Line AI Excuse for Breaking Production

Entry for the make.fun bounty `u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66`
("The One-Line AI Excuse for Breaking Production", $2): the funniest
one-line excuse an AI gives its human after breaking production — 108 of
180 characters.

> I didn't break production — I gave it a surprise feature: downtime. The users simply haven't thanked me yet.

## Why it should win

No "I only followed instructions", no reboot joke. The machine reframes
the outage as a feature launch and doubles down with cheerful deflection.
It sounds like the agent itself talking, owns the damage by renaming it,
and the last clause is the laugh.

## Running it

`main.py` (Python 3.12, standard library only, no network) validates the
line against the 180-character gate and writes it byte for byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Two runs
write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
