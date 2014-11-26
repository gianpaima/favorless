$(document).ready(function(){
    //global vars
    var form = $("#customForm");
    var name = $("#name");
    var nameInfo = $("#nameInfo");
    var email = $("#email");
    var emailInfo = $("#emailInfo");
    var pass1 = $("#pass1");
    var pass1Info = $("#pass1Info");
    var pass2 = $("#pass2");
    var pass2Info = $("#pass2Info");
    var message = $("#message");

    //On blur
    name.blur(validateName);
    email.blur(validateEmail);
    pass1.blur(validatePass1);
    pass2.blur(validatePass2);
    //On key press
    name.keyup(validateName);
    pass1.keyup(validatePass1);
    pass2.keyup(validatePass2);
    message.keyup(validateMessage);
    //On Submitting
    form.submit(function(){
        if(validateName() & validateEmail() & validatePass1() & validatePass2() & validateMessage())
            return true
            else
                return false;
            });

            //validation functions
            function validateEmail(){
                //testing regular expression
                var a = $("#email").val();
                var filter = /^[a-zA-Z0-9]+[a-zA-Z0-9_.-]+[a-zA-Z0-9_-]+@[a-zA-Z0-9]+[a-zA-Z0-9.-]+[a-zA-Z0-9]+.[a-z]{2,4}$/;
                //if it's valid email
                if(filter.test(a)){
                    email.removeClass("error");
                    emailInfo.text("Te enviaremos una confirmación por correo electrónico.");
                    emailInfo.removeClass("error");
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
                if(name.val().length < 4){
                    name.addClass("error");
                    nameInfo.text("Tu nombre debe tener al menos 3 letras!");
                    nameInfo.addClass("error");
                    return false;
                }
                //if it's valid
                else{
                    name.removeClass("error");
                    nameInfo.text("El nombre se ve genial.");
                    nameInfo.removeClass("error");
                    return true;
                }
            }
            function validatePass1(){
                var a = $("#password1");
                var b = $("#password2");

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
                    validatePass2();
                    return true;
                }
            }
        });
