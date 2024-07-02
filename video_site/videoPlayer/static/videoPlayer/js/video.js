document.addEventListener('DOMContentLoaded', () => {
    const commentsContainer = document.getElementById('comments-container');
    const submitButton = document.getElementById('submit-comment');
    const newCommentField = document.getElementById('new-comment');
    const nameField = document.getElementById('name')
    const videoPlayer = document.getElementById('main-video-player')

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

        (function () {
        var url = videoPlayer.dataset.url;
        var player = dashjs.MediaPlayer().create();
        player.initialize(document.querySelector("#videoPlayer"), url, true);
    })();

    // Event listener for the submit button
    submitButton.addEventListener('click', submitComment);


    // Initial rendering of comments
    renderComments();
});