// static/js/script.js
function toggleSearch() {
    const searchElement = document.querySelector('.blok_search');
    searchElement.classList.toggle('display_none');
}

function toggleUserMenu() {
    const userMenuElement = document.querySelector('.menu_blok');
    userMenuElement.classList.toggle('menu_blok_none');
}

function toggleMenu() {
    const menuElement = document.querySelector('.menu_blok');
    menuElement.classList.toggle('menu_blok_none');
}


// function toggleFilter() {
    
//     const filterElement = document.querySelector('.menu_blok');
//     filterElement.classList.toggle('menu_blok_none');

// }

function toggleFilter() {
    const aside = document.getElementById('aside');
    
    // Переключение класса hidden
    aside.classList.toggle('hidden');
}




const swiperty = new Swiper('.swiperty', {
  slidesPerView: 1,
  spaceBetween: 0, 
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  breakpoints: {
    640: { 
      slidesPerView: 2,
      spaceBetween: 10, 
    },
    1024: { 
      slidesPerView: 3,
      spaceBetween: 15, 
    },
  },
});

const swipertys = new Swiper('.swiper', {
  slidesPerView: 1,
  spaceBetween: 0, 
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  breakpoints: {
    640: { 
      slidesPerView: 1,
      spaceBetween: 0, 
    },
    1024: { 
      slidesPerView: 3,
      spaceBetween: 0, 
    },
  },
});


const swiper = new Swiper('.mySwipers', {
  slidesPerView: 1,
  spaceBetween: 15, 
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  breakpoints: {
    0: { 
      slidesPerView: 1,
      spaceBetween: 0, 
    },
    640: { 
      slidesPerView: 2,
      spaceBetween: 10, 
    },
    1024: { 
      slidesPerView: 3,
      spaceBetween: 15, 
    },
  },
});




const swipero = new Swiper(".mySwipero", {
  slidesPerView: 1,
  spaceBetween: 20,
  loop: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  breakpoints: {
    740: {
      slidesPerView: 3,
      spaceBetween: 10,
    },
    1024: {
      slidesPerView: 3,
      spaceBetween: 10,
    },
  },
});





const swip = new Swiper('.mySwiper', {
  slidesPerView: 3,
  spaceBetween: 0, 
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
  breakpoints: {
    640: { 
      slidesPerView: 1,
      spaceBetween: 0, 
    },
    1024: { 
      slidesPerView: 3,
      spaceBetween: 0, 
    },
    
  },
});
  
  const swipers = new Swiper('.swiper-container', {
    slidesPerView: 6, 
    spaceBetween: 5, 
    loop: true,  
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        1024: {
          slidesPerView: 6,
        },
        640: {
          slidesPerView: 4,
        },
        0: {
          slidesPerView: 2,
        },
      },
  });

  // const swiperss = new Swiper('.swiper', {
  //   spaceBetween: 30,  
  //   loop: true,  
  //   slidesPerView: 'auto', 
  //   navigation: {
  //     nextEl: '.swiper-button-next',
  //     prevEl: '.swiper-button-prev',
  //   },
  //   breakpoints: {
  //     1024: {
  //       slidesPerView: 3,
  //     },
  //     640: {
  //       slidesPerView: 2,
  //     },
  //     0: {
  //       slidesPerView: 1,
  //     },
  //   },
  // });


  document.querySelectorAll('[data-size]').forEach(button => {
    button.addEventListener('click', () => {
        document.querySelectorAll('[data-size]').forEach(btn => {
            btn.classList.remove('bg-black', 'text-white');
        });

        button.classList.add('bg-black', 'text-white');
    });
});


document.querySelectorAll('.flex .w-8').forEach(color => {
  color.addEventListener('click', () => {
      document.querySelectorAll('.flex .w-8').forEach(item => {
          item.classList.remove('bg-blue-500', 'border-blue-700');
          item.classList.add('bg-green-500');
      });
      color.classList.remove('bg-green-500');
      color.classList.add('bg-blue-500', 'border-blue-700');
  });
});


document.addEventListener("DOMContentLoaded", () => {
  const minusButton = document.querySelector(".flex .text-lg:first-child");
  const plusButton = document.querySelector(".flex .text-lg:last-child");
  const quantityInput = document.querySelector(".flex input[type='text']");

  minusButton.addEventListener("click", () => {
      let value = parseInt(quantityInput.value) || 1;
      if (value > 1) {
          quantityInput.value = value - 1;
      }
  });

  plusButton.addEventListener("click", () => {
      let value = parseInt(quantityInput.value) || 1;
      quantityInput.value = value + 1;
  });

  quantityInput.addEventListener("input", () => {
      let value = parseInt(quantityInput.value) || 1;
      quantityInput.value = value > 0 ? value : 1;
  });
});

function changeMainImage(imageUrl) {
  const mainImage = document.querySelector('[alt="Product Image"]');
  mainImage.src = imageUrl;
}


