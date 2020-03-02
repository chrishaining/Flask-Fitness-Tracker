from app import app, db
from app.models import User, JournalEntry
from flask import render_template, request, redirect
import random

@app.route('/')
def index():
    greeting = "WooooooW"
    user = User.query.get(1)
    entries = JournalEntry.query.all()
    best_day = user.find_best_day()
    return render_template('index.html', title="Home", greeting=greeting, user=user, entries=entries, best_day=best_day)

@app.route('/manage')
def manage_entries():
    return render_template('manage.html', title="Manage Your Entries")