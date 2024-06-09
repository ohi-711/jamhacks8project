document.addEventListener('DOMContentLoaded', () => {
    const scoreboard = document.getElementById('scoreboard');

    fetch('/get_scores')
        .then(response => JSON.stringify(response))
        .then(data => {
            scoreboard.innerHTML = data.map(score => `<div>${score}</div>`).join('');
        })
});
