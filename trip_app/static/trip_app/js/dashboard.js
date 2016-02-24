var id_in_set_id = 0;

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
  id_in_set_id = id; 
}


//for showing the associated activity with the selected trip
function if_activity_selected(id) {
  var a = document.getElementById(id); 
  if(a.className == "trip active") {
    return true;
  }
  else {
    return false;
  }
}

function clear() {
  $(".activity-list").empty();
}

function show_activity_list(name, location, description,
  expenses, start_datetime, end_datetime)
{
  var ul = document.getElementById("activity-list");
  var li = document.createElement("li");

  li.className = "activs-list";

  li.innerHTML = "<h4>" + name + "  -  " + location +
    "</h4><h5>" + description + "</h5>" +
    "<div class=activ-footer>" + start_datetime +
    "  -  " + end_datetime + "</div>";
  ul.appendChild(li);
}


function set_id() {
  document.getElementById("trip_activ_id").value = id_in_set_id.toString();
}