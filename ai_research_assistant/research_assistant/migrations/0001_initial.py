# Generated by Django 5.1.7 on 2025-03-31 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pdf_file', models.FileField(upload_to='uploads/')),
                ('extracted_text', models.TextField()),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
