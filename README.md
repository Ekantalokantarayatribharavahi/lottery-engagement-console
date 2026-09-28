# Lottery Engagement Console

A source-aware command-line instrument for interrogating South African National Lottery game structures.

## Mission

The console turns the engagement design into an executable artifact: a game registry, exact combination calculations, a probability translator, a misconception trap, and an engagement candidate sheet.

It is an information and calculation instrument. It does not predict lottery outcomes or claim that a particular number selection is more likely to win.

## Run

Requires Python 3.10+.

```bash
python -m lottery_engagement
python -m lottery_engagement registry
python -m lottery_engagement combinations
python -m lottery_engagement probability
python -m lottery_engagement trap
python -m lottery_engagement decision-sheet
```

Run tests with:

```bash
python -m pytest
```

## Mathematical model

The current PowerBall rule uses five main numbers from 1–50 and a PowerBall from 1–16. Therefore:

\[
\binom{50}{5}\times16=33,900,160.
\]

This matches the supplied design.

## Sources

The registry records the current 2026 South African lottery rule reference used to populate the game facts.
