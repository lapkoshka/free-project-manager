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
        <div class="company-name">
            <span>Brilliant Project Manager</span>
        </div>
    <div class="login-page">
        <div class="form">
            <form class="register-form">
                <input type="text" placeholder="email address" id="regemail"/>
                <input type="text" placeholder="nickname" id="regname"/>
                <input type="password" placeholder="password" id="regpassword"/>
                <input type="password" placeholder="repeat pass" id="regpassword2" />
                <button id="register">create</button>
                <p class="message">Already registered? <a href="#" id="signIn">Sign In</a></p>
            </form>
            <form class="login-form">
                <input type="text" placeholder="e-mail" id="username" />
                <input type="password" placeholder="password" id="password"/>
                <button id="submit">login</button>
                <p class="message" >Not registered? <a href="#" id="createAcc">Create an account</a></p>
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
        </script>
  <body>
</html>