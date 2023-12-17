function SendMessage() {
    input_value = $("#input_value").val();
    $.ajax({
        url: "/create_request_chat_bot/text=" + input_value,
        type: "POST",
        dataType: "json",
        success: function (data) {
            $(chat_box).replaceWith(data)
        }
    });
}