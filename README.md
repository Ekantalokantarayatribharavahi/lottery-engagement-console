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

## Mathematical correction preserved by the artifact

The design supplied `16` PowerBall values. The current official rule is one PowerBall selected from 1–20, so the jackpot sample space is:

\[
\binom{50}{5}\times20=42,375,200.
\]

The console therefore records the supplied `×16` value as a design discrepancy rather than encoding it as the current rule.

## Sources

The game registry records official South African National Lottery source URLs for the rule facts used by the application.
