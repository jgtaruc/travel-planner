var counter = 1;
function transition() {
  if(counter == 1) {
    document.getElementById('spring').className = "selected";
    document.getElementById('summer').className = "";
    document.getElementById('fall').className = "";
    document.getElementById('winter').className = "";
    document.getElementById('spring-bg').className = "bg-active";
    document.getElementById('summer-bg').className = "";
    document.getElementById('fall-bg').className = "";
    document.getElementById('winter-bg').className = "";
    counter++;
  }
  else if(counter == 2) {
    document.getElementById('spring').className = "";
    document.getElementById('summer').className = "selected";
    document.getElementById('fall').className = "";
    document.getElementById('winter').className = "";
    document.getElementById('spring-bg').className = "";
    document.getElementById('summer-bg').className = "bg-active";
    document.getElementById('fall-bg').className = "";
    document.getElementById('winter-bg').className = "";
    counter++;
  }
  else if(counter == 3) {
    document.getElementById('spring').className = "";
    document.getElementById('summer').className = "";
    document.getElementById('fall').className = "selected";
    document.getElementById('winter').className = "";
    document.getElementById('spring-bg').className = "";
    document.getElementById('summer-bg').className = "";
    document.getElementById('fall-bg').className = "bg-active";
    document.getElementById('winter-bg').className = "";
    counter++;
  }
  else {
    document.getElementById('spring').className = "";
    document.getElementById('summer').className = "";
    document.getElementById('fall').className = "";
    document.getElementById('winter').className = "selected";
    document.getElementById('spring-bg').className = "";
    document.getElementById('summer-bg').className = "";
    document.getElementById('fall-bg').className = "";
    document.getElementById('winter-bg').className = "bg-active";
    counter = 1;
  }
}

function select_spring() {
  counter = 1;
  transition();
}

function select_summer() {
  counter = 2;
  transition();
}

function select_fall() {
  counter = 3;
  transition();
}

function select_winter() {
  counter = 4;
  transition();
}

setInterval(transition, 8000);
