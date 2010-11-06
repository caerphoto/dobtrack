<%inherit file="/base.mako" />

<%def name="head_tags()">
</%def>

<h1>${c.pagetitle}</h1>
<p>
  ${c.rowsadded} items were added to the database.
</p>
<p>
  The following REP numbers appeared more than once:<br />
% for rep in c.duplicatereps:
    ${int(rep)}<br />
% endfor
</p>
<p>
  The following REP numbers had unrecognisable customer information:<br />
% for cust in c.unknowncustomers:
    REP: ${cust['rep']}, Customer: ${cust['customer']}<br />
% endfor
</p>

<p><a href="${url(controller='dobitem', action='index')}">Return to index</a>.</p>
