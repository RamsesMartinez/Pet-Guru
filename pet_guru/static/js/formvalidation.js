// New question "NO DATA" checkbox handelers
// Bovine form validation
function changecowrace() {
  var crace = document.getElementById('cowrace');
  var cracecheck = document.getElementById('cowracec');
  if (cracecheck.checked) {
    crace.value="Sin datos";
    $('#cowrace').prop("disabled", true);
  }
  else {
    crace.value="";
    $('#cowrace').prop("disabled", false);
  }
}
function changecowage() {
  var cage = document.getElementById('cowage');
  var cagecheck = document.getElementById('cowagec');
  if (cagecheck.checked) {
    cage.value="0000";
    $('#cowage').prop("disabled", true);
  }
  else {
    cage.value="";
    $('#cowage').prop("disabled", false);
  }
}
function changecowweight() {
  var cweight = document.getElementById('cowweight');
  var cweightcheck = document.getElementById('cowweightc');
  if (cweightcheck.checked) {
    cweight.value="0000";
    $('#cowweight').prop("disabled", true);
  }
  else {
    cweight.value="";
    $('#cowweight').prop("disabled", false);
  }
}
function changecowheart() {
  var cheart = document.getElementById('cowheart');
  var cheartcheck = document.getElementById('cowheartc');
  if (cheartcheck.checked) {
    cheart.value="0000";
    $('#cowheart').prop("disabled", true);
  }
  else {
    cheart.value="";
    $('#cowheart').prop("disabled", false);
  }
}
function changecowresp() {
  var cresp = document.getElementById('cowresp');
  var crespcheck = document.getElementById('cowrespc');
  if (crespcheck.checked) {
    cresp.value="0000";
    $('#cowresp').prop("disabled", true);
  }
  else {
    cresp.value="";
    $('#cowresp').prop("disabled", false);
  }
}
function changecowtemp() {
  var ctemp = document.getElementById('cowtemp');
  var ctempcheck = document.getElementById('cowtempc');
  if (ctempcheck.checked) {
    ctemp.value="0000";
    $('#cowtemp').prop("disabled", true);
  }
  else {
    ctemp.value="";
    $('#cowtemp').prop("disabled", false);
  }
}
function changecowcap() {
  var ccap = document.getElementById('cowcapilar');
  var ccapcheck = document.getElementById('cowcapc');
  if (ccapcheck.checked) {
    ccap.value="0000";
    $('#cowcapilar').prop("disabled", true);
  }
  else {
    ccap.value="";
    $('#cowcapilar').prop("disabled", false);
  }
}
function changecowmucos() {
  var cmucos = document.getElementById('cowmucosal');
  var cmucoscheck = document.getElementById('cowmucoc');
  if (cmucoscheck.checked) {
    cmucos.value="Sin datos";
    $('#cowmucosal').prop("disabled", true);
  }
  else {
    cmucos.value="";
    $('#cowmucosal').prop("disabled", false);
  }
}
function changecowlymph() {
  var clymph = document.getElementById('cowlymph');
  var clymphcheck = document.getElementById('cowlymphc');
  if (clymphcheck.checked) {
    clymph.value="Sin datos";
    $('#cowlymph').prop("disabled", true);
  }
  else {
    clymph.value="";
    $('#cowlymph').prop("disabled", false);
  }
}
function changecowruminal() {
  var crumnial = document.getElementById('cowruminal');
  var crumnialcheck = document.getElementById('cowrumic');
  if (crumnialcheck.checked) {
    crumnial.value="Sin datos";
    $('#cowruminal').prop("disabled", true);
  }
  else {
    crumnial.value="";
    $('#cowruminal').prop("disabled", false);
  }
}
function changecowcondition() {
  var ccond = document.getElementById('cowcondition');
  var ccondcheck = document.getElementById('cowcondc');
  if (ccondcheck.checked) {
    ccond.value="Sin datos";
    $('#cowcondition').prop("disabled", true);
  }
  else {
    ccond.value="";
    $('#cowcondition').prop("disabled", false);
  }
}



// Porcine form validation
function porchangerace() {
  var prace = document.getElementById('porrace');
  var pracecheck = document.getElementById('porracec');
  if (pracecheck.checked) {
    prace.value="Sin datos";
    $('#porrace').prop("disabled", true);
  }
  else {
    prace.value="";
    $('#porrace').prop("disabled", false);
  }
}
function porchangeage() {
  var page = document.getElementById('porage');
  var pagecheck = document.getElementById('poragec');
  if (pagecheck.checked) {
    page.value="0000";
    $('#porage').prop("disabled", true);
  }
  else {
    page.value="";
    $('#porage').prop("disabled", false);
  }
}
function porchangeweight() {
  var pweight = document.getElementById('porweight');
  var pweightcheck = document.getElementById('porweightc');
  if (pweightcheck.checked) {
    pweight.value="0000";
    $('#porweight').prop("disabled", true);
  }
  else {
    pweight.value="";
    $('#porweight').prop("disabled", false);
  }
}
function porchangephysio() {
  var pheart = document.getElementById('porphysio');
  var pheartcheck = document.getElementById('porphysioc');
  if (pheartcheck.checked) {
    pheart.value="Sin datos";
    $('#porphysio').prop("disabled", true);
  }
  else {
    pheart.value="";
    $('#porphysio').prop("disabled", false);
  }
}
function porchangeprod() {
  var pheart = document.getElementById('porprod');
  var pheartcheck = document.getElementById('porprodc');
  if (pheartcheck.checked) {
    pheart.value="Sin datos";
    $('#porprod').prop("disabled", true);
  }
  else {
    pheart.value="";
    $('#porprod').prop("disabled", false);
  }
}
function porchangecurse() {
  var pheart = document.getElementById('porcurse');
  var pheartcheck = document.getElementById('porcursec');
  if (pheartcheck.checked) {
    pheart.value="Sin datos";
    $('#porcurse').prop("disabled", true);
  }
  else {
    pheart.value="";
    $('#porcurse').prop("disabled", false);
  }
}
function porchangeheart() {
  var pheart = document.getElementById('porheart');
  var pheartcheck = document.getElementById('porheartc');
  if (pheartcheck.checked) {
    pheart.value="0000";
    $('#porheart').prop("disabled", true);
  }
  else {
    pheart.value="";
    $('#porheart').prop("disabled", false);
  }
}
function porchangeresp() {
  var presp = document.getElementById('porresp');
  var prespcheck = document.getElementById('porrespc');
  if (prespcheck.checked) {
    presp.value="0000";
    $('#porresp').prop("disabled", true);
  }
  else {
    presp.value="";
    $('#porresp').prop("disabled", false);
  }
}
function porchangetemp() {
  var ptemp = document.getElementById('portemp');
  var ptempcheck = document.getElementById('portempc');
  if (ptempcheck.checked) {
    ptemp.value="0000";
    $('#portemp').prop("disabled", true);
  }
  else {
    ptemp.value="";
    $('#portemp').prop("disabled", false);
  }
}
function porchangecolor() {
  var pcap = document.getElementById('porcolor');
  var pcapcheck = document.getElementById('porcolorc');
  if (pcapcheck.checked) {
    pcap.value="Sin datos";
    $('#porcolor').prop("disabled", true);
  }
  else {
    pcap.value="";
    $('#porcolor').prop("disabled", false);
  }
}
function porchangeatt() {
  var pmucos = document.getElementById('poratt');
  var pmucoscheck = document.getElementById('porattc');
  if (pmucoscheck.checked) {
    pmucos.value="Sin datos";
    $('#poratt').prop("disabled", true);
  }
  else {
    pmucos.value="";
    $('#poratt').prop("disabled", false);
  }
}
function porchangecond() {
  var plymph = document.getElementById('porcondition');
  var plymphcheck = document.getElementById('porcondc');
  if (plymphcheck.checked) {
    plymph.value="Sin datos";
    $('#porcondition').prop("disabled", true);
  }
  else {
    plymph.value="";
    $('#porcondition').prop("disabled", false);
  }
}



// Horse form validation
function changehorserace() {
  var hrrace = document.getElementById('horrace');
  var hrracecheck = document.getElementById('horracec');
  if (hrracecheck.checked) {
    hrrace.value="Sin datos";
    $('#horrace').prop("disabled", true);
  }
  else {
    hrrace.value="";
    $('#horrace').prop("disabled", false);
  }
}
function changehorseage() {
  var hrage = document.getElementById('horage');
  var hragecheck = document.getElementById('horagec');
  if (hragecheck.checked) {
    hrage.value="0000";
    $('#horage').prop("disabled", true);
  }
  else {
    hrage.value="";
    $('#horage').prop("disabled", false);
  }
}
function changehorseweight() {
  var hrweight = document.getElementById('horweight');
  var hrweightcheck = document.getElementById('horweightc');
  if (hrweightcheck.checked) {
    hrweight.value="0000";
    $('#horweight').prop("disabled", true);
  }
  else {
    hrweight.value="";
    $('#horweight').prop("disabled", false);
  }
}
function changehorseheart() {
  var hrheart = document.getElementById('horheart');
  var hrheartcheck = document.getElementById('horheartc');
  if (hrheartcheck.checked) {
    hrheart.value="0000";
    $('#horheart').prop("disabled", true);
  }
  else {
    hrheart.value="";
    $('#horheart').prop("disabled", false);
  }
}
function changehorseresp() {
  var hrresp = document.getElementById('horresp');
  var hrrespcheck = document.getElementById('horrespc');
  if (hrrespcheck.checked) {
    hrresp.value="0000";
    $('#horresp').prop("disabled", true);
  }
  else {
    hrresp.value="";
    $('#horresp').prop("disabled", false);
  }
}
function changehorsetemp() {
  var hrtemp = document.getElementById('hortemp');
  var hrtempcheck = document.getElementById('hortempc');
  if (hrtempcheck.checked) {
    hrtemp.value="0000";
    $('#hortemp').prop("disabled", true);
  }
  else {
    hrtemp.value="";
    $('#hortemp').prop("disabled", false);
  }
}
function changehorsecap() {
  var hrcap = document.getElementById('horcapilar');
  var hrcapcheck = document.getElementById('horcapc');
  if (hrcapcheck.checked) {
    hrcap.value="0000";
    $('#horcapilar').prop("disabled", true);
  }
  else {
    hrcap.value="";
    $('#horcapilar').prop("disabled", false);
  }
}
function changehorsemucos() {
  var hrmucos = document.getElementById('hormucosal');
  var hrmucoscheck = document.getElementById('hormucoc');
  if (hrmucoscheck.checked) {
    hrmucos.value="Sin datos";
    $('#hormucosal').prop("disabled", true);
  }
  else {
    hrmucos.value="";
    $('#hormucosal').prop("disabled", false);
  }
}
function changehorselymph() {
  var hrlymph = document.getElementById('horlymph');
  var hrlymphcheck = document.getElementById('horlymphc');
  if (hrlymphcheck.checked) {
    hrlymph.value="Sin datos";
    $('#horlymph').prop("disabled", true);
  }
  else {
    hrlymph.value="";
    $('#horlymph').prop("disabled", false);
  }
}
function changehorsecondition() {
  var hrage = document.getElementById('horcondition');
  var hragecheck = document.getElementById('horcondc');
  if (hragecheck.checked) {
    hrage.value="Sin datos";
    $('#horcondition').prop("disabled", true);
  }
  else {
    hrage.value="";
    $('#horcondition').prop("disabled", false);
  }
}



// Ovine form validation
function ovichangerace() {
  var prace = document.getElementById('ovirace');
  var pracecheck = document.getElementById('oviracec');
  if (pracecheck.checked) {
    prace.value="Sin datos";
    $('#ovirace').prop("disabled", true);
  }
  else {
    prace.value="";
    $('#ovirace').prop("disabled", false);
  }
}
function ovichangeage() {
  var page = document.getElementById('oviage');
  var pagecheck = document.getElementById('oviagec');
  if (pagecheck.checked) {
    page.value="0000";
    $('#oviage').prop("disabled", true);
  }
  else {
    page.value="";
    $('#oviage').prop("disabled", false);
  }
}
function ovichangeweight() {
  var pweight = document.getElementById('oviweight');
  var pweightcheck = document.getElementById('oviweightc');
  if (pweightcheck.checked) {
    pweight.value="0000";
    $('#oviweight').prop("disabled", true);
  }
  else {
    pweight.value="";
    $('#oviweight').prop("disabled", false);
  }
}
function ovichangephysio() {
  var pheart = document.getElementById('oviphysio');
  var pheartcheck = document.getElementById('oviphysioc');
  if (pheartcheck.checked) {
    pheart.value="Sin datos";
    $('#oviphysio').prop("disabled", true);
  }
  else {
    pheart.value="";
    $('#oviphysio').prop("disabled", false);
  }
}
function ovichangeprod() {
  var pheart = document.getElementById('oviprod');
  var pheartcheck = document.getElementById('oviprodc');
  if (pheartcheck.checked) {
    pheart.value="Sin datos";
    $('#oviprod').prop("disabled", true);
  }
  else {
    pheart.value="";
    $('#oviprod').prop("disabled", false);
  }
}
function ovichangezoo() {
  var pheart = document.getElementById('ovizoo');
  var pheartcheck = document.getElementById('ovizooc');
  if (pheartcheck.checked) {
    pheart.value="Sin datos";
    $('#ovizoo').prop("disabled", true);
  }
  else {
    pheart.value="";
    $('#ovizoo').prop("disabled", false);
  }
}
function ovichangeheart() {
  var pheart = document.getElementById('oviheart');
  var pheartcheck = document.getElementById('oviheartc');
  if (pheartcheck.checked) {
    pheart.value="0000";
    $('#oviheart').prop("disabled", true);
  }
  else {
    pheart.value="";
    $('#oviheart').prop("disabled", false);
  }
}
function ovichangeresp() {
  var presp = document.getElementById('oviresp');
  var prespcheck = document.getElementById('ovirespc');
  if (prespcheck.checked) {
    presp.value="0000";
    $('#oviresp').prop("disabled", true);
  }
  else {
    presp.value="";
    $('#oviresp').prop("disabled", false);
  }
}
function ovichangetemp() {
  var ptemp = document.getElementById('ovitemp');
  var ptempcheck = document.getElementById('ovitempc');
  if (ptempcheck.checked) {
    ptemp.value="0000";
    $('#ovitemp').prop("disabled", true);
  }
  else {
    ptemp.value="";
    $('#ovitemp').prop("disabled", false);
  }
}
function ovichangemucos() {
  var pcap = document.getElementById('ovimucos');
  var pcapcheck = document.getElementById('ovimucosc');
  if (pcapcheck.checked) {
    pcap.value="Sin datos";
    $('#ovimucos').prop("disabled", true);
  }
  else {
    pcap.value="";
    $('#ovimucos').prop("disabled", false);
  }
}
function ovichangelymph() {
  var pmucos = document.getElementById('ovilymph');
  var pmucoscheck = document.getElementById('ovilymphc');
  if (pmucoscheck.checked) {
    pmucos.value="Sin datos";
    $('#ovilymph').prop("disabled", true);
  }
  else {
    pmucos.value="";
    $('#ovilymph').prop("disabled", false);
  }
}
function ovichangeruminal() {
  var pmucos = document.getElementById('oviruminal');
  var pmucoscheck = document.getElementById('oviruminalc');
  if (pmucoscheck.checked) {
    pmucos.value="Sin datos";
    $('#oviruminal').prop("disabled", true);
  }
  else {
    pmucos.value="";
    $('#oviruminal').prop("disabled", false);
  }
}
function ovichangecond() {
  var plymph = document.getElementById('ovicondition');
  var plymphcheck = document.getElementById('ovicondc');
  if (plymphcheck.checked) {
    plymph.value="Sin datos";
    $('#ovicondition').prop("disabled", true);
  }
  else {
    plymph.value="";
    $('#ovicondition').prop("disabled", false);
  }
}



// Goat form validation
function goatchangerace() {
  var prace = document.getElementById('goatrace');
  var pracecheck = document.getElementById('goatracec');
  if (pracecheck.checked) {
    prace.value="Sin datos";
    $('#goatrace').prop("disabled", true);
  }
  else {
    prace.value="";
    $('#goatrace').prop("disabled", false);
  }
}
function goatchangeage() {
  var page = document.getElementById('goatage');
  var pagecheck = document.getElementById('goatagec');
  if (pagecheck.checked) {
    page.value="0000";
    $('#goatage').prop("disabled", true);
  }
  else {
    page.value="";
    $('#goatage').prop("disabled", false);
  }
}
function goatchangeweight() {
  var pweight = document.getElementById('goatweight');
  var pweightcheck = document.getElementById('goatweightc');
  if (pweightcheck.checked) {
    pweight.value="0000";
    $('#goatweight').prop("disabled", true);
  }
  else {
    pweight.value="";
    $('#goatweight').prop("disabled", false);
  }
}
function goatchangephysio() {
  var pheart = document.getElementById('goatphysio');
  var pheartcheck = document.getElementById('goatphysioc');
  if (pheartcheck.checked) {
    pheart.value="Sin datos";
    $('#goatphysio').prop("disabled", true);
  }
  else {
    pheart.value="";
    $('#goatphysio').prop("disabled", false);
  }
}
function goatchangeprod() {
  var pheart = document.getElementById('goatprod');
  var pheartcheck = document.getElementById('goatprodc');
  if (pheartcheck.checked) {
    pheart.value="Sin datos";
    $('#goatprod').prop("disabled", true);
  }
  else {
    pheart.value="";
    $('#goatprod').prop("disabled", false);
  }
}
function goatchangezoo() {
  var pheart = document.getElementById('goatzoo');
  var pheartcheck = document.getElementById('goatzooc');
  if (pheartcheck.checked) {
    pheart.value="Sin datos";
    $('#goatzoo').prop("disabled", true);
  }
  else {
    pheart.value="";
    $('#goatzoo').prop("disabled", false);
  }
}
function goatchangeheart() {
  var pheart = document.getElementById('goatheart');
  var pheartcheck = document.getElementById('goatheartc');
  if (pheartcheck.checked) {
    pheart.value="0000";
    $('#goatheart').prop("disabled", true);
  }
  else {
    pheart.value="";
    $('#goatheart').prop("disabled", false);
  }
}
function goatchangeresp() {
  var presp = document.getElementById('goatresp');
  var prespcheck = document.getElementById('goatrespc');
  if (prespcheck.checked) {
    presp.value="0000";
    $('#goatresp').prop("disabled", true);
  }
  else {
    presp.value="";
    $('#goatresp').prop("disabled", false);
  }
}
function goatchangetemp() {
  var ptemp = document.getElementById('goattemp');
  var ptempcheck = document.getElementById('goattempc');
  if (ptempcheck.checked) {
    ptemp.value="0000";
    $('#goattemp').prop("disabled", true);
  }
  else {
    ptemp.value="";
    $('#goattemp').prop("disabled", false);
  }
}
function goatchangecapilar() {
  var pcap = document.getElementById('goatcapilar');
  var pcapcheck = document.getElementById('goatcapilarc');
  if (pcapcheck.checked) {
    pcap.value="0000";
    $('#goatcapilar').prop("disabled", true);
  }
  else {
    pcap.value="";
    $('#goatcapilar').prop("disabled", false);
  }
}
function goatchangemucos() {
  var pcap = document.getElementById('goatmucos');
  var pcapcheck = document.getElementById('goatmucosc');
  if (pcapcheck.checked) {
    pcap.value="Sin datos";
    $('#goatmucos').prop("disabled", true);
  }
  else {
    pcap.value="";
    $('#goatmucos').prop("disabled", false);
  }
}
function goatchangelymph() {
  var pmucos = document.getElementById('goatlymph');
  var pmucoscheck = document.getElementById('goatlymphc');
  if (pmucoscheck.checked) {
    pmucos.value="Sin datos";
    $('#goatlymph').prop("disabled", true);
  }
  else {
    pmucos.value="";
    $('#goatlymph').prop("disabled", false);
  }
}
function goatchangeruminal() {
  var pmucos = document.getElementById('goatruminal');
  var pmucoscheck = document.getElementById('goatruminalc');
  if (pmucoscheck.checked) {
    pmucos.value="Sin datos";
    $('#goatruminal').prop("disabled", true);
  }
  else {
    pmucos.value="";
    $('#goatruminal').prop("disabled", false);
  }
}
function goatchangecough() {
  var pmucos = document.getElementById('goatcough');
  var pmucoscheck = document.getElementById('goatcoughc');
  if (pmucoscheck.checked) {
    pmucos.value="Sin datos";
    $('#goatcough').prop("disabled", true);
  }
  else {
    pmucos.value="";
    $('#goatcough').prop("disabled", false);
  }
}
function goatchangecond() {
  var plymph = document.getElementById('goatcondition');
  var plymphcheck = document.getElementById('goatcondc');
  if (plymphcheck.checked) {
    plymph.value="Sin datos";
    $('#goatcondition').prop("disabled", true);
  }
  else {
    plymph.value="";
    $('#goatcondition').prop("disabled", false);
  }
}



// Rabbit form validation
function rabchangerace() {
  var prace = document.getElementById('rabrace');
  var pracecheck = document.getElementById('rabracec');
  if (pracecheck.checked) {
    prace.value="Sin datos";
    $('#rabrace').prop("disabled", true);
  }
  else {
    prace.value="";
    $('#rabrace').prop("disabled", false);
  }
}
function rabchangeage() {
  var page = document.getElementById('rabage');
  var pagecheck = document.getElementById('rabagec');
  if (pagecheck.checked) {
    page.value="0000";
    $('#rabage').prop("disabled", true);
  }
  else {
    page.value="";
    $('#rabage').prop("disabled", false);
  }
}
function rabchangeweight() {
  var pweight = document.getElementById('rabweight');
  var pweightcheck = document.getElementById('rabweightc');
  if (pweightcheck.checked) {
    pweight.value="0000";
    $('#rabweight').prop("disabled", true);
  }
  else {
    pweight.value="";
    $('#rabweight').prop("disabled", false);
  }
}
function rabchangeheart() {
  var pheart = document.getElementById('rabheart');
  var pheartcheck = document.getElementById('rabheartc');
  if (pheartcheck.checked) {
    pheart.value="0000";
    $('#rabheart').prop("disabled", true);
  }
  else {
    pheart.value="";
    $('#rabheart').prop("disabled", false);
  }
}
function rabchangeresp() {
  var presp = document.getElementById('rabresp');
  var prespcheck = document.getElementById('rabrespc');
  if (prespcheck.checked) {
    presp.value="0000";
    $('#rabresp').prop("disabled", true);
  }
  else {
    presp.value="";
    $('#rabresp').prop("disabled", false);
  }
}
function rabchangetemp() {
  var ptemp = document.getElementById('rabtemp');
  var ptempcheck = document.getElementById('rabtempc');
  if (ptempcheck.checked) {
    ptemp.value="0000";
    $('#rabtemp').prop("disabled", true);
  }
  else {
    ptemp.value="";
    $('#rabtemp').prop("disabled", false);
  }
}
function rabchangecapilar() {
  var pcap = document.getElementById('rabcapilar');
  var pcapcheck = document.getElementById('rabcapilarc');
  if (pcapcheck.checked) {
    pcap.value="0000";
    $('#rabcapilar').prop("disabled", true);
  }
  else {
    pcap.value="";
    $('#rabcapilar').prop("disabled", false);
  }
}
function rabchangemucos() {
  var pcap = document.getElementById('rabmucos');
  var pcapcheck = document.getElementById('rabmucosc');
  if (pcapcheck.checked) {
    pcap.value="Sin datos";
    $('#rabmucos').prop("disabled", true);
  }
  else {
    pcap.value="";
    $('#rabmucos').prop("disabled", false);
  }
}
function rabchangelymph() {
  var pmucos = document.getElementById('rablymph');
  var pmucoscheck = document.getElementById('rablymphc');
  if (pmucoscheck.checked) {
    pmucos.value="Sin datos";
    $('#rablymph').prop("disabled", true);
  }
  else {
    pmucos.value="";
    $('#rablymph').prop("disabled", false);
  }
}
function rabchangedehy() {
  var pmucos = document.getElementById('rabdehy');
  var pmucoscheck = document.getElementById('rabdehyc');
  if (pmucoscheck.checked) {
    pmucos.value="Sin datos";
    $('#rabdehy').prop("disabled", true);
  }
  else {
    pmucos.value="";
    $('#rabdehy').prop("disabled", false);
  }
}
function rabchangecond() {
  var plymph = document.getElementById('rabcondition');
  var plymphcheck = document.getElementById('rabcondc');
  if (plymphcheck.checked) {
    plymph.value="Sin datos";
    $('#rabcondition').prop("disabled", true);
  }
  else {
    plymph.value="";
    $('#rabcondition').prop("disabled", false);
  }
}



// Birds  form validation
function birdchangetype() {
  var ptype = document.getElementById('birdtype');
  var ptypecheck = document.getElementById('birdtypec');
  if (ptypecheck.checked) {
    ptype.value="Sin datos";
    $('#birdtype').prop("disabled", true);
  }
  else {
    ptype.value="";
    $('#birdtype').prop("disabled", false);
  }
}
function birdchangezoo() {
  var pzoo = document.getElementById('birdzoo');
  var pzoocheck = document.getElementById('birdzooc');
  if (pzoocheck.checked) {
    pzoo.value="Sin datos";
    $('#birdzoo').prop("disabled", true);
  }
  else {
    pzoo.value="";
    $('#birdzoo').prop("disabled", false);
  }
}
function birdchangeagew() {
  var pagew = document.getElementById('birdagew');
  var pagewcheck = document.getElementById('birdagewc');
  if (pagewcheck.checked) {
    pagew.value="0000";
    $('#birdagew').prop("disabled", true);
  }
  else {
    pagew.value="";
    $('#birdagew').prop("disabled", false);
  }
}
function birdchangeagem() {
  var pagem = document.getElementById('birdagem');
  var pagemcheck = document.getElementById('birdagemc');
  if (pagemcheck.checked) {
    pagem.value="0000";
    $('#birdagem').prop("disabled", true);
  }
  else {
    pagem.value="";
    $('#birdagem').prop("disabled", false);
  }
}
function birdchangeplace() {
  var pplace = document.getElementById('birdplace');
  var pplacecheck = document.getElementById('birdplacec');
  if (pplacecheck.checked) {
    pplace.value="Sin datos";
    $('#birdplace').prop("disabled", true);
  }
  else {
    pplace.value="";
    $('#birdplace').prop("disabled", false);
  }
}
function birdchangequant() {
  var pquant = document.getElementById('birdquant');
  var pquantcheck = document.getElementById('birdquantc');
  if (pquantcheck.checked) {
    pquant.value="0000";
    $('#birdquant').prop("disabled", true);
  }
  else {
    pquant.value="";
    $('#birdquant').prop("disabled", false);
  }
}
function birdchangeexist() {
  var pexist = document.getElementById('birdexist');
  var pexistcheck = document.getElementById('birdexistc');
  if (pexistcheck.checked) {
    pexist.value="Sin datos";
    $('#birdexist').prop("disabled", true);
  }
  else {
    pexist.value="";
    $('#birdexist').prop("disabled", false);
  }
}
function birdchangeorigin() {
  var porigin = document.getElementById('birdorigin');
  var porigincheck = document.getElementById('birdoriginc');
  if (porigincheck.checked) {
    porigin.value="Sin datos";
    $('#birdorigin').prop("disabled", true);
  }
  else {
    porigin.value="";
    $('#birdorigin').prop("disabled", false);
  }
}
function birdchangemorb() {
  var pmorb = document.getElementById('birdmorb');
  var pmorbcheck = document.getElementById('birdmorbc');
  if (pmorbcheck.checked) {
    pmorb.value="0000";
    $('#birdmorb').prop("disabled", true);
  }
  else {
    pmorb.value="";
    $('#birdmorb').prop("disabled", false);
  }
}
function birdchangemort() {
  var pmort = document.getElementById('birdmort');
  var pmortcheck = document.getElementById('birdmortc');
  if (pmortcheck.checked) {
    pmort.value="0000";
    $('#birdmort').prop("disabled", true);
  }
  else {
    pmort.value="";
    $('#birdmort').prop("disabled", false);
  }
}
function birdchangedate() {
  var pdate = document.getElementById('birddate');
  var pdatecheck = document.getElementById('birddatec');
  if (pdatecheck.checked) {
    pdate.value="0000";
    $('#birddate').prop("disabled", true);
  }
  else {
    pdate.value="";
    $('#birddate').prop("disabled", false);
  }
}
function birdchangewater() {
  var pwater = document.getElementById('birdwater');
  var pwatercheck = document.getElementById('birdwaterc');
  if (pwatercheck.checked) {
    pwater.value="Sin datos";
    $('#birdwater').prop("disabled", true);
  }
  else {
    pwater.value="";
    $('#birdwater').prop("disabled", false);
  }
}
function birdchangeeat() {
  var peat = document.getElementById('birdeat');
  var peatcheck = document.getElementById('birdeatc');
  if (peatcheck.checked) {
    peat.value="Sin datos";
    $('#birdeat').prop("disabled", true);
  }
  else {
    pwater.value="";
    $('#birdeat').prop("disabled", false);
  }
}
function birdchangevaccine() {
  var pvaccine = document.getElementById('birdvaccine');
  var pvaccinecheck = document.getElementById('birdvaccinec');
  if (pvaccinecheck.checked) {
    pvaccine.value="Sin datos";
    $('#birdvaccine').prop("disabled", true);
  }
  else {
    pvaccine.value="";
    $('#birdvaccine').prop("disabled", false);
  }
}
function birdchangedefec() {
  var pdefec = document.getElementById('birddefec');
  var pdefeccheck = document.getElementById('birddefecc');
  if (pdefeccheck.checked) {
    pdefec.value="Sin datos";
    $('#birddefec').prop("disabled", true);
  }
  else {
    pdefec.value="";
    $('#birddefec').prop("disabled", false);
  }
}
function birdchangecondition() {
  var pcondition = document.getElementById('birdcondition');
  var pconditioncheck = document.getElementById('birdconditionc');
  if (pconditioncheck.checked) {
    pcondition.value="Sin datos";
    $('#birdcondition').prop("disabled", true);
  }
  else {
    pcondition.value="";
    $('#birdcondition').prop("disabled", false);
  }
}
function birdchangeplumage() {
  var pplumage = document.getElementById('birdplumage');
  var pplumagecheck = document.getElementById('birdplumagec');
  if (pplumagecheck.checked) {
    pplumage.value="Sin datos";
    $('#birdplumage').prop("disabled", true);
  }
  else {
    pplumage.value="";
    $('#birdplumage').prop("disabled", false);
  }
}
function birdchangelegs() {
  var plegs = document.getElementById('birdlegs');
  var plegscheck = document.getElementById('birdlegsc');
  if (plegscheck.checked) {
    plegs.value="Sin datos";
    $('#birdlegs').prop("disabled", true);
  }
  else {
    plegs.value="";
    $('#birdlegs').prop("disabled", false);
  }
}
function birdchangebreath() {
  var pbreath = document.getElementById('birdbreath');
  var pbreathcheck = document.getElementById('birdbreathc');
  if (pbreathcheck.checked) {
    pbreath.value="0000";
    $('#birdbreath').prop("disabled", true);
  }
  else {
    pbreath.value="";
    $('#birdbreath').prop("disabled", false);
  }
}
function birdchangedehy() {
  var pdehy = document.getElementById('birddehy');
  var pdehycheck = document.getElementById('birddehyc');
  if (pdehycheck.checked) {
    pdehy.value="Sin datos";
    $('#birddehy').prop("disabled", true);
  }
  else {
    pdehy.value="";
    $('#birddehy').prop("disabled", false);
  }
}
function birdchangeatt() {
  var patt = document.getElementById('birdatt');
  var pattcheck = document.getElementById('birdattc');
  if (pattcheck.checked) {
    patt.value="Sin datos";
    $('#birdatt').prop("disabled", true);
  }
  else {
    patt.value="";
    $('#birdatt').prop("disabled", false);
  }
}



// Horse form validation
function changehorserace() {
  var hrrace = document.getElementById('horrace');
  var hrracecheck = document.getElementById('horracec');
  if (hrracecheck.checked) {
    hrrace.value="Sin datos";
    $('#horrace').prop("disabled", true);
  }
  else {
    hrrace.value="";
    $('#horrace').prop("disabled", false);
  }
}
function changehorseage() {
  var hrage = document.getElementById('horage');
  var hragecheck = document.getElementById('horagec');
  if (hragecheck.checked) {
    hrage.value="0000";
    $('#horage').prop("disabled", true);
  }
  else {
    hrage.value="";
    $('#horage').prop("disabled", false);
  }
}
function changehorseweight() {
  var hrweight = document.getElementById('horweight');
  var hrweightcheck = document.getElementById('horweightc');
  if (hrweightcheck.checked) {
    hrweight.value="0000";
    $('#horweight').prop("disabled", true);
  }
  else {
    hrweight.value="";
    $('#horweight').prop("disabled", false);
  }
}
function changehorseheart() {
  var hrheart = document.getElementById('horheart');
  var hrheartcheck = document.getElementById('horheartc');
  if (hrheartcheck.checked) {
    hrheart.value="0000";
    $('#horheart').prop("disabled", true);
  }
  else {
    hrheart.value="";
    $('#horheart').prop("disabled", false);
  }
}
function changehorseresp() {
  var hrresp = document.getElementById('horresp');
  var hrrespcheck = document.getElementById('horrespc');
  if (hrrespcheck.checked) {
    hrresp.value="0000";
    $('#horresp').prop("disabled", true);
  }
  else {
    hrresp.value="";
    $('#horresp').prop("disabled", false);
  }
}
function changehorsetemp() {
  var hrtemp = document.getElementById('hortemp');
  var hrtempcheck = document.getElementById('hortempc');
  if (hrtempcheck.checked) {
    hrtemp.value="0000";
    $('#hortemp').prop("disabled", true);
  }
  else {
    hrtemp.value="";
    $('#hortemp').prop("disabled", false);
  }
}
function changehorsecap() {
  var hrcap = document.getElementById('horcapilar');
  var hrcapcheck = document.getElementById('horcapc');
  if (hrcapcheck.checked) {
    hrcap.value="0000";
    $('#horcapilar').prop("disabled", true);
  }
  else {
    hrcap.value="";
    $('#horcapilar').prop("disabled", false);
  }
}
function changehorsemucos() {
  var hrmucos = document.getElementById('hormucosal');
  var hrmucoscheck = document.getElementById('hormucoc');
  if (hrmucoscheck.checked) {
    hrmucos.value="Sin datos";
    $('#hormucosal').prop("disabled", true);
  }
  else {
    hrmucos.value="";
    $('#hormucosal').prop("disabled", false);
  }
}
function changehorselymph() {
  var hrlymph = document.getElementById('horlymph');
  var hrlymphcheck = document.getElementById('horlymphc');
  if (hrlymphcheck.checked) {
    hrlymph.value="Sin datos";
    $('#horlymph').prop("disabled", true);
  }
  else {
    hrlymph.value="";
    $('#horlymph').prop("disabled", false);
  }
}
function changehorsecondition() {
  var hrage = document.getElementById('horcondition');
  var hragecheck = document.getElementById('horcondc');
  if (hragecheck.checked) {
    hrage.value="Sin datos";
    $('#horcondition').prop("disabled", true);
  }
  else {
    hrage.value="";
    $('#horcondition').prop("disabled", false);
  }
}



// Dog form validation
function changedograce() {
  var hrrace = document.getElementById('dograce');
  var hrracecheck = document.getElementById('dogracec');
  if (hrracecheck.checked) {
    hrrace.value="Sin datos";
    $('#dograce').prop("disabled", true);
  }
  else {
    hrrace.value="";
    $('#dograce').prop("disabled", false);
  }
}
function changedogage() {
  var hrage = document.getElementById('dogage');
  var hragecheck = document.getElementById('dogagec');
  if (hragecheck.checked) {
    hrage.value="0000";
    $('#dogage').prop("disabled", true);
  }
  else {
    hrage.value="";
    $('#dogage').prop("disabled", false);
  }
}
function changedogweight() {
  var hrweight = document.getElementById('dogweight');
  var hrweightcheck = document.getElementById('dogweightc');
  if (hrweightcheck.checked) {
    hrweight.value="0000";
    $('#dogweight').prop("disabled", true);
  }
  else {
    hrweight.value="";
    $('#dogweight').prop("disabled", false);
  }
}
function changedogheart() {
  var hrheart = document.getElementById('dogheart');
  var hrheartcheck = document.getElementById('dogheartc');
  if (hrheartcheck.checked) {
    hrheart.value="0000";
    $('#dogheart').prop("disabled", true);
  }
  else {
    hrheart.value="";
    $('#dogheart').prop("disabled", false);
  }
}
function changedogresp() {
  var hrresp = document.getElementById('dogresp');
  var hrrespcheck = document.getElementById('dogrespc');
  if (hrrespcheck.checked) {
    hrresp.value="0000";
    $('#dogresp').prop("disabled", true);
  }
  else {
    hrresp.value="";
    $('#dogresp').prop("disabled", false);
  }
}
function changedogtemp() {
  var hrtemp = document.getElementById('dogtemp');
  var hrtempcheck = document.getElementById('dogtempc');
  if (hrtempcheck.checked) {
    hrtemp.value="0000";
    $('#dogtemp').prop("disabled", true);
  }
  else {
    hrtemp.value="";
    $('#dogtemp').prop("disabled", false);
  }
}
function changedogcap() {
  var hrcap = document.getElementById('dogcapilar');
  var hrcapcheck = document.getElementById('dogcapc');
  if (hrcapcheck.checked) {
    hrcap.value="0000";
    $('#dogcapilar').prop("disabled", true);
  }
  else {
    hrcap.value="";
    $('#dogcapilar').prop("disabled", false);
  }
}
function changedogmucos() {
  var hrmucos = document.getElementById('dogmucosal');
  var hrmucoscheck = document.getElementById('dogmucoc');
  if (hrmucoscheck.checked) {
    hrmucos.value="Sin datos";
    $('#dogmucosal').prop("disabled", true);
  }
  else {
    hrmucos.value="";
    $('#dogmucosal').prop("disabled", false);
  }
}
function changedogcough() {
  var hrcough = document.getElementById('dogcough');
  var hrcoughcheck = document.getElementById('dogcoughc');
  if (hrcoughcheck.checked) {
    hrcough.value="Sin datos";
    $('#dogcough').prop("disabled", true);
  }
  else {
    hrcough.value="";
    $('#dogcough').prop("disabled", false);
  }
}
function changedogpulse() {
  var hrage = document.getElementById('dogpulse');
  var hragecheck = document.getElementById('dogpulsec');
  if (hragecheck.checked) {
    hrage.value="Sin datos";
    $('#dogpulse').prop("disabled", true);
  }
  else {
    hrage.value="";
    $('#dogpulse').prop("disabled", false);
  }
}
function changedogskin() {
  var hrage = document.getElementById('dogskin');
  var hragecheck = document.getElementById('dogskinc');
  if (hragecheck.checked) {
    hrage.value="Sin datos";
    $('#dogskin').prop("disabled", true);
  }
  else {
    hrage.value="";
    $('#dogskin').prop("disabled", false);
  }
}



// Cat form validation
function changecatrace() {
  var catrace = document.getElementById('catrace');
  var catracecheck = document.getElementById('catracec');
  if (catracecheck.checked) {
    catrace.value="Sin datos";
    $('#catrace').prop("disabled", true);
  }
  else {
    catrace.value="";
    $('#catrace').prop("disabled", false);
  }
}
function changecatage() {
  var catage = document.getElementById('catage');
  var catagecheck = document.getElementById('catagec');
  if (catagecheck.checked) {
    catage.value="0000";
    $('#catage').prop("disabled", true);
  }
  else {
    catage.value="";
    $('#catage').prop("disabled", false);
  }
}
function changecatweight() {
  var catweight = document.getElementById('catweight');
  var catweightcheck = document.getElementById('catweightc');
  if (catweightcheck.checked) {
    catweight.value="0000";
    $('#catweight').prop("disabled", true);
  }
  else {
    catweight.value="";
    $('#catweight').prop("disabled", false);
  }
}
function changecatheart() {
  var catheart = document.getElementById('catheart');
  var catheartcheck = document.getElementById('catheartc');
  if (catheartcheck.checked) {
    catheart.value="0000";
    $('#catheart').prop("disabled", true);
  }
  else {
    catheart.value="";
    $('#catheart').prop("disabled", false);
  }
}
function changecatresp() {
  var catresp = document.getElementById('catresp');
  var catrespcheck = document.getElementById('catrespc');
  if (catrespcheck.checked) {
    catresp.value="0000";
    $('#catresp').prop("disabled", true);
  }
  else {
    catresp.value="";
    $('#catresp').prop("disabled", false);
  }
}
function changecattemp() {
  var cattemp = document.getElementById('cattemp');
  var cattempcheck = document.getElementById('cattempc');
  if (cattempcheck.checked) {
    cattemp.value="0000";
    $('#cattemp').prop("disabled", true);
  }
  else {
    cattemp.value="";
    $('#cattemp').prop("disabled", false);
  }
}
function changecatcap() {
  var catcap = document.getElementById('catcapilar');
  var catcapcheck = document.getElementById('catcapc');
  if (catcapcheck.checked) {
    catcap.value="0000";
    $('#catcapilar').prop("disabled", true);
  }
  else {
    catcap.value="";
    $('#catcapilar').prop("disabled", false);
  }
}
function changecatmucos() {
  var catmucos = document.getElementById('catmucosal');
  var catmucoscheck = document.getElementById('catmucoc');
  if (catmucoscheck.checked) {
    catmucos.value="Sin datos";
    $('#catmucosal').prop("disabled", true);
  }
  else {
    catmucos.value="";
    $('#catmucosal').prop("disabled", false);
  }
}
function changecatcough() {
  var catcough = document.getElementById('catcough');
  var catcoughcheck = document.getElementById('catcoughc');
  if (catcoughcheck.checked) {
    catcough.value="Sin datos";
    $('#catcough').prop("disabled", true);
  }
  else {
    catcough.value="";
    $('#catcough').prop("disabled", false);
  }
}
function changecatpulse() {
  var catage = document.getElementById('catpulse');
  var catagecheck = document.getElementById('catpulsec');
  if (catagecheck.checked) {
    catage.value="Sin datos";
    $('#catpulse').prop("disabled", true);
  }
  else {
    catage.value="";
    $('#catpulse').prop("disabled", false);
  }
}
function changecatskin() {
  var catage = document.getElementById('catskin');
  var catagecheck = document.getElementById('catskinc');
  if (catagecheck.checked) {
    catage.value="Sin datos";
    $('#catskin').prop("disabled", true);
  }
  else {
    catage.value="";
    $('#catskin').prop("disabled", false);
  }
}



// Wild life form validation
function changewildzoo() {
  var catzoo = document.getElementById('wildzoo');
  var wildzoocheck = document.getElementById('wildzooc');
  if (wildzoocheck.checked) {
    wildzoo.value="Sin datos";
    $('#wildzoo').prop("disabled", true);
  }
  else {
    wildzoo.value="";
    $('#wildzoo').prop("disabled", false);
  }
}
function changewildambiental() {
  var wildambiental = document.getElementById('wildambiental');
  var wildambientalcheck = document.getElementById('wildambientalc');
  if (wildambientalcheck.checked) {
    wildambiental.value="Sin datos";
    $('#wildambiental').prop("disabled", true);
  }
  else {
    wildambiental.value="";
    $('#wildambiental').prop("disabled", false);
  }
}
function changewildfeed() {
  var wildfeed = document.getElementById('wildfeed');
  var wildfeedcheck = document.getElementById('wildfeedc');
  if (wildfeedcheck.checked) {
    wildfeed.value="Sin datos";
    $('#wildfeed').prop("disabled", true);
  }
  else {
    wildfeed.value="";
    $('#wildfeed').prop("disabled", false);
  }
}
function changewildback() {
  var wildback = document.getElementById('wildback');
  var wildbackcheck = document.getElementById('wildbackc');
  if (wildbackcheck.checked) {
    wildback.value="Sin datos";
    $('#wildback').prop("disabled", true);
  }
  else {
    wildheart.value="";
    $('#wildback').prop("disabled", false);
  }
}
function changewildevol() {
  var wildevol = document.getElementById('wildevol');
  var wildevolcheck = document.getElementById('wildevolc');
  if (wildevolcheck.checked) {
    wildevol.value="Sin datos";
    $('#wildevol').prop("disabled", true);
  }
  else {
    wildevol.value="";
    $('#wildevol').prop("disabled", false);
  }
}
function changewildheart() {
  var wildheart = document.getElementById('wildheart');
  var wildheartcheck = document.getElementById('wildheartc');
  if (wildheartcheck.checked) {
    wildheart.value="0000";
    $('#wildheart').prop("disabled", true);
  }
  else {
    wildheart.value="";
    $('#wildheart').prop("disabled", false);
  }
}
function changewildresp() {
  var wildresp = document.getElementById('wildresp');
  var wildrespcheck = document.getElementById('wildrespc');
  if (wildrespcheck.checked) {
    wildresp.value="0000";
    $('#wildresp').prop("disabled", true);
  }
  else {
    wildresp.value="";
    $('#wildresp').prop("disabled", false);
  }
}
function changewildtemp() {
  var wildtemp = document.getElementById('wildtemp');
  var wildtempcheck = document.getElementById('wildtempc');
  if (wildtempcheck.checked) {
    wildtemp.value="0000";
    $('#wildtemp').prop("disabled", true);
  }
  else {
    wildtemp.value="";
    $('#wildtemp').prop("disabled", false);
  }
}
function changewildcap() {
  var wildcap = document.getElementById('wildcapilar');
  var wildcapcheck = document.getElementById('wildcapc');
  if (wildcapcheck.checked) {
    wildcap.value="0000";
    $('#wildcapilar').prop("disabled", true);
  }
  else {
    wildcap.value="";
    $('#wildcapilar').prop("disabled", false);
  }
}
function changewildmucos() {
  var wildmucos = document.getElementById('wildmucos');
  var wildmucoscheck = document.getElementById('wildmucoc');
  if (wildmucoscheck.checked) {
    wildmucos.value="Sin datos";
    $('#wildmucos').prop("disabled", true);
  }
  else {
    wildmucos.value="";
    $('#wildmucos').prop("disabled", false);
  }
}
function changewildlymph() {
  var wildlymph = document.getElementById('wildlymph');
  var wildlymphcheck = document.getElementById('wildlymphc');
  if (wildlymphcheck.checked) {
    wildlymph.value="Sin datos";
    $('#wildlymph').prop("disabled", true);
  }
  else {
    wildlymph.value="";
    $('#wildlymph').prop("disabled", false);
  }
}
function changewildruminal() {
  var wildage = document.getElementById('wildruminal');
  var wildagecheck = document.getElementById('wildruminalc');
  if (wildagecheck.checked) {
    wildage.value="Sin datos";
    $('#wildruminal').prop("disabled", true);
  }
  else {
    wildage.value="";
    $('#wildruminal').prop("disabled", false);
  }
}



// Aquatic organism form validation
function aqchangegene() {
  var aqgene = document.getElementById('aqgenetic');
  var aqgenecheck = document.getElementById('aqgenec');
  if (aqgenecheck.checked) {
    aqgene.value="Sin datos";
    $('#aqgenetic').prop("disabled", true);
  }
  else {
    aqgene.value="";
    $('#aqgenetic').prop("disabled", false);
  }
}
function aqchangezoo() {
  var catzoo = document.getElementById('aqzoo');
  var aqzoocheck = document.getElementById('aqzooc');
  if (aqzoocheck.checked) {
    aqzoo.value="Sin datos";
    $('#aqzoo').prop("disabled", true);
  }
  else {
    aqzoo.value="";
    $('#aqzoo').prop("disabled", false);
  }
}
function aqchangeage() {
  var aqage = document.getElementById('aqage');
  var aqagecheck = document.getElementById('aqagec');
  if (aqagecheck.checked) {
    aqage.value="0000";
    $('#aqage').prop("disabled", true);
  }
  else {
    aqage.value="";
    $('#aqage').prop("disabled", false);
  }
}
function aqchangeweight() {
  var aqweight = document.getElementById('aqweight');
  var aqweightcheck = document.getElementById('aqweightc');
  if (aqweightcheck.checked) {
    aqweight.value="0000";
    $('#aqweight').prop("disabled", true);
  }
  else {
    aqweight.value="";
    $('#aqweight').prop("disabled", false);
  }
}
function aqchangedensity() {
  var aqdensity = document.getElementById('aqdensity');
  var aqdensitycheck = document.getElementById('aqdensityc');
  if (aqdensitycheck.checked) {
    aqdensity.value="0000";
    $('#aqdensity').prop("disabled", true);
  }
  else {
    aqdensity.value="";
    $('#aqdensity').prop("disabled", false);
  }
}
function aqchangebiomass() {
  var aqbiomass = document.getElementById('aqbiomass');
  var aqbiomasscheck = document.getElementById('aqbiomassc');
  if (aqbiomasscheck.checked) {
    aqbiomass.value="0000";
    $('#aqbiomass').prop("disabled", true);
  }
  else {
    aqbiomass.value="";
    $('#aqbiomass').prop("disabled", false);
  }
}
function aqchangechange() {
  var aqchange = document.getElementById('aqchange');
  var aqchangecheck = document.getElementById('aqchangec');
  if (aqchangecheck.checked) {
    aqchange.value="0000";
    $('#aqchange').prop("disabled", true);
  }
  else {
    aqchange.value="";
    $('#aqchange').prop("disabled", false);
  }
}
function aqchangesowing() {
  var aqsowing = document.getElementById('aqsowing');
  var aqsowingcheck = document.getElementById('aqsowingc');
  if (aqsowingcheck.checked) {
    aqsowing.value="Sin datos";
    $('#aqsowing').prop("disabled", true);
  }
  else {
    aqsowing.value="";
    $('#aqsowing').prop("disabled", false);
  }
}
function aqchangetemp6() {
  var aqtemp6 = document.getElementById('aq6am');
  var aqtemp6check = document.getElementById('aqtemp6c');
  if (aqtemp6check.checked) {
    aqtemp6.value="0000";
    $('#aq6am').prop("disabled", true);
  }
  else {
    aqtemp6.value="";
    $('#aq6am').prop("disabled", false);
  }
}
function aqchangetemp3() {
  var aqtemp3 = document.getElementById('aq3pm');
  var aqtemp3check = document.getElementById('aqtemp3c');
  if (aqtemp3check.checked) {
    aqtemp3.value="0000";
    $('#aq3pm').prop("disabled", true);
  }
  else {
    aqtemp3.value="";
    $('#aq3pm').prop("disabled", false);
  }
}
function aqchangeox6() {
  var aqox6 = document.getElementById('aqox6');
  var aqox6check = document.getElementById('aqox6c');
  if (aqox6check.checked) {
    aqox6.value="0000";
    $('#aqox6').prop("disabled", true);
  }
  else {
    aqox6.value="";
    $('#aqox6').prop("disabled", false);
  }
}
function aqchangeox3() {
  var aqox3 = document.getElementById('aqox3');
  var aqox3check = document.getElementById('aqox3c');
  if (aqox3check.checked) {
    aqox3.value="0000";
    $('#aqox3').prop("disabled", true);
  }
  else {
    aqox3.value="";
    $('#aqox3').prop("disabled", false);
  }
}
function aqchangeph6() {
  var aqph6 = document.getElementById('aqph6');
  var aqph6check = document.getElementById('aqph6c');
  if (aqph6check.checked) {
    aqph6.value="0000";
    $('#aqph6').prop("disabled", true);
  }
  else {
    aqph6.value="";
    $('#aqph6').prop("disabled", false);
  }
}
function aqchangeph3() {
  var aqph3 = document.getElementById('aqph3');
  var aqph3check = document.getElementById('aqph3c');
  if (aqph3check.checked) {
    aqph3.value="0000";
    $('#aqph3').prop("disabled", true);
  }
  else {
    aqph3.value="";
    $('#aqph3').prop("disabled", false);
  }
}
function aqchangeaqno2() {
  var aqno2 = document.getElementById('aqno2');
  var aqno2check = document.getElementById('aqno2c');
  if (aqno2check.checked) {
    aqno2.value="0000";
    $('#aqno2').prop("disabled", true);
  }
  else {
    aqno2.value="";
    $('#aqno2').prop("disabled", false);
  }
}
function aqchangeaqnh4() {
  var aqnh4 = document.getElementById('aqnh4');
  var aqnh4check = document.getElementById('aqnh4c');
  if (aqnh4check.checked) {
    aqnh4.value="0000";
    $('#aqnh4').prop("disabled", true);
  }
  else {
    aqnh4.value="";
    $('#aqnh4').prop("disabled", false);
  }
}
function aqchangeaqnh3() {
  var aqnh3 = document.getElementById('aqnh3');
  var aqnh3check = document.getElementById('aqnh3c');
  if (aqnh3check.checked) {
    aqnh3.value="0000";
    $('#aqnh3').prop("disabled", true);
  }
  else {
    aqnh3.value="";
    $('#aqnh3').prop("disabled", false);
  }
}
function aqchangetransp() {
  var aqtransp = document.getElementById('aqtransp');
  var aqtranspcheck = document.getElementById('aqtranspc');
  if (aqtranspcheck.checked) {
    aqtransp.value="0000";
    $('#aqtransp').prop("disabled", true);
  }
  else {
    aqtransp.value="";
    $('#aqtransp').prop("disabled", false);
  }
}
function aqchangemort() {
  var aqmort = document.getElementById('aqmort');
  var aqmortcheck = document.getElementById('aqmortc');
  if (aqmortcheck.checked) {
    aqmort.value="0000";
    $('#aqmort').prop("disabled", true);
  }
  else {
    aqmort.value="";
    $('#aqmort').prop("disabled", false);
  }
}
function aqchangestr() {
  var aqstr = document.getElementById('aqstr');
  var aqstrcheck = document.getElementById('aqstrc');
  if (aqstrcheck.checked) {
    aqstr.value="0000";
    $('#aqstr').prop("disabled", true);
  }
  else {
    aqstr.value="";
    $('#aqstr').prop("disabled", false);
  }
}


// Bee form validation
function beechangespecie() {
  var hrspecie = document.getElementById('beespecie');
  var hrspeciecheck = document.getElementById('beespeciec');
  if (hrspeciecheck.checked) {
    hrspecie.value="Sin datos";
    $('#beespecie').prop("disabled", true);
  }
  else {
    hrspecie.value="";
    $('#beespecie').prop("disabled", false);
  }
}
function beechangeback() {
  var hrback = document.getElementById('beeback');
  var hrbackcheck = document.getElementById('beebackc');
  if (hrbackcheck.checked) {
    hrback.value="0000";
    $('#beeback').prop("disabled", true);
  }
  else {
    hrback.value="";
    $('#beeback').prop("disabled", false);
  }
}
function beechangecell() {
  var hrcell = document.getElementById('beecell');
  var hrcellcheck = document.getElementById('beecellc');
  if (hrcellcheck.checked) {
    hrcell.value="Sin datos";
    $('#beecell').prop("disabled", true);
  }
  else {
    hrcell.value="";
    $('#beecell').prop("disabled", false);
  }
}
function beechangebckbreed() {
  var hrbckbreed = document.getElementById('beebckbreed');
  var hrbckbreedcheck = document.getElementById('beebckbreedc');
  if (hrbckbreedcheck.checked) {
    hrbckbreed.value="0000";
    $('#beebckbreed').prop("disabled", true);
  }
  else {
    hrbckbreed.value="";
    $('#beebckbreed').prop("disabled", false);
  }
}
function beechangeegg() {
  var hregg = document.getElementById('beeegg');
  var hreggcheck = document.getElementById('beeeggc');
  if (hreggcheck.checked) {
    hregg.value="0000";
    $('#beeegg').prop("disabled", true);
  }
  else {
    hregg.value="";
    $('#beeegg').prop("disabled", false);
  }
}
function beechangequant() {
  var hrquant = document.getElementById('beequant');
  var hrquantcheck = document.getElementById('beequantc');
  if (hrquantcheck.checked) {
    hrquant.value="0000";
    $('#beequant').prop("disabled", true);
  }
  else {
    hrquant.value="";
    $('#beequant').prop("disabled", false);
  }
}
function beechangeobs() {
  var hrobs = document.getElementById('beeobs');
  var hrobscheck = document.getElementById('beeobsc');
  if (hrobscheck.checked) {
    hrobs.value="Sin datos";
    $('#beeobs').prop("disabled", true);
  }
  else {
    hrobs.value="";
    $('#beeobs').prop("disabled", false);
  }
}
function beechangerack() {
  var hrrack = document.getElementById('beerack');
  var hrrackcheck = document.getElementById('beerackc');
  if (hrrackcheck.checked) {
    hrrack.value="0000";
    $('#beerack').prop("disabled", true);
  }
  else {
    hrrack.value="";
    $('#beerack').prop("disabled", false);
  }
}