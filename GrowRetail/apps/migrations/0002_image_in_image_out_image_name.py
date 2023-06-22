# Generated by Django 4.2.2 on 2023-06-20 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="IN",
            field=models.DecimalField(decimal_places=2, default=2.4, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="image",
            name="OUT",
            field=models.DecimalField(decimal_places=2, default=3.6, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="image",
            name="name",
            field=models.CharField(default=2.2, max_length=100),
            preserve_default=False,
        ),
    ]
