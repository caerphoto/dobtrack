<%inherit file="/base.mako" />

<%def name="head_tags()">

</%def>

<h1>${c.pagetitle}</h1>

<p>Item added by: ${c.item.initials}</p>

<table class="itemdetail">
  <tr>
    <th>Customer</th>
    <th>Value</th>
    <th>Cost Centre</th>
    <th>Order Number</th>
  </tr>
  <tr>
    <td>${c.item.customer}</td>
    <td>${c.item.value}</td>
    <td>${c.item.costcentre}</td>
    <td>${c.item.order}</td>
  </tr>
</table>

<table class="itemdetail">
  <tr>
    <th>Make</th>
    <th>Model</th>
    <th>Part Number</th>
    <th>Serial Number</th>
    <th>Asset Tag</th>
    <th>Warranty</th>
  </tr>
  <tr>
    <td>${c.item.make}</td>
    <td>${c.item.model}</td>
    <td>${c.item.part}</td>
    <td>${c.item.serial}</td>
    <td>${c.item.asset}</td>
    <td>${c.item.warranty}</td>
  </tr>
</table>

<table class="itemdetail">
  <tr>
    <th>Location</th>
    <th>Issue</th>
    <th>Current State</th>
    <th>Solution</th>
  </tr>
  <tr id="itemstatus">
    <td>${c.item.location}</td>
    <td>${c.item.issue}</td>
    <td>${c.item.state}</td>
    <td>${c.item.solution}</td>
  </tr>
</table>

<table class="itemdetail">
  <tr>
    <th>GRN</th>
    <th>SAP/GDN</th>
    <th>Folio Number</th>
    <th>RTS Date</th>
  </tr>
  <tr>
    <td>${c.item.grn}</td>
    <td>${c.item.sap}</td>
    <td>${c.item.folio}</td>
    <td>${c.item.rtsdate}</td>
  </tr>
</table>

<p>
<a href="${url(controller='dobitem', action='edititem', id=c.item.rep)}">Edit item details...</a>
</p>

<form name="delete" method="post" action=
      "${url(controller='dobitem', action='deletefromdb', id=c.item.rep)}">
  <input type="submit" name="delitem" value="Delete Item" />
</form>
<p>
<br />
or <a href="${url(controller='dobitem', action='index')}">return to index</a>.
</p>