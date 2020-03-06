from app import app, db
from app.models import User, JournalEntry, FilterForm
from flask import render_template, request, redirect, jsonify
import random
from datetime import datetime
import json
import numpy as np

@app.route('/')
def index():
    greeting = "Welcome"
    user = User.query.get(1)
    entries = JournalEntry.query.all()
    # sorted_entries = user.sort_by_date()
    steps_best_day = user.find_best_day()
    total_steps = user.count_total_steps()
    steps_summary = user.create_five_figure_summary_for_steps()
    steps_variance = user.find_steps_variance()
    steps_standard_deviation = user.find_steps_standard_deviation()
    total_yoga = user.count_total_yoga_sessions()
    total_runs = user.count_total_runs()
    total_strength = user.count_total_strength_training_sessions()
    total_tai_chi = user.count_total_tai_chi_sessions()
    return render_template('index.html', title="Home", greeting=greeting, user=user, entries=entries, steps_best_day=steps_best_day, total_steps=total_steps, steps_summary=steps_summary, steps_variance=steps_variance, steps_standard_deviation=steps_standard_deviation, total_yoga=total_yoga, total_strength=total_strength, total_runs=total_runs, total_tai_chi=total_tai_chi)

@app.route('/manage')
def manage_entries():
    entries = JournalEntry.query.all()
    return render_template('manage.html', title="Manage Your Entries", entries=entries)

@app.route('/manage', methods=['POST'])
def add_entry():
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
    if 'strength_training' in request.form:
        strength_training = True
    else: 
        strength_training = False
    if 'tai_chi' in request.form:
        tai_chi = True
    else: 
        tai_chi = False
    newEntry = JournalEntry(date=date, steps=steps, description=description, yoga=yoga, running=running, strength_training=strength_training, tai_chi=tai_chi)
    db.session.add(newEntry)
    db.session.commit()
    return redirect('/manage')



@app.route('/manage/<int:entry_id>/edit', methods=['POST'])
def edit(entry_id):
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
    entry.strength_training = strength_training
    entry.tai_chi = tai_chi
    db.session.commit()
    return redirect('/manage')


@app.route('/manage/<int:entry_id>/delete', methods=['POST'])
def delete(entry_id):
    entry = JournalEntry.query.get(entry_id)
    db.session.delete(entry)
    db.session.commit()
    return redirect('/manage')


@app.route('/backup')
def backup():
    entries = JournalEntry.query.all()
    return render_template('backup.html', title="Backup Management Page", entries=entries)

@app.route('/backup', methods=['POST'])
def backup_add():
    raw_date = request.form['date']
    date = datetime.strptime(raw_date, "%Y-%m-%d")
    steps = request.form['steps']
    description = request.form['description']
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
    newEntry = JournalEntry(date=date, steps=steps, description=description, yoga=yoga, running=running, strength_training=strength_training, tai_chi=tai_chi)
    db.session.add(newEntry)
    db.session.commit()
    return redirect('/backup')

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

@app.route('/backup/<int:entry_id>/edit', methods=['POST'])
def backup_edit(entry_id):
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
    entry.strength_training = strength_training
    entry.tai_chi = tai_chi
    db.session.commit()
    return redirect('/backup')

@app.route('/backup/<int:entry_id>/delete', methods=['POST'])
def backup_delete(entry_id):
    entry = JournalEntry.query.get(entry_id)
    db.session.delete(entry)
    db.session.commit()
    return redirect('/backup')


# filter page
@app.route('/filter', methods=['GET', 'POST'])
def filter_by_steps():

    def unique(arr):
        new_list = []
        for element in arr:
            if element not in new_list:
                new_list.append(element)
        return new_list

    form = FilterForm()
    form.steps.choices = [(entry.id, entry.steps) for entry in JournalEntry.query.filter_by(yoga=True).all()]
    # choices = [(entry.id, entry.steps) for entry in JournalEntry.query.filter_by(yoga=True).all()]
    # choices_two = np.unique(choices)
    # form.steps.choices = choices_two
    # form.steps.choices = [entry for entry in JournalEntry.query.filter_by(yoga=True).all()]

    if request.method == 'POST':
        found_list = JournalEntry.query.filter_by(id=form.steps.data).all()
        dictionary = {}
        # counter = 0
        for item in found_list: 
            # return '<h2>{}{}</h2>'.format(item.id, item.show_pretty_date())

            # counter += 1
            dictionary[str(item.id)] = item.steps
            # counter += 1
            # dictionary.update( { str(counter): item} )
            # dictionary[str(counter)] = item
        # for item in found_list:
        #     # jsonify(item.serialize())
        # dictionary['key'] = found_list
        return '{}'.format(dictionary)
        # return "Bunny"
    # return chosen_list
        # strings = {}
        # counter = 0
        # things = []
        # for item in chosen_list: 
        #     bob = jsonify(item.serialize())
        #     counter += 1
        #     strings.update( { str(counter) : bob} )
            # strings[str(counter)] = item
        # res = json.dumps(strings)
        # return res
        # list_res = json.dumps(chosen_list)
        # bob = jsonify(strings.serialize())
        # return strings
        # return things
        # res = jsonify(strings)
        # res.status_code = 200
        # return res
        # return '<ul>{% for thing in strings %}<li>{{thing}}</li></ul>'
        # return strings
            # return '<h2>ID {}: date was {}</h2>'.format(form.steps.data, item.show_pretty_date())

            # return '<h2>ID {}: date was {}</h2>'.format(form.steps.data, item.show_pretty_date())
        # return '<h2>{}: number of steps was {}</h2>'.format(form.steps.data, chosen_entry.show_pretty_date())

    return render_template('filter.html', title="Filter", form=form, unique=unique)



