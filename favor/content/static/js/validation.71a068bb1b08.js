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
    var arreglo=[];
    //On blur
    name.blur(validateName);
    email.blur(validateEmail);
    pass1.blur(validatePass1);
    username.blur(validateUserName)
    //On key press
    name.keyup(validateName);
    username.keyup(validateUserName)
    pass1.keyup(validatePass1);


    $('#registrar').click(function()
    {
        
          if(arreglo[name.prop('id')] && arreglo[email.prop('id')] &&
           arreglo[pass1.prop('id')] &&arreglo[username.prop('id')])
        {
            console.log("Submit:"+form.submit())
            $('form').submit();
           // return true;
        }
        else
        {
            validateEmail();
            validateName();
            validatePass1();
            validateUserName();
                alert("false");
                console.log("false");
                return false;
        }
    });
    //On Submitting
 /*
    form.submit(function(event){
        event.preventDefault();
        console.log("asdasdasdasdasd");
        if(arreglo[0] && arreglo[1] && arreglo[2] &&arreglo[3] )
        {
            alert("true");
            console.log("true");
            return true;
        }
        else
            {
                alert("false");
                console.log("false");
                return false;
            }
        });
*/

    //validation functions
    function validateEmail(){
        //testing regular expression
        var a = $("#r_input_email").val();
        var filter = /^[a-zA-Z0-9]+[a-zA-Z0-9_.-]+[a-zA-Z0-9_-]+@[a-zA-Z0-9]+[a-zA-Z0-9.-]+[a-zA-Z0-9]+.[a-z]{2,4}$/;
        //if it's valid email
        if(filter.test(a))
        {
            
            var total={"tipo":"validarEmail","objetos":{"email":a}};
            jqxhrPost('validar/',total,$(this));
        }
        else
            arreglo[email.prop('id')]=false;
            emailInfo.removeClass("sucess");
            email.addClass("error");
            emailInfo.addClass("error");
            if(a.length!=0)
            {
                emailInfo.text("No parece ser un correo electrónico valido.");
            }
            else
            {
                emailInfo.text("¡Se requiere un email!");
            }
            
            return false;
        }
    
    function validateName(){
        //if it's NOT valid
        if(name.val().length == 0){
            arreglo[name.prop('id')]=false;
            name.removeClass("success")
            nameInfo.removeClass("success");
            name.addClass("error");
            nameInfo.text("¡Se requiere un nombre!");
            nameInfo.addClass("error");
            return false;
        }
        //if it's valid
        else{

        var total={"tipo":"validarNombre","objetos":{"nombre":name.val()}};
            
            jqxhrPost('validar/',total,$(this));
            
        }
    }
    function validatePass1(){
        //it's NOT valid
        if(pass1.val().length <6){
            arreglo[pass1.prop('id')]=false;
            pass1.removeClass("success");
            pass1Info.removeClass("success");
            pass1.addClass("error");
            pass1Info.text("La contraseña debe ser de al menos 6 caracteres.");
            pass1Info.addClass("error");
            return false;
        }
        //it's valid
        else{
            var total={"tipo":"validarPassword","objetos":{"password":pass1.val()}};
            jqxhrPost('validar/',total,$(this));
        }
    }

    function validateUserName(){
        //if it's NOT valid
        if(username.val().length < 1){
            arreglo[username.prop('id')]=false;
            username.removeClass("success");
            userInfo.removeClass("success");
            userInfo.text("¡Se requiere un nombre de usuario!");
            username.addClass("error");
            userInfo.addClass("error");
            return false;
        }
        //if it's valid
        else{

            var total={"tipo":"validarUsername","objetos":{"username":username.val()}};
            jqxhrPost('validar/',total,$(this));
            
        }
    }


    function jqxhrPost(url,data,obj)
    {          
        jqxhr=$.post( url , data, "json")
              .done(function(datas) {
               
                switch ($(obj).prop('id'))
                 {
                    case name.prop('id'):
                        if(datas.valido=="0")
                        {
                             arreglo[$(obj).prop('id')]=true;
                             name.removeClass("error");
                             nameInfo.text("El nombre se ve genial.");
                             nameInfo.removeClass("error");
                             name.addClass("success");
                             nameInfo.addClass("success");         
                        }
                        else
                        {
                            arreglo[$(obj).prop('id')]=false;
                            name.removeClass("success");
                            nameInfo.removeClass("success");
                            name.addClass("error");
                            nameInfo.text("¡Se requiere un nombre!");
                            nameInfo.addClass("error");   
                        }
                        
                        console.log("VIVA CHESPIRITO!");
                        break; 
                    case email.prop('id'):
                        if(datas.valido == "0")
                        {
                            arreglo[$(obj).prop('id')]=true;
                            email.removeClass("error");
                            emailInfo.text("Te enviaremos una confirmación por correo electrónico.");
                            emailInfo.removeClass("error");
                            email.addClass("success");
                            emailInfo.addClass("success");
                        }
                        else
                        {
                             arreglo[$(obj).prop('id')]=false;
                             emailInfo.removeClass("success");
                             email.addClass("error");
                             emailInfo.addClass("error");
                            if(datas.valido=="3")
                            {
                                emailInfo.text("No parece ser un correo electrónico valido.");
                            }
                            else
                                if(datas.valido=="1")
                                {
                                    emailInfo.text("Este email ya existe");
                                }
                                else
                                {
                                    console.log("Data email:"+datas.valido);
                                    emailInfo.text("Se requiere un email");
                                }
                        }
                        break;
                    case pass1.prop('id'):
                        if(datas.valido =="0")
                        {
                            arreglo[$(obj).prop('id')]=true;
                            pass1.removeClass("error");
                            pass1Info.removeClass("error");
                            pass1Info.text("Bien hecho!");
                            pass1.addClass("success");
                            pass1Info.addClass("success");      
                        }
                        else
                        {
                            arreglo[$(obj).prop('id')]=false;
                            pass1.removeClass("success");
                            pass1Info.removeClass("success");
                            pass1.addClass("error");
                            pass1Info.text("La contraseña debe ser de al menos 6 caracteres.");
                            pass1Info.addClass("error"); 
                        }
                         
                        console.log("VIVA CHESPIRITO!!!");
                        break; 
                    case username.prop('id'):
                        if(datas.valido == "0")
                        {
                            arreglo[$(obj).prop('id')]=true;
                            username.removeClass("error");
                            userInfo.removeClass("error");
                            userInfo.text("El nombre se ve genial.");
                            username.addClass("success");
                            userInfo.addClass("success");
                        }
                        else
                           { 
                            arreglo[$(obj).prop('id')]=false;
                            username.removeClass("success");
                            userInfo.removeClass("success");
                            username.addClass("error");
                            userInfo.addClass("error");
                                if(datas.valido == "1")
                                {
                                    userInfo.text("¡Ese usuario ya existe!");
                                }
                                else
                                {
                                    userInfo.text("¡Se requiere un nombre de usuario!");
                                }
                           }
                        console.log("VIVA CHESPIRITO!!!!"+datas.valido);
                        break;      
                    default: 
                        console.log("siempre");
                        
                 }
              })
              .fail(function() {
                arreglo[$(obj).prop('id')]=false;
                console.log("fail->"+arreglo[$(obj).prop('id')]);
              });
    }
// This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

/*
The functions below will create a header with csrftoken
*/

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});   

});
