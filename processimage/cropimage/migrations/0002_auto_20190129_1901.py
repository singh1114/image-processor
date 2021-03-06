# Generated by Django 2.1.5 on 2019-01-29 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cropimage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='image_name',
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='parent_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cropimage.ImageModel'),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(height_field='image_height', upload_to='images/', width_field='image_width'),
        ),
    ]
