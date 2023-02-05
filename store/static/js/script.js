const toggleBtn = document.querySelector('.toggle');
const navLinks = document.getElementById('navbar-sticky');
const header = document.querySelector('header');
const nav = document.querySelector('nav');
const loading = document.querySelector('.loading');


// handle loading
window.addEventListener('load', () => {
   loading.classList.add('hidden');
   loading.classList.remove('grid');
});


// handle toggle
toggleBtn.addEventListener('click', () => {
   navLinks.classList.toggle('hidden');
   document.querySelector('body').classList.toggle('disableScroll');
   if (window.scrollY == 0) {
      nav.classList.toggle('scrollNav');
      nav.style.padding = '0.5rem 0';
   }
   }
);

// handle nav animation
const navAnimation = () => {
   if (window.scrollY > 0) {
      nav.style.padding = '0.5rem 0';
      nav.classList.add('scrollNav');
      
   } else {
      nav.classList.remove('scrollNav');
      nav.style.padding = '1rem 0';
   }
};
navAnimation();

// handle scroll
window.addEventListener('scroll', () => {
   navAnimation();
});