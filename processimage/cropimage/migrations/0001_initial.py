# Generated by Django 2.1.5 on 2019-01-26 20:37

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('image_type', models.IntegerField(choices=[(0, 'Main Image'), (1, 'Horizontal Image'), (2, 'Vertical Image'), (3, 'Horizontal Small Image'), (4, 'Gallery Image')], default=0)),
                ('image', models.ImageField(height_field='image_height', upload_to='', width_field='image_width')),
                ('image_width', models.IntegerField(default=0)),
                ('image_height', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
    ]
