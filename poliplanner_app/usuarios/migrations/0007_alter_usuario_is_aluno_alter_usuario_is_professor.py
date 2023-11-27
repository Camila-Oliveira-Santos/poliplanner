from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "usuarios",
            "0006_usuario_groups_usuario_is_aluno_usuario_is_professor_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="is_aluno",
            field=models.BooleanField(default=False, verbose_name="Aluno?"),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="is_professor",
            field=models.BooleanField(default=False, verbose_name="Professor?"),
        ),
    ]