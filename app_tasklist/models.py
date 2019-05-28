from django.db import models

class Todo(models.Model):
    titulo = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    descricao = models.CharField(max_length=400, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)
    data_conclusao = models.DateTimeField(null=True)

    def __str__(self):
        return self.titulo