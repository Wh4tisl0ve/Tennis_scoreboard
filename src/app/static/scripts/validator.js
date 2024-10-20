function matchFieldsPlayerName() {
    if (document.getElementById('player1_name').value.trim() ===
        document.getElementById('player2_name').value.trim()) {
        alert('Имена игроков не могут быть идентичны');
        return false;
    } else {
        return true;
    }
}

function checkEmptyString() {
    let player1_name = document.getElementById('player1_name').value;
    let player2_name = document.getElementById('player2_name').value;

    if (!player1_name.trim() || !player2_name.trim()) {
        alert('Имя игрока не может состоять из пробелов');
        return false;
    }
    else{
        return true;
    }

}