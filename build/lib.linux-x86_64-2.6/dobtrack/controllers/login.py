import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from dobtrack.lib.base import BaseController, render

log = logging.getLogger(__name__)

class LoginController(BaseController):

    def login(self):
        """
        Show login form.
        """
        c.pagetitle = "Please Log In"
        return render("login.mako")

    def submit(self):
        """
        Verify username and password
        """

        # Both fields filled?
        form_username = str(request.params.get('username')).lower()
        form_password = str(request.params.get('password'))

        # Get user data from database
        #db_user = model.WebUser.query(User).get_by(name=form_username)
        #if db_user is None: # User does not exist
        valid_users = {
                "admin": "luminous",
                "hsbc": "rainwater",
                "tesco": "lightning",
                "hbos": "autumn",
                "specsavers": "blossom",
                "lloyds": "orchard",
                "boots": "cluster1"
                }

        try:
            valid_users[form_username]
        except KeyError:
            c.pagetitle = "Incorrect Username"
            return render('login.mako')

        # Wrong password? (MD5 hashes used here)
        #if db_user.passwd != md5.md5(form_password).hexdigest():
        if form_password != valid_users[form_username]:
            c.pagetitle = "Incorrect Password"
            return render('login.mako')

        # Mark user as logged in
        session['user'] = form_username
        session.save()

        # Send user back to the page he originally wanted to get to
        if session.get('path_before_login'):
            return redirect(session['path_before_login'])
        else: # if previous target is unknown, send the user to a welcome page
            return redirect("/")

    def logout(self):
        """
        Logout the user and display a confirmation message
        """
        if 'user' in session:
            del session['user']
            session.save()

        c.pagetitle = "Please Log In"
        return render('login.mako')
