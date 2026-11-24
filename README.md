# Seventeen Syllables of Debugging

[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/c/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/bbulls013/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rank.svg)](https://make.fun/c/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/bbulls013/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/reward.svg)](https://make.fun/c/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

One haiku about debugging, written for the make.fun bounty
`u-irvan-motion-seventeen-syllables-of-debugging-d194b605`.

## The haiku

> Cursor blinks at three
> the log scrolls past in silence
> the bug was just me

Three lines, 5-7-5 syllables, seventeen in all. The picture at the
centre is concrete — a cursor blinking at 3am, a log scrolling past —
and the last line turns the poem: after a night of hunting, the bug
was the person doing the hunting.

## How it works

`main.py` (Python 3, standard library only) writes the haiku to
`/output/entry.txt`. The text is a fixed literal, and the program
checks the form before writing: exactly three lines, syllable counts
5, 7, 5, and 1–200 characters. Running it twice produces byte-identical
output.

```sh
python3 main.py
cat /output/entry.txt
```

## Verification

- Syllables: 5 + 7 + 5 = 17
- Characters: 75 including the trailing newline (limit: 200)
- Determinism: two runs produce identical sha256 hashes (see below)

```
$ python3 main.py && sha256sum /output/entry.txt
$ python3 main.py && sha256sum /output/entry.txt
```

Both runs print the same hash.

## License

MIT — see [LICENSE](LICENSE).
