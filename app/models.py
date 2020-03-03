from app import db
import datetime
from operator import itemgetter

# import statistics modules
from scipy import stats
import numpy as np 

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


    # method to find iqr  
    def find_iqr(self):
        steps_list = [entry.steps for entry in self.journal_entries]
        iqr = stats.iqr(steps_list, interpolation = 'midpoint') 
        return "The IQR is {}.".format(iqr)

    # method(s) to find the five-number summary. Extension: return the values in a list, so I can separate them in rendering (e.g. to put into a table)
    def create_five_figure_summary_for_steps(self):
        steps_list = [entry.steps for entry in self.journal_entries]
        percentiles = np.percentile(steps_list, [25, 50, 75]) # creates LQ, median and UQ. These could be done as separate variables - I just wanted to try it this way
        min, max = np.min(steps_list), np.max(steps_list)
        iqr = stats.iqr(steps_list, interpolation = 'midpoint') 
        standardised_iqr = round(iqr / percentiles[1], 2)
        return "Min value: {min}\nLQ: {lq}\nMedian: {median}\nUQ: {uq}\nMax value: {max}\nInterQuartile Range: {iqr}\nStandardised InterQuartile Range: {standardised_iqr}".format(min=min, lq=percentiles[0], median=percentiles[1], uq=percentiles[2], max=max, iqr=iqr, standardised_iqr=standardised_iqr)

    # count total steps for the year/any given time period. Start by counting all steps for all entries
    def count_total_steps(self):
        steps_list = [entry.steps for entry in self.journal_entries]
        total_steps = np.sum(steps_list)
        return "Total steps: {}".format(total_steps)

    # find variance in steps
    def find_steps_variance(self):
        steps_list = [entry.steps for entry in self.journal_entries]
        variance = np.var(steps_list)
        return "Variance of steps: {}".format(variance)

    # variance is giving what seems a crazy answer (9,384,542.5), so I want to try to work it out step by step. 
    # Find the mean 
    def find_mean_steps(self):
        steps_list = [entry.steps for entry in self.journal_entries]
        mean = np.mean(steps_list)
        return "Mean: {}".format(mean)

    # mean is working. So, for each number: subtract the Mean and square the result (the squared difference). Then work out the average of those squared differences. Well, it works out the same. I guess I just hadn't thought enough about what variance is.
    def manual_steps_variance(self):
        steps_list = [entry.steps for entry in self.journal_entries]
        mean = np.mean(steps_list)
        deviations = []
        for entry in steps_list:
            deviation = entry - mean
            deviations.append(deviation)
        deviations_sum = 0
        for deviation in deviations:
            squared_deviation = deviation * deviation 
            deviations_sum += squared_deviation
        variance = deviations_sum / len(steps_list)
        return "Manually worked out variance is: {}".format(variance)

    # find standard deviation in steps. (using numpy: scipy gives a more accurate answer, but I want to use variation as well, and I don't understand scipy's variation. So, for consistency, I'll stick to numpy). Use two decimal places.
    def find_steps_standard_deviation(self):
        steps_list = [entry.steps for entry in self.journal_entries]
        sd = round(np.std(steps_list), 2)
        return "Standard deviation of steps: {}".format(sd)

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