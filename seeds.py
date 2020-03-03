from app import db, models
from app.models import User, JournalEntry, datetime

JournalEntry.query.delete()
User.query.delete()

user1 = User(first_name="Qazi", last_name="Raytnau")
db.session.add(user1)
db.session.commit()
users = User.query.all()

print(user1)

journal_entry1 = JournalEntry(steps=17514, description="I felt really tired today.", user=user1)
journal_entry2 = JournalEntry(date=datetime.datetime(2020, 3, 1), steps=19000, description="I felt really fine today.", user=user1)
journal_entry3 = JournalEntry(date=datetime.datetime(2020, 2, 29), steps=18523, description="Oh dear.", user=user1)
journal_entry4 = JournalEntry(date=datetime.datetime(2020, 2, 28), steps=25311, description="I felt really amazing today.", user=user1)


db.session.add(journal_entry1)
db.session.add(journal_entry2)
db.session.add(journal_entry3)
db.session.add(journal_entry4)

db.session.commit()
entries = JournalEntry.query.all()
print(entries)
entry_user = JournalEntry.query.get(1).user
print(entry_user.first_name)
top = user1.find_best_day()
print(top) #expect 25311

user_iqr = user1.find_iqr()
print(user_iqr)