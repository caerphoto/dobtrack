<%inherit file="/base.mako" />

<%def name="head_tags()">
    <link rel="stylesheet" type="text/css" href="/rtsform.css" />
    <style>
      @page {
        @top-right {
            content: "${c.item.folio}";
        }
      }
    </style>
</%def>

<p id="rtsform_controls">
<input type="button" value="Print" onclick="window.print()" /> &nbsp;
<input type="button" value="Close" onclick="window.close()" />
</p>

<div id="foliocontainer">Folio: <span id="folio">&nbsp;</span></div>

<h1>Fujitsu Services - WAR08</h1>
<h2>DOB/DOA Return To Good Stock Form</h2>

<div id="rep" class="detailsection">
    <div class="propertylabel">DOB/DOA stock control barcode:</div>
    <div class="itemproperty">${c.printrep}</div>
</div>

<div class="detailsection">
    <div class="propertylabel">Part #:</div>
    <div class="itemproperty">${c.item.part}</div>
</div>

<div id="itemdesc" class="detailsection">
    <div class="propertylabel">Item description:</div>
    <div class="itemproperty">${c.item.make} ${c.item.model}</div>
</div>

<div class="detailsection">
    <div class="propertylabel">Serial #:</div>
    <div class="itemproperty">${c.item.serial}</div>
</div>

<div class="detailsection">
    <div class="propertylabel">RTS date:</div>
    <div class="itemproperty">${c.item.rtsdate}</div>
</div>

<div class="detailsection">
    <div class="propertylabel">SAP # (604&hellip;):</div>
    <div class="itemproperty">${c.item.sap}</div>
</div>

<div class="detailsection">
    <div class="propertylabel">GRN # (840&hellip;):</div>
    <div class="itemproperty">${c.item.grn}</div>
</div>

<h3 id="sigsection">Accepted to WAR08 warehouse by:</h3>
<div>Name:
<div id="namebox">&nbsp;</div></div>

<div>Signature:
<div id="signaturebox">&nbsp;</div></div>
