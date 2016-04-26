from flask import render_template, redirect, url_for
from . import main
from app import db

@main.route('/')
def home():
    return render_template('index.html')
