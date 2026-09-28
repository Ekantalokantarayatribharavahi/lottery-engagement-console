from lottery_engagement.core import combination, percentage_from_combinations, probability_from_combinations, probability_statement


def test_required_combinations():
    assert combination(52, 6) == 20_358_520
    assert combination(50, 5) == 2_118_760
    assert combination(36, 5) == 376_992


def test_powerball_current_sample_space():
    assert combination(50, 5) * 20 == 42_375_200


def test_probability_translator():
    assert probability_from_combinations(100) == 0.01
    assert percentage_from_combinations(100) == 1


def test_probability_statement():
    assert "1 out of 42,375,200" in probability_statement(42_375_200, "PowerBall jackpot combination")


def test_invalid_combination():
    try:
        combination(5, 6)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid combination should raise ValueError")
