"""CLI entry point."""
import sys
from .console import combinations_text, decision_sheet_text, full_text, probability_text, registry_text, trap_text


def main() -> None:
    command = sys.argv[1] if len(sys.argv) > 1 else "all"
    commands = {
        "all": full_text,
        "registry": registry_text,
        "combinations": combinations_text,
        "probability": probability_text,
        "trap": trap_text,
        "decision-sheet": decision_sheet_text,
    }
    try:
        print(commands[command]())
    except KeyError:
        choices = ", ".join(commands)
        raise SystemExit(f"Unknown command {command!r}. Choose: {choices}")


if __name__ == "__main__":
    main()
