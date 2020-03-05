from app import app, db
from app.models import User, JournalEntry
from flask import render_template, request, redirect
import random
from datetime import datetime

@app.route('/')
def index():
    greeting = "WooooooW"
    user = User.query.get(1)
    entries = JournalEntry.query.all()
    sorted_entries = user.sort_by_date()
    steps_best_day = user.find_best_day()
    total_steps = user.count_total_steps()
    steps_summary = user.create_five_figure_summary_for_steps()
    steps_variance = user.find_steps_variance()
    steps_standard_deviation = user.find_steps_standard_deviation()
    total_yoga = user.count_total_yoga_sessions()
    total_runs = user.count_total_runs()
    total_strength = user.count_total_strength_training_sessions()
    total_tai_chi = user.count_total_tai_chi_sessions()
    return render_template('index.html', title="Home", greeting=greeting, user=user, entries=entries, steps_best_day=steps_best_day, total_steps=total_steps, steps_summary=steps_summary, steps_variance=steps_variance, steps_standard_deviation=steps_standard_deviation, sorted_entries=sorted_entries, total_yoga=total_yoga, total_strength=total_strength, total_runs=total_runs, total_tai_chi=total_tai_chi)

@app.route('/manage')
def manage_entries():
    entries = JournalEntry.query.all()
    return render_template('manage.html', title="Manage Your Entries", entries=entries)

@app.route('/manage', methods=['POST'])
def add_entry():
    # date = request.form['date']
    steps = request.form['steps']
    description = request.form['description']
    if 'yoga' in request.form:
        yoga = True
    else: 
        yoga = False
    # running = request.form['running']
    if 'running' in request.form:
        running = True
    else: 
        running = False
    newEntry = JournalEntry(steps=steps, description=description, yoga=yoga, running=running)
    db.session.add(newEntry)
    db.session.commit()
    return redirect('/manage')


@app.route('/manage/<int:entry_id>/edit', methods=['POST'])
def edit(entry_id):
    new_steps = request.form.get("new_steps")
    new_description = request.form.get("new_description")
    entry_id = request.form.get("entry_id")
    entry = JournalEntry.query.filter_by(id=entry_id).first()
    entry.steps = new_steps
    entry.description = new_description
    db.session.commit()
    return redirect('/manage')

@app.route('/manage/<int:entry_id>/delete', methods=['POST'])
def delete(entry_id):
    entry = JournalEntry.query.get(entry_id)
    db.session.delete(entry)
    db.session.commit()
    return redirect('/manage')


@app.route('/multi')
def multi_entries():
    entries = JournalEntry.query.all()
    return render_template('multi.html', title="Manage Your Multi Entries", entries=entries)

@app.route('/multi', methods=['POST'])
def add_multi_entry():
    raw_date = request.form['date']
    date = datetime.strptime(raw_date, "%Y-%m-%d")
    steps = request.form['steps']
    description = request.form['description']
    if 'yoga' in request.form:
        yoga = True
    else: 
        yoga = False
    # running = request.form['running']
    if 'running' in request.form:
        running = True
    else: 
        running = False
    newEntry = JournalEntry(date=date, steps=steps, description=description, yoga=yoga, running=running)
    db.session.add(newEntry)
    db.session.commit()
    return redirect('/multi')

# @app.route('/multi', methods=['POST'])
# def find_boolean():
    # steps = request.form['steps']
    # description = request.form['description']
    # checked = 'yoga' in request.form
    # yoga = request.form['yoga']
    # running = request.form['running']
    # newEntry = JournalEntry(steps=steps, description=description)
    # return render_template('multi.html', title="Manage Your Multi Entries", checked=checked)
    # return redirect('/multi')

@app.route('/multi/<int:entry_id>/edit', methods=['POST'])
def edit_multi(entry_id):
    new_steps = request.form.get("new_steps")
    new_description = request.form.get("new_description")
    entry_id = request.form.get("entry_id")
    if 'yoga' in request.form:
        yoga = True
    else: 
        yoga = False
    if 'running' in request.form:
        running = True
    else: 
        running = False

    if 'strength_training' in request.form:
        strength_training = True
    else: 
        strength_training = False

    if 'tai_chi' in request.form:
        tai_chi = True
    else: 
        tai_chi = False
    entry = JournalEntry.query.filter_by(id=entry_id).first()
    entry.steps = new_steps
    entry.description = new_description
    entry.yoga = yoga
    entry.running = running
    entry.strength_training = running
    entry.tai_chi = running
    db.session.commit()
    return redirect('/multi')