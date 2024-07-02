document.addEventListener('DOMContentLoaded', () => {
    const commentsContainer = document.getElementById('comments-container');
    const submitButton = document.getElementById('submit-comment');
    const newCommentField = document.getElementById('new-comment');
    const nameField = document.getElementById('name');

    let comments = Array.from(commentsContainer.children).map(child => child.innerHTML);

    // Function to render comments
    function renderComments() {
        commentsContainer.innerHTML = '';
            const displayedComments = comments;

        displayedComments.forEach(comment => {
            const commentElement = document.createElement('div');
            commentElement.className = 'comment';
            commentElement.innerText = comment;
            commentsContainer.appendChild(commentElement);
        });
    }

    // Function to handle comment submission
    function submitComment() {
        const newComment = newCommentField.value.trim();
        let name = nameField.value.trim()
        if (newComment) {
            comments.unshift(`${name}:${ newComment}`);
            renderComments();
        }
    }


    // Event listener for the submit button
    submitButton.addEventListener('click', submitComment);


    // Initial rendering of comments
    renderComments();
});