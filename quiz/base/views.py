from django.shortcuts import render
from quiz.base.models import Pergunta
# Create your views here.

def home(req):
  return render(req, 'base/home.html')

def perguntas(req, indice):
  pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice - 1]
  contexto = {'indice_questao': indice, 'pergunta': pergunta}
  return render(req, 'base/game.html', context=contexto)

def classificacao(req):
  return render(req, 'base/classificacao.html')