  var carouselItems = document.querySelectorAll('.carousel-item');
  var currentSlide = 0;
  var slideInterval = setInterval(nextSlide, 3000);

  function nextSlide() {
    carouselItems[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + 1) % carouselItems.length;
    carouselItems[currentSlide].classList.add('active');
  }