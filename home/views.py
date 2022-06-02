
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

gplayer_name: str
gplayer_lname: str
# creating an object of model to access its fields
detail = Player()
# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')
    # return HttpResponse("this is home page ")


def c_quizpage(request):
    # taking input from html page and accessing them in another html page
    player_name = request.POST['name']
    player_lname = request.POST['lastname']
    # detail = Player()
    detail.name = request.POST['name']
    # detail.name.save()
    detail.lastname = request.POST['lastname']
    # detail.lastname.save()
    detail.save()
    print(detail.name)
    print(detail.lastname)

    Questionss = Questionsds.objects.all()
    return render(request, 'c_quizpage.html', {'pname': player_name, 'plname': player_lname, 'Questionss': Questionss})


def ds_quizepage(request):
    ds_questions = Questions.objects.all()
    if request.method == 'POST':
        print(request.POST)
        Questionss = Questionsds.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in Questionss:
            total += 1
            print(request.POST.get(q.Question))
            print(q.Answer)
            print()
            if q.Answer == request.POST.get(q.Question):
                score += 1
                correct += 1
            else:
                wrong += 1
        percent = int((score / total) * 100)
        percentage1 = percent
        c_score = score
        c_wrong = wrong
        print(c_score)
        print(c_wrong)
        detail.c_score = score
        # detail.percentage += percent
        detail.save()
    return render(request, 'ds_quizepage.html', {'Questionss': ds_questions})


def dbms_quizepage(request):
    dbms_questions = Questionsdbms.objects.all()

    if request.method == 'POST':
        print(request.POST)
        Questionss = Questions.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in Questionss:
            total += 1
            print(request.POST.get(q.Question))
            print(q.Answer)
            print()
            if q.Answer == request.POST.get(q.Question):
                score += 1
                correct += 1
            else:
                wrong += 1
        percent = int((score / total) * 100)
        ds_score = score
        ds_wrong = wrong
        detail.ds_score = score
        # percentage1 = percentage1 + percent
        # detail.percentage += percent
        detail.save()
    return render(request, 'dbms_quizepage.html', {'Questionss': dbms_questions})


def result(request):
    # player_name = request.POST['name']
    # player_lname = request.POST['lastname']
    # total_score = request.POST['score']

    if request.method == 'POST':
        print(request.POST)
        Questionss = Questionsdbms.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in Questionss:
            total += 1
            print(request.POST.get(q.Question))
            print(q.Answer)
            print()
            if q.Answer == request.POST.get(q.Question):
                score += 1
                correct += 1
            else:
                wrong += 1
        percent = int((score / total) * 100)
        dbms_score = score
        print(dbms_score)
        dbms_wrong = wrong
        detail.dbms_score = score
        # percentage1 = percentage1 + percent
        # percentage1 /= 3
        # detail.percentage = percentage1
        detail.save()
        c_score = detail.c_score
        ds_score = detail.ds_score
        dbms_score = detail.dbms_score
        c_score1 = (c_score / 20) * 100
        ds_score2 = (ds_score/10)*100
        dbms_score3 = (dbms_score/20)*100

        percent = (c_score1 + ds_score2 + dbms_score3) / 3
        percent = round(percent, 2)

        print(c_score)
        print(ds_score)
        print(dbms_score)
        print(percent)

        detail.percentage = percent
        detail.save()

        Player1 = Player.objects.latest('id')
        context = {
            'c_score': c_score,
            'ds_score': ds_score,
            'dbms_score': dbms_score,
            'percent': percent
        }
    # creating a list of class variables
    # questionlist = [Questions1, Questions2, Questions3, Questions4, Questions5, Questions6, Questions7, Questions8, Questions9, Questions10]
    # Questionss = Questions.objects.all()
    return render(request, 'result.html', {'player': Player1, 'context': context})