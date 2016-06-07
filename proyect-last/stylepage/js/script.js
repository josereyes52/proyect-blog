$(document).ready(function() {

	$(".open").click(function(){
		$("#imagemodal").fadeTop(3000);


	});

	var flag = false;
	var scroll;

	$(window).scroll(function() {
		scroll = $(window).scrollTop();

		if(scroll  > 200){
			if(!flag){
				$("#logo").css({"margin-top": "1px", "with": "50px","height": "50px"});
				$("header").css({"background-color": "#3c3c3c"});
				$("nav").css({"padding-left": "32.5%"});
				flag=true;
				console.log(scroll);
				}
		}else{
			if(flag){
				$("#logo").css({"margin-top": "90px", "with": "250px","height": "250px"});
				$("header").css({"background-color": "transparent"});
				$("nav").css({"padding-left":"24.5%"});
				flag=false;
			}
		}
		// body...
	});

	
	});


