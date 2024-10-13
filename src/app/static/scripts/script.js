document.addEventListener('keydown', function (event) {
    if (event.code === 'KeyZ') {
        document.getElementById('player1_goal').click();
    }
    if (event.code === 'KeyX') {
        document.getElementById('player2_goal').click();
    }
});

document.addEventListener('DOMContentLoaded', () => checkWinner());

function checkWinner() {
    let match_win_value = 2;

    if (document.getElementById('match_player1').value == match_win_value) {
        document.getElementById('player1_name').classList.add("winner");
        disableButtonsGoals();
    }
    if (document.getElementById('match_player2').value == match_win_value) {
        document.getElementById('player2_name').classList.add("winner");
        disableButtonsGoals();
    }
}

function disableButtonsGoals() {
    let button_player1 = document.getElementById('player1_goal');
    let button_player2 = document.getElementById('player2_goal');

    button_player1.disabled = true;
    button_player1.style.cursor = 'default';

    button_player2.disabled = true;
    button_player2.style.cursor = 'default';
}




