from .score import score_of_last_ten_recipes, count_left_of_score_sequence

def test_score_of_last_ten_recipes():
    assert score_of_last_ten_recipes('37', 9) == '5158916779'
    assert score_of_last_ten_recipes('37', 5) == '0124515891'
    assert score_of_last_ten_recipes('37', 2018) == '5941429882'

def test_count_left_of_score_sequence():
    assert count_left_of_score_sequence('37', '51589') == 9
    assert count_left_of_score_sequence('37', '01245') == 5
    assert count_left_of_score_sequence('37', '92510') == 18
    assert count_left_of_score_sequence('37', '59414') == 2018
