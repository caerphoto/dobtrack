;
if (typeof DOB_ADD === "undefined") var DOB_ADD = {};

DOB_ADD.init = function() {
    $("[name='rep']").focus();
};

$(document).ready(DOB_ADD.init);