from django.db import models

# Create your models here.
class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = 'Disciplinas'

class Coordenador(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=30)
    coord = models.ForeignKey(Coordenador, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

class Disc_Curso(models.Model):
    disc = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.disc.nome + 'do curso de:' + self.curso.nome