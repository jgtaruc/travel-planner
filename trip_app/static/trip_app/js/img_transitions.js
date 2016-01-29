var counter = 1;
function transition() {
  if(counter == 1) {
    document.getElementById('spring').className = "bg-active";
    document.getElementById('summer').className = "";
    document.getElementById('fall').className = "";
    document.getElementById('winter').className = "";
    counter++;
  }
  else if(counter == 2) {
    document.getElementById('spring').className = "";
    document.getElementById('summer').className = "bg-active";
    document.getElementById('fall').className = "";
    document.getElementById('winter').className = "";
    counter++;
  }
  else if(counter == 3) {
    document.getElementById('spring').className = "";
    document.getElementById('summer').className = "";
    document.getElementById('fall').className = "bg-active";
    document.getElementById('winter').className = "";
    counter++;
  }
  else {
    document.getElementById('spring').className = "";
    document.getElementById('summer').className = "";
    document.getElementById('fall').className = "";
    document.getElementById('winter').className = "bg-active";
    counter = 1;
  }
}

setInterval(transition, 1000);

function select_bg() {

}
