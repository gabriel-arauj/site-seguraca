from django.db import models

class UserInseguro(models.Model):    
    user = models.CharField(max_length=255, verbose_name="Usuário")
    password = models.CharField(max_length=255, verbose_name="Password")

    class Meta:
        verbose_name = "Usuário Inseguro"
        verbose_name_plural = "Usuários Inseguros"

    def __str__(self):
        return self.user

class Comment(models.Model):    
    user = models.CharField(max_length=255, verbose_name="Usuário")
    comment = models.CharField(max_length=255, verbose_name="Comentário")

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"

    def __str__(self):
        return self.user

