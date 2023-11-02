
    // Add event listeners to the previous and next buttons
    document.querySelector('.previous-button').addEventListener('click', function() {
      // Get the current page number
      var currentPage = parseInt(document.querySelector('input[name="current_page"]').value);

      // Decrement the current page number
      currentPage--;

      // If the current page number is less than 1, set it to 1
      if (currentPage < 1) {
        currentPage = 1;
      }

      // Set the current page number in the hidden input field
      document.querySelector('input[name="current_page"]').value = currentPage;

      // Show the corresponding page
      document.querySelector('#page-' + currentPage).style.display = 'block';

      // Hide the other pages
      for (var i = 1; i <= 4; i++) {
        if (i !== currentPage) {
          document.querySelector('#page-' + i).style.display = 'none';
        }
      }
    });

    document.querySelector('.next-button').addEventListener('click', function() {
      // Get the current page number
      var currentPage = parseInt(document.querySelector('input[name="current_page"]').value);

      // Increment the current page number
      currentPage++;

      // If the current page number is greater than 4, set it to 4
      if (currentPage > 4) {
        currentPage = 4;
      }

      // Set the current page number in the hidden input field
      document.querySelector('input[name="current_page"]').value = currentPage;
    })
    
    let answer = document.querySelector('Q'+str(i)+'A').value;

    score = 'Q'+str(i)+'A';

