import pytest

from app.tennis_logic.tennis import Tennis


class TestTennisMatch:
    def setup_method(self):
        self.__tennis: Tennis = Tennis()

    @pytest.fixture
    def player1_win_match(self):
        """Создание ситуации, когда игрок побеждает в матче"""
        points_win_set = 4
        points_win_match = 6 * points_win_set

        for _ in range(points_win_match):
            self.__tennis.player1_goals()

    @pytest.mark.usefixtures('player1_win_match')
    def test_player1_win_match(self):
        """Проверка победы в матче"""
        result = "1"

        tennis_info = self.__tennis.get_dict()
        player1_point = tennis_info['match']['player1_value']

        assert player1_point == result

    @pytest.fixture
    def player2_win_match(self):
        """Создание ситуации, когда игрок побеждает в матче"""
        points_win_set = 4
        points_win_match = 6 * points_win_set

        for i in range(points_win_match):
            self.__tennis.player2_goals()

    @pytest.mark.usefixtures('player2_win_match')
    def test_player2_win_match(self):
        """Проверка победы в матче"""
        result = "1"

        tennis_info = self.__tennis.get_dict()
        player2_point = tennis_info['match']['player2_value']

        assert player2_point == result

    @pytest.fixture
    def create_tie_break(self):
        """Создание ситуации, когда возникает тай-брейк (6-6 по сетам)"""
        points_win_five_sets = 20
        points_win_six_sets = 24
        points_win_set = 4

        for _ in range(points_win_five_sets):
            self.__tennis.player1_goals()

        for _ in range(points_win_six_sets):
            self.__tennis.player2_goals()

        for _ in range(points_win_set):
            self.__tennis.player1_goals()

    @pytest.mark.usefixtures('create_tie_break')
    def test_player1_win_match_after_tie_brake(self):
        """Проверка механизма подсчета матчей после тай-брейка. При победе 'всухую'"""
        cnt_goals = 7
        result_player1 = "1"
        result_player2 = "0"

        for _ in range(cnt_goals):
            self.__tennis.player1_goals()

        tennis_info = self.__tennis.get_dict()
        player1_point = tennis_info['match']['player1_value']
        player2_point = tennis_info['match']['player2_value']

        assert player1_point == result_player1 and player2_point == result_player2

    @pytest.mark.usefixtures('create_tie_break')
    def test_player2_win_match_after_tie_brake(self):
        """Проверка механизма подсчета матчей после тай-брейка. При победе 'всухую'"""
        cnt_goals = 7
        result_player1 = "0"
        result_player2 = "1"

        for _ in range(cnt_goals):
            self.__tennis.player2_goals()

        tennis_info = self.__tennis.get_dict()
        player1_point = tennis_info['match']['player1_value']
        player2_point = tennis_info['match']['player2_value']

        assert player1_point == result_player1 and player2_point == result_player2

    @pytest.mark.usefixtures('create_tie_break')
    def test_player1_win_match_after_tie_brake_with_diff_two_point(self):
        """Проверка механизма подсчета матчей после тай-брейка с разницей в 2 мяча"""
        cnt_goals = 5
        result_player1 = "1"
        result_player2 = "0"

        for _ in range(cnt_goals):
            self.__tennis.player1_goals()
            self.__tennis.player2_goals()

        self.__tennis.player1_goals()
        self.__tennis.player1_goals()

        tennis_info = self.__tennis.get_dict()
        player1_point = tennis_info['match']['player1_value']
        player2_point = tennis_info['match']['player2_value']

        assert player1_point == result_player1 and player2_point == result_player2

    @pytest.mark.usefixtures('create_tie_break')
    def test_player2_win_match_after_tie_brake_with_diff_two_point(self):
        """Проверка механизма подсчета матчей после тай-брейка с разницей в 2 мяча"""
        cnt_goals = 5
        result_player1 = "0"
        result_player2 = "1"

        for _ in range(cnt_goals):
            self.__tennis.player1_goals()
            self.__tennis.player2_goals()

        self.__tennis.player2_goals()
        self.__tennis.player2_goals()

        tennis_info = self.__tennis.get_dict()
        player1_point = tennis_info['match']['player1_value']
        player2_point = tennis_info['match']['player2_value']

        assert player1_point == result_player1 and player2_point == result_player2

    def test_player1_win_tennis_match(self):
        """Проверка на победу игрока"""
        cnt_goals = 48
        result = "2"

        for _ in range(cnt_goals):
            self.__tennis.player1_goals()

        tennis_info = self.__tennis.get_dict()
        player1_point = tennis_info['match']['player1_value']

        assert player1_point == result and self.__tennis.get_winner_id() == 1

    def test_player2_win_tennis_match(self):
        """Проверка на победу игрока"""
        cnt_goals = 48
        result = "2"

        for _ in range(cnt_goals):
            self.__tennis.player2_goals()

        tennis_info = self.__tennis.get_dict()
        player2_point = tennis_info['match']['player2_value']

        assert player2_point == result and self.__tennis.get_winner_id() == 2

    def test_best_of_3(self):
        """Проверка на победу при достижении двух очков"""
        cnt_goals = 48
        result_player1 = "1"
        result_player2 = "2"

        for _ in range(int(cnt_goals / 2)):
            self.__tennis.player1_goals()

        for _ in range(cnt_goals):
            self.__tennis.player2_goals()

        tennis_info = self.__tennis.get_dict()
        player1_point = tennis_info['match']['player1_value']
        player2_point = tennis_info['match']['player2_value']

        assert player1_point == result_player1
        assert player2_point == result_player2
        assert self.__tennis.get_winner_id() == 2

    def test_is_game_over(self):
        """Проверка на окончание игры"""
        cnt_goals = 720
        result_other = "0"
        result_player2_match = "2"

        for _ in range(cnt_goals):
            self.__tennis.player2_goals()

        tennis_info = self.__tennis.get_dict()
        player1_point_game = tennis_info['game']['player1_value']
        player2_point_game = tennis_info['game']['player2_value']

        player1_point_set = tennis_info['set']['player1_value']
        player2_point_set = tennis_info['set']['player2_value']

        player1_point_match = tennis_info['match']['player1_value']
        player2_point_match = tennis_info['match']['player2_value']

        assert player1_point_game == result_other and player2_point_game == result_other
        assert player1_point_set == result_other and player2_point_set == result_other
        assert player1_point_match == result_other and player2_point_match == result_player2_match
        assert self.__tennis.is_end_game
