# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-19 13:27
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BeProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjName', models.CharField(max_length=50)),
                ('ProjURL', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('ProjDesc', models.CharField(blank=True, max_length=500)),
                ('image1', models.FileField(upload_to='')),
                ('image2', models.FileField(blank=True, upload_to='')),
                ('image3', models.FileField(blank=True, upload_to='')),
                ('image4', models.FileField(blank=True, upload_to='')),
                ('image5', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrganisationName', models.CharField(max_length=50)),
                ('YourPosition', models.CharField(max_length=50)),
                ('Loc', models.CharField(blank=True, max_length=50)),
                ('dateFrom', models.DateField(blank=True, default=datetime.date.today, verbose_name='Date')),
                ('dateTo', models.DateField(blank=True, default=datetime.date.today, verbose_name='Date')),
                ('Desc', models.CharField(blank=True, max_length=500)),
                ('Certificate', models.FileField(blank=True, upload_to='')),
                ('image1', models.FileField(upload_to='')),
                ('image2', models.FileField(blank=True, upload_to='')),
                ('image3', models.FileField(blank=True, upload_to='')),
                ('image4', models.FileField(blank=True, upload_to='')),
                ('image5', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem1_gpa', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4, null=True)),
                ('sem2_gpa', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4, null=True)),
                ('sem3_gpa', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4, null=True)),
                ('sem4_gpa', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4, null=True)),
                ('sem5_gpa', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4, null=True)),
                ('sem6_gpa', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4, null=True)),
                ('sem7_gpa', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4, null=True)),
                ('sem8_gpa', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompetitionName', models.CharField(max_length=50)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Desc', models.CharField(max_length=500)),
                ('URL', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('image1', models.FileField(upload_to='')),
                ('image2', models.FileField(blank=True, upload_to='')),
                ('image3', models.FileField(blank=True, upload_to='')),
                ('image4', models.FileField(blank=True, upload_to='')),
                ('image5', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalBeProject',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('ProjName', models.CharField(max_length=50)),
                ('ProjURL', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('ProjDesc', models.CharField(blank=True, max_length=500)),
                ('image1', models.TextField(max_length=100)),
                ('image2', models.TextField(blank=True, max_length=100)),
                ('image3', models.TextField(blank=True, max_length=100)),
                ('image4', models.TextField(blank=True, max_length=100)),
                ('image5', models.TextField(blank=True, max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical be project',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCommittee',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('OrganisationName', models.CharField(max_length=50)),
                ('YourPosition', models.CharField(max_length=50)),
                ('Loc', models.CharField(blank=True, max_length=50)),
                ('dateFrom', models.DateField(blank=True, default=datetime.date.today, verbose_name='Date')),
                ('dateTo', models.DateField(blank=True, default=datetime.date.today, verbose_name='Date')),
                ('Desc', models.CharField(blank=True, max_length=500)),
                ('Certificate', models.TextField(blank=True, max_length=100)),
                ('image1', models.TextField(max_length=100)),
                ('image2', models.TextField(blank=True, max_length=100)),
                ('image3', models.TextField(blank=True, max_length=100)),
                ('image4', models.TextField(blank=True, max_length=100)),
                ('image5', models.TextField(blank=True, max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical committee',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalHackathon',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('CompetitionName', models.CharField(max_length=50)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Desc', models.CharField(max_length=500)),
                ('URL', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('image1', models.TextField(max_length=100)),
                ('image2', models.TextField(blank=True, max_length=100)),
                ('image3', models.TextField(blank=True, max_length=100)),
                ('image4', models.TextField(blank=True, max_length=100)),
                ('image5', models.TextField(blank=True, max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical hackathon',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalInternship',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=50)),
                ('Position', models.CharField(blank=True, max_length=50)),
                ('Loc', models.CharField(blank=True, max_length=50)),
                ('From', models.DateField(blank=True, default=datetime.date.today, verbose_name='Date')),
                ('To', models.DateField(blank=True, default=datetime.date.today, verbose_name='Date')),
                ('desc', models.CharField(blank=True, max_length=500)),
                ('Certificate', models.TextField(blank=True, max_length=100)),
                ('image1', models.TextField(max_length=100)),
                ('image2', models.TextField(blank=True, max_length=100)),
                ('image3', models.TextField(blank=True, max_length=100)),
                ('image4', models.TextField(blank=True, max_length=100)),
                ('image5', models.TextField(blank=True, max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical internship',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProject',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('ProjName', models.CharField(max_length=50)),
                ('ProjURL', models.TextField(blank=True, validators=[django.core.validators.URLValidator()])),
                ('ProjDesc', models.CharField(blank=True, max_length=500)),
                ('image1', models.TextField(max_length=100)),
                ('image2', models.TextField(blank=True, max_length=100)),
                ('image3', models.TextField(blank=True, max_length=100)),
                ('image4', models.TextField(blank=True, max_length=100)),
                ('image5', models.TextField(blank=True, max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical project',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalResearchPaper',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Publication', models.CharField(max_length=100)),
                ('DateOfPublication', models.DateField(blank=True, default=datetime.date.today, verbose_name='Date')),
                ('Desc', models.CharField(blank=True, max_length=500)),
                ('LinkToPaper', models.TextField(blank=True, validators=[django.core.validators.URLValidator()])),
                ('PaperId', models.CharField(blank=True, max_length=50)),
                ('image1', models.TextField(max_length=100)),
                ('image2', models.TextField(blank=True, max_length=100)),
                ('image3', models.TextField(blank=True, max_length=100)),
                ('image4', models.TextField(blank=True, max_length=100)),
                ('image5', models.TextField(blank=True, max_length=100)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical research paper',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalSkill',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical skill',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(blank=True, max_length=50)),
                ('Position', models.CharField(blank=True, max_length=50)),
                ('Loc', models.CharField(blank=True, max_length=50)),
                ('From', models.DateField(blank=True, default=datetime.date.today, verbose_name='Date')),
                ('To', models.DateField(blank=True, default=datetime.date.today, verbose_name='Date')),
                ('desc', models.CharField(blank=True, max_length=500)),
                ('Certificate', models.FileField(blank=True, upload_to='')),
                ('image1', models.FileField(upload_to='')),
                ('image2', models.FileField(blank=True, upload_to='')),
                ('image3', models.FileField(blank=True, upload_to='')),
                ('image4', models.FileField(blank=True, upload_to='')),
                ('image5', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='KT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_semester', models.CharField(choices=[('SEM1', 'Semester 1'), ('SEM2', 'Semester 2'), ('SEM3', 'Semester 3'), ('SEM4', 'Semester 4'), ('SEM5', 'Semester 5'), ('SEM6', 'Semester 6'), ('SEM7', 'Semester 7'), ('SEM8', 'Semester 8')], max_length=20)),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kt', to='user_profile.Education')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProjName', models.CharField(max_length=50)),
                ('ProjURL', models.TextField(blank=True, validators=[django.core.validators.URLValidator()])),
                ('ProjDesc', models.CharField(blank=True, max_length=500)),
                ('image1', models.FileField(upload_to='')),
                ('image2', models.FileField(blank=True, upload_to='')),
                ('image3', models.FileField(blank=True, upload_to='')),
                ('image4', models.FileField(blank=True, upload_to='')),
                ('image5', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruiter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Publication', models.CharField(max_length=100)),
                ('DateOfPublication', models.DateField(blank=True, default=datetime.date.today, verbose_name='Date')),
                ('Desc', models.CharField(blank=True, max_length=500)),
                ('LinkToPaper', models.TextField(blank=True, validators=[django.core.validators.URLValidator()])),
                ('PaperId', models.CharField(blank=True, max_length=50)),
                ('image1', models.FileField(upload_to='')),
                ('image2', models.FileField(blank=True, upload_to='')),
                ('image3', models.FileField(blank=True, upload_to='')),
                ('image4', models.FileField(blank=True, upload_to='')),
                ('image5', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sap_Id', models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(99999999999), django.core.validators.MinValueValidator(10000000000)])),
                ('department', models.CharField(max_length=50)),
                ('photo', models.FileField(blank=True, upload_to='')),
                ('github_id', models.CharField(blank=True, max_length=50, null=True)),
                ('bio', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('mobileNo', models.CharField(max_length=50)),
                ('year', models.CharField(choices=[('FE', 'First Year'), ('SE', 'Second Year'), ('TE', 'Third Year'), ('BE', 'Final Year')], max_length=20)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_student', 'Can see student profile'),),
            },
        ),
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sap_Id', models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(99999999999), django.core.validators.MinValueValidator(10000000000)])),
                ('department', models.CharField(max_length=50)),
                ('photo', models.FileField(blank=True, upload_to='')),
                ('bio', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_teacher', 'Can see teacher profile'),),
            },
        ),
        migrations.AddField(
            model_name='skill',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.StudentProfile'),
        ),
        migrations.AddField(
            model_name='researchpaper',
            name='Published_under',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='verifiedpaper', to='user_profile.TeacherProfile'),
        ),
        migrations.AddField(
            model_name='researchpaper',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='researchpaper', to='user_profile.StudentProfile'),
        ),
        migrations.AddField(
            model_name='project',
            name='projectUnderTeacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='verifiedprojects', to='user_profile.TeacherProfile'),
        ),
        migrations.AddField(
            model_name='project',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projectskills', to='user_profile.Skill'),
        ),
        migrations.AddField(
            model_name='project',
            name='student_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='user_profile.StudentProfile'),
        ),
        migrations.AddField(
            model_name='internship',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internships', to='user_profile.StudentProfile'),
        ),
        migrations.AddField(
            model_name='historicalskill',
            name='user_profile',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user_profile.StudentProfile'),
        ),
        migrations.AddField(
            model_name='historicalresearchpaper',
            name='Published_under',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user_profile.TeacherProfile'),
        ),
        migrations.AddField(
            model_name='historicalresearchpaper',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalresearchpaper',
            name='student',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user_profile.StudentProfile'),
        ),
        migrations.AddField(
            model_name='historicalproject',
            name='projectUnderTeacher',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user_profile.TeacherProfile'),
        ),
        migrations.AddField(
            model_name='historicalproject',
            name='skill',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user_profile.Skill'),
        ),
        migrations.AddField(
            model_name='historicalproject',
            name='student_profile',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user_profile.StudentProfile'),
        ),
        migrations.AddField(
            model_name='historicalinternship',
            name='employee',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user_profile.StudentProfile'),
        ),
        migrations.AddField(
            model_name='historicalinternship',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalhackathon',
            name='student_profile',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user_profile.StudentProfile'),
        ),
        migrations.AddField(
            model_name='historicalcommittee',
            name='employee',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user_profile.StudentProfile'),
        ),
        migrations.AddField(
            model_name='historicalcommittee',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalbeproject',
            name='projectUnderTeacher',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user_profile.TeacherProfile'),
        ),
        migrations.AddField(
            model_name='historicalbeproject',
            name='student',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='user_profile.StudentProfile'),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='student_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.StudentProfile'),
        ),
        migrations.AddField(
            model_name='education',
            name='student_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='user_profile.StudentProfile'),
        ),
        migrations.AddField(
            model_name='committee',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='committee', to='user_profile.StudentProfile'),
        ),
        migrations.AddField(
            model_name='beproject',
            name='projectUnderTeacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='verifiedbeprojects', to='user_profile.TeacherProfile'),
        ),
        migrations.AddField(
            model_name='beproject',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beprojects', to='user_profile.StudentProfile'),
        ),
        migrations.AddField(
            model_name='beproject',
            name='teammates',
            field=models.ManyToManyField(blank=True, related_name='beteammate', to='user_profile.StudentProfile'),
        ),
    ]
