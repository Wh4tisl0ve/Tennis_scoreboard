from app.mini_framework import router


# в дальнейшем __init__.py в котором будет app, как во Flask, а роутер импортируется

@router.route(r'^\/new-match', methods=['GET'])
def create_new_match(request: dict):
    return 'Обработка создания нового матча'


@router.route(r'^\/match-score', methods=['GET', 'POST'])
def player_goal(request: dict):
    return '<h1>Обработка забитого мяча игроком<h1>'


@router.route(r'^\/matches', methods=['GET'])
def get_played_matches(request: dict):
    return '<h1>Получить все матчи<h1>'
