from django.contrib import admin
from sistema.models import Aluno, Professor

class AddAluno(admin.TabularInline):
	model = Aluno
	extra = 4

class ProfessorAdmin(admin.ModelAdmin):
	fieldsets = [
		('Nome', {'fields': ['nome']}),
		('Disciplina', {'fields': ['disciplina']})
	]
	inlines = [AddAluno]
	list_display = ('nome', 'disciplina')

admin.site.register(Professor, ProfessorAdmin)
