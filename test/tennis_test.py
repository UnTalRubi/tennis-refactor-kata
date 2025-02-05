import pytest

from src.tennis1 import TennisGame1
from src.tennis2 import TennisGame2
from src.tennis3 import TennisGame3
from src.tennis4 import TennisGame4
from src.tennis5 import TennisGame5
from src.tennis6 import TennisGame6
from src.tennis7 import TennisGame7
from tennis_unittest import play_game, test_cases


@pytest.mark.parametrize(
    "TennisGameClass",
    [
        TennisGame1,
        TennisGame2,
        TennisGame3,
        TennisGame4,
        TennisGame5,
        TennisGame6,
    ],
)
@pytest.mark.parametrize(
    "p1_points p2_points score p1_name p2_name".split(), test_cases
)
def test_get_score_most_games(
    TennisGameClass, p1_points, p2_points, score, p1_name, p2_name
):
    game = play_game(TennisGameClass, p1_points, p2_points, p1_name, p2_name)
    assert score == game.score()


@pytest.mark.parametrize(
    "p1_points p2_points score p1_name p2_name".split(), test_cases
)
def test_get_score_game7(p1_points, p2_points, score, p1_name, p2_name):
    game = play_game(TennisGame7, p1_points, p2_points, p1_name, p2_name)
    assert "Current score: " + score + ", enjoy your game!" == game.score()
