// Wait for page to load
document.addEventListener('DOMContentLoaded', function() {

    // Select inputs and buttom
    const name = document.querySelector('#name');
    const newEmail = document.querySelector('#email');
    const submit = document.querySelector('#submit');

    submit.disabled = true;

    // Listen for input for name and email, but don't disable until email has been provided 
    name.onkeyup = () => {
        if (name.nodeValue.length > 0) {
            submit.disabled = true;
        }
        else {
            submit.disabled = true;
        }
    }
    newEmail.onkeyup = () => {
        if (email.nodeValue.length > 0) {
            submit.disabled = false;
        }
        else {
            submit.disabled = true;
        }
    }

    // Listen for submission 
    document.querySelector('form').onsubmit = () => {

        const subscribe = newEmail.value;

        // Create list of new subscribers and append the item
        const sub_list = document.createElement('sub_list');
        sub_list.innerHTML = subscribe;

        document.querySelector('#subscriptions').append('sub_list');

        // Clear form 
        name.value = '';
        newEmail.value = '';

        submit.disabled = true;
        return false;
    }
});