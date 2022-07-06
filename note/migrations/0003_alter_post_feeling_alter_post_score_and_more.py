# Generated by Django 4.0.4 on 2022-06-29 11:51

from django.db import migrations, models
import note.validators


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='feeling',
            field=models.CharField(max_length=50, validators=[note.validators.validate_no_numbers, note.validators.validate_no_special_characters]),
        ),
        migrations.AlterField(
            model_name='post',
            name='score',
            field=models.IntegerField(validators=[note.validators.validate_score, note.validators.validate_no_special_characters]),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(error_messages={'unique': '이미 사용중인 닉네임입니다.'}, max_length=20, null=True, unique=True, validators=[note.validators.validate_no_special_characters]),
        ),
    ]