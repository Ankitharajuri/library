# Generated by Django 4.2.2 on 2023-07-22 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_user_borrower_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower',
            name='returned',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3),
        ),
    ]
