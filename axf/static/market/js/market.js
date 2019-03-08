$(function () {

    $('.market').width(innerWidth)

    var index = $.cookie('index')
    if(index){
        $('.type-slider li').eq(index).addClass('active')
    }else{
        $('.type-slider li:first').addClass('active')
    }

    $('.type-slider li').click(function () {
        $.cookie('index',$(this).index())
    })
    
    var categoryShow  = false
    $('.category-view').click(function () {
        categoryShow = !categoryShow
        categoryShow ? categoryViewShow() : categoryViewHide()
    })

    var sortShow = false
    $('.sort-view').click(function () {
        sortShow = !sortShow
        sortShow ? sortViewShow() : sortViewHide()
    })
    
    function categoryViewShow() {
        $('#category-bt').show()
        sortViewHide()
        sortShow = false
        $('.category-view i').removeClass('glyphicon-menu-up').addClass('glyphicon-menu-down')
    }

    function categoryViewHide() {
        $('#category-bt').hide()
        $('.category-view i').removeClass('glyphicon-menu-down').addClass('glyphicon-menu-up')
    }

    function sortViewShow() {
        $('#sort-bt').show()
        categoryViewHide()
        categoryShow = false
        $('.sort-view i').removeClass('glyphicon-menu-up').addClass('glyphicon-menu-down')
    }

    function sortViewHide() {
        $('#sort-bt').hide()
        $('.sort-view i').removeClass('glyphicon-menu-down').addClass('glyphicon-menu-up')
    }

    $('.bounce-view').click(function () {
        $('.bounce-view').hide()
    })
})