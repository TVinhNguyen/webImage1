# Generated by Django 5.1.6 on 2025-02-20 03:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0003_alter_collection_user_alter_image_user_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='image',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='image',
            name='file_size',
        ),
        migrations.RemoveField(
            model_name='image',
            name='mime_type',
        ),
        migrations.RemoveField(
            model_name='image',
            name='resolution',
        ),
        migrations.RemoveField(
            model_name='image',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='collections', to='media.image'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='collection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='downloads',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='image',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='default/avatar.jpg', upload_to='avatars/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='display_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
