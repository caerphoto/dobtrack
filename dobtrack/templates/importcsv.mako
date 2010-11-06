<%inherit file="/base.mako" />

<%def name="head_tags()">
</%def>

<h1>${c.pagetitle}</h1>

<p>Choose a file to import:</p>

<form name="uploadform" enctype="multipart/form-data" method="POST" action=
  "${url(controller='dobitem', action='upload')}">
Filename: <input type="file" name="csvfile" /><br />
<input type="submit" value="Upload" />
</form>
<p><a href="${url(controller='dobitem', action='index')}">Return to index</a>.</p>