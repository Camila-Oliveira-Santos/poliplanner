from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("usuarios", "0005_usuario_is_admin"),
    ]

    operations = [
        migrations.AddField(
            model_name="usuario",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="usuario",
            name="is_aluno",
            field=models.BooleanField(default=False, verbose_name="aluno status"),
        ),
        migrations.AddField(
            model_name="usuario",
            name="is_professor",
            field=models.BooleanField(default=False, verbose_name="professor status"),
        ),
        migrations.AddField(
            model_name="usuario",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="is_admin",
            field=models.BooleanField(default=False, verbose_name="admin status"),
        ),
    ]
