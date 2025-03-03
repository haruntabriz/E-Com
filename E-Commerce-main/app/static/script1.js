//slaider contener

const sliderTrack = document.querySelector('.slider-track');
const slides = document.querySelectorAll('.slide');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');
const dotsContainer = document.querySelector('.slider-controls');
let currentIndex = 0;
let touchStartX = 0;
let touchEndX = 0;

// Create dots
function createDots() {
    dotsContainer.innerHTML = '';
    slides.forEach((_, index) => {
        const dot = document.createElement('div');
        dot.classList.add('slider-dot');
        if(index === currentIndex) dot.classList.add('active');
        dot.addEventListener('click', () => goToSlide(index));
        dotsContainer.appendChild(dot);
    });
}

function updateSlider() {
    sliderTrack.style.transform = `translateX(-${currentIndex * 100}%)`;
    document.querySelectorAll('.slider-dot').forEach((dot, index) => {
        dot.classList.toggle('active', index === currentIndex);
    });
}

function goToSlide(index) {
    currentIndex = (index + slides.length) % slides.length;
    updateSlider();
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
    updateSlider();
}

function prevSlide() {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    updateSlider();
}

// Touch handling
function handleTouchStart(e) {
    touchStartX = e.touches[0].clientX;
}

function handleTouchEnd(e) {
    touchEndX = e.changedTouches[0].clientX;
    if(touchStartX - touchEndX > 50) nextSlide();
    if(touchStartX - touchEndX < -50) prevSlide();
}

// Initialize
createDots();

// Event listeners
nextBtn.addEventListener('click', nextSlide);
prevBtn.addEventListener('click', prevSlide);
sliderTrack.addEventListener('touchstart', handleTouchStart, false);
sliderTrack.addEventListener('touchend', handleTouchEnd, false);

// Responsive handling
let resizeTimer;
window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => {
        sliderTrack.style.transition = 'none';
        updateSlider();
        setTimeout(() => {
            sliderTrack.style.transition = 'transform 0.5s cubic-bezier(0.4, 0, 0.2, 1)';
        }, 10);
    }, 250);
});

// Auto-play
let autoPlay = setInterval(nextSlide, 5000);
sliderTrack.addEventListener('mouseenter', () => clearInterval(autoPlay));
sliderTrack.addEventListener('mouseleave', () => autoPlay = setInterval(nextSlide, 5000));
sliderTrack.addEventListener('touchstart', () => clearInterval(autoPlay));

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if(e.key === 'ArrowLeft') prevSlide();
    if(e.key === 'ArrowRight') nextSlide();
});

//cart added item

//Cart functionality remains the same
        let cart = JSON.parse(localStorage.getItem('cart')) || [];
        
        function addToCart(name, price) {
            cart.push({ 
                id: Date.now(),
                name: name, 
                price: price 
            });
            localStorage.setItem('cart', JSON.stringify(cart));
            updateCartCount();
        }

        function updateCartCount() {
            document.getElementById('cartCount').textContent = cart.length;
        }
        
        // Initialize cart count
        updateCartCount();


    //footer section
    
    function handleSubscribe(event) {
        event.preventDefault();
        const emailInput = event.target.querySelector('.newsletter-input');
        const email = emailInput.value;
        
        if(validateEmail(email)) {
            // Add your subscription logic here
            alert('Thank you for subscribing!');
            emailInput.value = '';
        } else {
            alert('Please enter a valid email address');
        }
    }

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    // Add click handlers for social links
    document.querySelectorAll('.social-link').forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            // Add your social media tracking/redirect logic here
            console.log(`Redirecting to: ${this.href}`);
        });
    });