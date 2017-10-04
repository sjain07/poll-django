"""
Definition of models.
"""

from django.db import models
from django.db.models import Sum

class Poll(models.Model):
    """A poll object for use in the application views and repository."""
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def total_votes(self):
        """Calculates the total number of votes for this poll."""
        return self.choice_set.aggregate(Sum('votes'))['votes__sum']

    def __unicode__(self):
        """Returns a string representation of a poll."""
        return self.text

class Choice(models.Model):
    """A poll choice object for use in the application views and repository."""
    poll = models.ForeignKey(Poll)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def votes_percentage(self):
        """Calculates the percentage of votes for this choice."""
        total = self.poll.total_votes()
        return self.votes / float(total) * 100 if total > 0 else 0

    def __unicode__(self):
        """Returns a string representation of a choice."""
        return self.text

class Patient(models.Model):
    Name = models.CharField(max_length=200)
    MobileNo = models.CharField(max_length=10)

    def __unicode__(self):
        return self.Name + self.MobileNo

class Doctor(models.Model):
    Name = models.CharField(max_length=200)
    MobileNo = models.CharField(max_length=10)

    def __unicode__(self):
        return self.Name + self.MobileNo    

class Prescription(models.Model):
        Patient = models.ForeignKey(Patient)
        Date = models.DateTimeField()
        Doctor = models.ForeignKey(Doctor)