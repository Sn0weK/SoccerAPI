# Generated by Django 2.2.1 on 2020-09-22 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_date', models.DateTimeField()),
                ('home_score', models.IntegerField()),
                ('away_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('position', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('abbreviation', models.CharField(max_length=3)),
                ('country', models.CharField(max_length=3)),
                ('stadium_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_x', models.FloatField()),
                ('position_y', models.FloatField()),
                ('period', models.IntegerField()),
                ('time', models.IntegerField()),
                ('on_target', models.BooleanField()),
                ('is_goal', models.BooleanField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccerstats.Match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccerstats.Player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccerstats.Team')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccerstats.Team'),
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_x', models.FloatField()),
                ('position_y', models.FloatField()),
                ('is_successful', models.BooleanField()),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccerstats.Match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pass_player', to='soccerstats.Player')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pass_target', to='soccerstats.Player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soccerstats.Team')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='soccerstats.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='soccerstats.Team'),
        ),
    ]