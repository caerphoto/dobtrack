from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1288351263.396848
_template_filename='/home/andy/dobtrack/dobtrack/templates/index.mako'
_template_uri='/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head_tags']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        session = context.get('session', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n<div id="darkener"></div>\n<div id="margins">\n\n<p id="userinfo">User: <span id="username">')
        # SOURCE LINE 10
        __M_writer(escape(session["user"]))
        __M_writer(u'</span>. <a href="/logout">Log out</a>.</p>\n\n<h1>')
        # SOURCE LINE 12
        __M_writer(escape(c.pagetitle))
        __M_writer(u'</h1>\n\n<div id="divFilterOptions">\n  <ul id="ulCols"></ul>\n\n  Search\n  <select id="selFilterBy"></select>\n  on\n  <select id="selSheet">\n    <option value="L" selected="selected">live</option>\n    <option value="H">history</option>\n    <option value="B">both</option>\n  </select>\n  sheet for\n  <input id="listfilter" type="text" value="" />\n  <input id="btnSearch" type="button" value="Search" />\n  &nbsp;&nbsp;<input id="btnClear" type="button" value="Clear" />\n</div>\n\n<div id="divTableControls">\n  <div id="divCols">Visible columns</div>\n  <select id="selItemsPerPage" name="selItemsPerPage">\n    <option value="10">10</option>\n    <option value="15">15</option>\n    <option value="25" selected="selected">25</option>\n    <option value="50">50</option>\n    <option value="75">75</option>\n    <option value="100">100</option>\n    <option value="150">150</option>\n    <option value="200">200</option>\n    <option value="0">(all)</option>\n  </select>\n  <label for="selItemsPerPage">items/page.</label>\n  <label for="selPageList">Page:</label>\n  <input id="btnPrevPage" type="button" value="&lt; prev" disabled="disabled" />\n  <select id="selPageList" name="selPageList">\n  </select>\n  <input id="btnNextPage" type="button" value="next &gt;" />\n\n  &nbsp;(')
        # SOURCE LINE 51
        __M_writer(escape(c.itemcount))
        __M_writer(u' items total, <span id="visiblecount"></span>&nbsp;of <span id="filteredcount">')
        __M_writer(escape(c.itemcount))
        __M_writer(u'</span> shown)\n</div>\n<table>\n  <thead class="colhead">\n    <tr id="columnheaders">\n    </tr>\n  </thead>\n  <tbody id="indextable">\n  </tbody>\n</table>\n<div id="loadingmessage">Loading item data...</div>\n\n<p id="otheractions">\n  <a id="lnkAddNewItem">Add new item...</a> |\n  <img src="/link_icon_grey.gif" width="12" height="11" />\n  <a href="" id="lnkHere" target="_blank"\n    title="Right-click and choose Copy Shortcut">Link to this view</a> |\n  <a href="/exportcsv" id="lnkExport">Download as spreadsheet</a> |\n  <img src="/link_icon_grey.gif" width="12" height="11" />\n  <a href="/tableprint" id="tableprint" target="_blank"\n    title="Link opens in a new window">Printable version</a>\n</p>\n\n<div id="itemeditor">\n<h2 id="itemloadingmessage"><img src="/ajax-loader_pale-blue.gif" width="16"\n    height="16" style="vertical-align: middle"> Checking item details...</h2>\n<h2 id="editorheading">Details for item # <span id="rep">1234</span> (added by \n    <span id="initials"></span>&nbsp;on <span id="datein"></span>):</h2>\n<h2 id="newitemheading">Enter details for new item:</h2>\n\n<div id="itemdetails_leftcol">\n  <div class="detailsection" id="section1">\n   <div class="propbox">\n      <label class="text" for="rep">REP number:</label>\n      <input type="text" name="rep" />\n    </div>\n\n    <div class="propbox" id="repinuse">\n      REP number is already in use\n    </div>\n    <div class="propbox" id="repok">\n      REP number OK\n    </div>\n    <div class="propbox" id="pendingrep">\n      Enter a REP number\n    </div>\n\n    <div class="propbox">\n      <label class="text" for="kind" id="lblKind">DOA/DOB:</label>\n      <select name="kind">\n        <option value="DOA">DOA</option>\n        <option value="DOB">DOB</option>\n      </select>\n    </div>\n\n    <div class="propbox" id="divCustomer">\n      <label class="text" for="customer" id="lblCustomer">Customer:</label>\n      <select name="customer">\n      </select>\n    </div>\n\n    <div class="propbox" id="divFujitsuOwned">\n      <label for="fujitsuowned" id="lblFujitsuOwned">\n        <input name="fujitsuowned" type="checkbox" id="chkFujitsuOwned" />\n        Fujitsu owned</label>\n    </div>\n\n    <div class="propbox">\n      <label class="text" for="value">Value:</label>\n      <input type="text" name="value" value="0.00" />\n    </div>\n    <div class="propbox">\n      <label class="text" for="costcentre">Cost centre:</label>\n      <input type="text" name="costcentre" value="" />\n    </div>\n\n    <div class="propbox">\n      <label class="text" for="ordernum">Order #:</label>\n      <input type="text" name="ordernum" value="" />\n    </div>\n  </div>\n\n\n  <div class="detailsection">\n    <div class="propbox">\n      <label class="text" for="make">Make:</label>\n      <input type="text" name="make" value="" />\n    </div>\n    <div class="propbox">\n      <label class="text" for="model">Model:</label>\n      <input type="text" name="model" value="" />\n    </div>\n    <div class="propbox">\n      <label class="text" for="part"><span class="rts_mandatory">*</span> Part #:</label>\n      <input type="text" name="part" value="" />\n    </div>\n    <div class="propbox">\n      <label class="text" for="serial"><span class="rts_mandatory">*</span> Serial #:</label>\n      <input type="text" name="serial" value="" />\n    </div>\n    <div class="propbox">\n      <label class="text" for="asset">Asset #:</label>\n      <input type="text" name="asset" value="" />\n    </div>\n    <div class="propbox">\n      <label class="text" for="warranty">Warranty:</label>\n      <input type="text" name="warranty" value="" />\n    </div>\n  </div>\n\n  <div class="detailsection">\n    <div class="propbox">\n      <label class="text" for="location">Location:</label>\n      <input type="text" name="location" value="" />\n    </div>\n\n    <div id="sapgrn" class="propbox">\n      <label class="text" for="sap"><span class="rts_mandatory">*</span> SAP/GRN:</label>\n      <input id="tbx_sap" class="sapgrn" type="text" name="sap" value="" /><input id="tbx_grn" class="sapgrn" type="text" name="grn" value="" />\n    </div>\n\n    <div class="propbox">\n      <label class="text" for="folio">Folio:</label>\n      <input type="text" name="folio" value="" />\n    </div>\n    <div class="propbox">\n      <label class="text" for="rtsdate">RTS Date:</label>\n      <input type="text" name="rtsdate" value="" />\n    </div>\n  </div>\n</div>\n\n\n<div id="itemdetails_rightcol">\n  <div id="textareas">\n    <div class="detailsection">\n      <label for="issue">Issue:</label>\n      <textarea class="longinput" name="issue"></textarea>\n    </div>\n\n    <div class="detailsection" id="sec_state">\n      <label for="state">Current state:</label>\n      <textarea class="longinput" name="state"></textarea>\n    </div>\n\n    <div class="detailsection">\n      <label for="solution">Solution:</label>\n      <textarea class="longinput" name="solution"></textarea>\n    </div>\n\n    <div class="detailsection">\n      <label for="comment">Comment:</label>\n      <textarea class="longinput" name="comment"></textarea>\n    </div>\n  </div>\n</div>\n\n<div id="editorcontrols">\n    <div id="editorbuttons">\n      <input type="button" id="deleteitem" value="Delete Item" disabled="true"/>\n      <input type="button" id="applyedit" value="Apply" />\n      <input type="button" id="okedit" value="OK" />\n      <input type="button" id="canceledit" value="Cancel" />\n    </div>\n\n    <div id="otheroptions">\n      <span class="rts_mandatory">*</span> required fields for <a href="" target="_blank" id="lnkPrint">printing RTS forms</a>.\n    </div>\n</div>\n\n<div id="debug1">&nbsp;</div>\n<div id="debug2">&nbsp;</div>\n\n\n</div>\n\n<!--\n<p id="logheader">JavaScript event log (<a href="#" id="hidelog">hide</a>):</p>\n-->\n<div id="log"></div>\n\n<p id="authorinfo">dobtrack by <a href="mailto:andy.farrell@uk.fujitsu.com">\nAndy Farrell</a></p>\n\n</div>\n\n<script type="text/javascript" src="/jquery.js"></script>\n<script type="text/javascript" src="/common.js"></script>\n<script type="text/javascript" src="/index.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    <link rel="stylesheet" type="text/css" href="/base.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


