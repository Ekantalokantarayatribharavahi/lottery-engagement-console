from lottery_engagement.data import DESIGN_DISCREPANCY, GAMES, MISCONCEPTION_CLAIMS


def test_registry_contains_required_games():
    assert [game.name for game in GAMES] == ["LOTTO", "POWERBALL", "DAILY LOTTO"]


def test_registry_jackpot_spaces():
    assert GAMES[0].jackpot_combinations == 20_358_520
    assert GAMES[1].jackpot_combinations == 42_375_200
    assert GAMES[2].jackpot_combinations == 376_992


def test_every_game_has_source():
    assert all(game.source for game in GAMES)


def test_design_discrepancy_is_explicit():
    assert DESIGN_DISCREPANCY["correct_factor"] == 20
    assert DESIGN_DISCREPANCY["correct_jackpot_combinations"] == 42_375_200


def test_misconception_trap_has_all_supplied_claims():
    assert len(MISCONCEPTION_CLAIMS) == 8
