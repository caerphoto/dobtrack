DTR.cache = {

    resetage: function() {
        this.age = 0;
        clearInterval(this.agetimer);
        this.agetimer = setInterval(function() {
           this.age++;
        }, 60000);
    },

    sort: function() {
        var asc = this.sortasc ? "ascending" : "decending";
        DTR.log("Sorting by '" + this.sortby + "' (" + asc + ")...");
        // Sort by "rep" if the parameter doesn't refer to a valid
        // field name
        var sb = DTR.propIndex(this.sortby) === -1 ? "rep" : this.sortby;
        var rh = this.sortasc ? -1 : 1;
        this.filtered.sort(function(a, b) {
            var x = a[sb];
            var y = b[sb];
            return ((x < y) ? rh : ((x > y) ? -rh : 0));
        });
        DTR.log("...sort complete");
    },

    filter: function(col, s, exclude) {
        DTR.log("Filtering: col = '"+col+"', s = '"+s+"'");
        // Returns a sub-list of items[] based on filter settings
        var result = [];
        var sheet = $("#selSheet").val();

        switch (col) {
            case "value": {
                s = s.match(/\d+/g).join("");
                break;
            }
            case "fujitsuowned": {
                s = s[0] === "F" ? "tr" : "fa";
                break;
            }
            default: {

            }
        }

        if (col) {
            for (var r = 0, m = this.items.length; r < m; r++) {
                // Only bother with the row if it's on the currently
                // selected sheet
                var i = this.items[r];
                var rs = i.folio === 0 ? "L" : "H";
                if (rs === sheet || sheet === "B") {
                    var idx = (i[col]+"").indexOf(s);
                    if (exclude ? idx === -1 : idx !== -1) {
                        result.push(i);
                    }
                }
            }
        } else {
            for (var r = 0, m = this.items.length; r < m; r++) {
                var i = this.items[r];
                var rs = i.folio === 0 ? "L" : "H";
                if (rs === sheet || sheet === "B") {
                    // search in all columns
                    for (var c = DTR.properties.length - 1; c--; ) {
                        var f = DTR.properties[c];
                        var idx = (i[f]+"").indexOf(s);
                        if (exclude ? idx === -1 : idx !== -1) {
                            result.push(i);
                            break;
                        }
                    }
                }
            }
        }

        DTR.log("filter complete: " + result.length + " items in list");
        $("#filteredcount").text(result.length);
        this.filtered = result;
        DTR.buildPageList();
        return result.length;
    }
}; // DTR.cache = {...}

