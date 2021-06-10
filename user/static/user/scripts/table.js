window.onload = () =>{
    var coll = document.getElementsByClassName("otworzMenu");
    var i;

    for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function() {
            this.classList.toggle("active");

            var content = this.nextElementSibling;
            if (content.style.maxHeight){
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    }
}

function sortTableWhite(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("openingsTableWhite");
    switching = true;
    dir = "asc";
    while (switching) {
      switching = false;
      rows = table.rows;
      for (i = 1; i < (rows.length - 1); i++) {
        shouldSwitch = false;
        x = rows[i].getElementsByTagName("TD")[n];
        y = rows[i + 1].getElementsByTagName("TD")[n];
        if (dir == "asc") {
          if (parseInt(x.innerHTML) > parseInt(y.innerHTML)) {
            shouldSwitch = true;
            break;
          }
        } else if (dir == "desc") {
          if (parseInt(x.innerHTML) < parseInt(y.innerHTML)) {
            shouldSwitch = true;
            break;
          }
        }
      }
      if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        switchcount ++;
      } else {
        if (switchcount == 0 && dir == "asc") {
          dir = "desc";
          switching = true;
        }
      }
    }
    }
  function sortTableBlack(n) {
      var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
      table = document.getElementById("openingsTableBlack");
      switching = true;
      dir = "asc";
      while (switching) {
        switching = false;
        rows = table.rows;
        for (i = 1; i < (rows.length - 1); i++) {
          shouldSwitch = false;
          x = rows[i].getElementsByTagName("TD")[n];
          y = rows[i + 1].getElementsByTagName("TD")[n];
          if (dir == "asc") {
            if (parseInt(x.innerHTML) > parseInt(y.innerHTML)) {
              console.log(x.innerHTML);
              shouldSwitch = true;
              break;
            }
          } else if (dir == "desc") {
            if (parseInt(x.innerHTML) < parseInt(y.innerHTML)) {
              shouldSwitch = true;
              break;
            }
          }
        }
        if (shouldSwitch) {
          rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
          switching = true;
          switchcount ++;
        } else {
          if (switchcount == 0 && dir == "asc") {
            dir = "desc";
            switching = true;
          }
        }
      }
    }