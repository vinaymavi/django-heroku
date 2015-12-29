from __future__ import unicode_literals

from django.db import models


# TODO create seprate model files for group of models.
class Instructions(models.Model):
    text = models.CharField(max_length=2000)
    add_date = models.DateField('add_date')


class Grade(models.Model):
    text = models.CharField(max_length=10, unique=True)
    add_date = models.DateField('add_date', )

    def __str__(self):
        return self.text


class FunctionArea(models.Model):
    text = models.CharField(max_length=10, unique=True)
    add_date = models.DateField('add_date', )

    def __str__(self):
        return self.text


class Designation(models.Model):
    text = models.CharField(max_length=200, unique=True)
    add_date = models.DateField('add_date')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    function_area = models.ForeignKey(FunctionArea, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=10, unique=True)
    add_date = models.DateField('add_date')
    join_date = models.DateField('add_date')

    def __str__(self):
        return self.first_name + ' ' + self.last_name + '(' + self.emp_id + ')'


class Trigger(models.Model):
    text = models.CharField(max_length=200)
    add_date = models.DateField('add_date')

    def __str__(self):
        return self.text


class TraningCategory(models.Model):
    text = models.CharField(max_length=200)
    add_date = models.DateField('add_date')

    def __str__(self):
        return self.text


class NeedCategory(models.Model):
    text = models.CharField(max_length=200)
    add_date = models.DateField('add_date')

    def __str__(self):
        return self.text


class ModeOfLearning(models.Model):
    text = models.CharField(max_length=200)
    add_date = models.DateField('add_date')

    def __str__(self):
        return self.text


class ImpactOnWork(models.Model):
    text = models.CharField(max_length=200)
    add_date = models.DateField('add_date')

    def __str__(self):
        return self.text


class LearningPlan(models.Model):
    text = models.CharField(max_length=1000)
    trigger = models.ForeignKey(Trigger, on_delete=models.CASCADE)
    training_cat = models.ForeignKey(TraningCategory, on_delete=models.CASCADE)
    need_cat = models.ForeignKey(NeedCategory, on_delete=models.CASCADE)
    mode_of_learn = models.ForeignKey(ModeOfLearning, on_delete=models.CASCADE)
    impact_on_work = models.ForeignKey(ImpactOnWork, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    start_date = models.DateField('start_date')
    end_date = models.DateField('end_date')
    add_date = models.DateField('add_date')


class ScoreCardArea(models.Model):
    text = models.CharField(max_length=200)
    add_date = models.DateField('add_date')

    def __str__(self):
        return self.text


class Objective(models.Model):
    text = models.CharField(max_length=2000)
    score_card_area = models.ForeignKey(ScoreCardArea, on_delete=models.CASCADE)
    start_date = models.DateField('start_date')
    end_date = models.DateField('end_date')
    add_date = models.DateField('add_date')
    measure = models.CharField(max_length=2000)
