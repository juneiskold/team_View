document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.video-wrapper').forEach(wrapper => {
        const video = wrapper.querySelector('video');

        wrapper.addEventListener('mouseenter', () => {
            video.play(); // Play the video on hover
        });

        wrapper.addEventListener('mouseleave', () => {
            video.pause(); // Pause and reset the video on mouse leave
            video.currentTime = 0;
        });
    });
});