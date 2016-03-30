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
  expenses, start_datetime, end_datetime, id, csrftoken)
{
  var ul = document.getElementById("activity-list");
  var li = document.createElement("li");

  li.className = "activs-list";

  li.innerHTML = "<h4>" + name + "  -  " + location +
    "<div class=edit-activ>" +
      "<li><a class='glyphicon glyphicon-pencil' data-toggle=modal data-target=#activModal" + id +" href=#></a></li>"+
      "<li><a class='glyphicon glyphicon-remove' href=/home/delete_activity" + id + "></a></li>" +
    "</div>" +
    "</h4><h5>" + description + "</h5>" +
    "<div class=activ-footer>" + start_datetime +
    "  -  " + end_datetime + "</div>" + 

    "<div class=modal fade id=activModal" + id + " role=dialog>" +
      "<div class=modal-dialog>" +

        "<div class=modal-content>" +
          "<form action=/home/edit_activity method=POST onsubmit=set_id()>" +
            "<div class=modal-header>" +
              csrftoken +
              "<button type=button class=close data-dismiss=modal>&times;</button>" +
              "<h4 class=modal-title>Edit Activity</h4>" +
            "</div>" +
            "<div class=modal-body>" +
              "<input type=hidden name=activ_id value=" + id + ">" +
              "<label>Acivity Name: </label>" +
              "<input class=input-lg name=activ_name value="+ name +" required>" +

              "<label>Activity Description: </label>" +
              "<input class=input-lg name=activ_description value="+ description +" required>" +

              "<label>Activity Location: </label>" +
              "<input class=input-lg name=activ_location value=" + location + "  required>" +

              "<label>Activity Expense: </label>" +
              "<input class=input-lg type=number step=0.01 min=0.00 value=" + expenses.toString()  + " name=activ_expense  required>" +

             /*"<div id=date_picker>" +
                "<label>Activity Start Date:</label>" +
                "<p>{{activity_form.activ_start_datetime}}<p>" +
              "</div> " +

              "<div id=date_picker>" +
                "<label>Activity End Date:</label>" +
                "<p>{{activity_form.activ_end_datetime}}<p>" +
              "</div>" +*/

            "</div>" +

            "<div class=modal-footer>" +
              "<button name=add-activ-btn  class=btn btn-default>Add</button>" +
              "<button type=button class=btn btn-default data-dismiss=modal>Close</button>" +
            "</div>" +
          "</form>" +
        "</div>";
  ul.appendChild(li);
}


function set_id() {
  document.getElementById("trip_activ_id").value = id_in_set_id.toString();
}