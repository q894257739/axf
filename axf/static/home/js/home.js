$(function () {
    $('.home').width(innerWidth)

     var swiper = new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        slidesPerView: 1,
        paginationClickable: true,
        spaceBetween: 30,
        loop: true,
         autoplay: 3000,
    });

     var swiper = new Swiper('#mustbuySwiper', {
        slidesPerView: 3,
         autoplay: 2000,
    });
})