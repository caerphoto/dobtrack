;
if (typeof console === "undefined") {
    var console = {
        // Very basic reproduction of Chrome/Firebug's console window
        // Assumes there is an element called "log"; does nothing if not
        log: function() {
            var s = [];
            var elog = document.getElementById("log");
            if (elog) {
                for (var i = 0; i < arguments.length; i++) {
                    s.push(arguments[i]);
                }
                var p = document.createElement("p");
                var t = document.createTextNode(s.join(" "));
                p.appendChild(t);
                elog.appendChild(p);
                $(elog).scrollTop(elog.scrollHeight);
            }
        }
    }
} else {
    $("#log").remove();
    $("#logheader").remove();
}

if (typeof DTR === "undefined") var DTR = {
    clickedok: false,

    // Eventually this will be passed to the app from the server. The order
    // is important here as it determines the order of columns on the table.
    fields: [
        {ref: "rep", label: "REP #", shortlabel: "REP"},
        {ref: "initials", label: "Initials", shortlabel: "Init"},
        {ref: "datein", label: "Date To Us", shortlabel: "Date&nbsp;in"},
        {ref: "kind", label: "DOA/DOB", shortlabel: "A/B"},
        {ref: "customer", label: "Customer", shortlabel: "Cust"},
        {ref: "fujitsuowned", label: "Owner", shortlabel: "Owner"},
        {ref: "value", label: "Value (&pound;)", shortlabel: "Value"},
        {ref: "costcentre", label: "Cost Centre", shortlabel: "Cost-C"},
        {ref: "ordernum", label: "Order Number", shortlabel: "Order&nbsp;#"},
        {ref: "make", label: "Make", shortlabel: "Make"},
        {ref: "model", label: "Model", shortlabel: "Model"},
        {ref: "part", label: "Part Number", shortlabel: "Part&nbsp;#"},
        {ref: "serial", label: "Serial Number", shortlabel: "Serial&nbsp;#"},
        {ref: "asset", label: "Asset Tag", shortlabel: "Asset&nbsp;#"},
        {ref: "warranty", label: "Warranty Date", shortlabel: "Warranty"},
        {ref: "location", label: "Location", shortlabel: "Location"},
        {ref: "issue", label: "Reported Issue", shortlabel: "Issue"},
        {ref: "state", label: "Current State", shortlabel: "State"},
        {ref: "solution", label: "Solution", shortlabel: "Solution"},
        {ref: "sap", label: "SAP (604&hellip;)", shortlabel: "SAP"},
        {ref: "grn", label: "GRN (840&hellip;)", shortlabel: "GRN"},
        {ref: "rtsdate", label: "RTS Date", shortlabel: "RTS&nbsp;Date"},
        {ref: "folio", label: "Folio Number", shortlabel: "Folio"},
        {ref: "comment", label: "Comment", shortlabel: "Comment"}
    ],

    modified: {
        rep: false,
        kind: false,
        customer: false,
        fujitsuowned: false,
        owner: false,
        value: false,
        costcentre: false,
        ordernum: false,
        make: false,
        model: false,
        part: false,
        serial: false,
        asset: false,
        warranty: false,
        location: false,
        issue: false,
        state: false,
        solution: false,
        grn: false,
        sap: false,
        rtsdate: false,
        folio: false
    },

    numcols: 7,
    username: "",
    customers: [],

    // Default settings - can be overridden by cookie or parameter string
    sortby: "rep",
    sortasc: false,
    filterstr: "",
    filterby: "",
    sheet: "L",
    page: 0,
    perpage: 25,
    cols: "0001000011000011000000",

    numfiltered: 0,
    numtotal: 0,

    cacheage: 0,
    cacheagetimer: 0,

    items: [],

    rowinuse: {},

    logstarttime: 0,
    lastevent: 0
};


DTR.schar = function(c) {
    return document.createEntityReference(c);
},

DTR.initlog = function() {
    DTR.logstarttime = new Date();
    DTR.lastevent = DTR.logstarttime;
};

DTR.log = function(text) {
    var now = new Date();
    console.log((now - DTR.logstarttime)+"ms", " [", text, "] ",
                (now - DTR.lastevent)+"ms");
    DTR.lastevent = now;
};

DTR.getItemFromRep = function(rep) {
    for (var i = DTR.items.length; i--; ) {
        if (DTR.items[i].rep == rep) {
            return DTR.items[i];
        }
    }
};

DTR.propIndex = function(property) {
    for (var i = this.fields.length; i--;) {
        if (this.fields[i].ref === property) {
            return i;
        }
    }
    return -1;
};

DTR.urlParams = function() {
    return ["?sortby=", DTR.sortby, "&sortdir=", DTR.sortasc ? "asc" : "desc",
            "&filter=", DTR.filterstr, "&filterby=", DTR.filterby,
            "&sheet=", DTR.sheet, "&page=", DTR.page,
            "&perpage=", DTR.perpage, "&cols=", DTR.cols].join("");
};

DTR.readQueryString = function () {
    DTR.log("Attempting to read query string...");
    var qs = window.location.search.substring(1);

    if (qs.length === 0) {
        DTR.log("...no query string found.");
        return false;
    }

    var queries = qs.split("&");
    var params = {};
    for (var i = queries.length; i--; ) {
        var q = queries[i].split("=");
        params[q[0]] = q[1];
    }

    DTR.sortby = params.sortby || DTR.sortby;
    DTR.sortasc = params.sortdir === "asc";
    DTR.filterstr = decodeURIComponent(params.filter);
    DTR.filterby = params.filterby;
    DTR.sheet = params.sheet || DTR.sheet;
    DTR.page = +params.page;
    DTR.perpage = +params.perpage || DTR.perpage;

    if (!params.cols) {
        // Default if cols param is not specified
        params.cols = "0001000011000011000000";
    }

    DTR.cols = params.cols;
    DTR.log("...query string read.");

    return true;
};

// create/readCookie functions from http://www.quirksmode.org/js/cookies.html
DTR.createCookie = function(name, value, days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        var expires = "; expires="+date.toGMTString();
    }
    else {
        var expires = "";
    }
    document.cookie = name + "=" + value + expires + "; path=/";
};

DTR.readCookie = function(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == " ") {
            c = c.substring(1, c.length);
        }
        if (c.indexOf(nameEQ) == 0) {
            return c.substring(nameEQ.length, c.length);
        }
    }
    return null;
};

DTR.formatDate = function(d) {
    // Turns the "yyyymmdd" datestring (as stored in the DB) into a more
    // familiar "dd/mm/yy"
    if (d) {
        var n = d.match(/\d+/g)
        if (n && (n.join("").length >= 6)) {
            var year = d.slice(2, 4);
            var month = d.slice(4, 6);
            var day = d.slice(6, 8);
            return [day, month, year].join("/");
        } else {
            return "UNKNOWN";
        }
    } else {
        return "";
    }
};

DTR.unformatDate = function(s) {
    // Tries to turn "dd/mm/yy" or "dd/mm/yyyy" into "yyyymmdd"
    var date = s.split("/");
    if (date.length === 3) {
        if (date[0].length === 1) {
            date[0] = "0" + date[0];
        }
        if (date[1].length === 1) {
            date[1] = "0" + date[1];
        }
        if (date[2].length === 2) {
            date[2] = "20" + date[2];
        }
        return [date[2], date[1], date[0]].join("");
    } else {
        return "";
    }
};

DTR.buildTable = function() {
    var p = DTR.fields;
    var pl = p.length;
    var items = DTR.items;

    // Build table headings
    DTR.log("  Building table headings...");
    var headrow = document.getElementById("columnheaders");

    for (var i = 0; i < pl; i++) {
        var th = document.createElement("th");
        var a = document.createElement("a");
        a.innerHTML = p[i].shortlabel;

        th.id = "sortby_" + p[i].ref;

        th.className = "i"+p[i].ref;
        th.appendChild(a);

        if (p[i].ref === DTR.sortby) {
            th.className += DTR.sortasc ? " sortasc" : " sortdesc";
        }

        headrow.appendChild(th);
    }
    DTR.log("  ...done");

    // No point continuing if there are no items.
    // TODO: show a message saying something like "No items found".
    if (items.length === 0) return;

    // Build the body of the table from cached and filtered array

    // Note: originally I used jQuery for this part but it turns out that
    // using the standard DOM functions is about 5-10 times quicker.
    var cv = DTR.propIndex("value");
    var co = DTR.propIndex("fujitsuowned");
    var cw = DTR.propIndex("warranty");
    var cd = DTR.propIndex("datein");
    var cr = DTR.propIndex("rtsdate");

    var today = (function() {
        var now = new Date();
        var day = "" + now.getDate();
        var month = "" + (now.getMonth() +1 );
        var year = "" + now.getFullYear();

        if (month.length === 1) {
            month = "0" + month;
        }

        if (day.length === 1) {
            day = "0" + day;
        }
        return [year, month, day].join("");
    }());

    DTR.log("Date string for today: " + today);

    var tbroot = document.getElementById("indextable");
    var frag = document.createDocumentFragment();

    // Work out item range to display
    var lastitem = DTR.perpage;
    if (lastitem > items.length || DTR.perpage === 0) {
        lastitem = items.length;
    }

    DTR.log("  Starting main table loop...");
    for (var r = 0; r < lastitem; r++)  {
        var i = items[r];
        var rc = i.folio === 0 ? "i" : "h";
        var tr = document.createElement("tr");
        var td = document.createElement("th");
        var tn = document.createTextNode(i.rep);
        td.className = "irep";
        td.appendChild(tn);
        tr.appendChild(td);
        tr.className = rc;
        for (var c = 1; c < pl; ++c) {
            var cp = p[c].ref;
            td = document.createElement("td");
            td.className = "i" + cp;
            var txt = ""
            switch (c) {
                case co: {
                    txt = i.fujitsuowned ? "FUJ" : "CUS";
                    break;
                }
                case cv: {
                    txt = (i.value/100).toFixed(2);
                    break;
                }
                case cw: {
                    txt = DTR.formatDate(i.warranty);
                    if (i.warranty < today) {
                        td.className += " oow";
                    }
                    break;
                }
                case cd: {
                    txt = DTR.formatDate(i.datein);
                    break;
                }
                case cr: {
                    txt = DTR.formatDate(i.rtsdate);
                    break;
                }
                default: txt = i[cp];
            }
            tn = document.createTextNode(txt);
            td.appendChild(tn);
            tr.appendChild(td);
        }
        frag.appendChild(tr);
    } // for (r)
    tbroot.appendChild(frag);
    DTR.log("  ...done");
}
