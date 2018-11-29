from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from disciplina.models import Disciplina, Disc_Curso
from .models import Professor, Professor_Disc, ProfDisc_Curso, PlanoDesc
from .forms import ProfForm, ProfDiscForm
# Create your views here.


"""
Lista as disciplinas ministradas pelo professor
"""
@login_required
def professor_list(request):
    data = {}
    prof = Professor.objects.get(name=request.user)
    prof_disc = Professor_Disc.objects.filter(professor=prof)
    disc = Disciplina.objects.all()
    lista1=[] # lista para armazenar as disciplinas em prof_disc do professor X
    data['lista1']= lista1
    form = ProfDiscForm(request.POST or None, prof)
    data['professor'] = prof
    data['prof_discs'] = prof_disc
    data['disciplina'] = disc
    data['form'] = form
    for i in prof_disc:
        lista1.append(i.disciplina.id)
    if request.method == 'POST':
        if form.is_valid():
            pd = form.cleaned_data['profDisc']
            for disc in pd:
                d = Disciplina.objects.get(nome=disc)
                if d.id not in lista1:
                    profdisc= Professor_Disc(professor=prof, disciplina=d)
                    profdisc.save()
            return redirect('professor:list_prof')
    return render(request, "professor/listagem.html", data)


#Plano de aula da disciplina do professor
@login_required
def professor_listPlan(request, discId):
    data = {}
    prof = Professor.objects.get(name=request.user)
    disc = Disciplina.objects.get(id=discId)
    plan = PlanoDesc.objects.filter(profDiscCurso__profDisc__id=discId)
    data['planos']=plan
    data['disc']=Professor_Disc.objects.get(disciplina=disc, professor=prof)
    print('**************************************')
    for p in plan:
        print(p)
    print('***************************************')
    return render(request, "professor/listagemPlano.html", data)


#remover
def professor_new(request):
    data = {}
    form = ProfForm(request.POST or None)

    if form.is_valid():
        print('yesssssssssssssssssssssssss')
        print(request.POST)
        profName = form.cleaned_data['profName']
        print(profName)
        profEmail = form.cleaned_data['profEmail']
        disc = form.cleaned_data['profDisc']
        #Prof = Professor
        Prof= Professor(name=profName,email=profEmail)
        print(Prof)
        Prof.save()
        for d in disc:
            print('discicplimaaaaaaaaaaaa')
        #disc = Disciplina.objects.get(id=disc)
        # pd = Professor_Disc(professor=Prof, disciplina=disc)
        # pd.save()
        return redirect('professor:list_prof')
    if request.method == 'POST':
        print(request.POST)

    data['form'] = form
    data['disciplinas'] = Disciplina.objects.all()
    return render(request, 'professor/prof_form.html', data)

#REVISARRRRR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@login_required
def update_professor(request, name):
    data={}
    prof = Professor.objects.get(name=name)
    usuario = User.objects.get(username=request.user)
    form = ProfForm(request.POST or None)
    print("**************************************")
    print(request.POST)
    print(request.user.username)
    data['prof']=prof
    data['form']=form
    if form.is_valid():
        profName = form.cleaned_data['profName']
        prof.name = profName

        print('professo:')
        print(prof.name)
        print('usuario:')
        print(request.user)
        print(usuario)
        print(request.POST)

        # prof.save()
        usuario.save()
        print(profName)
        return redirect('professor:list_prof')

    return render(request, 'professor/prof-form.html', data)


@login_required
def new_plan(request, profdisc):
    data = {}
    pd = Professor_Disc.objects.get(id=profdisc)
    data['profDisc']=pd
    print("*********************************************")

    print("*********************************************")
    #form = Plan_DescForm(request.POST or None, profdisc)

    return render(request, 'professor/new_plan.html', data)






