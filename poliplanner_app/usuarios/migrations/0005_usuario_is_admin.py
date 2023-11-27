from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0004_usuario_nome"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuario",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
    ]