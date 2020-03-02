from app import db
import datetime
from operator import itemgetter

# create a user class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64))
    journal_entries = db.relationship('JournalEntry', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User {} {}>'.format(self.first_name, self.last_name)

    # method to identify the best day for steps 
    def find_best_day(self):
        steps_list = [(entry.date, entry.steps) for entry in self.journal_entries]
        just_the_steps = [value for (key, value) in steps_list]
        result_date = max(steps_list, key=itemgetter(1))[0]
        result_steps = max(just_the_steps)
        pretty_result = result_date.strftime("%A %d %B %Y")
        return "Your best day was {} with {} steps.".format(pretty_result, result_steps)

class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.datetime.now())
    steps = db.Column(db.Integer)
    description = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        entry_date = self.date.strftime("%A %d %B %Y")
        return '<Journal Entry {}>'.format(entry_date)