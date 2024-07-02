document.addEventListener('DOMContentLoaded', () => {

        const videoPlayer = document.getElementById('main-video-player');

        (function () {
        var url = videoPlayer.dataset.url;
        var player = dashjs.MediaPlayer().create();
        player.initialize(videoPlayer, url, true);
    })();


});