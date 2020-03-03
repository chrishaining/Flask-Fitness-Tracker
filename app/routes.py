from app import app, db
from app.models import User, JournalEntry
from flask import render_template, request, redirect
import random

@app.route('/')
def index():
    greeting = "WooooooW"
    user = User.query.get(1)
    entries = JournalEntry.query.all()
    steps_best_day = user.find_best_day()
    total_steps = user.count_total_steps()
    steps_summary = user.create_five_figure_summary_for_steps()
    steps_variance = user.find_steps_variance()
    steps_standard_deviation = user.find_steps_standard_deviation()
    return render_template('index.html', title="Home", greeting=greeting, user=user, entries=entries, steps_best_day=steps_best_day, total_steps=total_steps, steps_summary=steps_summary, steps_variance=steps_variance, steps_standard_deviation=steps_standard_deviation)

@app.route('/manage')
def manage_entries():
    return render_template('manage.html', title="Manage Your Entries")

@app.route('/manage', methods=['POST'])
def add_entry():
    # date = request.form['date']
    steps = request.form['steps']
    description = request.form['description']
    newEntry = JournalEntry(steps=steps, description=description)
    db.session.add(newEntry)
    db.session.commit()
    return redirect('/manage')