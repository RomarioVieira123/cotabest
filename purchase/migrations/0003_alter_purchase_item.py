# Generated by Django 4.1.3 on 2022-11-17 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_rename_puchaseitem_purchaseitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='item',
            field=models.ManyToManyField(related_name='item_purchase', to='purchase.purchaseitem'),
        ),
    ]