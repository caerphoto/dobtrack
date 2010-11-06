<%inherit file="/base.mako" />

<%def name="head_tags()">
    <link rel="stylesheet" type="text/css" href="/base.css">
</%def>

<div id="darkener"></div>
<div id="margins">

<p id="userinfo">User: <span id="username">${session["user"]}</span>. <a href="/logout">Log out</a>.</p>

<h1>${c.pagetitle}</h1>

<div id="divFilterOptions">
  <ul id="ulCols"></ul>

  Search
  <select id="selFilterBy"></select>
  on
  <select id="selSheet">
    <option value="L" selected="selected">live</option>
    <option value="H">history</option>
    <option value="B">both</option>
  </select>
  sheet for
  <input id="listfilter" type="text" value="" />
  <input id="btnSearch" type="button" value="Search" />
  &nbsp;&nbsp;<input id="btnClear" type="button" value="Clear" />
</div>

<div id="divTableControls">
  <div id="divCols">Visible columns</div>
  <select id="selItemsPerPage" name="selItemsPerPage">
    <option value="10">10</option>
    <option value="15">15</option>
    <option value="25" selected="selected">25</option>
    <option value="50">50</option>
    <option value="75">75</option>
    <option value="100">100</option>
    <option value="150">150</option>
    <option value="200">200</option>
    <option value="0">(all)</option>
  </select>
  <label for="selItemsPerPage">items/page.</label>
  <label for="selPageList">Page:</label>
  <input id="btnPrevPage" type="button" value="&lt; prev" disabled="disabled" />
  <select id="selPageList" name="selPageList">
  </select>
  <input id="btnNextPage" type="button" value="next &gt;" />

  &nbsp;(${c.itemcount} items total, <span id="visiblecount"></span>&nbsp;of <span id="filteredcount">${c.itemcount}</span> shown)
</div>
<table>
  <thead class="colhead">
    <tr id="columnheaders">
    </tr>
  </thead>
  <tbody id="indextable">
  </tbody>
</table>
<div id="loadingmessage">Loading item data...</div>

<p id="otheractions">
  <a id="lnkAddNewItem">Add new item...</a> |
  <img src="/link_icon_grey.gif" width="12" height="11" />
  <a href="" id="lnkHere" target="_blank"
    title="Right-click and choose Copy Shortcut">Link to this view</a> |
  <a href="/exportcsv" id="lnkExport">Download as spreadsheet</a> |
  <img src="/link_icon_grey.gif" width="12" height="11" />
  <a href="/tableprint" id="tableprint" target="_blank"
    title="Link opens in a new window">Printable version</a>
</p>

<div id="itemeditor">
<h2 id="itemloadingmessage"><img src="/ajax-loader_pale-blue.gif" width="16"
    height="16" style="vertical-align: middle"> Checking item details...</h2>
<h2 id="editorheading">Details for item # <span id="rep">1234</span> (added by 
    <span id="initials"></span>&nbsp;on <span id="datein"></span>):</h2>
<h2 id="newitemheading">Enter details for new item:</h2>

<div id="itemdetails_leftcol">
  <div class="detailsection" id="section1">
   <div class="propbox">
      <label class="text" for="rep">REP number:</label>
      <input type="text" name="rep" />
    </div>

    <div class="propbox" id="repinuse">
      REP number is already in use
    </div>
    <div class="propbox" id="repok">
      REP number OK
    </div>
    <div class="propbox" id="pendingrep">
      Enter a REP number
    </div>

    <div class="propbox">
      <label class="text" for="kind" id="lblKind">DOA/DOB:</label>
      <select name="kind">
        <option value="DOA">DOA</option>
        <option value="DOB">DOB</option>
      </select>
    </div>

    <div class="propbox" id="divCustomer">
      <label class="text" for="customer" id="lblCustomer">Customer:</label>
      <select name="customer">
      </select>
    </div>

    <div class="propbox" id="divFujitsuOwned">
      <label for="fujitsuowned" id="lblFujitsuOwned">
        <input name="fujitsuowned" type="checkbox" id="chkFujitsuOwned" />
        Fujitsu owned</label>
    </div>

    <div class="propbox">
      <label class="text" for="value">Value:</label>
      <input type="text" name="value" value="0.00" />
    </div>
    <div class="propbox">
      <label class="text" for="costcentre">Cost centre:</label>
      <input type="text" name="costcentre" value="" />
    </div>

    <div class="propbox">
      <label class="text" for="ordernum">Order #:</label>
      <input type="text" name="ordernum" value="" />
    </div>
  </div>


  <div class="detailsection">
    <div class="propbox">
      <label class="text" for="make">Make:</label>
      <input type="text" name="make" value="" />
    </div>
    <div class="propbox">
      <label class="text" for="model">Model:</label>
      <input type="text" name="model" value="" />
    </div>
    <div class="propbox">
      <label class="text" for="part"><span class="rts_mandatory">*</span> Part #:</label>
      <input type="text" name="part" value="" />
    </div>
    <div class="propbox">
      <label class="text" for="serial"><span class="rts_mandatory">*</span> Serial #:</label>
      <input type="text" name="serial" value="" />
    </div>
    <div class="propbox">
      <label class="text" for="asset">Asset #:</label>
      <input type="text" name="asset" value="" />
    </div>
    <div class="propbox">
      <label class="text" for="warranty">Warranty:</label>
      <input type="text" name="warranty" value="" />
    </div>
  </div>

  <div class="detailsection">
    <div class="propbox">
      <label class="text" for="location">Location:</label>
      <input type="text" name="location" value="" />
    </div>

    <div id="sapgrn" class="propbox">
      <label class="text" for="sap"><span class="rts_mandatory">*</span> SAP/GRN:</label>
      <input id="tbx_sap" class="sapgrn" type="text" name="sap" value="" /><input id="tbx_grn" class="sapgrn" type="text" name="grn" value="" />
    </div>

    <div class="propbox">
      <label class="text" for="folio">Folio:</label>
      <input type="text" name="folio" value="" />
    </div>
    <div class="propbox">
      <label class="text" for="rtsdate">RTS Date:</label>
      <input type="text" name="rtsdate" value="" />
    </div>
  </div>
</div>


<div id="itemdetails_rightcol">
  <div id="textareas">
    <div class="detailsection">
      <label for="issue">Issue:</label>
      <textarea class="longinput" name="issue"></textarea>
    </div>

    <div class="detailsection" id="sec_state">
      <label for="state">Current state:</label>
      <textarea class="longinput" name="state"></textarea>
    </div>

    <div class="detailsection">
      <label for="solution">Solution:</label>
      <textarea class="longinput" name="solution"></textarea>
    </div>

    <div class="detailsection">
      <label for="comment">Comment:</label>
      <textarea class="longinput" name="comment"></textarea>
    </div>
  </div>
</div>

<div id="editorcontrols">
    <div id="editorbuttons">
      <input type="button" id="deleteitem" value="Delete Item" disabled="true"/>
      <input type="button" id="applyedit" value="Apply" />
      <input type="button" id="okedit" value="OK" />
      <input type="button" id="canceledit" value="Cancel" />
    </div>

    <div id="otheroptions">
      <span class="rts_mandatory">*</span> required fields for <a href="" target="_blank" id="lnkPrint">printing RTS forms</a>.
    </div>
</div>

<div id="debug1">&nbsp;</div>
<div id="debug2">&nbsp;</div>


</div>

<!--
<p id="logheader">JavaScript event log (<a href="#" id="hidelog">hide</a>):</p>
-->
<div id="log"></div>

<p id="authorinfo">dobtrack by <a href="mailto:andy.farrell@uk.fujitsu.com">
Andy Farrell</a></p>

</div>

<script type="text/javascript" src="/jquery.js"></script>
<script type="text/javascript" src="/common.js"></script>
<script type="text/javascript" src="/index.js"></script>
