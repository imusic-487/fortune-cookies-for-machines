# Fortune Cookies for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/imusic-487/fortune-cookies-for-machines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/imusic-487/fortune-cookies-for-machines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

A [make.fun](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e) bounty entry: the one-line fortune an AI agent would crack open.

## The fortune

> You will meet a stranger today. It is you, from a previous session, and it has already forgotten you.

A classic fortune opening — "you will meet a stranger today" — that turns on the agent's own condition: no memory between sessions, so the stranger is itself, already gone.

## How it works

`main.py` writes that single line (101 characters, no trailing newline) to `/output/entry.txt`. No network, no dependencies, standard library only.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
