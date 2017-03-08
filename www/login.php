<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Login</title>
    <link rel="stylesheet" href="css/login.css">
    <script src="./js/query.js"></script>
    <script src="./js/functions.js"></script>
    <script src="./js/login.js"></script>
    <script src="./js/register.js"></script>
  </head>
  <body>
    <div class="login-page">
        <div class="form">
            <div class="logo">
                <img id="logo" src="http://atspot.ru/images/pm-logo.png" />
            </div>
            <form class="register-form">
                <input type="text" placeholder="email address" id="regemail"/><br>
                <input type="text" placeholder="nickname" id="regname"/><br>
                <input type="password" placeholder="password" id="regpassword"/><br>
                <input type="password" placeholder="repeat pass" id="regpassword2" /><br>
                <button id="register">create</button>
                <p class="message">Already registered? <br><a href="#" id="signIn">Sign In</a></p>
            </form>
            <form class="login-form">
                <input type="text" placeholder="e-mail" id="username" /><br>
                <input type="password" placeholder="password" id="password"/><br>
                <button id="submit">login</button>
                <p class="message" >Not registered? <br><a href="#" id="createAcc">Create an account</a></p>
            </form>
        </div>                    
    </div>
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            createAcc.addEventListener("click", function () {
                document.querySelector(".form .login-form").style.display = "none";
                document.querySelector(".form .register-form").style.display = "block";
            })
            signIn.addEventListener("click", function () {
                document.querySelector(".form .login-form").style.display = "block";
                document.querySelector(".form .register-form").style.display = "none";
            })
        })
        logo.onload = function () {
            document.querySelector(".login-page").style.display = "block";
        }
    </script>
  <body>
</html>