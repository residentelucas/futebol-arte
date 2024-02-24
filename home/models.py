from django.db import models

# Create your models here.
from django.db import models
from django.utils.html import mark_safe


# Create your models here. (base de dados)
GENERO_CHOICES = (
        ("",""),
        ("M","MASCULINO"),
        ("F","FEMININO"),
    )

class Pais(models.Model):
    nome = models.CharField(max_length=50)
    continente = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'

    def __str__(self) -> str:
        return self.nome

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    regiao = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

#relacioanamento
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    populacao = models.IntegerField()

    def __str__(self) -> str:
        return self.nome

    #relacioanamento
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

class Clube(models.Model):
    escudo = models.ImageField(null=True, upload_to='clubes')
    nome = models.CharField(max_length=100)
    ano_fundacao = models.PositiveIntegerField(default=1900)
    divisao_atual= models.CharField(max_length=50,)
    genero = models.CharField(max_length=50,choices=GENERO_CHOICES, default='')

    #relacioanamento
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
            return self.nome


class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(null=True, upload_to='jogadores')
    posicao_principal = models.CharField(max_length=50)
    numero_camisa = models.IntegerField()
    sexo = models.CharField(max_length=50,choices=GENERO_CHOICES, default='')
    
    # relacionamento
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)
    clube = models.ForeignKey(Clube, on_delete=models.SET_NULL, related_name='sem_clube', null=True)
    

    class Meta:
        verbose_name = 'Jagador'
        verbose_name_plural = 'Jogadores'

    def __str__(self) -> str:
        return self.nome

class Competicao(models.Model):
    nome = models.CharField(max_length=100)
    tipo_disputa = models.CharField(max_length=100)
    #categoria de campeonatos
    cc = (
        ("CA", "CAMPEONATO"),
        ("COPA", "COPA"),
    )
    categoria = models.CharField(max_length=50, choices=cc, default='CA')

    class Meta:
        verbose_name = 'Competição'
        verbose_name_plural = 'Competições'

    def __str__(self) -> str:
        return self.nome

class Titulo(models.Model):
    resultado = models.CharField(max_length=100)
    ano_conquista = models.PositiveIntegerField(default=1900)
    data_exata = models.DateField()
    
    # relacionamento
    clube = models.ForeignKey(Clube, on_delete=models.SET_NULL, null=True)
    competicao = models.ForeignKey(Competicao,on_delete=models.SET_NULL, null=True)
    

    class Meta:
        verbose_name = 'Título'
        verbose_name_plural = 'Títulos'

    def __str__(self) -> str:
        return self.resultado