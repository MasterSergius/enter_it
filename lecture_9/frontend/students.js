function get_students_by_city (city) {
  var url = "http://localhost:8080/api/v1/get_students_by_city?city=" + encodeURIComponent(city);
  fetch(url)
    .then(response => response.json())
    .then(data => {
        renderTable(data);
    })
    .catch(error => {
        document.getElementById("results").innerHTML = "<p>Error: " + error + "</p>";
    });
}


function get_students_by_group (group) {
  var url = "http://localhost:8080/api/v1/get_students_by_group?group=" + encodeURIComponent(group);
  fetch(url)
    .then(response => response.json())
    .then(data => {
        renderTable(data);
    })
    .catch(error => {
        document.getElementById("results").innerHTML = "<p>Error: " + error + "</p>";
    });
}


function renderTable(data) {
  var resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = "";

  if (data.length === 0) {
      resultsDiv.innerHTML = "<p>No results found.</p>";
      return;
  }

  var table = document.createElement("table");
  var headerRow = table.insertRow();

  var headers = Object.keys(data[0]);
  headers.forEach(headerText => {
      var header = document.createElement("th");
      header.textContent = headerText;
      headerRow.appendChild(header);
  });

  data.forEach(item => {
      var row = table.insertRow();
      headers.forEach(header => {
          var cell = row.insertCell();
          cell.textContent = item[header];
      });
  });

  resultsDiv.appendChild(table);
}


document.addEventListener("DOMContentLoaded", function() {
  document.getElementById('filter_button').onclick = function() {
    var filterType = document.querySelector('input[name="students_filter"]:checked').id;
    var filterValue = document.getElementById(filterType+"_input").value
    if (filterType == "city_filter") {
        get_students_by_city(filterValue);
    }
    if (filterType == "group_filter") {
        get_students_by_group(filterValue);
    }
  };
});
