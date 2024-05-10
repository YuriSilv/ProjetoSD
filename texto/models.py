from django.db import models
from django.utils import timezone
from equipe.models import Pesquisador
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
#from ..equipe.models import Pesquisador

# Create your models here.

def validar_extensao_texto(value):
    formatos = ['pdf', 'docx']
    ext = str(value).split('.')[-1]
    if ext.lower() not in formatos:
        raise ValidationError(f'O arquivo de formato {ext} é inválido. Favor subir um .pdf ou .docx')

class Monografia(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='titulo')
    
    autor = models.OneToOneField(Pesquisador, 
                                 on_delete=models.CASCADE, 
                                 related_name='autor_monografias')
    
    orientador = models.ForeignKey(Pesquisador, 
                                   on_delete=models.CASCADE, 
                                   related_name='orientador_monografias', 
                                   limit_choices_to={'cargo':'PROFESSOR'})
    
    coorientador = models.ForeignKey(Pesquisador, 
                                     on_delete=models.CASCADE, 
                                     related_name='coorientador_monografias', 
                                     limit_choices_to={'cargo':'PROFESSOR'})
    
    resumo = models.TextField(verbose_name='resumo')

    palavras_chave = models.CharField(max_length=255, 
                                      verbose_name='palavras chaves')

    data_entrega = models.DateTimeField(default=timezone.now, 
                                        verbose_name='data')

    arquivo = models.FileField(upload_to='', 
                               verbose_name='uploads',
                               validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx']), 
                                           validar_extensao_texto],
                               help_text="Suba somente PDF's ou Docx's")
    
    banca = models.ManyToManyField(Pesquisador, 
                                   blank=True, 
                                   null=True, 
                                   verbose_name='banca', 
                                   limit_choices_to={'cargo':'PROFESSOR', 'cargo':'TECNICO'})
    
    nota_final = models.FloatField(max_length=3, 
                                   blank=True, 
                                   null=True, 
                                   validators=[MinValueValidator(0.0), MaxValueValidator(100)],
                                   verbose_name='nota final')

    area_concentração = models.CharField(max_length=255, 
                                         blank=True, 
                                         null=True, 
                                         verbose_name='áreas pesquisa')


    def __str__(self):
        return f'{self.titulo}'