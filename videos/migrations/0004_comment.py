# Generated by Django 4.1 on 2023-11-16 13:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0003_remove_video_video_image_video_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('created_date', models.DateField(null=True)),
                ('updated_date', models.DateField(null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='videos.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
