var id_in_set_id = 0;

function toggle_active(id) {
  if(id > 0) {
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
  expenses, start_date, end_date, id, csrftoken)
{
  var ul = document.getElementById("activity-list");
  var li = document.createElement("li");

  li.className = "activs-list";

  li.innerHTML = 
    "<div class=edit-activ>" +
      "<li><a class='glyphicon glyphicon-pencil' data-toggle=modal data-target=#activModal" + id + "></a></li>"+
      "<li><a class='glyphicon glyphicon-remove' href=/home/delete_activity/" + id + "></a></li>" +
    "</div>" +
    "<h4>Name: " + name + "</h4>" +
    "<h5>Location: " + location + "</h5>" +
    "<h5>Description: " + description + "</h5>" +
    "<h5>Expense: " + expenses + "</h5>" +
    "<div class=activ-footer>" + start_date +
    "  -  " + end_date + "</div>";
  ul.appendChild(li);
}


function set_id() {
  document.getElementById("trip_activ_id").value = id_in_set_id.toString();
}