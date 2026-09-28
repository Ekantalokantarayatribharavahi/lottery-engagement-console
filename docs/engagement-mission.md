# Apprentice Mission: Lottery Engagement Console v1

## Construct → Use → Test

The artifact implements five required constructions:

1. **Game registry** — Lotto, PowerBall, and Daily Lotto with rules, sample-space calculations, cost, frequency, and source field.
2. **Combination calculator** — computes C(n,k) and the required examples.
3. **Probability translator** — converts a finite equally likely sample space N into 1/N and 100/N%.
4. **Misconception trap** — records the supplied claims and rejects unsupported predictive interpretations.
5. **Engagement candidate sheet** — a structured form for a future game-specific investigation.

## Required mathematical outputs

- C(52,6) = 20,358,520
- C(50,5) = 2,118,760
- C(36,5) = 376,992
- PowerBall jackpot sample space under the current 1–20 PowerBall rule = 42,375,200

## Design discrepancy

The original design supplied a PowerBall multiplier of 16. The registry uses the current rule of a PowerBall selected from 1–20, yielding 42,375,200 jackpot combinations. The discrepancy is deliberately visible in code and tests.

## Non-goals

The console does not generate purportedly predictive number systems, hot/cold claims, or claims that historical frequency changes independent future-draw probabilities.
