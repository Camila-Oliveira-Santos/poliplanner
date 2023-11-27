from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0003_remove_usuario_nome"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuario",
            name="nome",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
