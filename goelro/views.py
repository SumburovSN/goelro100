import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.conf import settings

from . import info, forms

# Create your views here.


def show(request):
    return HttpResponse('Hello Goelro!')


def index(request):
    return render(request, 'index.html', {})


def form_handler(request):
    full_response = 'Welcome to %s' % request.path
    full_response += '<br>' + 'Host is %s' % request.get_host()
    full_response += '<br>' + 'Полный путь %s' % request.get_full_path()
    full_response += '<br>' + 'Защищено: %s' % request.is_secure()
    full_response += '<br>' + 'Method: %s' % request.method
    full_response += '<br>' + 'Data: %s' % request.headers
    return HttpResponse(full_response)
    # if request.POST:
    #     full_response = response1 + '<br>' + response2 + '<br>' + response3 + '<br>' + response4 + '<br>'
    #     return HttpResponse('Request is POST')
    # else:
    #     return HttpResponse('Request is GET')


# def base(request):
#     return render(request, 'start.html', {})

def base(request):
    html = 'start.html'
    titles = info.get_titles()
    nav = info.get_nav()
    authors = info.authors
    authors_names = info.author_short()
    context = {
        'titles': titles,
        'nav': nav,
        'authors': authors,
        'authors_names': authors_names,
    }
    return render(request, html, context)


def article(request, number):
    html = 'article' + str(number) + '.html'
    title = info.articles[number-1][0]
    authors = info.articles[number-1][1]

    titles = info.get_titles()
    nav = info.get_nav()

    author_list = []
    for i in authors:
        author_list.append(info.authors[i])
    authors_names = info.author_short()
    context = {
        'title': title,
        'titles': titles,
        'nav': nav,
        'authorList': author_list,
        'authors_names': authors_names,
    }

    return render(request, html, context)


def audios(request):
    html = 'audio.html'

    titles = info.get_titles()
    nav = info.get_nav()
    authors_names = info.author_short()

    path = settings.MEDIA_ROOT

    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

    context = {
        'titles': titles,
        'nav': nav,
        'files': files,
        'authors_names': authors_names,
    }

    return render(request, html, context)


def audio(request, number):
    path = "./media/audio/"
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    file_name = files[number]
    try:
        fname = os.path.join(path, file_name)
        f = open(fname, "rb")
        response = HttpResponse(f.read())
        response['Content-Type'] = 'audio/mp3'
        response['Content-Length'] = os.path.getsize(fname)
        return response
    except:
        return HttpResponse()


def quizzes(request):
    html = 'quizzes.html'

    titles = info.get_titles()

    nav = info.get_nav()
    authors_names = info.author_short()

    context = {
        'titles': titles,
        'quizzes': info.quizzes,
        'nav': nav,
        'authors_names': authors_names,
    }

    return render(request, html, context)


def quiz(request, number):
    html = 'quiz.html'
    nav = info.get_nav()
    authors_names = info.author_short()

    if number == 1:
        raw = info.quiz1
    if number == 2:
        raw = info.quiz2

    quiz = []
    verify = []
    i = 1
    for question in raw:
        name = 'question' + str(i)
        quiz.append(
            {'name': name,
             'question': question[0],
             'options': question[1],
             'check': "",
             'chosen': "",
             }
        )
        verify.append(question[2])
        i += 1

    context = {
        'nav': nav,
        'section': number,
        'quiz': quiz,
        'Verified': False,
        'authors_names': authors_names,
    }
    if request.POST:
        i = 1
        right = 0
        for question in quiz:
            name = 'question' + str(i)
            if name not in request.POST:
                question['check'] = False
            elif int(request.POST[name]) == verify[i-1]:
                question['check'] = True
                question['chosen'] = int(request.POST[name])
                right += 1
            else:
                question['check'] = False
                question['chosen'] = int(request.POST[name])
            i += 1

        ratio = round((right / len(quiz) * 100), 1)
        context = {
            'nav': nav,
            'section': number,
            'quiz': quiz,
            'Verified': True,
            'ratio': ratio,
            'authors_names': authors_names,
        }

        return render(request, html, context)
    else:
        return render(request, html, context)


def references(request):
    html = 'references.html'
    titles = info.get_titles()
    nav = info.get_nav()
    authors_names = info.author_short()
    context = {
        'titles': titles,
        'nav': nav,
        'authors_names': authors_names,
    }

    return render(request, html, context)


class QuizFormView(generic.TemplateView):
    questionnaire = forms.Quiz

    def post(self, request):
        form = forms.Quiz(request.POST)

        context = {
            'questionnaire': form
        }
        data = request.POST['question']
        return HttpResponse(data)
        # if form.is_valid():
        #     data = form.cleaned_data
        #     return HttpResponse(data.items())
        # else:
        #     return render(request, 'quiz.html', context)

    def get(self, request):

        context = {
            'questionnaire': self.questionnaire
        }
        return render(request, 'quiz_test.html', context)


def test1_check(request):
    response = 'Запрос: %s' % request.GET['id_question']
    return HttpResponse(response)
