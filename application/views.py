from flask import render_template, flash, url_for, redirect

from models import SignupModel
from decorators import admin_required
from forms import SignupForm


def index():
    """List all examples"""
    form = SignupForm()
    if form.validate_on_submit():
        SignupModel(email=form.email.data).put()
        flash(u'Thank you for your interest!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)


@admin_required
def view_signups():
    signups = SignupModel.all().order("timestamp")
    return render_template('view_signups.html', signups=signups)


def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''
