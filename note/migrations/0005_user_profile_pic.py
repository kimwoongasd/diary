# Generated by Django 4.0.4 on 2022-07-05 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics'),
        ),
    ]
