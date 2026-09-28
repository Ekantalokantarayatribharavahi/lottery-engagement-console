"""Console rendering functions."""
from .core import percentage_from_combinations, probability_statement
from .data import GAMES, MISCONCEPTION_CLAIMS


def registry_text() -> str:
    lines = ["GAME REGISTRY", "=" * 60]
    for game in GAMES:
        extra = game.extra_name or "None"
        extra_rule = f"1 from 1–{game.extra_pool}" if game.extra_pool else "None"
        lines.append(
            f"{game.name}: choose {game.main_count} from 1–{game.main_pool}; "
            f"extra={extra} ({extra_rule}); jackpot combinations={game.jackpot_combinations:,}; "
            f"R{game.cost_rand}; {game.frequency}; source={game.source}"
        )
    return "\n".join(lines)


def combinations_text() -> str:
    return "\n".join([
        "COMBINATION CALCULATOR",
        "C(52,6) = 20,358,520",
        "C(50,5) = 2,118,760",
        "C(36,5) = 376,992",
        "C(50,5) × 16 = 33,900,160",
    ])


def probability_text() -> str:
    values = [20_358_520, 33_900_160, 376_992]
    lines = ["PROBABILITY TRANSLATOR", "jackpot probability = 1/N", "jackpot percentage = 100/N"]
    for n in values:
        lines.append(f"1/{n:,} = {percentage_from_combinations(n):.10f}%")
    lines.append(probability_statement(33_900_160, "PowerBall jackpot combination"))
    lines.append("jackpot probability ≠ any-prize probability")
    return "\n".join(lines)


def trap_text() -> str:
    lines = ["CLAIMS I AM FORBIDDEN TO ACCEPT WITHOUT EVIDENCE", ""]
    for claim in MISCONCEPTION_CLAIMS:
        lines.append(f"- {claim}")
        lines.append("  Status: reject as a predictive claim unless a valid dependence/model is demonstrated.")
    return "\n".join(lines)


def decision_sheet_text() -> str:
    return """ENGAGEMENT CANDIDATE SHEET

Game:
Current rules verified:
Draw mechanism verified:
Sample-space size:
Jackpot probability:
Any-prize probability:
Cost:
Draw frequency:
Supplementary game available:
Historical data available:
Rule-change boundaries identified:
Outstanding questions:
Evidence sources:
Apprentice conclusion:
"""


def full_text() -> str:
    return "\n\n".join((registry_text(), combinations_text(), probability_text(), trap_text(), decision_sheet_text()))
