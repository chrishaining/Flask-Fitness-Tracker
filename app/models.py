from app import db
import datetime
from operator import itemgetter

# create a user class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64))
    journal_entries = db.relationship('JournalEntry', backref='user', lazy='dynamic')

    # ideas for additional attributes: running/cardio (time); measurement of fitness (e.g. distance in a given time period); gym days (could break it down into body parts); yoga; tai chi; meditation; weight

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

    # method(s) to find the five-number summary 

    # count total steps for the year/any given time period

    # count total number of times the user has done a given activity (e.g. number of gym visits)

    # method to find the most common words and/or phrases in the user's descriptions.

    # method(s) to filter entries. Ideas: by month/year/day of the week

class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.datetime.now())
    steps = db.Column(db.Integer)
    description = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        entry_date = self.date.strftime("%A %d %B %Y")
        return '<Journal Entry {}>'.format(entry_date)