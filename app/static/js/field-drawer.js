function writeHistory() {
    $.each(localStorage, function(key, value) {
        var history = JSON.parse(localStorage.getItem(key));
        var key_name = key.replace(/( |\(|\(|\)|\+|:)/g, '');
        $('#history').append('<a href="#' + key_name + '" class="btn btn-info" data-toggle="collapse">' + key + '</a>&nbsp;');
        $('#history').append('<a href="javascript:void(0)" onclick="drawFromHistory(\'' + key + '\');" class="btn btn-primary" data-toggle="collapse">Use</a>&nbsp;');
        $('#history').append('<a href="javascript:void(0)" onclick="deleteHistory(\'' + key + '\');" class="btn btn-danger">Remove</a></br/><br/>');
        $('#history').append('<div id="' + key_name + '" class="collapse">' + history.result + '<br/><br/></div>');
        console.log(JSON.parse(localStorage.getItem(key)))
    });
}
function deleteHistory(key) {
    localStorage.removeItem(key);
    console.log(key);
    $('#history').html("");
    writeHistory();
}

function drawFromHistory(key) {
    var item = JSON.parse(localStorage.getItem(key));
    $("#anchor1").val(item.anchor1);
    $("#anchor2").val(item.anchor2);
    $("#draw_tools_export").val(item.draw_tools_export);
}

$(document).ready(function() {
    var clipboard = new Clipboard('.btn');

    $('form').submit(function (e) {
        var url = "/draw";
        $.ajax({
            type: "POST",
            url: url,
            data: $('form').serialize(),
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
        e.preventDefault();
    });
    // Inject our CSRF token into our AJAX request.
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", "{{ form.csrf_token._value() }}")
            }
        }
    });
    writeHistory()
});
