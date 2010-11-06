;
if (typeof DOB_EDIT === "undefined") var DOB_EDIT = {};

DOB_EDIT.init = function() {
    $("[name='value']").focus(); // gets overridden in additem.js

    // store current values of fields, so we can highlight fields that change
    var initial_vals = {
        rep: $("[name='rep']").val(),
        initials: $("[name='initials']").val(),
        customer: $("[name='customer']").val(),
        fujitsuowned: $("[name='fujitsuowned']").is(':checked'),
        value: $("[name='value']").val(),
        costcentre: $("[name='costcentre']").val(),
        order: $("[name='order']").val(),

        make: $("[name='make']").val(),
        model: $("[name='model']").val(),
        part: $("[name='part']").val(),
        serial: $("[name='serial']").val(),
        asset: $("[name='asset']").val(),
        warranty: $("[name='warranty']").val(),

        location: $("[name='location']").val(),

        grn: $("[name='grn']").val(),
        sap: $("[name='sap']").val(),

        folio: $("[name='folio']").val(),
        rtsdate: $("[name='rtsdate']").val(),

        issue: $("[name='issue']").val(),
        state: $("[name='state']").val(),
        solution: $("[name='solution']").val()
    }

    $("input,textarea").keydown(function(event) {
        // prevent form being submitted when Enter is pressed
        // (as users are likely to press it by mistake)
        if (event.keyCode == '13') {
            event.preventDefault();
        }
    });

    // Needs to be keyup otherwise the colour doesn't change until the next
    // key is pressed
    $("input[type='text'],textarea").keyup(function(event) {
        if ($(event.target).val().toUpperCase() == initial_vals[event.target.name]) {
            $(event.target).css("background-color", "#FFF");
        } else {
            $(event.target).css("background-color", "#FEA");
        }

        // *** TO DO: implement special handler for GRN/SAP when pasting from
        // clipboard (i.e. remove separator and any whitespace/other junk)
    });

    // Prevent non-numeric keypresses in Value and Folio fields
    // If a . is entered in Folio, it will be rounded out of existence later
    $("[name='value'],[name='folio']").keypress(function(event) {
        var c = String.fromCharCode(event.which);
        if ("0123456789.".indexOf(c) == -1) {
            event.preventDefault();
        }
    });

    // special handler for checkboxes, because they're stupid
    $("input[type='checkbox']").click(function(event) {
        if ($(event.target).is(':checked') == initial_vals[event.target.name]) {
            $("[for='"+event.target.name+"']").css("background-color", "#CCE0E9");

            // can't change a checkbox's background on Firefox and Chrome in
            // Ubuntu, but I'm leaving this in just in case it works in IE
            $(event.target).css("background-color", "#CCE0E9");
            $("#debug1").text($(event.target).is(':checked'));
        }
        else {
            $("[for='"+event.target.name+"']").css("background-color", "#FEA");
            $(event.target).css("background-color", "#FEA");
            $("#debug1").text($(event.target).is(':checked'));
        }
    });

};

$(document).ready(DOB_EDIT.init);