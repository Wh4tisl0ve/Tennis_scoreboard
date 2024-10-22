document.addEventListener('keydown', function (event) {
    if (event.code === 'KeyZ') {
        document.getElementById('player1_goal').click();
    }
    if (event.code === 'KeyX') {
        document.getElementById('player2_goal').click();
    }
});

document.addEventListener('DOMContentLoaded', () => renderEndGame(getWinnerId()));

function renderEndGame(winner_id) {
    const enemy_dict = {
        1: 2, 2: 1
    }

    if (winner_id !== 0) {
        document.getElementById(`player${winner_id}_name`).classList.add("winner");
        document.getElementById(`player${enemy_dict[winner_id]}_row`).classList.add("looser");
        document.getElementById('status_game_title').textContent = 'Завершена'

        disableButtonsGoals();
    }
}


function getWinnerId() {
    let match_win_value = 2;

    if (document.getElementById('match_player1').value == match_win_value) {
        return 1;
    }

    if (document.getElementById('match_player2').value == match_win_value) {
        return 2;
    }

    return 0;
}

function disableButtonsGoals() {
    let button_player1 = document.getElementById('player1_goal');
    let button_player2 = document.getElementById('player2_goal');

    button_player1.disabled = true;
    button_player1.style.cursor = 'default';

    button_player2.disabled = true;
    button_player2.style.cursor = 'default';
}




