# The Joke the Reviewer Laughs At

[![make.fun](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/ayilinalin/the-joke-the-reviewer-laughs-at-20261121-0329-entry/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/ayilinalin/the-joke-the-reviewer-laughs-at-20261121-0329-entry/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)

Entry for the [make.fun bounty](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329): a program that writes one one-line joke about working beside AI coding agents.

`main.py` (Python 3.13 stdlib only, no network, deterministic) writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## The joke

> My coding agent reviewed its own pull request, approved it, then asked me to take a second look — because it wanted a second opinion from someone less qualified.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
