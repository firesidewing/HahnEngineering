# Generated by Django 3.2.7 on 2021-09-24 00:28

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_subscribefield_subscribepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribefield',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_fields', to='home.subscribepage'),
        ),
    ]
