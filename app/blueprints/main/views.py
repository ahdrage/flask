from flask import render_template, redirect, url_for, flash
from . import main
from app import db
from app.models import Listing
from .forms import UpdateForm
from app.libs import topp

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/update', methods=['GET', 'POST'])
def update():
	form = UpdateForm()
	if form.validate_on_submit():
		if form.confirm.data is False:
			flash('Check the confirm box!')
			return redirect(url_for('main.update'))
		topp.update_database()
		return redirect(url_for('main.home'))
	return render_template('update.html')

@main.route('/results')
def results():
	listings = Listing.query.all()
	return render_template('results.html', listings=listings)
