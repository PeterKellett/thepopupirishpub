$(document).ready(() => {
	console.log("main.js");
	animateLandingImage();

	$(".nav-link:not(.dropdown-toggle)").click(function() {
		console.log("clicked", this);
		$(".navbar-collapse").collapse("hide");
		console.log("attr = ", );
		$(this).addClass('active');
		// $(this).siblings().removeClass('active');
		// $('.nav-link').removeClass('active');
	});

	//Bootstrap carousel functionality
	// $('.carousel').carousel()

	//////////////////////////////////////
	$("#form-submit").click((e) => {
		console.log("form-submit")
		e.preventDefault();
		var form = document.getElementById("form");
		console.log("form = ", form)
		var submitter = document.getElementById("form-submit");
		const formData = new FormData(form);
		console.log("formData = ", formData)
		if (!form.checkValidity()) {
			console.log("IF")
			// Create the temporary button, click and remove it
			var tmpSubmit = document.createElement("button");
			form.appendChild(tmpSubmit);
			tmpSubmit.click();
			form.removeChild(tmpSubmit);
		} else {
			console.log("ELSE")
			console.log("formData = ", formData)
			// Form is valid, let the user proceed or do whatever we need to
			data = {};
			formData.forEach(function (value, key) {
				data[key] = value;
			});
			
			console.log("data = ", data)
			const host = window.location.host;
			var url = "";
			if (host.includes("heroku")) {
				console.log("HEROKU");
				url = "https://www.thepopupirishpub.com/";
			} else {
				console.log("DEVELOPMENT");
				url = "http://127.0.0.1:8000";
			}
			fetch(url, {
				method: "POST",
				credentials: "same-origin",
				headers: {
					"X-Requested-With": "XMLHttpRequest",
					"X-CSRFToken": getCookie("csrftoken"),
				},
				body: JSON.stringify(data),
			}).then((response) => {
				console.log("response = ", response);
				if (response.status == 200) {
					form.style.display = "none";
					$(".form-wrapper").append(
						`<div class="message-wrapper">
                        <p>Thank you for your enquiry.</p>
                        <p>We will be in contact shortly via the email you provided.</p>
                    </div>`
					);
				}
			});
			// .then((data) => {
			//     console.log("response.data = ", data);
			//     if (data.status == "Checkout Complete") {
			//         // location.reload();

			//     }
			// });
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
