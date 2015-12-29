# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, unique=True)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('emp_id', models.CharField(max_length=10, unique=True)),
                ('add_date', models.DateField(verbose_name='add_date')),
                ('join_date', models.DateField(verbose_name='add_date')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ert.Designation')),
            ],
        ),
        migrations.CreateModel(
            name='FunctionArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=10, unique=True)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=10, unique=True)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='ImpactOnWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='LearningPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=20)),
                ('start_date', models.DateField(verbose_name='start_date')),
                ('end_date', models.DateField(verbose_name='end_date')),
                ('add_date', models.DateField(verbose_name='add_date')),
                ('impact_on_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ert.ImpactOnWork')),
            ],
        ),
        migrations.CreateModel(
            name='ModeOfLearning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='NeedCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('add_date', models.DateField(verbose_name='add_date')),
            ],
        ),
        migrations.AddField(
            model_name='objective',
            name='score_card_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ert.ScoreCardArea'),
        ),
        migrations.AddField(
            model_name='learningplan',
            name='mode_of_learn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ert.ModeOfLearning'),
        ),
        migrations.AddField(
            model_name='learningplan',
            name='need_cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ert.NeedCategory'),
        ),
        migrations.AddField(
            model_name='learningplan',
            name='training_cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ert.TrainingCategory'),
        ),
        migrations.AddField(
            model_name='learningplan',
            name='trigger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ert.Trigger'),
        ),
        migrations.AddField(
            model_name='designation',
            name='function_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ert.FunctionArea'),
        ),
        migrations.AddField(
            model_name='designation',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ert.Grade'),
        ),
    ]
