document.addEventListener('DOMContentLoaded', () => {
    const videoPlayer = document.getElementById('player'); // Corrected to get the video element

    if (!videoPlayer) {
        // console.error('Video player element not found');
        return;
    }

    const url = videoPlayer.dataset.url;
    console.log(url)
    const player = dashjs.MediaPlayer().create();
    player.initialize(videoPlayer, url, true);
});
