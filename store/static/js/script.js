const toggleBtn = document.querySelector('.toggle');
const navLinks = document.getElementById('navbar-sticky');
const header = document.querySelector('header');
const nav = document.querySelector('nav');
const loading = document.querySelector('.loading');
const overlay = document.querySelector('.overlay');


// handle loading
window.addEventListener('load', () => {
   loading.classList.add('hidden');
   loading.classList.remove('grid');
   if (overlay) {
      overlay.remove();
   }
});


// handle toggle
toggleBtn.addEventListener('click', () => {
   navLinks.classList.toggle('hidden');
   document.querySelector('body').classList.toggle('disableScroll');
   if (window.scrollY == 0) {
      nav.classList.toggle('scrollNav');
      nav.style.padding = '0.5rem 0';
   }
});

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
const handleScrollEvent = () => {
   window.removeEventListener("scroll", handleScrollEvent)
   setTimeout(() => {
      navAnimation()
      window.addEventListener("scroll", handleScrollEvent)
   }, 200)
}
window.addEventListener("scroll", handleScrollEvent)

if (!navigator.share) {
   document.querySelectorAll('.share').forEach(btn => btn.remove());
}

// handle share
const handleShare = (url, title) => {
   if (navigator.share) {
      navigator.share({
         title: title,
         url: url
      })
         .then(() => console.log('Successful share'))
         .catch((error) => console.log('Error sharing', error));
   } else {
      alert('Share not supported');

   }
}



// product details

// Thumbnails and Hero
const thumbnails = document.querySelectorAll(".thumbnails div");
const hero = document.getElementById("hero");

thumbnails.forEach((e) => {
   e.addEventListener("click", () => {
      lightBox(thumbnails, hero, e.id);
   });
});


function lightBox(thumbsLight, heroLight, index) {
   thumbsLight.forEach((e) => {
      e.children[0].classList.remove("active");
      e.classList.remove("ring-active");
   });

   let thumbnailsArray = Array.from(thumbsLight);
   let found = thumbnailsArray.find((e) => e.id == index);

   found.classList.add("ring-active");
   found.children[0].classList.add("active");

   heroLight.src = found.children[0].src;

   heroLight.classList.add("animate-change");
   setTimeout(() => {
      heroLight.classList.remove("animate-change");
   }, 400);
}

const previous = document.getElementById("previous-mobile");
const next = document.getElementById("next-mobile");
next?.addEventListener("click", () => {
   let active = document.querySelector(".thumbnails div.ring-active");
   if (active.nextElementSibling) {
      lightBox(thumbnails, hero, active.nextElementSibling.id);
   } else {
      lightBox(thumbnails, hero, thumbnails[0].id);
   }
});
previous?.addEventListener("click", () => {
   let active = document.querySelector(".thumbnails div.ring-active");
   if (active.previousElementSibling) {
      lightBox(thumbnails, hero, active.previousElementSibling.id);
   } else {
      lightBox(thumbnails, hero, thumbnails[thumbnails.length - 1].id);
   }
});



function decrement(e) {
   const btn = e.target.parentNode.parentElement.querySelector(
      'button[data-action="decrement"]'
   );
   const target = btn.nextElementSibling;
   let value = Number(target.value);
   if (value > 1) {
      value--;
   }
   target.value = value;
}

function increment(e) {
   const btn = e.target.parentNode.parentElement.querySelector(
      'button[data-action="decrement"]'
   );
   const target = btn.nextElementSibling;
   let value = Number(target.value);
   value++;
   target.value = value;
}

const decrementButtons = document.querySelectorAll(
   `button[data-action="decrement"]`
);

const incrementButtons = document.querySelectorAll(
   `button[data-action="increment"]`
);

decrementButtons.forEach(btn => {
   btn.addEventListener("click", decrement);
});

incrementButtons.forEach(btn => {
   btn.addEventListener("click", increment);
});

document.querySelectorAll('.cart-form').forEach(form => {
   form.addEventListener('submit', (e) => {
      e.preventDefault();
      const form = new FormData(e.target);
      const data = {};
      for (const [key, value] of form.entries()) {
         data[key] = value;
      }
      fetch('/api/cart/', {
         method: 'POST',
         body: JSON.stringify(data),
         headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': data['csrfmiddlewaretoken']
         }
      }).then(res => {
         if (res.ok) {
            const span = e.target.querySelector('button[type="submit"] span')
            span.classList.add('scale-100')
            setTimeout(() => {
               span.classList.remove('scale-100')
            }, 1000);
         }
      })
   })
});


const wishlistCounter = document.querySelector('.wishlist-counter')
const handleWishlist = (el) => {
   fetch(el.dataset.url, {
      method: `${el.dataset.isInWishlist ? 'DELETE' : 'POST'}`,
      headers: {
         'Content-Type': 'application/json',
         'X-CSRFToken': el.dataset.csrf,
      }
   }).then(res => res.json()).then(data => {
      if (data.success) {
         if (el.dataset.isInWishlist) {
            wishlistCounter.textContent = parseInt(wishlistCounter.textContent) - 1;
            el.removeAttribute('data-is-in-wishlist')
            el.querySelector('i').classList.remove('text-red-500');
            if (el.dataset.inactiveClass) {
               el.querySelector('i').classList.add(el.dataset.inactiveClass);
            }
            el.querySelector('i').classList.add('scale-150');
         } else {
            wishlistCounter.textContent = parseInt(wishlistCounter.textContent) + 1;
            el.setAttribute('data-is-in-wishlist', true)
            el.querySelector('i').classList.add('text-red-500', 'scale-150');
            if (el.dataset.inactiveClass) {
               el.querySelector('i').classList.remove(el.dataset.inactiveClass);
            }
         }
         setTimeout(() => {
            el.querySelector('i').classList.remove('scale-150');
         }, 200)
      }
   })
}