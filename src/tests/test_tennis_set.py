import pytest

from app.tennis_logic.tennis import Tennis


class TestTennisSet:
    def setup_method(self):
        self.__tennis: Tennis = Tennis()

    @pytest.fixture(params=[
        (1, "0"),
        (2, "0"),
        (3, "0"),
        (4, "1")
    ])
    def goals_data(self, request):
        return request.param

    def test_player1_scores_set_correctly(self, goals_data):
        """Проверка корректности начисления победы в сете для 1 игрока"""
        cnt_goals, result = goals_data

        for _ in range(cnt_goals):
            self.__tennis.player1_goals()

        tennis_info = self.__tennis.get_dict()
        player_value_set = tennis_info['set']['player1_value']

        assert player_value_set == result

    def test_player2_scores_set_correctly(self, goals_data):
        """Проверка корректности начисления победы в сете для 2 игрока"""
        cnt_goals, result = goals_data

        for _ in range(cnt_goals):
            self.__tennis.player2_goals()

        tennis_info = self.__tennis.get_dict()
        player_value_set = tennis_info['set']['player2_value']

        assert player_value_set == result

    @pytest.fixture
    def create_draw(self):
        """Создание ситуации 40-40"""
        player_three_goals = 3
        for _ in range(player_three_goals):
            self.__tennis.player1_goals()
            self.__tennis.player2_goals()

    @pytest.mark.usefixtures('create_draw')
    def test_player1_win_after_ad(self):
        """Проверка работы механизма победы в сете после преимущества"""
        result_player1 = '1'
        result_player2 = '0'

        self.__tennis.player1_goals()
        self.__tennis.player1_goals()

        tennis_info = self.__tennis.get_dict()
        player1_point = tennis_info['set']['player1_value']
        player2_point = tennis_info['set']['player2_value']

        assert player1_point == result_player1 and player2_point == result_player2

    @pytest.mark.usefixtures('create_draw')
    def test_player2_win_after_ad(self):
        """Проверка работы механизма победы в сете после преимущества"""
        result_player1 = '0'
        result_player2 = '1'

        self.__tennis.player2_goals()
        self.__tennis.player2_goals()

        tennis_info = self.__tennis.get_dict()
        player1_point = tennis_info['set']['player1_value']
        player2_point = tennis_info['set']['player2_value']

        assert player1_point == result_player1 and player2_point == result_player2

    @pytest.fixture
    def player1_win_match(self):
        """Создание ситуации, когда игрок побеждает в матче"""
        points_win_set = 4
        points_win_match = 6 * points_win_set

        for _ in range(points_win_match):
            self.__tennis.player1_goals()

    @pytest.mark.usefixtures('player1_win_match')
    def test_reset_player1_point_after_win(self):
        """Проверка работы механизма сброса очков в сете, после победы 1 игрока в матче"""
        result = '0'

        tennis_info = self.__tennis.get_dict()
        player1_point = tennis_info['set']['player1_value']
        player2_point = tennis_info['set']['player2_value']

        assert player1_point == result and player2_point == result

    @pytest.fixture
    def player2_win_match(self):
        """Создание ситуации, когда игрок побеждает в матче"""
        points_win_set = 4
        points_win_match = 6 * points_win_set

        for i in range(points_win_match):
            self.__tennis.player2_goals()

    @pytest.mark.usefixtures('player2_win_match')
    def test_reset_player2_point_after_win(self):
        """Проверка работы механизма сброса очков в сете, после победы 2 игрока в матче"""
        result = '0'

        tennis_info = self.__tennis.get_dict()
        player1_point = tennis_info['set']['player1_value']
        player2_point = tennis_info['set']['player2_value']

        assert player1_point == result and player2_point == result

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
    def test_goals_after_tie_brake(self):
        """Проверка работы механики начисления очков после объявления тай-брейка"""
        result = '1'

        self.__tennis.player1_goals()
        self.__tennis.player2_goals()

        tennis_info = self.__tennis.get_dict()
        player1_point = tennis_info['game']['player1_value']
        player2_point = tennis_info['game']['player2_value']

        assert player1_point == result and player2_point == result

    @pytest.fixture(params=[
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "0")
    ])
    def points_tie_brake_data(self, request):
        return request.param

    @pytest.mark.usefixtures('create_tie_break')
    def test_player1_add_point_after_tie_brake(self, points_tie_brake_data):
        """Проверка механизма начисления очков при тай-брейке"""
        cnt_goals, result = points_tie_brake_data

        for _ in range(cnt_goals):
            self.__tennis.player1_goals()

        tennis_info = self.__tennis.get_dict()
        player1_point = tennis_info['game']['player1_value']

        assert player1_point == result

    @pytest.mark.usefixtures('create_tie_break')
    def test_player2_add_point_after_tie_brake(self, points_tie_brake_data):
        """Проверка механизма начисления очков при тай-брейке"""
        cnt_goals, result = points_tie_brake_data

        for _ in range(cnt_goals):
            self.__tennis.player2_goals()

        tennis_info = self.__tennis.get_dict()
        player2_point = tennis_info['game']['player2_value']

        assert player2_point == result

    @pytest.mark.usefixtures('create_tie_break')
    def test_reset_point_after_diff_two_point_tie_brake(self):
        """Проверка механизма сброса очков при победе в матче с разницей в два очка во время тай брейка"""
        cnt_goals = 6
        result = "0"

        for _ in range(cnt_goals):
            self.__tennis.player1_goals()
            self.__tennis.player2_goals()

        self.__tennis.player1_goals()
        self.__tennis.player2_goals()
        self.__tennis.player1_goals()
        self.__tennis.player2_goals()

        # diff two points
        self.__tennis.player1_goals()
        self.__tennis.player1_goals()

        tennis_info = self.__tennis.get_dict()
        player1_point = tennis_info['set']['player1_value']
        player2_point = tennis_info['set']['player2_value']

        assert player1_point == result and player2_point == result

    @pytest.mark.usefixtures('create_tie_break')
    def test_set_continue_if_diff_points_not_two_point(self):
        """Проверка продолжится ли тай-брейк, если разница очков будет меньше двух очков"""
        cnt_goals = 6
        result_player1 = "7"
        result_player2 = "6"

        for _ in range(cnt_goals):
            self.__tennis.player1_goals()
            self.__tennis.player2_goals()

        self.__tennis.player1_goals()

        tennis_info = self.__tennis.get_dict()
        player1_point = tennis_info['game']['player1_value']
        player2_point = tennis_info['game']['player2_value']

        assert player1_point == result_player1 and player2_point == result_player2
