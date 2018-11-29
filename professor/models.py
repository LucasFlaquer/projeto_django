from django.db import models
from disciplina.models import Disciplina, Curso, Disc_Curso



#Create your models here.
class Professor(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=200)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name_plural = 'Professores'

class Professor_Disc(models.Model):
	professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
	disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

	# def __str__(self):
	# 	return self.professor.name + ' para ' + self.disciplina.nome


class ProfDisc_Curso(models.Model):
	Manha = 'MN'
	Tarde = 'TD'
	Noite = 'NT'
	Periodo = (
		(Manha, 'Matutino'),
		(Tarde, 'Vesperino'),
		(Noite, 'Noturno'),
	)
	profDisc = models.ForeignKey(Professor_Disc, on_delete=models.CASCADE)
	DiscCurso = models.ForeignKey(Disc_Curso, on_delete=models.CASCADE)
	turma = models.CharField(max_length=10)
	periodo = models.CharField(max_length=2, choices=Periodo, default=Noite)


class PlanoDesc(models.Model):
	profDiscCurso = models.ForeignKey(ProfDisc_Curso, on_delete=models.CASCADE)
	semestre = models.CharField(max_length=4)
	#carga horaria
	teoria = models.IntegerField()
	pratica = models.IntegerField()

#
# class PlanoAula(models.Model):
# 	semana = models.IntegerField(min_value=1, max_value=22)
