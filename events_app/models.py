"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref


class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=True, unique=True)
    events_attending = db.relationship('Event', secondary='table_guest_event', back_populates='guests')


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    date_and_time = db.Column(db.DateTime, nullable=False)
    guests = db.relationship('Guest', secondary='table_guest_event', back_populates = 'events_attending')

    #NOTE:  completed ToDo in Event Model, but must comment out title, description, date_and_time to run. I have yet to completely find error



guest_event_table = db.Table(
    'table_guest_event',
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id')),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)