document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Animate sections on scroll
    const sections = document.querySelectorAll('.section');
    
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'all 0.6s cubic-bezier(0.22, 1, 0.36, 1)';
        observer.observe(section);
    });

    // Dynamic background gradient movement
    const background = document.querySelector('.shapes');
    let angle = 0;

    function moveGradient() {
        angle = (angle + 0.2) % 360;
        background.style.background = `
            radial-gradient(circle at ${50 + Math.sin(angle * Math.PI / 180) * 10}% ${50 + Math.cos(angle * Math.PI / 180) * 10}%, var(--secondary-color) 0%, transparent 20%),
            radial-gradient(circle at ${80 + Math.cos(angle * Math.PI / 180) * 10}% ${20 + Math.sin(angle * Math.PI / 180) * 10}%, var(--primary-color) 0%, transparent 20%)
        `;
        requestAnimationFrame(moveGradient);
    }

    moveGradient();
});
