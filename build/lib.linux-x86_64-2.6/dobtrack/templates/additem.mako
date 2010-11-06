<%inherit file="/base.mako" />

<%def name="head_tags()">
    <script type="text/javascript" src="/edititem.js"></script>
    <script type="text/javascript" src="/additem.js"></script>
</%def>

<h1>${c.pagetitle}</h1>

<form name="add" method="POST" action=
      "${url(controller='dobitem', action='addtodb')}">
  <div id="singlelines">
  <table>
    <tr>
      <th class="itemdetails_leftcol"><label for="rep">REP number:</label></th>
      <td><input type="text" name="rep" value="${c.newrep}" /></td>
    </tr>
    <tr>
      <th><label for="initials">Initials:</label></th>
      <td><input type="text" name="initials" value="AF" /></td>
    </tr>
    <tr>
      <th><label for="customer">Customer:</label></th>
      <td>
        <select name="customer">
          <option value="TESCO">Tesco</option>
          <option value="HSBC">HSBC</option>
          <option value="SPECSAVERS">Specsavers</option>
        </select>
        <input type="checkbox" name="fujitsuowned" id="fujitsuowned" /><label
          for="fujitsuowned">Fujitsu owned</label>
      </td>
    </tr>
    <tr>
      <th><label for="value">Value:</label></th>
      <td><input type="text" name="value" value="0.00"/></td>
    </tr>
    <tr>
      <th><label for="costcentre">Cost centre:</label></th>
      <td><input type="text" name="costcentre" /></td>
    </tr>
    <tr>
      <th><label for="order">Order number:</label></th>
      <td><input type="text" name="order" /></td>
    </tr>
  </table>

  <table>
    <tr>
      <th class="itemdetails_leftcol"><label for="make">Make:</label></th>
      <td><input type="text" name="make" /></td>
    </tr>
    <tr>
      <th><label for="model">Model:</label></th>
      <td><input type="text" name="model" /></td>
    </tr>
    <tr>
      <th><label for="part">Part number:</label></th>
      <td><input type="text" name="part" /></td>
    </tr>
    <tr>
      <th><label for="serial">Serial number:</label></th>
      <td><input type="text" name="serial" /></td>
    </tr>
    <tr>
      <th><label for="asset">Asset tag:</label></th>
      <td><input type="text" name="asset" /></td>
    </tr>
    <tr>
      <th><label for="warranty">Warranty:</label></th>
      <td><input type="text" name="warranty" /></td>
    </tr>
  </table>

  <table>
    <tr>
      <th class="itemdetails_leftcol"><label for="location">Location:</label></th>
      <td><input type="text" name="location" /></td>
    </tr>
  </table>
  </div>
  <div id="textareas">
    <p>Issue:</p>
    <div class="textarea"><textarea name="issue"></textarea></div>
    <p>Current State:</p>
    <div class="textarea"><textarea name="state">Awaiting parts/test</textarea></div>
    <input type="submit" name="submit" value="Submit" />
  </div>

</form>
<div id="formender">
<a href="${url(controller='dobitem', action='index')}">Return to index</a>
</div>