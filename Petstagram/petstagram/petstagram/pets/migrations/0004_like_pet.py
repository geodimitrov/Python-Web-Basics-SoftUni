# Generated by Django 3.2.3 on 2021-06-13 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_auto_20210613_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='pet',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pets.pet'),
            preserve_default=False,
        ),
    ]