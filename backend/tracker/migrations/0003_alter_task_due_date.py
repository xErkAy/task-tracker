# Generated by Django 5.1.1 on 2024-10-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Срок исполнения'),
        ),
    ]
