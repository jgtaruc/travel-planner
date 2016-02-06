function toggle_active(id) {
  var actives = document.getElementsByClassName("trip active");
  if(document.getElementById(id).className == "trip active")
    document.getElementById(id).className = "trip";
  else {
    for(i=0; i<actives.length; i++) {
      actives[i].className = "trip";
    }
    document.getElementById(id).className = "trip active";
  }
}
