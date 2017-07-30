$(document).ready(function() {
    $('form').submit(function (e) {
        var url = "/draw"; // send the form data here.
        $.ajax({
            type: "POST",
            url: url,
            data: $('form').serialize(), // serializes the form's elements.
            success: function (data) {
                $("#result").text(data.result),
                $('#myModal').modal('show'),
                $("#anchor1").val(data.anchor1);
                $("#anchor2").val(data.anchor2);
            },
            error: function(error){
                console.log(error);
            }
        });
        e.preventDefault(); // block the traditional submission of the form.
    });
    // Inject our CSRF token into our AJAX request.
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", "{{ form.csrf_token._value() }}")
            }
        }
    });
    var clipboard = new Clipboard('.btn');
});

