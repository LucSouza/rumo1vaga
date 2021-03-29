from django.shortcuts import render, redirect
from quiz.base.models import Pergunta
from quiz.base.models import Aluno
from quiz.base.forms import AlunoForm

# Create your views here.

def home(req):
  if req.method == "POST":
    #Usuario existe
    email = req.POST['email']
    try:
      aluno = Aluno.objects.get(email=email)
    except Aluno.DoesNotExist:
      #Usuario não existe
      form = AlunoForm(req.POST)
      if form.is_valid():
          aluno = form.save()
          req.session['aluno_id'] = aluno.id
          return redirect('/perguntas/1')
      else:
          contexto = {'form': form}
          return render(req, 'base/home.html', contexto)
    else:
        req.session['aluno_id'] = aluno.id
        return redirect('/perguntas/1')
  return render(req, 'base/home.html')

def perguntas(req, indice):
  pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice - 1]
  contexto = {'indice_questao': indice, 'pergunta': pergunta}
  return render(req, 'base/game.html', context=contexto)

def classificacao(req):
  return render(req, 'base/classificacao.html')