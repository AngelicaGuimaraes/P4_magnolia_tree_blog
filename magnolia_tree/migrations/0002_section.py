# Generated by Django 3.2.16 on 2022-12-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magnolia_tree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(blank=True, help_text='Enter a section of the body', max_length=200, unique=True)),
            ],
            options={
                'ordering': ['section_name'],
            },
        ),
    ]
