<%inherit file="/base.mako" />

<%def name="head_tags()">
    <link rel="stylesheet" type="text/css" href="/base.css">
</%def>

<h1>${c.pagetitle}</h1>

<form name="login" action="submitlogin">
    <label for="username">
        User:
        <input type="text" name="username" />
    </label>

    <label for="password">
        Password:
        <input type="password" name="password" />
    </label>

    <input type="submit" value="OK" />
</form>