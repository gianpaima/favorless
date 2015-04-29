$(document).ready(function(){
    //global vars
    var form = $("#customForm");
    var name = $("#r_input_name_complete");
    var nameInfo = $("#nameInfo");
    var email = $("#r_input_email");
    var emailInfo = $("#emailInfo");
    var pass1 = $("#r_input_password");
    var pass1Info = $("#pass1Info");
    var username = $("#r_input_usuario");
    var userInfo = $("#userInfo");

    //On blur
    name.blur(validateName);
    email.blur(validateEmail);
    pass1.blur(validatePass1);
    username.blur(validateUserName)
    //On key press
    name.keyup(validateName);
    username.keyup(validateUserName)
    pass1.keyup(validatePass1);
    //On Submitting
    form.submit(function(){
        if(validateName() & validateEmail() & validatePass1() & validateUserName)
            return true
            else
                return false;
            });

            //validation functions
            function validateEmail(){
                //testing regular expression
                var a = $("#r_input_email").val();
                var filter = /^[a-zA-Z0-9]+[a-zA-Z0-9_.-]+[a-zA-Z0-9_-]+@[a-zA-Z0-9]+[a-zA-Z0-9.-]+[a-zA-Z0-9]+.[a-z]{2,4}$/;
                //if it's valid email
                if(filter.test(a)){
                    email.removeClass("error");
                    emailInfo.text("Te enviaremos una confirmación por correo electrónico.");
                    emailInfo.removeClass("error");
                    name.addClass("success");
                    emailInfo.addClass("success");
                    return true;
                }
                //if it's NOT valid
                else{
                    email.addClass("error");
                    emailInfo.text("No parece ser un correo electrónico valido.");
                    emailInfo.addClass("error");
                    return false;
                }
            }
            function validateName(){
                //if it's NOT valid
                if(name.val().length < 2){
                    name.addClass("error");
                    nameInfo.text("Tu nombre debe tener al menos 2 letras!");
                    nameInfo.addClass("error");
                    return false;
                }
                //if it's valid
                else{
                    name.removeClass("error");
                    nameInfo.text("El nombre se ve genial.");
                    nameInfo.removeClass("error");
                    name.addClass("success");
                    nameInfo.addClass("success");
                    return true;
                }
            }
            function validatePass1(){
                //it's NOT valid
                if(pass1.val().length <5){
                    pass1.addClass("error");
                    pass1Info.text("La contraseña debe ser de al menos 6 caracteres.");
                    pass1Info.addClass("error");
                    return false;
                }
                //it's valid
                else{
                    pass1.removeClass("error");
                    pass1Info.text("Bien hecho!");
                    pass1Info.removeClass("error");
                    name.addClass("success");
                    pass1Info.addClass("success");
                    return true;
                }
            }

            function validateUserName(){
                //if it's NOT valid
                if(username.val().length < 2){
                    username.addClass("error");
                    userInfo.text("Tu nombre debe tener al menos 2 letras!");
                    userInfo.addClass("error");
                    return false;
                }
                //if it's valid
                else{
                    username.removeClass("error");
                    userInfo.text("El nombre se ve genial.");
                    userInfo.removeClass("error");
                    username.addClass("success");
                    userInfo.addClass("success");
                    return true;
                }
            }
        });
