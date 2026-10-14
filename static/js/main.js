$(document).ready(() => {
	console.log("main.js");
	animateLandingImage();

	$(".nav-link:not(.dropdown-toggle)").click(function() {
		console.log("clicked", this);
		$(".navbar-collapse").collapse("hide");
		$(this).addClass('active');
	});

	//////////////////////////////////////
	$("#form-submit").click((e) => {
		console.log("form-submit");
		e.preventDefault();
		
		var form = document.getElementById("form");
		const formData = new FormData(form);
		
		if (!form.checkValidity()) {
			// Force native browser validation popups if fields are missing
			var tmpSubmit = document.createElement("button");
			form.appendChild(tmpSubmit);
			tmpSubmit.click();
			form.removeChild(tmpSubmit);
		} else {
			// Collect form data cleanly
			var data = {};
			formData.forEach(function (value, key) {
				data[key] = value;
			});
			
			var url = form.getAttribute("action") || "/en/";
	
			fetch(url, {
				method: "POST",
				credentials: "same-origin",
				headers: {
					"Content-Type": "application/json", // Tells Django to parse this as structured JSON data
					"X-Requested-With": "XMLHttpRequest",
					"X-CSRFToken": getCookie("csrftoken"),
				},
				body: JSON.stringify(data),
			}).then((response) => {
				console.log("Response metadata received: ", response);
				
				if (response.ok) {
					// SUCCESS OPTION: Completely fade out the form elements and substitute the message box
					$("#form").fadeOut(400, function() {
						// This locates your wrapper div and swaps the inner content seamlessly
						$(".form-wrapper").html(`
							<div class="message-wrapper text-center p-4" style="background-color: #f4fdf7; border: 1px solid #c3e6cb; border-radius: 4px;">
								<h4 style="color: #155724; margin-bottom: 10px;">✔ Message Sent Successfully!</h4>
								<p style="color: #212529; margin-bottom: 0;">Thank you for your enquiry. We will be in contact shortly via the email address you provided.</p>
							</div>
						`);
					});
				} else {
					alert("Something went wrong with the transmission. Please check your inputs and try again.");
				}
			}).catch((error) => {
				console.error("Network interface connection failure: ", error);
			});
		}
	});
	
	


	function getCookie(name) {
		let cookieValue = null;
		if (document.cookie && document.cookie !== "") {
			const cookies = document.cookie.split(";");
			for (let i = 0; i < cookies.length; i++) {
				const cookie = cookies[i].trim();
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === name + "=") {
					cookieValue = decodeURIComponent(
						cookie.substring(name.length + 1)
					);
					break;
				}
			}
		}
		return cookieValue;
	}
	function animateLandingImage() {
		$('#home').addClass('zoom')
	}
});
