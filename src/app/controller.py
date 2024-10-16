from app.mini_framework import app
from app.mini_framework.pagination.pagination import Pagination
from app.models import MatchStory
from app.services.match_create_service import match_create_service
from app.repository.matches_repository import matches_repo
from app.repository.match_story_repository import matches_story_repo
from app.services.match_score_service import match_score_service
from app.tennis_logic.tennis import Tennis


@app.route(r'^\/$', methods=['GET'])
def render_main_page(request: dict, start_response) -> str:
    start_response('200 OK', [('Content-Type', 'text/html')])
    return app.render_template('index.html')


@app.route(r'^\/new-match', methods=['POST'])
def create_new_match(request: dict, start_response) -> str:
    players_dict = request.get('input_data')

    new_match = match_create_service.create_match(player1_name=players_dict['player1_name'],
                                                  player2_name=players_dict['player2_name'])

    tennis = Tennis()

    match_story_record = MatchStory(id_match=new_match.id,
                                    score=tennis.to_dict(),
                                    match_status=tennis.status_to_dict())
    matches_story_repo.add(match_story_record)

    start_response('302 Redirect', [('Location', f'/match-score?uuid={new_match.uuid}')])

    return ''


@app.route(r'^\/match-score', methods=['GET'])
def get_match_score(request: dict, start_response) -> str:
    uuid = request.get('uuid')
    match = matches_repo.find_by_uuid(uuid)

    tennis = match_score_service.deserialize_tennis(match)

    tennis_serialize = match_score_service.serialize_tennis(match)
    tennis_serialize['tennis'] = tennis.to_render()

    start_response('200 OK', [('Content-Type', 'text/html')])
    return app.render_template('pages/match-score.html', data=tennis_serialize)


@app.route(r'^\/match-score', methods=['POST'])
def player_scored(request: dict, start_response) -> str:
    num_player_scored = request.get('input_data').get('player_id')

    uuid = request.get('uuid')
    match = matches_repo.find_by_uuid(uuid)

    tennis = match_score_service.deserialize_tennis(match)

    match_score_service.player_goals(num_player_scored, tennis, match)

    if tennis.is_end_game:
        match_score_service.add_winner(tennis, match)

    start_response('302 Redirect', [('Location', f'/match-score?uuid={match.uuid}')])
    return ''


@app.route(r'^\/matches', methods=['GET'])
def get_played_matches(request: dict, start_response) -> str:
    player_name_filter = request.get('filter_by_player_name', '')
    page_num = int(request.get('page', 1))
    items_per_page = int(request.get('per_page', 10))

    finished_matches = matches_repo.find_finished_matches(player_name_filter, page_num, items_per_page)
    count_records = matches_repo.find_count_finished_matches(player_name_filter)

    pagination = Pagination(count_records,
                            current_page=page_num,
                            items_per_page=items_per_page,
                            filters={'filter_by_player_name': player_name_filter,
                                     'per_page': items_per_page})

    start_response('200 OK', [('Content-Type', 'text/html')])

    return app.render_template('pages/finished_matches.html',
                               data=finished_matches,
                               pagination=pagination)
