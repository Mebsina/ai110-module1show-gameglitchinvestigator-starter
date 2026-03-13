from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"

def test_decimal_input_truncates():
    # "1.9" is parsed as 1, not a clean integer, should this be rejected?
    ok, value, _ = parse_guess("1.9")
    assert ok == True
    assert value == 1

def test_negative_number_accepted():
    # Negative numbers pass parse_guess with no error, even though valid range is 1-100
    ok, value, _ = parse_guess("-1")
    assert ok == True
    assert value == -1

def test_extremely_large_number_accepted():
    # Extremely large numbers pass parse_guess with no error, even though valid range is 1-100
    ok, value, _ = parse_guess("99999999")
    assert ok == True
    assert value == 99999999
