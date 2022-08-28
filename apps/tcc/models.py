from django.db import models


class Autor(models.Model):

    nome = models.CharField(max_length=150)
    ultimo_nome = models.CharField(max_length=150)
    foto = models.ImageField(upload_to='foto')

    def __str__(self):
        return self.nome


class Orientador(models.Model):

    nome = models.CharField(max_length=150)
    ultimo_nome = models.CharField(max_length=150)
    link_do_curriculo = models.URLField(max_length=150)

    def __str__(self):
        return self.nome

class Curso(models.Model):

    modalidades = (('Bacharelado', 'Bacharelado'), ('Licenciatura', 'Licenciatura'), ('Tecnológo', 'Tecnológo'))

    nome = models.CharField(max_length=150)
    modalidade = models.CharField(max_length=150, choices = modalidades)

    def __str__(self):
        return self.nome


class Tcc(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    ano_documento = models.IntegerField(verbose_name="ano_documento")
    resumo = models.TextField()
    arquivo_documento = models.FileField(upload_to='tcc')
    palavras_chave = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

