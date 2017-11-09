// New question "NO DATA" checkbox handelers
// Cow form validation
function changecowrace() {
    var crace = document.getElementById('cowrace');
    var cracecheck = document.getElementById('cowracec');
    if (cracecheck.checked) {
        crace.value="Sin datos";
    }
    else {
        crace.value="";
    }
}