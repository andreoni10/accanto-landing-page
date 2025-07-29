// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const navMenu = document.getElementById('nav-menu');
    
    mobileMenuBtn.addEventListener('click', function() {
        navMenu.classList.toggle('active');
        mobileMenuBtn.classList.toggle('active');
    });
    
    // Close mobile menu when clicking on links
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navMenu.classList.remove('active');
            mobileMenuBtn.classList.remove('active');
        });
    });
});

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const headerHeight = document.querySelector('.header').offsetHeight;
            const targetPosition = target.offsetTop - headerHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// Active navigation link highlighting
window.addEventListener('scroll', function() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link');
    const headerHeight = document.querySelector('.header').offsetHeight;
    
    let current = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop - headerHeight - 100;
        const sectionHeight = section.offsetHeight;
        
        if (window.pageYOffset >= sectionTop && 
            window.pageYOffset < sectionTop + sectionHeight) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === `#${current}`) {
            link.classList.add('active');
        }
    });
});

// Header background change on scroll
// window.addEventListener('scroll', function() {
//     const header = document.querySelector('.header');
//     if (window.scrollY > 100) {
//         header.style.background = 'rgba(255, 255, 255, 0.98)';
//         header.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
//     } else {
//         header.style.background = 'rgba(255, 255, 255, 0.95)';
//         header.style.boxShadow = 'none';
//     }
// });

// Form submission
// document.querySelector('.contact-form').addEventListener('submit', function(e) {
//     e.preventDefault();
    
//     // Get form data
//     // const formData = new FormData(this);
//     // const name = formData.get('name');
//     // const email = formData.get('email');
//     // const telephone = formData.get('telephone');
    
//     // Simple validation
//     // if (!name || !email || !telephone) {
//     //     alert('Por favor, preencha todos os campos.');
//     //     return;
//     // }
    
//     // Simulate form submission
//     const submitBtn = this.querySelector('button[type="submit"]');
//     const originalText = submitBtn.textContent;
    
//     submitBtn.textContent = 'Enviando...';
//     submitBtn.disabled = true;
    
//     setTimeout(() => {
//         alert('Mensagem enviada com sucesso! Entraremos em contato em breve.');
//         this.reset();
//         submitBtn.textContent = originalText;
//         submitBtn.disabled = false;
//     }, 2000);
// });

// Animate elements on scroll
function animateOnScroll() {
    const cards = document.querySelectorAll('.card');
    const sections = document.querySelectorAll('.section');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    // Initially hide elements
    [...cards, ...sections].forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

// Initialize animations when page loads
document.addEventListener('DOMContentLoaded', animateOnScroll);

// Button hover effects
document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-2px)';
    });
    
    btn.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
    });
});

// Add parallax effect to hero background
window.addEventListener('scroll', function() {
    const hero = document.querySelector('.hero');
    const heroBackground = document.querySelector('.hero-background');
    
    if (hero && heroBackground) {
        const scrolled = window.pageYOffset;
        const parallax = scrolled * 0.5;
        
        heroBackground.style.transform = `translateY(${parallax}px)`;
    }
});

// Utility function to debounce scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Apply debouncing to scroll events
const debouncedScrollHandler = debounce(() => {
    // Re-run scroll-dependent functions
    window.dispatchEvent(new Event('scroll'));
}, 10);

