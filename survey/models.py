from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Survey(models.Model):
    title = models.CharField(max_length=100)
    posted = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class CompletedSurvey(models.Model):
    posted = models.DateTimeField(auto_now=True)
    survey = models.ForeignKey(Survey)
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title


class Question(models.Model):
    posted = models.DateTimeField(auto_now=True)
    survey = models.ForeignKey(Survey)
    question = models.CharField(max_length=300)

    def __unicode__(self):
        return self.question


class Answer(models.Model):
    posted = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question)
    answer = models.CharField(max_length=300)
    completed_survey = models.ForeignKey(CompletedSurvey)

    def __unicode__(self):
        return self.answer







