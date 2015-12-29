# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ert', '0002_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('emp_id', models.CharField(unique=True, max_length=10)),
                ('add_date', models.DateField(verbose_name='add_date')),
                ('join_date', models.DateField(verbose_name='add_date')),
                ('designation', models.ForeignKey(to='ert.Designation')),
            ],
        ),
        migrations.CreateModel(
            name='FunctionArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(unique=True, max_length=10)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='ImpactOnWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=2000)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='LearningPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=20)),
                ('start_date', models.DateField(verbose_name='start_date')),
                ('end_date', models.DateField(verbose_name='end_date')),
                ('add_date', models.DateField(verbose_name='add_date')),
                ('impact_on_work', models.ForeignKey(to='ert.ImpactOnWork')),
            ],
        ),
        migrations.CreateModel(
            name='ModeOfLearning',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='NeedCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=2000)),
                ('start_date', models.DateField(verbose_name='start_date')),
                ('end_date', models.DateField(verbose_name='end_date')),
                ('add_date', models.DateField(verbose_name='add_date')),
                ('measure', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='ScoreCardArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='TraningCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.AddField(
            model_name='objective',
            name='score_card_area',
            field=models.ForeignKey(to='ert.ScoreCardArea'),
        ),
        migrations.AddField(
            model_name='learningplan',
            name='mode_of_learn',
            field=models.ForeignKey(to='ert.ModeOfLearning'),
        ),
        migrations.AddField(
            model_name='learningplan',
            name='need_cat',
            field=models.ForeignKey(to='ert.NeedCategory'),
        ),
        migrations.AddField(
            model_name='learningplan',
            name='training_cat',
            field=models.ForeignKey(to='ert.TraningCategory'),
        ),
        migrations.AddField(
            model_name='learningplan',
            name='trigger',
            field=models.ForeignKey(to='ert.Trigger'),
        ),
    ]
