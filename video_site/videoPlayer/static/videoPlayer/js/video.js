
    document.addEventListener('DOMContentLoaded', () => {
    const commentsContainer = document.getElementById('comments-container');
    const submitButton = document.getElementById('submit-comment');
    const newCommentField = document.getElementById('new-comment');
    const nameField = document.getElementById('name');
    const commentForm = document.getElementById('comment-submission-form');

    let comments = Array.from(commentsContainer.children).map(child => child.innerHTML);

    // Function to render comments
    function renderComments() {
        commentsContainer.innerHTML = '';
        comments.forEach(comment => {
            const commentElement = document.createElement('div');
            commentElement.className = 'comment';
            commentElement.innerText = comment;
            commentsContainer.appendChild(commentElement);
        });
    }

    // Function to handle comment submission via AJAX
    function submitComment(event) {
        event.preventDefault(); // Prevent default form submission

        const newComment = newCommentField.value.trim();
        const name = nameField.value.trim();

        if (newComment && name) {
            const formData = new FormData(commentForm);

            // Send the form data using fetch API
            fetch(commentForm.action, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken'), // Add CSRF token for Django
                },
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                if (data.message === 'Comment submitted successfully!') {
                    comments.unshift(`${name}: ${newComment}`);
                    renderComments();
                    newCommentField.value = ''; // Clear the input field after submission
                    nameField.value = ''; // Clear the name field after submission
                } else {
                    // Handle server-side validation errors or other issues
                    alert('Error submitting comment.');
                }
            })
            .catch(error => console.error('Error:', error));
        }
    }

    // Event listener for the submit button
    submitButton.addEventListener('click', submitComment);

    // Initial rendering of comments
    renderComments();
});
