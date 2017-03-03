<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <title>Brilliant Projects</title>
    <link href="lib/bootstrap.min.css" rel="stylesheet">
    <link href="lib/animate.css" rel="stylesheet">
    <link rel="stylesheet" href="css/font-awesome.min.css">
    <link href="css/home-style.css" rel="stylesheet">
    <link href="css/post-style.css" rel="stylesheet">
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
    <script src="./js/menu.js"></script>
    <script src="./js/query.js"></script>
    <script src="./js/functions.js"></script>
    <script src="./js/auth.js"></script>
  </head>
  <body>
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="./">Vote!</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li><a href="#" id="addProject">Add Project</a></li>
            <li class="Actions">
            </li>
          </ul>
          <ul class="nav navbar-nav navbar-right">
            <li><a href="#" id="profileusername"></a></li>
            <li><a href="#" id="logOut">Log out</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>
      <div class="add-bg" id="addBg">
      <div class="add-project">
        <div class="row">
          <div class="col-md-2"></div>
          <div class="col-md-8"><h2>New project</h2></div>
        </div>
        <div class="row">
          <div class="col-md-2"></div>
          <div class="col-md-8">
              <label for="projectname">Name:</label>
              <input type="text" class="form-control" id="projectname">
          </div>
        </div>
        <div class="row">
          <div class="col-md-2"></div>
          <div class="col-md-8">
            <textarea class="form-control" rows="5" placeholder="Your description..." id="projectdescription"></textarea><br>
            <button type="button" class="btn btn-sm btn-default" id="createProject">Create</button>
          </div>
        </div>
      </div>
     </div>