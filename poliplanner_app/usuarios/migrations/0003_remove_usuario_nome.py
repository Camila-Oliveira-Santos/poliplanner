from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0002_alter_usuario_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usuario",
            name="nome",
        ),
    ]
