document.addEventListener('DOMContentLoaded', () => {
    const scoreboard = document.getElementById('scoreboard');

    fetch('/get_scores')
        .then(function(response) {
        return response.json();
        }).then(function(data) {
        console.log(data);
        //scoreboard.innerHTML = res.map(score => `<div>${score}</div>`).join('');
});
})
