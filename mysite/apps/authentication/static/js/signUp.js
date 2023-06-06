$(document).ready(() => {
    csrf()
    signUpForm()
})

function csrf() {
    function getCookie(name) {
        var cookieValue = null;

        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $.ajaxSetup({
        headers:{
           'X-CSRFToken': getCookie("csrftoken")
        }
     });
}

function signUpForm() {
    const formId = 'form#signUp';
    const formBut = '#form-submit'

    $(formId).on('submit', (e) => {
        e.preventDefault();
        $.ajax({
            url: 'signUp',
            type: 'POST',
            dataType: 'json',
            data: {
                username: $(formId + ' #id_username').val(),
                first_name: $(formId + ' #id_first_name').val(),
                last_name: $(formId + ' #id_last_name').val(),
                email: $(formId + ' #id_email').val(),
                phoneNumber: $(formId + ' #id_phoneNumber').val(),
                password: $(formId + ' #id_password').val(),
                password2: $(formId + ' #id_password2').val(),
            },
            success: function (data) {
                if ('errors' in data) {
                    $(formId + ' .message-error').each((index, el) => {
                        $(el).remove();
                    });
                    $(formId + ' .invalid-data').each((index, e2) => {
                        $(e2).removeClass('invalid-data');
                    });

                    for (let key in data['errors']) {
                        let result = '';
                        if (key == '__all__') {
                            $(formId).find('input#id_password').addClass('invalid-data');
                            $(formId).find('input#id_password2').addClass('invalid-data');

                            $(formId).find('#id_password2').after(() => {
                                for (let k in data['errors'][key]) {
                                    result += data['errors'][key][k] + '<br>';
                                }
                                return '<div class="message-error">' + result + '</div>'
                            })

                        }
                        else {
                            $(formId).find('input[name="' + key + '"]').addClass('invalid-data');
                            $(formId).find('input[name="' + key + '"]').after(() => {


                                for (let k in data['errors'][key]) {
                                    result += data['errors'][key][k] + '<br>';
                                }

                                return '<div class="message-error">' + result + '</div>'
                            });

                        }

                    }
                }
                if ('success' in data) {
                    $(formId + ' .message-error').each((index, el) => {
                        $(el).remove();
                    });
                    $(formId + ' .valid-data').each((index, e2) => {
                        $(e2).removeClass('valid-data');
                    });
                    $(formId + ' input').each((index, e2) => {
                        $(e2).addClass('valid-data');
                    });
                    window.location.replace("/");
                }
            },
            error: function (data) {
                console.log('Server Error')
            }
        })
    });
}