function apply_form_field_error(fieldname, error) {
	var input = $("#id_" + fieldname),
		container = $("#div_id_" + fieldname),
		error_msg = $("<span />").addClass("help-inline ajax-error").text(error[0]);

	container.addClass("error");
	error_msg.insertAfter(input);
}

function clear_form_field_errors(form) {
	$(".ajax-error", $(form)).remove();
	$(".error", $(form)).removeClass("error");
}

function django_message(msg, level) {
	var levels = {
		warning: 'alert',
		error: 'error',
		success: 'success',
		info: 'info'
	},
	source = $('#message_template').html(),
	template = Handlebars.compile(source),
	context = {
		'tags': levels[level],
		'message': msg
	},
	html = template(context);

	$("#message_area").append(html);
}

function django_block_message(msg, level) {
	var source = $("#message_block_template").html(),
		template = Handlebars.compile(source),
		context = {level: level, body: msg},
		html = template(context);

	$("#message_area").append(html);
}

$(document).on("submit", "#inquiry_form", function(e) {
	e.preventDefault();
	var csrftoken = $("[name=csrfmiddlewaretoken]").val();
	var self = $(this),
		url = self.attr("action"),
		ajax_req = $.ajax({
			url: url,
			type: "POST",
			data: {
				first_name: self.find("#id_first_name").val(),
				last_name: self.find("#id_last_name").val(),
				email_address: self.find("#id_email_address").val(),
				csrfmiddlewaretoken: csrftoken
			},
			success: function(data, textStatus, jqXHR) {
				console.log(data);
				if (data.first_name) {
					message = data.first_name + ", thanks for your interest. We received your inquiry and will be in touch shortly.";
				} else {
					message = "Thanks for your interest. We received your inquiry and will be in touch shortly.";
				}
				django_message(message, "success");
			},
			error: function(data, textStatus, jqXHR) {
				console.log("Error: Could not submit inquiry: ", data);
				var errors = $.parseJSON(data.responseText);
				$.each(errors, function(index, value) {
					if (index === "__all__") {
						django_message(value[0], "error");
					} else {
						apply_form_field_error(index, value);
					}
				});
			}
		});
});
