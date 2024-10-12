from app.mini_framework import app
from app.models import MatchStory
from app.services.match_create_service import match_create_service
from app.repository.players_repository import players_repo
from app.repository.matches_repository import matches_repo
from app.repository.match_story_repository import matches_story_repo
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

    match_story_record = MatchStory(id_match=new_match.id, score=tennis.to_dict(), match_status=tennis.status_to_dict())
    matches_story_repo.add(match_story_record)

    start_response('302 Redirect', [('Location', f'/match-score?uuid={new_match.uuid}')])

    return ''


@app.route(r'^\/match-score', methods=['GET'])
def get_match_score(request: dict, start_response) -> str:
    uuid = request.get('uuid')
    match = matches_repo.find_by_uuid(uuid)

    player1 = players_repo.find_by_id(match.player1_id)
    player2 = players_repo.find_by_id(match.player2_id)

    last_record_story = matches_story_repo.get_last_record_story_by_match_id(match.id)

    tennis = Tennis()
    tennis.deserialize_dict(last_record_story.score, last_record_story.match_status)

    tennis_serialize = {"uuid": uuid,
                        "player1_name": player1.name,
                        "player2_name": player2.name,
                        "tennis": tennis.to_render()}

    start_response('200 OK', [('Content-Type', 'text/html')])
    return app.render_template('pages/match-score.html', data=tennis_serialize)


@app.route(r'^\/match-score', methods=['POST'])
def player_scored(request: dict, start_response) -> str:
    num_player_scored = request.get('input_data').get('player_id')
    # возможно здесь будет сервис с определением победителя и тд
    uuid = request.get('uuid')
    match = matches_repo.find_by_uuid(uuid)

    last_record_story = matches_story_repo.get_last_record_story_by_match_id(match.id)

    tennis = Tennis()
    tennis.deserialize_dict(last_record_story.score, last_record_story.match_status)

    if num_player_scored == '1':
        tennis.player1_goals()
    else:
        tennis.player2_goals()

    match_story_record = MatchStory(id_match=match.id, score=tennis.to_dict(), match_status=tennis.status_to_dict())
    matches_story_repo.add(match_story_record)

    start_response('302 Redirect', [('Location', f'/match-score?uuid={match.uuid}')])
    return ''


@app.route(r'^\/matches', methods=['GET'])
def get_played_matches(request: dict) -> str:
    return '<h1>Get all played match</h1>'
