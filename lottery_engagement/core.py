"""Mathematical and presentation primitives."""
from math import factorial


def combination(n: int, k: int) -> int:
    """Return C(n,k), rejecting invalid parameters."""
    if n < 0 or k < 0 or k > n:
        raise ValueError("Require n >= 0 and 0 <= k <= n")
    return factorial(n) // (factorial(k) * factorial(n - k))


def probability_from_combinations(n: int) -> float:
    """Probability of one specified outcome among n equally likely outcomes."""
    if n <= 0:
        raise ValueError("Combination count must be positive")
    return 1 / n


def percentage_from_combinations(n: int) -> float:
    return 100 / n


def probability_statement(n: int, label: str = "particular combination") -> str:
    return (
        f"One {label} corresponds to 1 out of {n:,} equally possible "
        "combinations under the stated model."
    )
