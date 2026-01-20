function searchTable() {
    console.log("Function called");
    // Declare variables
    var input, filter, table, tr, td, i, j, txtValue;
    input = document.getElementById("searchInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("itemTable");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows
    for (i = 1; i < tr.length; i++) {
        // Initialize flag for matching any cell
        var matchAnyCell = false;
        td = tr[i].getElementsByTagName("td");
        // Loop through all cells in current row
        for (j = 0; j < td.length; j++) {
            txtValue = td[j].textContent || td[j].innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                matchAnyCell = true;
                break; // Stop looping if match found in any cell
            }
        }
        // Show or hide row based on whether it matches any cell
        tr[i].style.display = matchAnyCell ? "" : "none";
    }
}
