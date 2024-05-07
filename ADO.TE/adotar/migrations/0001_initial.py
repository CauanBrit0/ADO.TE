# Generated by Django 5.0.5 on 2024-05-07 21:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('divulgar', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoAdocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('status', models.CharField(choices=[('AG', 'Aguardando Aprovação'), ('AP', 'Aprovado'), ('R', 'Recusado')], max_length=2)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='divulgar.pet')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]