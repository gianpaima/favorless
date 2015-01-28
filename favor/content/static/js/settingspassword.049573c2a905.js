$(document).ready(function()
{
	var passwordBefore= $('#passwordBefore');
	var passwordNow=$('#passwordNow');
	var passwordRepeat=$('#passwordRepeat');
	var form=$('#formulario');
	passwordBefore.keyup(passwordZero);
	passwordNow.keyup(passwordFirst);
	passwordRepeat.keyup(passwordSecond);
	var errorInfo=$('#errorInfo');
	$('#actualizar').click(function(){
		if(passwordZero() && passwordFirst() && passwordSecond() )
		{
			console.log("fin");
			form.submit();
		}
		else
		{ //errorInfo
			if(passwordBefore.val().length == 0 || passwordBefore.val().length <6)
			{
				if(passwordBefore.val().length == 0)
				{
					errorInfo.text("Debes ingresar tu contraseña actual para poder cambiarla.");
					console.log("Debes ingresar tu contraseña actual para poder cambiarla.");
				}
				else
				{
					errorInfo.text("Tu contraseña actual debe ser mayor a 5 caracteres");
					console.log("Tu contraseña actual debe ser mayor a 5 caracteres")
				}
			}
			else
			{
				if(passwordNow.val().length== 0 || passwordNow.val().length<6)
				{
					if(passwordNow.val().length == 0)
					{
						errorInfo.text("Debes introducir una nueva contraseña para poder cambiarla.");
						console.log("Debes introducir una nueva contraseña para poder cambiarla.");
					}
					else
					{
						errorInfo.text("Tu nueva contraseña debe tener mas de 5 caracteres.");
						console.log("Tu nueva contraseña debe tener mas de 5 caracteres.");
					}
				}
				else
				{
					if(passwordNow.val() != passwordRepeat.val())
					{
						errorInfo.text("Tu nueva contraseña debe ser confirmada correctamente.");
						console.log("Tu nueva contraseña debe ser confirmada correctamente.")
					}
				}
			}	
		}
	});

	function passwordZero()
	{ 
		activar();
		if(passwordBefore.val().length != 0  || passwordBefore.val().length>5)
			return true;
		else
			return false;
	}


	function passwordFirst()
	{
		activar();
		var infoErrorFirst= $('#passInfoNow');
		if(passwordNow.val().length < 6)
		{
			infoErrorFirst.text("Error Pass1:La contraseña debe ser de al menos 6 caracteres.");
			console.log("Error Pass1:La contraseña debe ser de al menos 6 caracteres.")
			return false;
		}
		else
		{
			infoErrorFirst.text("Bien hecho!");
			console.log("Bien hecho!");
			return true;
		}
	}

	function passwordSecond()
	{
		activar();
		var infoErrorSecond = $('#passInfoAgain');
		if(passwordRepeat.val().length<6)
		{
			infoErrorSecond.text("Error Pass2:La contraseña debe ser de al menos 6 caracteres.");
			console.log("Error Pass2:La contraseña debe ser de al menos 6 caracteres.")
			return false;
		}
		else
		{
			if(passwordNow.val() == passwordRepeat.val())
			{
				infoErrorSecond.text("Bien hecho los dos pass son iguales.");	
				console.log("Bien hecho los dos pass son iguales.");
				return true;
			}
			else
			{
				infoErrorSecond.text("Error: Deben de coincidir las contraseñas");
				console.log("Error: Deben de coincidir las contraseñas");
				return false;
			}
		}
	}

	function activar()
	{
		var actualizar=$("#actualizar");
		if(!(passwordBefore.val().length == 0 && 
			passwordNow.val().length==0 && 
			passwordRepeat.val().length==0))
		{
			if(actualizar.is( ":disabled"))
			{
				actualizar.prop( "disabled", false );	
			}
			
		}
		else
		{
			if(!actualizar.is(":disabled"))
			{
				actualizar.prop( "disabled", true );		
			}
			
		}
	}

});