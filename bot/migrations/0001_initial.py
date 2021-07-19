# Generated by Django 3.2.4 on 2021-07-18 18:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=80, verbose_name='Article title')),
                ('text', models.TextField(verbose_name='Article body')),
                ('posted_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Posted date')),
                ('edited_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Edited date')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Blog name')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(unique=True, verbose_name='User telegram id')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(max_length=15, null=True, verbose_name='First name')),
                ('last_name', models.CharField(max_length=15, null=True, verbose_name='Last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='User is active?')),
                ('ban', models.BooleanField(default=False, verbose_name='Banned')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users registered in the bot',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Category name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='BlogSubscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bot.blog', verbose_name='Blog')),
                ('subscriber', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogsubscribers', to='bot.botuser', verbose_name='Blog subscriber')),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Blog subscribers',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(max_length=3, related_name='categories', to='bot.Category', verbose_name="Blog's category"),
        ),
        migrations.AddField(
            model_name='blog',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='botusers', to='bot.botuser', verbose_name='Blog owner'),
        ),
        migrations.CreateModel(
            name='ArticleView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.IntegerField(default=0, verbose_name='Article views')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.article', verbose_name='Article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bot.botuser', verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bot.blog', verbose_name='Blog'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bot.category', verbose_name='Category'),
        ),
    ]
