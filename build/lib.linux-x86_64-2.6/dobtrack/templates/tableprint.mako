<%inherit file="/base.mako" />

<%def name="head_tags()">
    <link rel="stylesheet" type="text/css" href="/tableprint.css">
</%def>

<input type="button" value="Close" onclick="window.close()" />

<h1>${c.pagetitle}</h1>

<table>
  <thead class="colhead">
    <tr id="columnheaders">
    </tr>
    <tr id="loadingmessage" class="i loadingmessage">
      <td colspan="8" style="padding: 1em">
        <img src="/ajax-loader_grey.gif" width="16" height="16"
             style="vertical-align: -30%" /> Loading item data...
      </td>
    </tr>
  </thead>
  <tbody id="indextable">
  </tbody>
</table>

<script type="text/javascript" src="/jquery.js"></script>
<script type="text/javascript" src="/common.js"></script>
<script type="text/javascript" src="/tableprint.js"></script>
