// Function to adjust page size based on screen width
function adjustPageSize() {
    const width = window.innerWidth;

    if (width >= 992 && width <= 1600) {
        document.body.style.transform = "scale(0.9)";
    } else if (width >= 700 && width <= 767) {
        document.body.style.transform = "scale(0.8)";
    } else if (width >= 600 && width < 700) {
        document.body.style.transform = "scale(0.75)";
    } else if (width <= 600) {
        document.body.style.transform = "scale(0.5)";
    } else {
        document.body.style.transform = "scale(1)";
    }
}

// Adjust page size on window resize
window.addEventListener('resize', adjustPageSize);

// Initial call to adjust page size based on current screen width
adjustPageSize();

// Toggle Left Menu Collapse
const toggleBtn = document.querySelector('.toggle-btn');
const leftMenu = document.querySelector('.left-menu');

toggleBtn.addEventListener('click', () => {
    leftMenu.classList.toggle('collapsed');
});
