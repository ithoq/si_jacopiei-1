from django.db import models
import datetime
from django.utils import timezone

class Professor(models.Model):
	nome = models.CharField(max_length = 32)
	disciplina = models.CharField(max_length = 64)

class Aluno(models.Model):
	nome = models.CharField(max_length = 32)
	professor = models.ForeignKey(Professor)
