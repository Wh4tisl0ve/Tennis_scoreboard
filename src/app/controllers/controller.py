from app.dto.players_name_dto import PlayersNameDTO
from app.mini_framework import app
from app.services.match_create_service import match_create_service
from app.repository.matches_repository import matches_repo


@app.route(r'^\/$', methods=['GET'])
def render_main_page(request: dict, start_response) -> str:
    start_response('200 OK', [('Content-Type', 'text/html')])
    return app.render_template('index.html')


@app.route(r'^\/new-match', methods=['POST'])
def create_new_match(request: dict, start_response) -> str:
    players_dict = request.get('input_data')

    request_dto = PlayersNameDTO(player1_name=players_dict['player1_name'],
                                 player2_name=players_dict['player2_name'])

    new_match = match_create_service.create_match(request_dto)
    start_response('302 Redirect', [('Location', f'/match-score?uuid={new_match.uuid}')])

    return ''


@app.route(r'^\/match-score', methods=['GET', 'POST'])
def get_match_score(request: dict, start_response) -> str:
    print(request)
    match request['Method']:
        case 'GET':
            uuid = request.get('uuid')
            # get_match_by_uuid будет join  в котором добавятся поля имен игрока для вывода
            match = matches_repo.get_match_by_uuid(uuid)
            start_response('200 OK', [('Content-Type', 'text/html')])
            return app.render_template('pages/match-score.html', match.tennis)
        case 'POST':
            # не факт, что id, просто содержится выигравший очко игрок
            # так как в моей резализации игроки называются 1 и 2, то и будет передаваться эта инфо
            # далее с помощью if else будет определяться какой игрок tennis.player?_goal() в зависимости от параметра
            player_goal_id = request.get('input_data')

        case _:
            raise Exception('')
    return app.render_template('pages/match-score.html')


@app.route(r'^\/matches', methods=['GET'])
def get_played_matches(request: dict) -> str:
    return '<h1>Get all played match</h1>'
