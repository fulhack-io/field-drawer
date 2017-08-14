function writeHistory() {
    $.each(localStorage, function(key, value) {
        var history = JSON.parse(localStorage.getItem(key))
        var key_name = key.replace(/( |\(|\(|\)|\+|:)/g, '')
        $('#history').append('<a href="#' + key_name + '" class="btn btn-info" data-toggle="collapse">' + key + '</a></br/><br/>')
        $('#history').append('<div id="' + key_name + '" class="collapse">' + history.result + '<br/><br/></div>')
        console.log(JSON.parse(localStorage.getItem(key)))
    });
}
$(document).ready(function() {
    $('form').submit(function (e) {
        var url = "/draw"; // send the form data here.
        $.ajax({
            type: "POST",
            url: url,
            data: $('form').serialize(), // serializes the form's elements.
            success: function (data) {
                $("#result").text(data.result);
                $('#result-modal').modal('show');
                $("#anchor1").val(data.anchor1);
                $("#anchor2").val(data.anchor2);
                var store_me = { 'anchor1': data.anchor1,
                                 'anchor2': data.anchor2,
                                 'draw_tools_export': data.draw_tools_export,
                                 'result': data.result
                };
                localStorage.setItem(Date(), JSON.stringify(store_me));
                $('#history').html("");
                writeHistory();

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
    writeHistory()
});
