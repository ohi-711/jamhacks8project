document.addEventListener('DOMContentLoaded', function() {
    const texts = document.querySelectorAll('.text');
    const prompt = document.getElementById('prompt');
    let index = 0;
  
    // Display the first sentence and prompt initially
    texts[index].classList.add('visible');
    prompt.style.display = 'block';
  
    // Listen for spacebar key press to move to the next sentence
    document.addEventListener('keydown', function(event) {
      if (event.keyCode === 32) { // Spacebar key code
        // Hide the current sentence
        texts[index].classList.remove('visible');
        
        // Move to the next sentence
        index++;
        if (index < texts.length) {
          // Display the next sentence
          texts[index].classList.add('visible');
        } else {
          // If all sentences are displayed, hide the prompt
          prompt.style.display = 'none';
          console.log('All sentences displayed.');
        }
      }
    });
  });
  