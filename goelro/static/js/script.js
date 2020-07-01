function answered(id){
    document.getElementById(id).style.color = "green";
}

//function changeAudio(number){
//	var xhttp = new XMLHttpRequest();
//	xhttp.onreadystatechange = function() {
//		if (this.readyState == 4 && this.status == 200) {
//			document.getElementById("audioPlayer").src = this.responseText;
//		}
//	};
//	xhttp.open("GET", "audio/"+number);
//	xhttp.send();
//}

function changeAudio(source){
    document.getElementById("audioPlayer").src = source;
}

function scrollFunction() {
    let upButton = document.getElementById("upBtn");
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    upButton.style.display = "block";
    } else {
    upButton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}