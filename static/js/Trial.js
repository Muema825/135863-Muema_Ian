document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault();
   
    var dob = new Date(document.getElementById('dob').value);
 var currentDate = new Date();

 if (dob > currentDate) {
   alert('Date of Birth cannot be greater than the current date.');
 } else {
   // Submit the form
 }
    var gender = document.getElementById('gender').value;
    var description = document.getElementById('description').value;
   
    alert('Age: ' + age + '\nGender: ' + gender + '\nDescription: ' + description);
   });