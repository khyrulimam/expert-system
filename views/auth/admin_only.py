import functools

from flask import redirect, url_for, g


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('base.login'))
        return view(**kwargs)

    return wrapped_view
