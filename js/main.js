/**
 * The Uniform Maker - Main JavaScript v2.0
 * Professional, Clean Theme
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

    // Close menu on link click
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

  if (navbar) {
    window.addEventListener('scroll', function() {
      if (window.pageYOffset > 50) {
        navbar.classList.add('navbar-scrolled');
      } else {
        navbar.classList.remove('navbar-scrolled');
      }
    });
  }

  // ===== Scroll Animations =====
  const animateElements = document.querySelectorAll('.animate');

  if (animateElements.length) {
    const observerOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.1
    };

    const observer = new IntersectionObserver(function(entries) {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('fade-in-up');
          entry.target.style.opacity = '1';
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    animateElements.forEach(el => observer.observe(el));
  }

  // ===== Smooth Scroll for anchor links =====
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href !== '#') {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          const offset = 100;
          const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - offset;
          window.scrollTo({ top: targetPosition, behavior: 'smooth' });
        }
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
          field.style.backgroundColor = '#fef2f2';

          const errorId = field.id + '-error';
          if (!document.getElementById(errorId)) {
            const errorMsg = document.createElement('span');
            errorMsg.id = errorId;
            errorMsg.className = 'form-error';
            errorMsg.style.color = '#dc2626';
            errorMsg.style.fontSize = '0.875rem';
            errorMsg.style.marginTop = '4px';
            errorMsg.style.display = 'block';
            errorMsg.textContent = 'Acest câmp este obligatoriu';
            field.parentElement.appendChild(errorMsg);
          }
        } else {
          field.style.borderColor = '';
          field.style.backgroundColor = '';
          const errorMsg = document.getElementById(field.id + '-error');
          if (errorMsg) errorMsg.remove();
        }
      });

      // Email validation
      const emailField = form.querySelector('input[type="email"]');
      if (emailField && emailField.value) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(emailField.value)) {
          isValid = false;
          emailField.style.borderColor = '#dc2626';
        }
      }

      if (!isValid) {
        e.preventDefault();
      }
    });

    // Remove error styles on input
    form.querySelectorAll('input, textarea, select').forEach(field => {
      field.addEventListener('input', function() {
        this.style.borderColor = '';
        this.style.backgroundColor = '';
        const errorMsg = document.getElementById(this.id + '-error');
        if (errorMsg) errorMsg.remove();
      });
    });
  });
});
