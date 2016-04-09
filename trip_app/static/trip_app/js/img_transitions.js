var counter = 1;

/*
transition function is responsible for dynamic transitioning of
background images.
selected classname applies to the img-ctrls.
bg-active classname applies to the background image.
*/
function transition() {
  if(counter == 1) {
    document.getElementById('travel1').className = "selected";
    document.getElementById('travel2').className = "";
    document.getElementById('travel3').className = "";
    document.getElementById('travel4').className = "";
    document.getElementById('travel1-bg').className = "bg-active";
    document.getElementById('travel2-bg').className = "";
    document.getElementById('travel3-bg').className = "";
    document.getElementById('travel4-bg').className = "";
    counter++;
  }
  else if(counter == 2) {
    document.getElementById('travel1').className = "";
    document.getElementById('travel2').className = "selected";
    document.getElementById('travel3').className = "";
    document.getElementById('travel4').className = "";
    document.getElementById('travel1-bg').className = "";
    document.getElementById('travel2-bg').className = "bg-active";
    document.getElementById('travel3-bg').className = "";
    document.getElementById('travel4-bg').className = "";
    counter++;
  }
  else if(counter == 3) {
    document.getElementById('travel1').className = "";
    document.getElementById('travel2').className = "";
    document.getElementById('travel3').className = "selected";
    document.getElementById('travel4').className = "";
    document.getElementById('travel1-bg').className = "";
    document.getElementById('travel2-bg').className = "";
    document.getElementById('travel3-bg').className = "bg-active";
    document.getElementById('travel4-bg').className = "";
    counter++;
  }
  else {
    document.getElementById('travel1').className = "";
    document.getElementById('travel2').className = "";
    document.getElementById('travel3').className = "";
    document.getElementById('travel4').className = "selected";
    document.getElementById('travel1-bg').className = "";
    document.getElementById('travel2-bg').className = "";
    document.getElementById('travel3-bg').className = "";
    document.getElementById('travel4-bg').className = "bg-active";
    counter = 1;
  }
}

//if user click img-ctrls and selected a toggle button, the below functions will
//change the background image corresponding background image
function select_travel1() {
  counter = 1;
  transition();
}

function select_travel2() {
  counter = 2;
  transition();
}

function select_travel3() {
  counter = 3;
  transition();
}

function select_travel4() {
  counter = 4;
  transition();
}


//set the interval on which the background changes.
//in this case the background image changes every 8 seconds.
setInterval(transition, 8000);
