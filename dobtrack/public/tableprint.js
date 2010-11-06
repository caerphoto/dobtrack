DTR.getItems = function() {
    DTR.log("Calling $.getJSON()...")
    $.getJSON("/getitems" + DTR.urlParams(), function(data) {
        DTR.log("...callback called.")
        DTR.items = data.items.slice(0);
        $("#loadingmessage").hide();
        DTR.buildTable();
        window.print();
    });
};

DTR.init = function() {
    DTR.readQueryString();
    DTR.perpage = 0;

    DTR.log("Condensing DTR.properties...")

    // Rebuild properties list to only include visible columns, so buildTable
    // will not add columns that wouldn't get printed anyway
    var oldprops = DTR.fields.slice(1);
    DTR.fields = [{ref: "rep", label: "REP #", shortlabel: "REP"}];
    for (var i = 0; i < oldprops.length; i++) {
        if (DTR.cols.charAt(i) === "1") {
            DTR.fields.push(oldprops[i]);
            DTR.log("Adding column: " + oldprops[i].ref);
        }
    }

    DTR.getItems();
};

$(document).ready(DTR.init);
