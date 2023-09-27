from django.db import models

# Create your models here.

class cidade(models.Model):
     cidade = models.CharField(max_length=50)
     uf = models.CharField(max_length=2)
     def __str__(self):
        return "self.cidade, self.uf"

class pessoas(models.Model):
    professor = models.CharField(max_length=50)
    estudantes = models.CharField(max_length=50)
    coordenador = models.CharField(max_length=50)
    nome_pessoas = models.CharField(max_length=50)
    mae = models.CharField(max_length=50)
    pai = models.CharField(max_length=50)
    cpf = models.CharField(max_length=13)
    data_nasc = models.CharField(max_length=10)
    cidade_pessoas = models.ForeignKey(cidade, on_delete=models.CASCADE)
    uf_pessoas = models.ForeignKey(cidade, on_delete=models.CASCADE)
    def __str__(self):
        return "self.professor, self.estudantes, self.coordenador"

class ocupacao(models.Model):
     professor = models.CharField(max_length=50)
     estudantes = models.CharField(max_length=50)
     coordenador = models.CharField(max_length=50)
     diretor = models.CharField(max_length=50)
     nome_ocupacao = models.CharField(max_length=50)
     def __str__(self):
        return "self.professor, self.estudantes, self.coordenador"
     
class instituicao(models.Model):
     nome_instituicao = models.CharField(max_length=50)
     site = models.CharField(max_length=50)
     telefone = models.CharField(max_length=11)
     def __str__(self):
        return "self.nome_instituicao"
     
class area(models.Model):
     nome_area = models.CharField(max_length=50)
     biologia = models.CharField(max_length=50)
     agro = models.CharField(max_length=50)
     computacao = models.CharField(max_length=50)
     def __str__(self):
        return "self.nome_area"
     
class cursos(models.Model):
     nome_curso = models.CharField(max_length=50)
     carga_horaria = models.CharField(max_length=4)
     aduracao_meses = models.CharField(max_length=3)
     area_curso = models.ForeignKey(area, on_delete=models.CASCADE)
     instituicao_curso = models.ForeignKey(instituicao, on_delete=models.CASCADE)
     def __str__(self):
        return "self.nome_curso"
     
class periodo(models.Model):
     primeiro_periodo = models.CharField(max_length=50)
     primeiro_periodo = models.CharField(max_length=50)
     def __str__(self):
        return "self.periodo"
     
class disciplina(models.Model):
     nome_disciplina = models.CharField(max_length=50)
     area_diciplina = models.ForeignKey(area, on_delete=models.CASCADE)
     def __str__(self):
        return "self.nome_disciplina"
     
class matricula(models.Model):
    instituicao_matiricula = models.ForeignKey(instituicao, on_delete=models.CASCADE)
    cursos_matricula = models.ForeignKey(cursos, on_delete=models.CASCADE)
    disciplina_matricula = models.ForeignKey(disciplina, on_delete=models.CASCADE)
    def __str__(self):
        return "self.instituicao_matricula"
    
class avaliacoes(models.Model):
    descricao = models.CharField(max_length=100)
    disciplina_avaliacoes = models.ForeignKey(disciplina, on_delete=models.CASCADE)
    cursos_avaliacoes = models.ForeignKey(cursos, on_delete=models.CASCADE)
    def __str__(self):
        return "self.descricao"
    
class frequencia(models.Model):
    disciplina_frequencia = models.ForeignKey(disciplina, on_delete=models.CASCADE)
    cursos_frequencia = models.ForeignKey(cursos, on_delete=models.CASCADE)
    faltas = models.CharField(max_length=3)
    def __str__(self):
        return "self.frequencia"
    
class turmas(models.Model):
    periodo_mat_ves_not = models.CharField(max_length=10)
    nome_turma = models.CharField(max_length=20)
    periodo_turmas = models.ForeignKey(periodo, on_delete=models.CASCADE)
    def __str__(self):
        return "self.periodo_turmas"
    
class ocorrencias(models.Model):
    descricao = models.CharField(max_length=100)
    data = models.CharField(max_length=10)
    curso_ocorrencias = models.ForeignKey(cursos, on_delete=models.CASCADE)
    disciplina_ocorrencias = models.ForeignKey(disciplina, on_delete=models.CASCADE)
    pessoas_ocorrencias = models.ForeignKey(pessoas, on_delete=models.CASCADE)
    def __str__(self):
        return "self.ocorrencias"
    
class disciplinasporcursos (models.Model):
    nome_disciplinas_por_cursos = models.CharField(max_length=100)
    carga_horária = models.CharField(max_length=4)
    cursos_disciplinasporcursos = models.ForeignKey(cursos, on_delete=models.CASCADE)
    periodo_disciplinasporcursos = models.ForeignKey(periodo, on_delete=models.CASCADE)
    def __str__(self):
        return "self.nome_disciplinasporcursos"
    
class tipoavaliacao(models.Model):
    prova = models.CharField(max_length=100)
    trabalho = models.CharField(max_length=100)
    projeto = models.CharField(max_length=100)
    lista = models.CharField(max_length=100)
    def __str__(self):
        return "self.prova"
    

    


     