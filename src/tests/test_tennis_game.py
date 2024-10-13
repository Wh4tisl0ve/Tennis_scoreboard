import pytest

from app.tennis_logic.tennis import Tennis


class TestTennisGame:
    def setup_method(self):
        self.__tennis: Tennis = Tennis()

    @pytest.fixture(params=[
        (1, "15"),
        (2, "30"),
        (3, "40"),
        (4, "0")
    ])
    def goals_data(self, request):
        return request.param

    @pytest.fixture
    def create_draw(self):
        player_three_goals = 3
        for _ in range(player_three_goals):
            self.__tennis.player1_goals()
            self.__tennis.player2_goals()

    def test_player1_scores_points_correctly(self, goals_data):
        """Проверка корректности начисления очков для 1 игрока"""
        cnt_goals, result = goals_data

        for _ in range(cnt_goals):
            self.__tennis.player1_goals()

        tennis_info = self.__tennis.to_render()
        player_point = tennis_info['game']['player1_value']

        assert player_point == result

    def test_player2_scores_points_correctly(self, goals_data):
        """Проверка корректности начисления очков для 2 игрока"""
        cnt_goals, result = goals_data

        for _ in range(cnt_goals):
            self.__tennis.player2_goals()

        tennis_info = self.__tennis.to_render()
        player_point = tennis_info['game']['player2_value']

        assert player_point == result

    @pytest.mark.usefixtures('create_draw')
    def test_ad_player1(self):
        """Проверка работы механизма преимущества игрока 1"""
        result_player1 = 'AD'
        result_player2 = '40'

        self.__tennis.player1_goals()

        tennis_info = self.__tennis.to_render()
        player1_point = tennis_info['game']['player1_value']
        player2_point = tennis_info['game']['player2_value']

        assert player1_point == result_player1 and player2_point == result_player2

    @pytest.mark.usefixtures('create_draw')
    def test_ad_player2(self):
        """Проверка работы механизма преимущества игрока 2"""
        result_player1 = '40'
        result_player2 = 'AD'

        self.__tennis.player2_goals()

        tennis_info = self.__tennis.to_render()
        player1_point = tennis_info['game']['player1_value']
        player2_point = tennis_info['game']['player2_value']

        assert player2_point == result_player2 and player1_point == result_player1

    @pytest.mark.usefixtures('create_draw')
    def test_minus_point_enemy_player1(self):
        """Проверка работы механизма потери преимущества игрока 2"""
        result = '40'

        self.__tennis.player2_goals()
        self.__tennis.player1_goals()

        tennis_info = self.__tennis.to_render()
        player1_point = tennis_info['game']['player1_value']
        player2_point = tennis_info['game']['player2_value']

        assert player1_point == result and player2_point == result

    @pytest.mark.usefixtures('create_draw')
    def test_minus_point_enemy_player2(self):
        """Проверка работы механизма потери преимущества игрока 1"""
        result = '40'

        self.__tennis.player1_goals()
        self.__tennis.player2_goals()

        tennis_info = self.__tennis.to_render()
        player1_point = tennis_info['game']['player1_value']
        player2_point = tennis_info['game']['player2_value']

        assert player1_point == result and player2_point == result

    @pytest.mark.usefixtures('create_draw')
    def test_reset_player1_point_after_ad(self):
        """Проверка работы механизма сброса очков после взятия очка при преимуществе(AD)"""
        result = '0'

        self.__tennis.player1_goals()
        self.__tennis.player1_goals()

        tennis_info = self.__tennis.to_render()
        player1_point = tennis_info['game']['player1_value']
        player2_point = tennis_info['game']['player2_value']

        assert player1_point == result and player2_point == result

    @pytest.mark.usefixtures('create_draw')
    def test_reset_player2_point_after_ad(self):
        """Проверка работы механизма сброса очков после взятия очка при преимуществе(AD)"""
        result = '0'

        self.__tennis.player2_goals()
        self.__tennis.player2_goals()

        tennis_info = self.__tennis.to_render()
        player1_point = tennis_info['game']['player1_value']
        player2_point = tennis_info['game']['player2_value']

        assert player1_point == result and player2_point == result
