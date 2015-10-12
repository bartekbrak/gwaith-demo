from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False,
                                        auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('rate', models.FloatField()),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together={('date', 'rate', 'currency')},
        ),
    ]
