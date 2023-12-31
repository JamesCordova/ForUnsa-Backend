# Generated by Django 4.2.2 on 2023-07-19 23:33

import apps.forum.models.custom_user
import apps.forum.models.post
import apps.forum.models.reaction
import apps.forum.models.report
import apps.forum.models.school
import apps.forum.models.section
import apps.forum.validators
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApprovalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('X', 'Deleted')], default='A', max_length=1)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PostBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('X', 'Deleted')], default='A', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('likes_count', models.BigIntegerField(default=0, editable=False)),
                ('dislikes_count', models.BigIntegerField(default=0, editable=False)),
                ('comments_count', models.BigIntegerField(default=0, editable=False)),
                ('user', models.ForeignKey(on_delete=models.SET(apps.forum.models.custom_user.CustomUser.get_deleted_user), to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('X', 'Deleted')], default='A', max_length=1)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('X', 'Deleted')], default='A', max_length=1)),
                ('description', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReportType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('X', 'Deleted')], default='A', max_length=1)),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('X', 'Deleted')], default='A', max_length=1)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=64, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('X', 'Deleted')], default='A', max_length=1)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('posts_count', models.BigIntegerField(default=0, editable=False)),
                ('slug', models.SlugField(editable=False, max_length=64, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('X', 'Deleted')], default='A', max_length=1)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=32, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SavePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('X', 'Deleted')], default='A', max_length=1)),
                ('made_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.postbase')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-post'],
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('X', 'Deleted')], default='A', max_length=1)),
                ('information', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.postbase')),
                ('report_type', models.ForeignKey(default=apps.forum.models.report.ReportType.get_default_type, on_delete=django.db.models.deletion.SET_DEFAULT, to='forum.reporttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-post'],
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('X', 'Deleted')], default='A', max_length=1)),
                ('biography', models.CharField(blank=True, max_length=255)),
                ('img', models.ImageField(default='profiles/default.jpg', upload_to='profiles', validators=[apps.forum.validators.MaxWeightValidator(2)])),
                ('is_featured', models.BooleanField(default=False)),
                ('semester', models.CharField(default='not defined', max_length=32)),
                ('slug', models.SlugField(editable=False, max_length=64, unique=True)),
                ('current_school', models.ForeignKey(default=apps.forum.models.school.School.get_default_school, on_delete=models.SET(apps.forum.models.school.School.get_default_school), to='forum.school')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ReactPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('X', 'Deleted')], default='A', max_length=1)),
                ('made_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.postbase')),
                ('post_reaction', models.ForeignKey(on_delete=models.SET(apps.forum.models.reaction.Reaction.get_default_reaction), to='forum.reaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-post'],
                'unique_together': {('post', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='forum.postbase')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField(blank=True, max_length=255)),
                ('img', models.ImageField(blank=True, upload_to='posts', validators=[apps.forum.validators.MaxWeightValidator(2)])),
                ('file', models.FileField(blank=True, upload_to='docs', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'docx'])])),
                ('slug', models.SlugField(editable=False, max_length=64)),
                ('approval_status', models.ForeignKey(default=apps.forum.models.post.ApprovalStatus.get_default_status, on_delete=django.db.models.deletion.SET_DEFAULT, to='forum.approvalstatus')),
                ('post_type', models.ForeignKey(default=apps.forum.models.post.PostType.get_default_type, on_delete=django.db.models.deletion.SET_DEFAULT, to='forum.posttype')),
                ('section', models.ForeignKey(default=apps.forum.models.section.Section.get_default_section, on_delete=models.SET(apps.forum.models.section.Section.get_default_section), to='forum.section')),
                ('tags', models.ManyToManyField(blank=True, to='forum.tag')),
            ],
            options={
                'ordering': ['-likes_count'],
            },
            bases=('forum.postbase',),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('postbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='forum.postbase')),
                ('content', models.TextField(max_length=255)),
                ('posted_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted_on_%(class)s', to='forum.postbase')),
            ],
            options={
                'ordering': ['-likes_count'],
            },
            bases=('forum.postbase',),
        ),
    ]
