document.addEventListener("DOMContentLoaded", () => {
    const cursor = document.querySelector(".custom-cursor");
    const trail = document.querySelector(".cursor-trail");

    const hoverTargets = document.querySelectorAll('button, a, .hover-target');

    hoverTargets.forEach(el => {
      el.addEventListener('mouseenter', () => {
        customCursor.classList.add('glow');
        cursorTrail.classList.add('glow');
      });

      el.addEventListener('mouseleave', () => {
        customCursor.classList.remove('glow');
        cursorTrail.classList.remove('glow');
      });
    });

    // Update positions on mouse move (always include the centering offset)
    document.addEventListener("mousemove", (e) => {
      const baseTransform = `translate(${e.clientX}px, ${e.clientY}px) translate(-50%, -50%)`;
      cursor.style.transform = baseTransform;
      // Apply scale based on whether click-zoom is active
      if (trail.classList.contains("click-zoom")) {
        trail.style.transform = `${baseTransform} scale(2)`;
      } else {
        trail.style.transform = `${baseTransform} scale(1)`;
      }
    });

    // Toggle zoom on mouse down/up
    document.addEventListener("mousedown", () => {
      trail.classList.add("click-zoom");
    });
    document.addEventListener("mouseup", () => {
      trail.classList.remove("click-zoom");
    });

    // Click Effect: expanding circle at click location
    document.addEventListener("click", (e) => {
      const clickEffect = document.createElement("div");
      clickEffect.classList.add("click-effect");
      clickEffect.style.left = `${e.clientX}px`;
      clickEffect.style.top = `${e.clientY}px`;
      document.body.appendChild(clickEffect);
      setTimeout(() => {
        clickEffect.remove();
      }, 500);
    });

    // Magnetic effect on hover for buttons and elements with class "magnetic"
    document.querySelectorAll("button, .magnetic").forEach((el) => {
      el.addEventListener("mousemove", (e) => {
        const rect = el.getBoundingClientRect();
        const offsetX = e.clientX - rect.left - rect.width / 2;
        const offsetY = e.clientY - rect.top - rect.height / 2;
        const transformValue = `translate(${e.clientX + offsetX}px, ${e.clientY + offsetY}px) translate(-50%, -50%)`;
        cursor.style.transform = transformValue;
        if (trail.classList.contains("click-zoom")) {
          trail.style.transform = `${transformValue} scale(2)`;
        } else {
          trail.style.transform = `${transformValue} scale(1)`;
        }
      });

      // Use the event parameter in mouseleave so the code works correctly
      el.addEventListener("mouseleave", (e) => {
        const transformValue = `translate(${e.clientX}px, ${e.clientY}px) translate(-50%, -50%)`;
        cursor.style.transform = transformValue;
        if (trail.classList.contains("click-zoom")) {
          trail.style.transform = `${transformValue} scale(2)`;
        } else {
          trail.style.transform = `${transformValue} scale(1)`;
        }
      });

      // Optional: Button click pulse effect on the element itself
      el.addEventListener("click", (e) => {
        const pulseEffect = document.createElement("div");
        pulseEffect.classList.add("click-effect");
        pulseEffect.style.left = `${e.offsetX}px`;
        pulseEffect.style.top = `${e.offsetY}px`;
        el.appendChild(pulseEffect);
        setTimeout(() => {
          pulseEffect.remove();
        }, 500);
      });
    });
    document.addEventListener("DOMContentLoaded", function () {
      let images = document.querySelectorAll(".image-gallery img");
      let index = 0;
    
      function showNextImage() {
          images[index].style.display = "none";
          index = (index + 1) % images.length;
          images[index].style.display = "block";
      }
    
      setInterval(showNextImage, 3000); // Change image every 3 seconds
    });
  });

  function handleScrollFadeIn() {
    const fadeIns = document.querySelectorAll('.fade-in');
    fadeIns.forEach(item => {
      const rect = item.getBoundingClientRect();
      const windowHeight = window.innerHeight || document.documentElement.clientHeight;
      // Adjust "trigger" point as needed (e.g., 100px from bottom of viewport)
      if (rect.top <= windowHeight - 100) {
        item.classList.add('visible');
      }
    });
  }

  // Run on scroll and on page load
  window.addEventListener('scroll', handleScrollFadeIn);
  window.addEventListener('load', handleScrollFadeIn);

  document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".service-card");
  
    cards.forEach((card, index) => {
      card.style.animationDelay = `${index * 0.2}s`; // Staggered delay effect
    });
  });
  document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".service-card");
    
    // Apply a staggered animation delay for each card
    cards.forEach((card, index) => {
      card.style.animationDelay = `${index * 0.2}s`;
    });
  });
    
document.addEventListener('DOMContentLoaded', function(){
  // List of icon classes (without the "fa" prefix since it's added in the code)
  var icons = [
    'fa-book',
    'fa-graduation-cap',
    'fa-university',
    'fa-pencil-alt',
    'fa-chalkboard-teacher',
    'fa-school',
    'fa-user-graduate',
    'fa-laptop',
    'fa-microscope',
    'fa-pen',
    'fa-globe',
    'fa-flask',
    'fa-calculator',
    'fa-book-open',
    'fa-chalkboard',
    'fa-lightbulb',
    'fa-folder-open',
    'fa-highlighter',
    'fa-brain',
    'fa-scroll'
  ];
  
  // Select all timeline icon elements
  var timelineIcons = document.querySelectorAll('.timeline-icon');
  
  timelineIcons.forEach(function(el){
    // Pick a random icon from the list
    var randomIcon = icons[Math.floor(Math.random() * icons.length)];
    // Insert the icon element; note the "fa" class is added along with the random class
    el.innerHTML = '<i class="fa ' + randomIcon + '"></i>';
  });
});

document.querySelectorAll('.education-item').forEach((item, index) => {
  item.style.animationDelay = `${index * 0.2}s`;
});

document.querySelectorAll('.timeline-content').forEach((item, index) => {
  item.style.animationDelay = `${index * 0.2}s`;
});
document.querySelectorAll('.project-card').forEach((item, index) => {
  item.style.animationDelay = `${index * 0.2}s`;
});


document.addEventListener('DOMContentLoaded', function(){
  // List of FontAwesome icon classes for work experience
  var icons = [
    'fa-briefcase',
    'fa-laptop-code',
    'fa-chart-line',
    'fa-cogs',
    'fa-lightbulb',
    'fa-user-tie',
    'fa-network-wired',
    'fa-building'
  ];
  
  // Select all timeline-icon elements
  var timelineIcons = document.querySelectorAll('.worktimeline-icon');
  
  timelineIcons.forEach(function(el){
    // Randomly select an icon from the list
    var randomIcon = icons[Math.floor(Math.random() * icons.length)];
    // Inject the FontAwesome icon into the timeline-icon container
    el.innerHTML = '<i class="fa ' + randomIcon + '"></i>';
  });
});




console.log("Inline JavaScript is working!");
        
if (localStorage.getItem('darkMode') === 'enabled') {
    document.body.classList.add('dark-mode');
    document.getElementById('modeIcon').classList.remove('bi-cloud-sun');
    document.getElementById('modeIcon').classList.add('bi-moon');
}

document.getElementById("darkModeToggle").addEventListener("click", function() {
    const isDarkMode = document.body.classList.toggle("dark-mode");

    const modeIcon = document.getElementById("modeIcon");
    if (isDarkMode) {
        modeIcon.classList.remove("bi-cloud-sun");
        modeIcon.classList.add("bi-moon");
        localStorage.setItem("darkMode", "enabled");
    } else {
        modeIcon.classList.remove("bi-moon");
        modeIcon.classList.add("bi-cloud-sun");
        localStorage.removeItem("darkMode");
    }
});


document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll(".home-edu");

    const observerOptions = {
        root: null,
        rootMargin: "0px",
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Activate the main section
                entry.target.classList.add("active");

                // Activate the internal effects
                entry.target.querySelectorAll(".effect-wrapper").forEach(effectElement => {
                    effectElement.classList.add("start-effect");
                });

                // Stop observing once active
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    sections.forEach(section => observer.observe(section));
});


document.addEventListener("DOMContentLoaded", function () {
  const heroSection = document.getElementById("hero");
  const navLink = document.querySelector('a[href="#hero"]');

  window.addEventListener("scroll", function () {
    const rect = heroSection.getBoundingClientRect();
    if (rect.top <= 50 && rect.bottom >= 50) {
      navLink.classList.add("active");
    } else {
      navLink.classList.remove("active");
    }
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const heroSection = document.getElementById("educationpage");
  const navLink = document.querySelector('a[href="#educationpage"]');

  window.addEventListener("scroll", function () {
    const rect = heroSection.getBoundingClientRect();
    if (rect.top <= 50 && rect.bottom >= 50) {
      navLink.classList.add("active");
    } else {
      navLink.classList.remove("active");
    }
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const heroSection = document.getElementById("skillspage");
  const navLink = document.querySelector('a[href="#skillspage"]');

  window.addEventListener("scroll", function () {
    const rect = heroSection.getBoundingClientRect();
    if (rect.top <= 50 && rect.bottom >= 50) {
      navLink.classList.add("active");
    } else {
      navLink.classList.remove("active");
    }
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const heroSection = document.getElementById("projectpage");
  const navLink = document.querySelector('a[href="#projectpage"]');

  window.addEventListener("scroll", function () {
    const rect = heroSection.getBoundingClientRect();
    if (rect.top <= 50 && rect.bottom >= 50) {
      navLink.classList.add("active");
    } else {
      navLink.classList.remove("active");
    }
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const heroSection = document.getElementById("servicespage");
  const navLink = document.querySelector('a[href="#servicespage"]');

  window.addEventListener("scroll", function () {
    const rect = heroSection.getBoundingClientRect();
    if (rect.top <= 50 && rect.bottom >= 50) {
      navLink.classList.add("active");
    } else {
      navLink.classList.remove("active");
    }
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const heroSection = document.getElementById("contactpage");
  const navLink = document.querySelector('a[href="#contactpage"]');

  window.addEventListener("scroll", function () {
    const rect = heroSection.getBoundingClientRect();
    if (rect.top <= 50 && rect.bottom >= 50) {
      navLink.classList.add("active");
    } else {
      navLink.classList.remove("active");
    }
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const heroSection = document.getElementById("educationpage");
  const navLink = document.querySelector('a[href="#educationpage"]');

  window.addEventListener("scroll", function () {
    const rect = heroSection.getBoundingClientRect();
    if (rect.top <= 50 && rect.bottom >= 50) {
      navLink.classList.add("active");
    } else {
      navLink.classList.remove("active");
    }
  });
});
