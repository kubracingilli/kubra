# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('content_type', models.CharField(null=True, choices=[('wiki', 'Wiki Page'), ('general', 'Gneric Page Type'), ('personal', 'My Custom Personel Content')], default='general', max_length=8)),
                ('view_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='author')),
            ],
        ),
    ]
