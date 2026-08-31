<p align="center">
  <img src="https://sncfoundation.github.io/logos/brainfuck.svg" width="96" alt="Brainfuck client logo">
</p>

<h1 align="center">Brainfuck client</h1>

<p align="center"><b>If it reconciles from here, it reconciles anywhere</b><br>
A <a href="https://sncfoundation.github.io">Sheet-Native Computing Foundation</a> project &#183; analog of <b>a client library</b></p>

---

**Status:** 📝 Unsaved Draft &#183; this project is a proposal. Design notes and contributions are welcome.

## About

If it reconciles from here, it reconciles anywhere Part of the spreadsheet-native stack — the Sheet stays the source of truth, and it reconciles.

## Get involved

- 📋 Tracking issue &amp; design: [sncfoundation/sheeternetes#28](https://github.com/sncfoundation/sheeternetes/issues/28)
- 🗺️ [SNCF Landscape](https://sncfoundation.github.io/landscape.html)
- 🧩 [All projects](https://sncfoundation.github.io/projects.html)
- ⚖️ [Governance &amp; how to contribute](https://github.com/sncfoundation/governance)
- 🎓 [Get certified (CSFE)](https://sncfoundation.github.io/certification.html)

## Status legend

Everything starts as an **Unsaved Draft**. It reconciles up the tiers from there — see the
[maturity model](https://sncfoundation.github.io/foundation.html#maturity).

---

<sub>Licensed under Apache-2.0. The SNCF does not recommend running production on a spreadsheet. If you do, please film it.</sub>


## It actually works

Brainfuck can't speak HTTP — but it can **emit a manifest**, which is a perfectly good client
when you pipe it into `skctl`. This repo ships a generator, a tiny interpreter, and a ready
program that prints a Deployment manifest.

```bash
# print the manifest the Brainfuck way, then apply it
python3 bf.py apply.bf | skctl apply /dev/stdin

# generate a Brainfuck program for any manifest string
python3 bfgen.py '{"deployments":[{"name":"web","image":"nginx","replicas":2}]}' > web.bf
python3 bf.py web.bf | skctl apply /dev/stdin
```

- `bf.py` — a minimal Brainfuck interpreter.
- `bfgen.py` — generates a Brainfuck program that prints any string.
- `apply.bf` — a generated program that prints a Deployment manifest.

If it reconciles from here, it reconciles anywhere.

