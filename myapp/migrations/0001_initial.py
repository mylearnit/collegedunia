# Generated by Django 5.1.3 on 2024-11-11 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('cutoff_year', models.CharField(max_length=200)),
                ('cutoff_course_name', models.CharField(max_length=200)),
                ('cutoff_course_id', models.CharField(max_length=200)),
                ('cutoff_cutoff', models.CharField(max_length=200)),
                ('cutoff_exam', models.CharField(max_length=200)),
                ('cutoff_cutoff_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('stream_data_name', models.CharField(max_length=200)),
                ('stream_data_id', models.IntegerField(null=True)),
                ('display_name', models.CharField(max_length=200)),
                ('sub_stream_data_name', models.CharField(max_length=200)),
                ('sub_stream_data_id', models.IntegerField(null=True)),
                ('short_head', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('duration_year', models.CharField(max_length=200)),
                ('duration_month', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=200)),
                ('course_type', models.CharField(max_length=200)),
                ('degree_could_be', models.CharField(max_length=200)),
                ('short_admission', models.CharField(max_length=200, null=True)),
                ('qna_count', models.CharField(max_length=200, null=True)),
                ('admission_criteria', models.CharField(max_length=200, null=True)),
                ('admission_admission_post_id', models.CharField(max_length=200, null=True)),
                ('admission_admission_post_title', models.CharField(max_length=200, null=True)),
                ('admission_admission_post_name', models.CharField(max_length=200, null=True)),
                ('admission_display_head', models.CharField(max_length=200, null=True)),
                ('admission_admission_start_date', models.CharField(max_length=200, null=True)),
                ('admission_admission_end_date', models.CharField(max_length=200, null=True)),
                ('course_rating', models.CharField(max_length=200, null=True)),
                ('reviews_count', models.IntegerField(null=True)),
                ('categories', models.JSONField()),
                ('url', models.CharField(max_length=200, null=True)),
                ('forum_data', models.JSONField()),
                ('qna_data', models.JSONField()),
                ('qna_link', models.CharField(max_length=200, null=True)),
                ('course_tag_id', models.IntegerField(null=True)),
                ('fees_data_amount', models.CharField(max_length=200, null=True)),
                ('fees_data_text', models.CharField(max_length=200, null=True)),
                ('fees_data_is_tentative', models.CharField(max_length=200, null=True)),
                ('fees_data_priority_category', models.CharField(max_length=200, null=True)),
                ('type', models.CharField(max_length=200, null=True)),
                ('stream_id', models.IntegerField(null=True)),
                ('course_id', models.IntegerField(null=True)),
                ('course_tag', models.CharField(max_length=200, null=True)),
                ('available_seats', models.CharField(max_length=200, null=True)),
                ('courses_count', models.IntegerField(null=True)),
                ('eligibility', models.CharField(max_length=200, null=True)),
                ('offered_by', models.JSONField()),
                ('admission_guide_link', models.CharField(max_length=200, null=True)),
                ('cutoff_year', models.CharField(max_length=200, null=True)),
                ('cutoff_course_name', models.CharField(max_length=200, null=True)),
                ('cutoff_course_id', models.CharField(max_length=200, null=True)),
                ('cutoff_cutoff', models.CharField(max_length=200, null=True)),
                ('cutoff_exam', models.CharField(max_length=200, null=True)),
                ('cutoff_cutoff_type', models.CharField(max_length=200, null=True)),
                ('duration', models.CharField(max_length=200, null=True)),
                ('is_discontinued', models.IntegerField(null=True)),
                ('ranking_stats_key_college_id', models.IntegerField(null=True)),
                ('ranking_stats_key_stream_id', models.IntegerField(null=True)),
                ('ranking_stats_key_agency_id', models.IntegerField(null=True)),
                ('ranking_stats_key_data_key', models.CharField(max_length=200, null=True)),
                ('exams', models.ManyToManyField(to='myapp.exam')),
                ('streams', models.ManyToManyField(to='myapp.stream')),
            ],
        ),
    ]
