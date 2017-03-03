<?php require 'header.php'; ?>
    <div class="bg-voted" id="bgVoted">
      <div class="voted" id="voted">
        <div class="voted-for">
          <h4>like</h4>
        </div>
        <div class="voted-against">
          <h4>dislike</h4>
        </div>
      </div>
    </div>
    <script src="./js/components/comment.js"></script>
    <script src="./js/post-app.js"></script>
    <div id="container" class="container hide">
      <!--Head-->
      <div class="row post-header">
        <div class="col-md-12">
          <header>
            <h2 id="postHead"></h2>
          </header>
        </div>
      </div>
        <!--Descriptin and voting-->
        <div class="row description">
          <div class="col-md-1 voting">
            <div class="plus"><i class="fa fa-thumbs-up fa-2x" aria-hidden="true" id="like"></i></div>
            <div class="counter" id="rating">0</div>
            <div class="minus"><i class="fa fa-thumbs-down fa-flip-horizontal fa-2x" aria-hidden="true" id="dislike"></i></div>
          </div>
            <div id="description" class="col-md-8 text-description">
              
            </div>
            <div class="col-md-2"></div>
          </div>
          <!--Decide by project and createtor-->
          <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-9 accept-panel">
              <div class="judge-buttons" id="judge">
                <button type="button" class="btn btn-sm btn-success" id="success">Success</button>
                <button type="button" class="btn btn-sm btn-danger" id="deny">Deny</button>
              </div>
              <div class="creator">            
                <span>Created by <a href="#" id="author"></a></span>
              </div>
            </div>
          </div>
        <!--YARR!-->
        <div class="row">
          <div class="col-md-1"></div>
          <div class="col-md-8">
            <textarea class="form-control" rows="7" cols="20" id="comment"></textarea><br>
            <button type="button" class="btn btn-sm btn-default" id="sendcomments">Send</button>
          </div>
        </div>
        <div class="row post-header">
          <div class="col-md-12">
            <header>
              <h3 id="answerCount"></h3>
            </header>
          </div>
        </div>
    </div><!--Container CLOSE-->
<?php require 'footer.php'; ?>