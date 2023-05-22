# Generated by Django 4.2.1 on 2023-05-22 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('categoria_producto_id', models.IntegerField(primary_key=True, serialize=False)),
                ('categoria_padre_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('departamento_id', models.IntegerField(primary_key=True, serialize=False)),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('direccion_id', models.IntegerField(primary_key=True, serialize=False)),
                ('usuario_id', models.IntegerField()),
                ('direccion', models.CharField(max_length=200)),
                ('direccion_actual', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('producto_id', models.IntegerField(primary_key=True, serialize=False)),
                ('orden_date', models.DateField()),
                ('nombre', models.CharField(max_length=200)),
                ('precio', models.FloatField()),
                ('categoria_producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.categoriaproducto')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('municipio_id', models.IntegerField(primary_key=True, serialize=False)),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('departamento_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='InventarioProducto',
            fields=[
                ('inventario_producto_id', models.IntegerField(primary_key=True, serialize=False)),
                ('referencia', models.CharField(max_length=200)),
                ('serial', models.CharField(max_length=200)),
                ('producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('factura_id', models.IntegerField(primary_key=True, serialize=False)),
                ('usuario_id', models.IntegerField()),
                ('fecha_factura', models.DateField()),
                ('valor_total', models.IntegerField()),
                ('direcion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.direccion')),
            ],
        ),
        migrations.AddField(
            model_name='direccion',
            name='municipio_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.municipio'),
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('detalle_factura_id', models.IntegerField(primary_key=True, serialize=False)),
                ('factura_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.factura')),
                ('inventario_producto_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.inventarioproducto')),
            ],
        ),
    ]
