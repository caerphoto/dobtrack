DTR.firstload = true;

DTR.getVCols = function() {
    // Returns a string where each character represents a column's
    // visibility; "1" is a visible column, "0" is not.
    var result = "";
    $("#ulCols input").each(function() {
       if (this.checked) {
           result += "1";
       } else {
           result += "0";
       }
    });

    return result;
};

DTR.setVCols = function(cols) {
    DTR.log("Applying column visibility (cols = " + cols + ")");
    for (var f = 1; f < DTR.fields.length; f++) {
        // Stupid IE doesn't support cols[f-1], so use cols.charAt(f-1) instead
        if (cols.charAt(f - 1) === "1") {
            chk = $("#vc_" + DTR.fields[f].ref)[0];
            chk.checked = true;
            DTR.cssDisplay(".i" + DTR.fields[f].ref, "");
        }
    }
};

DTR.updateURLs = function() {
    $("#lnkHere").attr("href", "" + DTR.urlParams());
    $("#lnkExport").attr("href", "/export" + DTR.urlParams());
    $("#tableprint").attr("href", "/tableprint" + DTR.urlParams());

    // Save current view settings
    DTR.createCookie("sortby", DTR.sortby, 7);
    DTR.createCookie("sortdir", DTR.sortasc ? "asc" : "desc", 7);
    DTR.createCookie("filter", DTR.filterstr, 7);
    DTR.createCookie("filterby", DTR.filterby, 7);
    DTR.createCookie("sheet", DTR.sheet, 7);
    DTR.createCookie("page", DTR.page, 7);
    DTR.createCookie("perpage", DTR.perpage, 7);
    DTR.createCookie("cols", DTR.cols, 7);
};

DTR.getItems = function() {
    DTR.log("getItems() called...")

    $.getJSON("/getitems" + DTR.urlParams(), function(data) {
        DTR.log("Ajax callback() called");

        DTR.items = data.items.slice(0);
        DTR.numfiltered = data.filtered;
        DTR.numtotal = data.total;
        $("#filteredcount").text(DTR.numfiltered);
        DTR.customers = data.customers;
        if (!DTR.username) {
            DTR.buildCustomerList();
        }
        DTR.username = data.username;
        // This is just a UI "convenience" - even if the user figures out how
        // to GET the relevant URL associated with the button, the server will
        // just ignore it anyway if they're not "admin".
        if (DTR.username !== "admin") {
            $("#deleteitem").hide();
            $("#applyedit").hide();
            $("#okedit").hide();
        }

        DTR.buildPageList();
        DTR.setPageControls();
        DTR.setupTable();

        DTR.updateURLs();

        var selPageList = document.getElementById("selPageList")
        selPageList.selectedIndex = DTR.page;

        // Reset "age timer" then set it to increment every minute
        DTR.cacheage = 0;
        window.clearInterval(DTR.cacheagetimer);
        DTR.cacheagetimer = window.setInterval(function() {
            DTR.cacheage += 1;
        }, 60000);
    });
};

DTR.buildCustomerList = function() {
    DTR.log("Building customer list...");
    $selCustomer = $("#divCustomer select").first();

    $selCustomer.html("");
    for (var c = 0; c < DTR.customers.length; c++) {
        var $opt = $("<option></option>");
        $opt.val(DTR.customers[c].value);
        $opt.html(DTR.customers[c].text);
        DTR.log("Name: " + DTR.customers[c].text +
                ", Value: " + DTR.customers[c].value);
        $selCustomer.append($opt);
    }
    if (DTR.username === "admin") {
        $selCustomer.append(
            $('<option value="UNKNOWN">(UNKNOWN)</option>'));
    }
    DTR.log("...done");

}

DTR.buildPageList = function() {
    DTR.log("Filling #selPageList...");
    var selPageList = document.getElementById("selPageList");
    selPageList.innerHTML = "";

    // calculate number of pages
    if (DTR.perpage) {
        var numpages = Math.ceil(DTR.numfiltered / DTR.perpage);
    } else {
        var numpages = 1;
    }

    var chosen = 0;
    for (var i = 0; i < numpages; i++) {
        var opt = document.createElement("option");
        var v = (i + 1) + "";
        if (i === DTR.page) {
            chosen = i;
        }
        var txt = document.createTextNode(v);
        opt.appendChild(txt);
        selPageList.appendChild(opt);
    }
    $("#selPageList").removeAttr("disabled");
};

DTR.setPageControls = function() {
    DTR.log("setPageControls() called");
    if (DTR.perpage) {
        var maxpages = Math.ceil(DTR.numfiltered / DTR.perpage) - 1;
    } else {
        var maxpages = 0;
    }

    DTR.log("  Total: " + DTR.numfiltered +
            ", Perpage: " + DTR.perpage +
            ", Maxpages: " + maxpages);
    DTR.log("  Page: " + DTR.page);
    if (DTR.page === 0) {
        $("#btnPrevPage").attr("disabled", "disabled");
    } else {
        $("#btnPrevPage").removeAttr("disabled");
    }
    if (DTR.page === maxpages) {
        $("#btnNextPage").attr("disabled", "disabled");
    } else {
        $("#btnNextPage").removeAttr("disabled");
    }
};

DTR.refilter = function() {
    DTR.log("refilter() called");
    DTR.filterby = ($("#selFilterBy").val()).substr(10);
    DTR.filterstr = ($("#listfilter").val()).toUpperCase();
    var inv = !!$("#chkInvertFilter").attr("checked");
    DTR.sheet = $("#selSheet").val();

    $("#indextable").html("");
    $("#loadingmessage").show();

    $("#btnPrevPage").attr("disabled", "disabled");
    $("#selPageList").attr("disabled", "disabled");
    $("#btnNextPage").attr("disabled", "disabled");

    DTR.getItems();
};

DTR.editorloading = function(loading) {
    if (loading) {
        $("#applyedit").attr("disabled", "disabled");
        $("#okedit").attr("disabled", "disabled");
        $("#deleteitem").attr("disabled", "disabled");
        $("#itemloadingmessage").show();
        $("#editorheading").hide();
    } else {
        $("#okapplyedit").removeAttr("disabled");
        $("#applyedit").removeAttr("disabled");
        $("#deleteitem").removeAttr("disabled");
        $("#itemloadingmessage").hide();
        $("#editorheading").show();
    }
};


DTR.setupTable = function() {
    DTR.log("Starting setupTable()...");
    $("#columnheaders").html("");

    DTR.buildTable();
    $("#loadingmessage").hide();

    var startitem = DTR.perpage * DTR.page + 1;
    var enditem = startitem + DTR.items.length - 1;
    $("#visiblecount").html(startitem + " &ndash; " + enditem);

    var de = document.documentElement;
    var db = document.body;
    var doc = de.offsetHeight ? de : db;
    $("#darkener").height(Math.max(doc.scrollHeight, doc.offsetHeight));

    DTR.log("  Assigning handlers...");
    $("#indextable tr").click(function(event) {
        DTR.showEditor(function() {
            var r = $(event.target).parent();
            return r.children("th").text();
        }());
    });

    // It'd be nice to do this with tr:hover in CSS but, of course, IE6
    // doesn't know what that means.
    $("#indextable tr").hover(
        function(event) {
            DTR.oldrowbg = this.style.backgroundColor;
            this.style.backgroundColor = "#FFF";
        },
        function(event) {
            this.style.backgroundColor = DTR.oldrowbg;
        }
    );

    $("#columnheaders th").hover(
        function(event) {
            DTR.oldheadbg = this.style.backgroundColor;
            this.style.backgroundColor = "#777";
        },
        function(event) {
            this.style.backgroundColor = DTR.oldheadbg;
        }
    )

    $("#columnheaders th").click(function(event) {
        // Find out which heading was clicked
        var target = event.target;
        if (event.target.tagName === "A") {
            target = $(event.target).parent()[0];
            event.stopPropagation();
        }

        DTR.log(" ***** ID of clicked element: " + target.id);

        var newsort = (target.id).substr(7);
        if (newsort === DTR.sortby) {
            DTR.sortasc = !DTR.sortasc;
        } else {
            DTR.sortby = newsort;
        }

        DTR.refilter();
    });

    DTR.log("  ...done");
    $(window).resize();
    DTR.log("setupTable() complete");
};

DTR.updaterow = function(item) {
    // Update the index table after applying changes to an item.
    var thisrow = $("th:contains('"+item.rep+"')").parent();
    var rownum = thisrow.index() + 1;
    DTR.log("update of row: "+rownum);

    // == rather than === is deliberate here in case .folio is made a
    // string
    thisrow[0].className = item.folio == 0 ? "i" : "h";

    var cacheindex = 0;
    for (var i = DTR.items.length-1; i--;) {
        try {
            if (DTR.items[i].rep === item.rep) {
                cacheindex = i;
                break;
            }
        } catch (TypeError) {
            DTR.log("Failed to read cache.items[" + i + "]");
        }

    }

    // Update table and local cache
    var dval = (item.value/100).toFixed(2);
    for (var field in item) {
        if (item.hasOwnProperty(field)) {
            var sel = "td.i" + field;
            var txt = "";
            switch (field) {
                case "value": {
                    txt = dval;
                    break;
                }
                case "fujitsuowned": {
                    txt = item.fujitsuowned ? "FUJ" : "CUS";
                    break;
                }
                case "warranty": {
                    txt = DTR.formatDate(item.warranty);
                    break;
                }
                case "datein": {
                    txt = DTR.formatDate(item.datein);
                    break;
                }
                case "rtsdate": {
                    txt = DTR.formatDate(item.rtsdate);
                    break;
                }
                default: txt = item[field];
            }
            thisrow.children(sel).text(txt);
            DTR.items[cacheindex][field] = item[field];
        }
    }

    // Re-display the editor (causing the data to be reloaded)
    if (!DTR.clickedok) {
        DTR.showEditor(item.rep);
    }
};

DTR.applychanges = function() {
    // Validates changes then sends/adds them to the DB
    $("#okedit").attr("disabled", "disabled");
    $("#applyedit").attr("disabled", "disabled");

    // Remove non-digits from REP <input>
    repbox = $("#itemeditor [name='rep']");
    var rep = (repbox.val()).match(/\d+/g)
    if (rep) {
        rep = rep.join("");
    }
    repbox.val(rep);

    var isnewitem = !!rep;
    var params = "?";

    if (!isnewitem) {
        rep = $("#rep").text();
        params = "/" + rep + params;
    }

    // Context-independent list of fields to read automatically from
    var fields = [
        "kind",
        "customer",
        "value",
        "costcentre",
        "ordernum",
        "make",
        "model",
        "part",
        "serial",
        "asset",
        "warranty",
        "issue",
        "state",
        "solution",
        "location",
        "grn",
        "sap",
        "comment"
    ];

    // Context-dependent fields
    if (isnewitem) {
        fields.push("rep");
    } else {
        fields.push("folio", "rtsdate");
    }

    if ($("[name='customer']").val() === "") {
        $("[name='customer']").val("UNKNOWN");
    }

    // The regexp here reads digits up to the decimal point, then the decimal
    // point, then any digits between it and the next non-digit.
    // E.g.: "£1234.56" would give "1234.56", and "1234.56.78" would give
    // "1234.56"
    var v = $("[name='value']").val();

    if (v) {
        v = v.match(/^\d+(?:\.?\d+)/);
    } else {
        v = "0.00";
    }

    $("[name='value']").val(v);
    v = $("[name='warranty']").val();
    $("[name='warranty']").val(DTR.unformatDate(v));

    v = $("[name='rtsdate']").val();
    $("[name='rtsdate']").val(DTR.unformatDate(v));

    for (var i=0; i < fields.length; i++) {
        var p1 = "";
        if (i > 0) {
            p1 = "&" + fields[i] + "=";
        } else {
            p1 = fields[i] + "=";
        }

        var p2 = "[name='" + fields[i] + "']";
        var p3 = $(p2).val();

        if (p3 === null) {
            p3 = "UNKNOWN";
        }

        params += p1 + encodeURIComponent(p3);
    }

    var fujown = document.getElementById("chkFujitsuOwned").checked;

    params += fujown ? "&fujitsuowned=yes" : "&fujitsuowned=no";

    if (isnewitem) {
        $("#itemeditor h2").hide();
        $("#darkener").hide();
        $("#itemeditor").fadeOut(100);
        $.get("/addtodb" + params, function(item) {
            DTR.refilter();
        });
    } else {
        $("#darkener").hide();
        $("#itemeditor").fadeOut(100);

        // "Disable" row until its data is updated properly
        var thisrow = $("th:contains('" + rep + "')").parent()[0];
        thisrow.className = "pendingupdate";
        $(thisrow).unbind("click");
        DTR.log("Sending edited item details to server...")
        DTR.log("(fujown = "+fujown+")");
        $.get("/applyitemedit/" + params, function(data) {
            DTR.log("/applyitemedit returned with:");
            DTR.log(data);
            $(thisrow).click(function(event) {
                DTR.showEditor($(event.target).parent().children("th").text());
            });
            if (!isnewitem) {
                DTR.updaterow(data);
            }
        });
    }

    DTR.editorloading(true);
};

DTR.deleteitem = function() {
    var rep = $("#rep").text();
    DTR.log("Deleting item with rep = " + rep);
    var targetrow = $("th:contains('"+rep+"')").parent()[0];

    if (confirm("Are you sure you want to remove this item from the database?\n\n" +
                "REP #: " + rep +
                "\nMake: " + $("[name='make']").val() +
                "\nModel: " + $("[name='model']").val() +
                "\n\nWARNING: This cannot be undone.")) {

        DTR.showLists();

        targetrow.className = "deleting"
        $(targetrow).unbind();
        $("#itemeditor").fadeOut(100);
        $("#darkener").hide();

        $.get("/deleteitem/"+rep, function() {
            var r = $("th:contains('"+rep+"')").parent();
            r.fadeOut(600, function() {
                r.remove();
            });
        });
    } else {
        DTR.showLists();
    }
};


DTR.resetModified = function() {
    // Reset modified status for all fields
    for (field in DTR.modified) {
        if (DTR.modified.hasOwnProperty(field)) {
            DTR.modified[field] = false;
        }
    }
}

DTR.detailfiller = function(item) {
    DTR.editorloading(false);
    $("#rep").text(item.rep);

    // Find equivalent item in cache
    var citem = function() {
        for (var i = DTR.items.length; i--; ) {
            if (item.rep === DTR.items[i].rep) {
                return DTR.items[i];
            }
        }
        // This shouldn't happen, but just in case:
        DTR.items.push(item);
        return item;
    }();

    DTR.resetModified();

    var bgCol = $("#section1").css("background-color");

    if (item.initials) {
        $("#initials").text(item.initials);
    } else {
        $("#initials").text("[unknown]");
    }

    if (item.datein) {
        $("#datein").text(DTR.formatDate(item.datein));
    } else {
        $("#datein").text("[unknown date]");
    }

    // Need to do this (and bind keypress/keyup) here since the data is loaded
    // dynamically, rather than on page load.
    var v = item.value / 100;
    $("[name='value']").val(v.toFixed(2));

    $("[name='warranty']").val(DTR.formatDate(item.warranty));
    $("[name='rtsdate']").val(DTR.formatDate(item.rtsdate));

    for (var field in item) {
        if (item.hasOwnProperty(field)) {
            if (field !== "rep" && field !== "value" && field !== "warranty" &&
                field !== "rtsdate") {
                $("[name='"+field+"']").val(item[field]);
            }
        }
    }

    $("#itemeditor option").removeAttr("selected");

    // Special handler for Customer field - attempts to match the database
    // value to an appropriate list option.
    // Should no longer be needed as of 29/9/10 as this is done server-side
    // when importing the CSV
    var m = (item.customer).toUpperCase();
    $("option[value='"+m+"']").attr("selected", "selected");

    DTR.log("  m = '" + m + "'");

    // Default to customer-owned
    var slash = item.customer.indexOf("/");
    if (slash !== -1) {
        DTR.log("Index of '/' character: " + slash);
    }

    var chk = "";
    if (slash !== -1) {
        DTR.modified.customer = true;
        DTR.modified.owner = true;
        chk = item.customer[slash + 1] === "F" ? "checked" : "";
        DTR.log("  customer['/'+1] = "+item.customer[slash + 1] +
                ", chk = '" + chk + "'");
    } else {

        if (item.fujitsuowned) {
            chk = "checked";
        }
    }
    $("#chkFujitsuOwned").attr("checked", chk);
    item.fujitsuowned = chk ? true : false;

    // Handler for DOB/DOA field - default to "DOB" if it's not "DOA"
    $("option[value='" + (item.kind === "DOA" ? "DOA": "DOB") +
        "']").attr("selected", "selected");

    $("[name='issue']").text(item.issue);
    $("[name='state']").text(item.state);
    $("[name='solution']").text(item.solution);

    // Colour lables of <select>s and checkboxes, since the controls'
    // background colours themselves can't be changed
    $("#lblCustomer").css("background-color",
                          item.customer === citem.customer ? bgCol : "#FEA");
    $("#lblKind").css("background-color",
                      item.kind === citem.kind ? bgCol : "#FEA");

    // This seems like an unnecessary hack:
    var io = item.fujitsuowned;
    var co = citem.fujitsuowned;
    var thesame = io === co;
    $("#lblFujitsuOwned").css("background-color", thesame ? bgCol : "#FEA");

    $("#okedit").removeAttr("disabled");
    $("#applyedit").removeAttr("disabled");

    $("#lnkPrint").attr("href", "/rtsform/"+item.rep);

    // Needs to be keyup otherwise the colour doesn't change until the next
    // key is pressed

    var fieldChange = function(field) {
        // check if this is an actual input field
        if (field.nodeName) {
            if (field.name === "warranty") {
                var modified = DTR.unformatDate($(field).val()) !=
                    item[field.name];
            }    else {
                var modified = $(field).val().toUpperCase() !=
                    item[field.name];
            }

            $(field).css("background-color", modified ? "#FEA" : "#FFF");
            DTR.modified[field.name] = modified;
        } // if (field.name)
        if (field.className === "sapgrn") {
            // Try to magically turn a pasted SAP+GRN combo into separate
            // values
            $sap = $("#tbx_sap");
            $grn = $("#tbx_grn");

            var sapstr = $sap.val();
            if (sapstr.length > 8) {
                var parts = sapstr.match(/\d+/g)
                if (parts && (parts[0] !== sapstr)) {
                    $sap.val(parts[0].slice(0, 8));
                    $grn.val(parts[1].slice(0, 8));
                    fieldChange($grn[0]);
                }
            }
            // make borders red if SAP/GRN is not valid
            // TODO - put this in a separate function and generalise it for
            // use with other fields
            tbxsap = document.getElementById("tbx_sap");
            tbxgrn = document.getElementById("tbx_grn");
            if (tbxsap.value.length === 8 && tbxgrn.value.length === 8) {
                tbxsap.style.borderColor = "#CCC";
                tbxgrn.style.borderColor = "#ccc";
            }
            else {
                tbxsap.style.borderColor = "#F88";
                tbxgrn.style.borderColor = "#F88";
            }
        }
    }

    // Trigger a fake SAP/GRN change in order to set their border colours
    // on editor load
    fieldChange({className: "sapgrn"});

    var inp = $("#itemeditor input:text");

    inp.keyup(function(event) {
        fieldChange(this)
    });
    inp.change(function(event) {
        fieldChange(this);
    });
    inp.blur(function(event) {
        fieldChange(this);
    });

    var txa = $("#itemeditor textarea");
    txa.keyup(function() {
        fieldChange(this);
    });
    txa.change(function() {
        fieldChange(this);
    });
    txa.blur(function() {
        fieldChange(this);
    });

    $("#itemeditor select").change(function(event) {
        var modified = $(event.target).val() != item[event.target.name];
        DTR.log("<select> '"+event.target.name+"' changed.");
        DTR.modified[event.target.name] = modified;
    });

    $("#chkFujitsuOwned").change(function(event) {
        var modified = event.target.checked != item[event.target.name];
        DTR.modified.fujitsuowned = modified;
        DTR.log("chkFujOwned.checked = "+event.target.checked+
                ", modified = "+modified);
    });
};

DTR.showEditor = function(rep) {
    // Shows the item editor and sets it up to either recieve the details of
    // an existing item, filled via a callback from a $.get() request, or
    // blanks all the fields in preparation for the user entering the details
    // of a new item.
    var itemeditor = $("#itemeditor");

    $("#selItemsPerPage").css("visibility", "hidden");
    $("#selPageList").css("visibility", "hidden");
    $("#selSheet").css("visibility", "hidden");
    $("#selFilterBy").css("visibility", "hidden");


    if (rep === 0) {
        itemeditor.attr("class", "i");
        $("#pendingrep").show();
    } else {
        itemeditor[0].className =
            $("#indextable th:contains("+rep+")").parent().attr("class");
        $("#pendingrep").hide();
    }

    $("#darkener").show();
    itemeditor.show();

    // Slight hack to make the SAP input box width correct, so it lines up
    // with the other boxes (except, alas, in Firefox where it's 1px out)
    if (DTR.firstload) {
        var w = $("#tbx_sap").width();
        w -= 10; // 10px because its border-right is 8px, plus the other
                 // two borders (its left, and tbx_grn's right)
        $("#tbx_sap").width(w);

        DTR.firstload = false;
    }

    // Show editor centred (v & h) in window (theoretically - doesn't always
    // work properly. I should fix this < TODO)
    var wh = $(window).height();
    var eh = itemeditor.height();
    var et = (wh - eh) / 2;

    var ww = $(window).width();
    var ew = itemeditor.width();
    var el = (ww - ew) / 2;

    var o = {
        left: el + $(window).scrollLeft(),
        top: et + $(window).scrollTop()
    };
    itemeditor.offset(o);

    // clear existing values/text/etc.
    itemeditor.find("option").removeAttr("selected");
    itemeditor.find("select").val("");
    itemeditor.find("input:text").val("");
    itemeditor.find("textarea").text(""); // not sure why both are necessary
    itemeditor.find("textarea").val("");  // here but it doesn't hurt

    // reset colours
    itemeditor.find("input:text, select, textarea").css("background-color",
                    "#FFF");
    itemeditor.find("#chkFujitsuOwned")[0].checked = false;

    itemeditor.find("label").css("background-color",
                                 $("#section1").css("background-color"));

    // Remove all titles and warnings ("Add item", "Details for..." etc.)
    itemeditor.find("h2").hide();
    itemeditor.find("#repinuse").hide();
    itemeditor.find("#repok").hide();

    itemeditor.find("input:text").not("[name='rep']").unbind();
    itemeditor.find("textarea").unbind();

    if (rep === 0) {
        // Show/hide headings appropriate adding a new item
        itemeditor.find("[name='rep']").parent().show();
        itemeditor.find("[name='folio']").parent().hide();
        itemeditor.find("[name='rtsdate']").parent().hide();
        itemeditor.find("#newitemheading").show();

        // Defaults for new item
        itemeditor.find("[name='kind']").val("DOB");
        itemeditor.find("[name='customer']").val("UNKNOWN");

        // Disabled by default - only enabled once user enters a valid REP
        itemeditor.find("#okedit").attr("disabled", "disabled");

        // don't need Delete and Apply buttons, but want to keep the layout
        itemeditor.find("#applyedit").css("visibility", "hidden");
        itemeditor.find("#deleteitem").css("visibility", "hidden");
        itemeditor.find("#otheroptions").css("visibility", "hidden");

        itemeditor.find("[name='rep']").focus();

        // Mark REP as modified right from the start so the user is asked for
        // confirmation if they click Cancel
        DTR.resetModified();
        DTR.modified.rep = true;
    } else {
        // displaying data for an existing item
        itemeditor.find("[name='rep']").parent().hide();
        itemeditor.find("[name='folio']").parent().show();
        itemeditor.find("[name='rtsdate']").parent().show();

        itemeditor.find("#itemloadingmessage").show();

        // These buttons are relevant for when displaying an existing item
        itemeditor.find("#applyedit").css("visibility", "visible");
        itemeditor.find("#deleteitem").css("visibility", "visible");
        itemeditor.find("#otheroptions").css("visibility", "visible");

        // Load from cache if the data there is less than 5 minutes old,
        // otherwise get details from server
        DTR.log("cacheage: " + DTR.cacheage);
        if (DTR.cacheage < 5) {
            DTR.detailfiller(DTR.getItemFromRep(rep));
        } else {
            $.get("/getitem/" + rep, DTR.detailfiller);
        }

    } // if (rep === 0)
};

DTR.cssDisplay = function(sel, display) {
    // Changes the 'display' CSS property of the rule with the given selector
    // (this is much quicker than changing the visibility of each element
    // individually)

    // IE stores CSS rules in 'rules[]'; others store them in 'cssRules[]'
    if (document.styleSheets[0].cssRules) {
        var docrules = document.styleSheets[0].cssRules;
    } else {
        var docrules = document.styleSheets[0].rules;
    }

    DTR.log("Changing CSS rule '" + sel + "' to '" + display + "'...");
    for (var i = 0; i < docrules.length; i++) {
        var st = docrules[i].selectorText + "";
        if (st.toLowerCase() == sel) {
            docrules[i].style.display = display;
            break;
        }
    }
    DTR.log("...done");
};

DTR.buildVColsList = function() {
    DTR.log("Building column visibility list...");
    var props = DTR.fields.slice(1);

    // Add checkboxes to #ulCols that toggle the relevant column's visibility
    var ulCols = $("#ulCols");
    for (var i = 0; i < props.length; i++) {
        var li = document.createElement("li");
        var lbl = document.createElement("label");
        var inp = document.createElement("input");
        var txt = document.createTextNode("");

        inp.type = "checkbox";
        inp.id = "vc_" + props[i].ref;
        inp.nodeValue = "i" + props[i].ref;

        lbl.htmlFor = "vc_" + props[i].ref;
        lbl.innerHTML = props[i].label;
        lbl.insertBefore(inp, lbl.firstChild);

        li.appendChild(lbl);

        ulCols.append(li);
    }

    ulCols.hide();
    DTR.log("...done");
};

// Workaround for stupid IE display bug where <select> elements show through
// absolute positioned elements, regardless of z-index
DTR.showLists = function() {
    $("#selItemsPerPage").css("visibility", "visible");
    $("#selPageList").css("visibility", "visible");
    $("#selSheet").css("visibility", "visible");
    $("#selFilterBy").css("visibility", "visible");
}
DTR.hideLists = function() {
    $("#selItemsPerPage").css("visibility", "hidden");
    $("#selPageList").css("visibility", "hidden");
    $("#selSheet").css("visibility", "hidden");
    $("#selFilterBy").css("visibility", "hidden");
}

DTR.init = function() {
    DTR.initlog();
    DTR.log("init started");

    DTR.buildVColsList();

    if (!DTR.readQueryString()) {
        // Try to read from cookie
        DTR.log("Attempting to read cookies...")
        DTR.sortby = DTR.readCookie("sortby") || DTR.sortby;
        DTR.sortasc = DTR.readCookie("sortdir") === "asc";
        DTR.filterstr = DTR.readCookie("filter") || DTR.filterstr;
        DTR.filterby = DTR.readCookie("filterby") || DTR.filterby;
        DTR.sheet = DTR.readCookie("sheet") || DTR.sheet;
        DTR.page = +DTR.readCookie("page") || DTR.page;
        DTR.perpage = +DTR.readCookie("perpage") || DTR.perpage;
        DTR.cols = DTR.readCookie("cols") || "0001000011110011000000";
        DTR.log("...done.");
    }
    DTR.setVCols(DTR.cols);

    $("#listfilter").val(DTR.filterstr);
    $("#selSheet").val(DTR.sheet);

    $("#itemeditor").hide();

    DTR.log("Filling Filter dropdown list...");
    // Fill the "Filter" dropdown list
    (function() {
        var p = DTR.fields;
        var pl = p.length;
        var sel = $("#selFilterBy");
        sel.append($("<option value='filterby'>(all fields)</option>"));
        for (var i = 0; i < pl; i++) {
            var opt = $("<option></option>");
            opt.attr("value", "filterby.i" + p[i].ref);
            opt.html(p[i].label);
            sel.append(opt);
        }
    }());
    DTR.log("...done");

    DTR.log("Setting up itemeditor...");
    // Item editor stuff
    var t;
    $("#itemeditor [name='rep']").keyup(function(event) {
        // Disable OK button until we're sure the REP is unique
        $("#okedit").attr("disabled", "disabled");
        var rep = $(event.target).val();
        if (rep) {
            // Remove non-digits
            rep = rep.match(/\d+/g);
            if (rep) {
                rep = rep.join("");
            } else {
                return;
            }

            var setRepLoader = function(loading) {
                var bgpos = loading ? "4px" : "-16px";
                $("#repinuse").css("background-position", bgpos);
                $("#repok").css("background-position", bgpos);
                $("#pendingrep").css("background-position", bgpos);
            }

            // Half-second delay to avoid spamming the server with requests
            clearTimeout(t);
            t = setTimeout(function() {
                setRepLoader(true);
                $.get("/doesrepexist/"+rep, function(exists) {
                    setRepLoader(false);
                    $("#pendingrep").hide();
                    if (exists) {
                        $("#repinuse").show();
                        $("#repok").hide();
                    } else {
                        $("#okedit").removeAttr("disabled");
                        $("#repinuse").hide();
                        $("#repok").show();
                    }
                });
            }, 500);
        } else {
            clearTimeout(t);
            $("#repok").hide();
            $("#repinuse").hide();
            $("#pendingrep").show();
        }
    });


    var modified = function() {
        DTR.log("Checking for modified fields...");
        for (field in DTR.modified) {
            if (DTR.modified.hasOwnProperty(field)) {
                if (DTR.modified[field]) {
                    DTR.log("  Field '"+field+"' has been modified.");
                    return true;
                }
            }
        }
        DTR.log("...none found.");
        return false;
    };

    $("#canceledit").click(function() {
        var mod = DTR.username === "admin" ? modified() : false;

        if (mod) {
            if (confirm("Are you sure you want to close without "+
                        "saving changes?")) {
                $("#darkener").hide();
                $("#itemeditor").fadeOut(100);

                DTR.showLists();
            };
        } else {
            DTR.showLists();

            $("#darkener").hide();
            $("#itemeditor").fadeOut(100);
        }
    });

    $("#deleteitem").click(function() {
        DTR.deleteitem();
    });

    $("#applyedit").click(function() {
        DTR.clickedok = false;
        // Will apply changes whether the details have been modified or not
        DTR.applychanges();
    });

    $("#okedit").click(function() {
        DTR.clickedok = true;
        DTR.showLists();
        if (modified()) {
            DTR.applychanges();
        } else {
            $("#darkener").hide();
            $("#itemeditor").fadeOut(100);
        }
    });

    DTR.log("...done");

    $("#lnkAddNewItem").click(function() {
        DTR.showEditor(0);
    });


    DTR.log("VCols stuff...");
    // Visible columns stuff
    var vctimer;
    $("#divCols").click(function() {
        var dc = $("#divCols");
        var uc = $("#ulCols");
        var od = dc.offset();
        var ou = uc.offset();

        clearTimeout(vctimer);
        $("#ulCols").show();
        uc.offset(od);
    });

    // Hide the vcols list 300ms after the mouse pointer leaves it
    $("#ulCols").mouseleave(function() {
        clearTimeout(vctimer);
        vctimer = setTimeout(function() {
            $("#ulCols").hide();
        }, 300);
    });

    // Cancel hiding if the mouse pointer re-enters the list
    $("#ulCols").mouseenter(function() {
        clearTimeout(vctimer);
    });

    // Toggle relevant column's visibility depending on which box was clicked
    $("#ulCols input").click(function() {
        var d = $(this).attr("checked") ? "" : "none";
        DTR.cssDisplay(".i" + (this.id).slice(3), d);

        // Update internal record if which columns are visible
        DTR.cols = DTR.getVCols();

        // Make sure CSV and 'Link to this page' links are up to date
        DTR.updateURLs();

        // This bit is just so the "Loading..." message spans the full width
        // of the table. I might change it later so it displays as a <div>
        // separate from the table, so this bit won't be necessary.
        var vcount = 0;
        $("#ulCols input").each(function() {
            if (this.checked) {
                vcount += 1;
            }
        });

        DTR.log("# of checked columns: " + vcount);

        // Not entirely sure why I need to add 2 here, it should just be 1
        // to account for the lack of a REP option in the vcols list
        $("#loadingmessage td")[0].colSpan =  vcount + 2;

    });

    DTR.log("...done");

    DTR.log("Filter setup...");
    // Filter stuff
    $("#selFilterBy").change(function() {
        if ($("#listfilter").val()) {
            DTR.page = 0;
            DTR.refilter();
        }
    });

    $("#chkInvertFilter").click(function() {
        if ($("#listfilter").val()) {
            DTR.page = 0;
            DTR.refilter();
        }
    });

    $("#btnClear").click(function() {
        if ($("#listfilter").val()) {
            $("#selFilterBy").val("filterby");
            $("#listfilter").val("");
            $("#chkInvertFilter").removeAttr("checked");
            DTR.page = 0;
            DTR.refilter();
        }
    });

    $("#listfilter").keyup(function(event) {
        if (event.keyCode === 13) {
            DTR.page = 0;
            DTR.refilter();
        }
    });

    $("#selSheet").change(function() {
        DTR.page = 0;
        DTR.refilter();
    });

    $("#btnSearch").click(function() {
        DTR.page = 0;
        DTR.refilter();
    });

    DTR.log("...done");

    // Pagination stuff
    DTR.log("Pagination setup...");

    $("#selItemsPerPage").change(function() {
        var selItemsPerPage = document.getElementById("selItemsPerPage");
        var i = selItemsPerPage.selectedIndex;
        DTR.perpage = parseInt(selItemsPerPage.options[i].value, 10);
        DTR.log("DTR.perpage changed to: " + DTR.perpage);
        DTR.buildPageList();
        DTR.page = 0;
        document.getElementById("selPageList").selectedIndex = DTR.page;
        $("#selPageList").change();
    });

    $("#btnPrevPage").click(function() {
        DTR.page--;
        document.getElementById("selPageList").selectedIndex = DTR.page;
        $("#selPageList").change();
    });

    $("#selPageList").change(function() {
        DTR.page = $("#selPageList")[0].selectedIndex;
        DTR.refilter();//setPageControls();
    });

    $("#btnNextPage").click(function() {
        DTR.page++;
        document.getElementById("selPageList").selectedIndex = DTR.page;
        $("#selPageList").change();
    });

    $("#hidelog").click(function() {
        $("#logheader").hide();
        $("#log").hide();
    });

    DTR.log("...done");

    $(document).ajaxError(function(e, xhr, settings, exception) {
        document.innerHTML = "";
        document.write(xhr.responseText);
    });

    // ...and finally
    DTR.log("init finished, loading item data from server...");
    $.ajaxSetup({
        cache: false
    })

    if (DTR.filterby) {
        $("#selFilterBy").val("filterby.i" + DTR.filterby);
    }
    $("#listfilter").val(DTR.filterstr);
    $("#selSheet").val(DTR.sheet);
    $("#selItemsPerPage").val(DTR.perpage);

    DTR.refilter();
};

$(document).ready(DTR.init);
