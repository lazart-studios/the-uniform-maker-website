/**
 * The Uniform Maker - Main JavaScript
 * Navigație mobile și animații simple
 */

document.addEventListener('DOMContentLoaded', function() {
  // ===== Mobile Navigation =====
  const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
  const navLinks = document.querySelector('.nav-links');
  
  if (mobileMenuToggle && navLinks) {
    mobileMenuToggle.addEventListener('click', function() {
      this.classList.toggle('active');
      navLinks.classList.toggle('active');
      document.body.classList.toggle('menu-open');
    });
    
    // Închide meniul la click pe un link
    const navLinksItems = navLinks.querySelectorAll('a');
    navLinksItems.forEach(link => {
      link.addEventListener('click', function() {
        mobileMenuToggle.classList.remove('active');
        navLinks.classList.remove('active');
        document.body.classList.remove('menu-open');
      });
    });
  }
  
  // ===== Navbar scroll effect =====
  const navbar = document.querySelector('.navbar');
  let lastScroll = 0;
  
  window.addEventListener('scroll', function() {
    const currentScroll = window.pageYOffset;
    
    // Adaugă/eliminați clasă pentru navbar transparent pe scroll
    if (currentScroll > 50) {
      navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.08)';
    } else {
      navbar.style.boxShadow = 'none';
    }
    
    lastScroll = currentScroll;
  });
  
  // ===== Scroll Animations =====
  const animateElements = document.querySelectorAll('.animate');
  
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
  };
  
  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Adaugă delay pentru animație staggered
        const delay = entry.target.dataset.delay || 0;
        entry.target.style.animationDelay = delay + 'ms';
        entry.target.style.opacity = '1';
        entry.target.classList.add('fade-in-up');
        
        // Oprește observarea după animație
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  animateElements.forEach(el => observer.observe(el));
  
  // ===== Smooth Scroll pentru anchor links =====
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        const offset = 100; // Offset pentru navbar sticky
        const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
        
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
  
  // ===== Form Validation =====
  const forms = document.querySelectorAll('form');
  
  forms.forEach(form => {
    form.addEventListener('submit', function(e) {
      const requiredFields = form.querySelectorAll('[required]');
      let isValid = true;
      
      requiredFields.forEach(field => {
        if (!field.value.trim()) {
          isValid = false;
          field.style.borderColor = '#dc2626';
          
          // Adaugă mesaj de eroare dacă nu există
          let errorMsg = field.parentElement.querySelector('.error-message');
          if (!errorMsg) {
            errorMsg = document.createElement('span');
            errorMsg.className = 'error-message';
            errorMsg.style.color = '#dc2626';
            errorMsg.style.fontSize = '0.875rem';
            errorMsg.style.marginTop = '4px';
            errorMsg.style.display = 'block';
            errorMsg.textContent = 'Acest câmp este obligatoriu';
            field.parentElement.appendChild(errorMsg);
          }
        } else {
          field.style.borderColor = '';
          const errorMsg = field.parentElement.querySelector('.error-message');
          if (errorMsg) errorMsg.remove();
        }
      });
      
      // Validare email
      const emailField = form.querySelector('input[type="email"]');
      if (emailField && emailField.value) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(emailField.value)) {
          isValid = false;
          emailField.style.borderColor = '#dc2626';
        }
      }
      
      // Validare telefon
      const phoneField = form.querySelector('input[type="tel"]');
      if (phoneField && phoneField.value) {
        const phonePattern = /^[0-9\+\-\s]{10,}$/;
        if (!phonePattern.test(phoneField.value)) {
          isValid = false;
          phoneField.style.borderColor = '#dc2626';
        }
      }
      
      if (!isValid) {
        e.preventDefault();
      }
    });
    
    // Elimină stilul de eroare la input
    form.querySelectorAll('input, textarea').forEach(field => {
      field.addEventListener('input', function() {
        this.style.borderColor = '';
        const errorMsg = this.parentElement.querySelector('.error-message');
        if (errorMsg) errorMsg.remove();
      });
    });
  });
  
  // ===== Counter Animation pentru statistici =====
  const counters = document.querySelectorAll('.stat-item h3');
  
  const counterObserver = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = entry.target;
        const text = target.textContent;
        const number = parseInt(text.replace(/\D/g, ''));
        const suffix = text.replace(/[0-9]/g, '');
        
        if (!isNaN(number)) {
          let current = 0;
          const increment = number / 50;
          const timer = setInterval(() => {
            current += increment;
            if (current >= number) {
              target.textContent = number + suffix;
              clearInterval(timer);
            } else {
              target.textContent = Math.floor(current) + suffix;
            }
          }, 30);
        }
        
        counterObserver.unobserve(target);
      }
    });
  }, { threshold: 0.5 });
  
  counters.forEach(counter => counterObserver.observe(counter));
  
  // ===== Current Year in Footer =====
  const yearElements = document.querySelectorAll('.current-year');
  yearElements.forEach(el => {
    el.textContent = new Date().getFullYear();
  });
});
