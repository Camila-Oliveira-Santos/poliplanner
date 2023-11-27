from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class AdmUsuario(BaseUserManager):
    
    def get_by_natural_key(self, email_):
        return self.get(email=email_)

    def create_user(self, nome, email, is_aluno, is_professor, password=None):
        if not email:
            raise ValueError('Users must have an e-mail')

        user = self.model(
            nome=nome,
            email=email,
            is_aluno=is_aluno,
            is_professor=is_professor,
        )
        user.set_password(password)
        user.activated=True
        user.save(using=self._db)
        return user

    def create_superuser(self, nome, email, is_aluno, is_professor, password):
        user = self.create_user(email=email, 
                                nome=nome,
                                is_aluno=is_aluno,
                                is_professor=is_professor,
                                password=password,
                                )
        user.activated= True
        user.is_admin = True
        user.is_aluno = True
        user.is_professor = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField('admin status',default=False)
    is_aluno = models.BooleanField('Aluno?', default=False)
    is_professor = models.BooleanField('Professor?', default=False)

    objects = AdmUsuario()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'is_aluno', 'is_professor']

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin

    def natural_key(self):
        return self.email

    def __str__(self):
        return f'{self.nome}'
