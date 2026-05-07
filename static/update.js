function addGame() {
    let gameName = document.getElementById('game_name').value
    let year = document.getElementById('year').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'game_name': gameName,
                             'year': year})
    })
    .then(response => {
        if (response.ok) {
            window.location.reload(); // Обновляем страницу после успешного добавления
        }
    })
    .catch(error => console.error('Error:', error));
}

function clearList() {
    fetch('/clear', {
        method: 'DELETE',
        headers: {'Content-Type': 'application/json'}
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        if (data.status === 'success') {
            window.location.reload()
        }
   .catch(error => console.error('Error:', error));
}