
// This code adds the class 'active' to the hovered element in the navbar
// It also animates the navbar on scroll

// Add the 'active' class to the hovered element
// When the mouse enters the navbar-item element, add the class 'active' to it
$('.navbar-item').hover(addActiveClass, removeActiveClass);

function addActiveClass() {
    $(this).addClass('active');
}

function removeActiveClass() {
    $(this).removeClass('active');
}

// Animate the navbar on scroll
// When the user scrolls the page, execute this function
$(window).scroll(animateNavbar);

function animateNavbar() {
    // If the user has scrolled more than 50 pixels from the top of the page
    if ($(this).scrollTop() > 50) {
        // Add the class 'navbar-scroll' to the navbar
        $('.navbar').addClass('navbar-scroll');
    } else {
        // If the user has scrolled less than 50 pixels from the top of the page
        // Remove the class 'navbar-scroll' from the navbar
        $('.navbar').removeClass('navbar-scroll');
    }
}
