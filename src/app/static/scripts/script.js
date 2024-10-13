document.addEventListener('keydown', function (event) {
    if (event.code === 'KeyZ') {
        document.getElementById('player1_goal').click();
    }
    if (event.code === 'KeyX') {
        document.getElementById('player2_goal').click();
    }
});


function clickButtonGoalHandler(player_id_goal) {
    let player1_name = document.getElementById('player1_name');
    let player2_name = document.getElementById('player2_name');

    let player1_match = document.getElementById('match_player1');
    let player2_match = document.getElementById('match_player2');
    alert(player1_match.value + " " + player2_match.value)
}




