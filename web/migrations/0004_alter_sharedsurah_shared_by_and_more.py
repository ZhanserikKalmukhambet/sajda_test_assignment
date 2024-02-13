# Generated by Django 5.0.2 on 2024-02-13 18:33

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_userdhikrread_timestamp_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedsurah',
            name='shared_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surah_shared_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sharedsurah',
            name='shared_with',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surah_shared_with', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sharedsurah',
            name='surah',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.surah'),
        ),
        migrations.AlterField(
            model_name='userdhikrread',
            name='last_read',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 13, 18, 33, 22, 203200, tzinfo=datetime.timezone.utc)),
        ),
    ]