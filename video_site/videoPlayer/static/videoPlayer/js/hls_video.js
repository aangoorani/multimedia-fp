document.addEventListener("DOMContentLoaded", () => {
    const videoPlayer = document.getElementById('player'); // Corrected to get the video element
    const url = videoPlayer.dataset.url;
    let hls = new Hls();
    hls.loadSource(url);
    hls.attachMedia(videoPlayer); // Corrected to use 'videoPlayer' instead of 'video'
    hls.on(Hls.Events.MANIFEST_PARSED, function() {
        videoPlayer.play();
    });
});
