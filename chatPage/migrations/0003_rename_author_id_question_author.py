# Generated by Django 5.0.4 on 2024-07-03 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatPage', '0002_rename_author_question_author_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='author_id',
            new_name='author',
        ),
    ]