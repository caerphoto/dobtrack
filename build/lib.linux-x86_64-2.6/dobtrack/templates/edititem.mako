<%inherit file="/base.mako" />

<%def name="head_tags()">
    <script type="text/javascript" src="/edititem.js"></script>
</%def>

<h1>${c.pagetitle}</h1>

<p>Item added by <strong>${c.item.initials}</strong></p>
<form id="delitem" name="delete" method="post" action=
      "${url(controller='dobitem', action='deletefromdb', id=c.item.rep)}">
    <input type="submit" name="delitem" value="Delete Item" /> (WARNING: cannot be undone)
</form>

<form name="add" method="POST" action=
      "${url(controller='dobitem', action='applyitemedit', id=c.item.rep)}">
  <div id="singlelines">
  <table>
    <tr>
      <th class="itemdetails_leftcol"><label for="customer">Customer:</label></th>
      <td>
        <select name="customer">
          <option value="TESCO">Tesco</option>
          <option value="HSBC">HSBC</option>
          <option value="SPECSAVERS">Specsavers</option>
        </select>
% if c.item.fujitsuowned:
        <input type="checkbox" name="fujitsuowned" id="fujitsuowned" checked="checked" />
% else:
        <input type="checkbox" name="fujitsuowned" id="fujitsuowned" />
% endif
        <label for="fujitsuowned">Fujitsu owned</label>
      </td>
    </tr>
    <tr>
      <th><label for="value">Value:</label></th>
      <td><input type="text" name="value" value='${"{0:.2f}".format(c.item.value / 100.0)}' /></td>
    </tr>
    <tr>
      <th><label for="costcentre">Cost centre:</label></th>
      <td><input type="text" name="costcentre" value="${c.item.costcentre}" /></td>
    </tr>
    <tr>
      <th><label for="order">Order number:</label></th>
      <td><input type="text" name="order" value="${c.item.order}" /></td>
    </tr>
  </table>

  <table>
    <tr>
      <th class="itemdetails_leftcol"><label for="make">Make:</label></th>
      <td><input type="text" name="make" value="${c.item.make}" /></td>
    </tr>
    <tr>
      <th><label for="model">Model:</label></th>
      <td><input type="text" name="model" value="${c.item.model}" /></td>
    </tr>
    <tr>
      <th><label for="part">Part number:</label></th>
      <td><input type="text" name="part" value="${c.item.part}" /></td>
    </tr>
    <tr>
      <th><label for="serial">Serial number:</label></th>
      <td><input type="text" name="serial" value="${c.item.serial}" /></td>
    </tr>
    <tr>
      <th><label for="asset">Asset tag:</label></th>
      <td><input type="text" name="asset" value="${c.item.asset}" /></td>
    </tr>
    <tr>
      <th><label for="warranty">Warranty:</label></th>
      <td><input type="text" name="warranty" value="${c.item.warranty}" /></td>
    </tr>
  </table>

  <table>
    <tr>
      <th class="itemdetails_leftcol"><label for="location">Location:</label></th>
      <td><input type="text" name="location" value="${c.item.location}" /></td>
    </tr>
  </table>
  <table>
    <tr>
      <th class="itemdetails_leftcol"><label for="grn">GRN - SAP:</label></th>
      <td>
            <input type="text" name="grn" id="grn" value="${c.item.grn}" maxlength="8"/>
            <input type="text" name="sap" id="sap" value="${c.item.sap}" maxlength="8"/>
      </td>
    </tr>
  </table>

  <table>
    <tr>
      <th class="itemdetails_leftcol"><label for="folio">Folio:</label></th>
      <td><input type="text" name="folio" value="${c.item.folio}" /></td>
    </tr>
    <tr>
      <th><label for="rtsdate">RTS Date:</label></th>
      <td><input type="text" name="rtsdate" value="${c.item.rtsdate}" /></td>
    </tr>
  </table>


  </div>
  <div id="textareas">
    <p>Issue:</p>
    <div class="textarea"><textarea name="issue">${c.item.issue}</textarea></div>

    <p>Current State:</p>
    <div class="textarea"><textarea name="state">${c.item.state}</textarea></div>

    <p>Solution:</p>
    <div class="textarea"><textarea name="solution">${c.item.solution}</textarea></div>

    <input type="submit" name="submit" value="Apply Changes" />
  </div>
</form>
<div id="formender">
<div id="debug1">&nbsp;</div>
<div id="debug2">&nbsp;</div>
<a href="${url(controller='dobitem', action='index')}">Return to index</a>
</div>