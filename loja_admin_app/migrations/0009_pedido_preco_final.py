# Generated by Django 5.1.6 on 2025-02-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja_admin_app', '0008_ofertas_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='preco_final',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
