# from tkinter import CASCADE
# from unittest.util import _MAX_LENGTH
import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model): #note lack of 's' at end of Question and Choice; blueprint for each separate question / choice
    question_text = models.CharField(max_length=200) #most of the time, better to use charfield vs just text so that user can't put in unlimited text; .CharField requires a max_length; .TextField doesn't require option (i.e. max-length) but still requires ()

    pub_date = models.DateTimeField() #enables entries to be sorted according to time

    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1) #>= makes this a comparison that will return true or false whether question has been published within the past 24 hours
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name="choices", on_delete=models.CASCADE) #every choice must be tied to specific question; requirecd to give it 2 things
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) #store number of votes per choice

    def __str__(self):
        return self.choice_text