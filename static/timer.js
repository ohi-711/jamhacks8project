document.addEventListener('DOMContentLoaded', function() {
    const timer = document.getElementById('timer');
    const roundOver = document.getElementById('roundOver');
  
    let seconds = 60;
  
    // Function to update the timer every second
    function updateTimer() {
      timer.textContent = seconds;
  
      if (seconds === 0) {
        // Display the "Round Over!" screen when the timer reaches 0
        roundOver.style.display = 'block';
        clearInterval(interval); // Stop the countdown
      } else {
        seconds--;
      }
    }
  
    // Call updateTimer function every second
    const interval = setInterval(updateTimer, 1000);
  });
  