# Generated by Django 4.2 on 2023-09-23 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testTask', '0006_remove_lesson_view_access_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='Default_Name', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='surname',
            field=models.CharField(default='Default_Surname', max_length=100),
        ),
    ]