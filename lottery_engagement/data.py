"""Source-backed game registry data."""
from dataclasses import dataclass
from math import comb

NATIONAL_LOTTERY = "https://www.nationallottery.co.za/"
RULES_REFERENCE = "https://www.lottery.co.za/2026-south-africa-lottery-changes"

@dataclass(frozen=True)
class Game:
    name: str
    main_count: int
    main_pool: int
    extra_name: str | None
    extra_pool: int | None
    cost_rand: int
    frequency: str
    source: str

    @property
    def main_combinations(self) -> int:
        return comb(self.main_pool, self.main_count)

    @property
    def jackpot_combinations(self) -> int:
        return self.main_combinations * (self.extra_pool or 1)

GAMES = (
    Game("LOTTO", 6, 52, "Bonus Ball", None, 5, "Wednesday and Saturday", RULES_REFERENCE),
    Game("POWERBALL", 5, 50, "PowerBall", 16, 10, "Tuesday and Friday", RULES_REFERENCE),
    Game("DAILY LOTTO", 5, 36, None, None, 3, "Every day except 25 December", RULES_REFERENCE),
)

DESIGN_DISCREPANCY = None

MISCONCEPTION_CLAIMS = (
    "A number is overdue.",
    "A number is hot.",
    "A number is cold.",
    "A number appeared frequently, therefore it will appear again.",
    "A number has not appeared recently, therefore it is more likely next.",
    "A visually unusual combination cannot occur.",
    "A balanced-looking combination is more likely.",
    "A previous draw affects the next draw without evidence of dependence.",
)
