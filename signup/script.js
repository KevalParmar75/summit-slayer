 // Toggle visibility to Log In form
 document.getElementById('show-login').addEventListener('click', function (event) {
    event.preventDefault();
    document.getElementById('login').checked = true;
});

// Toggle visibility to Sign Up form
document.getElementById('show-signup').addEventListener('click', function (event) {
    event.preventDefault();
    document.getElementById('signup').checked = true;
});

// Redirect to index.html after successful sign-up or login
document.querySelector('#signup-form form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission
    // Perform your form submission logic here (e.g., AJAX request)
    window.location.href = 'index.html'; // Redirect to index.html
});

document.querySelector('#login-form form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission
    // Perform your form submission logic here (e.g., AJAX request)
    window.location.href = 'index.html'; // Redirect to index.html
});

// Guest Access Button Action
document.getElementById('guest-access-btn').addEventListener('click', function () {
    window.location.href = 'index.html'; // Redirect to index.html
});