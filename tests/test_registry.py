from lottery_engagement.data import DESIGN_DISCREPANCY, GAMES, MISCONCEPTION_CLAIMS


def test_registry_contains_required_games():
    assert [game.name for game in GAMES] == ["LOTTO", "POWERBALL", "DAILY LOTTO"]


def test_registry_jackpot_spaces():
    assert GAMES[0].jackpot_combinations == 20_358_520
    assert GAMES[1].jackpot_combinations == 33_900_160
    assert GAMES[2].jackpot_combinations == 376_992


def test_powerball_rule_and_cost():
    game = GAMES[1]
    assert game.main_pool == 50
    assert game.main_count == 5
    assert game.extra_pool == 16
    assert game.cost_rand == 10


def test_every_game_has_source():
    assert all(game.source for game in GAMES)


def test_design_matches_current_powerball_rule():
    assert DESIGN_DISCREPANCY is None


def test_misconception_trap_has_all_supplied_claims():
    assert len(MISCONCEPTION_CLAIMS) == 8
