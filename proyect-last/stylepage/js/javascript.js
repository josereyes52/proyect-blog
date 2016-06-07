function desplegar(value,elemento,url) {
	var visibility = value;
	var ventana = elemento;

	if(visibility==true){
		document.getElementById("imagemodal").src=url;
		document.getElementById("imagemodal").style.opacity = 1;
		document.getElementById(elemento).style.visibility="visible";
		
	}else{
		if(visibility==false){
		document.getElementById("imagemodal").style.opacity = 0;
		document.getElementById(elemento).style.visibility="hidden";
		console.log(visibility);
		}
	}


	// body...
}

