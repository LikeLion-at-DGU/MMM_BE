# Generated by Django 4.1.7 on 2023-08-18 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='editorprofile',
            name='email',
            field=models.EmailField(db_index=True, default='', max_length=254, unique=True),
        ),
    ]
