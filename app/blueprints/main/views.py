from flask import render_template, redirect, url_for
from . import main
from app import db
from app.models import Listing
from .forms import UpdateForm

@main.route('/')
def home():
    return render_template('index.html')
