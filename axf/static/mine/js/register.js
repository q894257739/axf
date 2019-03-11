$(function () {
    $('.register').width(innerWidth)

    var reg = new RegExp("^[a-z0-9A-Z]+[- | a-z0-9A-Z . _]+@([a-z0-9A-Z]+(-[a-z0-9A-Z]+)?\\.)+[a-z]{2,}$")

    $('#email-v').blur(function () {

        if ($('#email-v').val() == '') {
            $('#email-v').popover('hide')
            $('#email').removeClass('has-success')
            $('#email').removeClass('has-error')
            $('#email-t').removeClass('glyphicon-ok')
            $('#email-t').removeClass('glyphicon-remove')
            return
        }

        if (reg.test($('#email-v').val())) {

            request_data = {
                'email': $('#email-v').val()
            }
            $.get('/axf/checkemail/', request_data, function (response) {
                if (response.status == 1) {
                    $('#email-v').attr('data-content', response.msg)
                    $('#email').removeClass('has-error').addClass('has-success')
                    $('#email-t').removeClass('glyphicon-remove').addClass('glyphicon-ok')
                    $('#email-v').popover('hide')
                } else {
                    $('#email-v').attr('data-content', response.msg)
                    $('#email-v').popover('show')
                    $('#email').removeClass('has-success').addClass('has-error')
                    $('#email-t').removeClass('glyphicon-ok').addClass('glyphicon-remove')
                }
            })
        } else {
            $('#email-v').popover('show')
            $('#email').removeClass('has-success').addClass('has-error')
            $('#email-t').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })

    var p_reg = new RegExp('^(?:\\d+|[a-zA-Z]+|[!@#$%^&*]+)$')

    $('#password-v').blur(function () {
        if ($('#password-v').val() == '') {
            $('#password-v').attr('data-content', '密码不能为空')
            $('#password-v').popover('show')
            $('#password').removeClass('has-success').addClass('has-error')
            $('#password-t').removeClass('glyphicon-ok').addClass('glyphicon-remove')
            return
        }
        if (p_reg.test($('#password-v').val())) {

            if ($('#password-v').val() == '') {
                return
            }

            if ($('#password-v').val().length >= 3 && $('#password-v').val().length <= 10) {
                $('#password').removeClass('has-error').addClass('has-success')
                $('#password-t').removeClass('glyphicon-remove').addClass('glyphicon-ok')
                $('#password-v').popover('hide')
            } else {
                $('#password').removeClass('has-success').addClass('has-error')
                $('#password-t').removeClass('glyphicon-ok').addClass('glyphicon-remove')
            }
        }
    })


    $('#password-v,#password-v2').blur(function () {

        if ($('#password-v2').val() == '') {
            return
        }

        var pass1 = $('#password-v').val()
        var pass2 = $('#password-v2').val()
        if (pass1 == pass2) {
            $('#password-v2').popover('hide')
            $('#password2').removeClass('has-error').addClass('has-success')
            $('#password-t2').removeClass('glyphicon-remove').addClass('glyphicon-ok')
            $('#password-v2').popover('hide')
        } else {
            $('#password-v2').attr('data-content', "两次输入密码不一致")
            $('#password-v2').popover('show')
            $('#password2').removeClass('has-success').addClass('has-error')
            $('#password-t2').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })


    $('#password-v,#password-v2').blur(function () {

        if ($('#password-v2').val() == '') {
            return
        }

        var pass1 = $('#password-v').val()
        var pass2 = $('#password-v2').val()
        if (pass1 == pass2) {
            $('#password-v2').popover('hide')
            $('#password2').removeClass('has-error').addClass('has-success')
            $('#password-t2').removeClass('glyphicon-remove').addClass('glyphicon-ok')
            $('#password-v2').popover('hide')
        } else {
            $('#password-v2').attr('data-content', "两次输入密码不一致")
            $('#password-v2').popover('show')
            $('#password2').removeClass('has-success').addClass('has-error')
            $('#password-t2').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })

    $('#name-v').blur(function () {
        if ($(this).val() == '') {
            $('#name-v').popover('hide')
            return
        }

        if ($(this).val().length >= 2 && $(this).val().length <= 8) {
            $('#name').removeClass('has-error').addClass('has-success')
            $('#name-t').removeClass('glyphicon-remove').addClass('glyphicon-ok')
            $('#name-v').popover('hide')
        } else {
            $('#name-v').attr('data-content', "请输入2-8个字符")
            $('#name-v').popover('show')
            $('#name').removeClass('has-success').addClass('has-error')
            $('#name-t').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })


    $('#subButton').click(function () {
        var isregister = true
        $('.form-group').each(function () {
            if (!$(this).is('.has-success')) {
                isregister = false
                console.log(isregister)

            }
        })
        if (isregister) {
            $('#form').submit()
        }
    })
})