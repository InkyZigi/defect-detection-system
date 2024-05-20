# Generated by Django 4.1.12 on 2024-04-19 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ADModel',
            fields=[
                ('MID', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('Params', models.JSONField(null=True)),
                ('Description', models.CharField(max_length=300, null=True)),
            ],
            options={
                'db_table': 'models',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('CID', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('Cname', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=300, null=True)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('DID', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('Dname', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=300, null=True)),
                ('CID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detection.company')),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EID', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('Password', models.CharField(max_length=100)),
                ('Ename', models.CharField(max_length=100)),
                ('ContactNum', models.CharField(max_length=20, null=True)),
                ('Role', models.CharField(choices=[('A', 'admin'), ('M', 'manager'), ('P', 'operator')], max_length=20)),
                ('CID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='detection.company')),
                ('DID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='detection.department')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('SID', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('Production', models.JSONField(null=True)),
                ('OrderDate', models.DateTimeField(null=True)),
                ('TargetDate', models.DateTimeField(null=True)),
                ('EndDate', models.DateTimeField(null=True)),
                ('Approval', models.BooleanField(default=False)),
                ('EID', models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='employee', to='detection.employee')),
            ],
            options={
                'db_table': 'sheets',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='Dmanager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager_related', to='detection.employee'),
        ),
        migrations.CreateModel(
            name='Approvals',
            fields=[
                ('AID', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('Content', models.JSONField(null=True)),
                ('Action', models.CharField(max_length=20, null=True)),
                ('State', models.CharField(max_length=20, null=True)),
                ('AcceptorID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acceptor', to='detection.employee')),
                ('RequesterID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to='detection.employee')),
            ],
        ),
    ]