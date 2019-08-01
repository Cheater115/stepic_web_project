from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Question, Answer
from .forms import AskForm, AnswerForm

# Test views
def test(request, *args, **kwargs):
    return HttpResponse('OK')

# Paginator for questions
def paginate_questions(request, qs):
    limit = 10
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

# View for main page: show new questions(/, /new/)
def new_questions(request):
    question_list = Question.objects.new()
    questions = paginate_questions(request, question_list)
    return render(request, 'new.html', {
        "questions": questions,
    })

# View for page with popular questions(/popular/)
def popular_questions(request):
    question_list = Question.objects.popular()
    questions = paginate_questions(request, question_list)
    return render(request, 'popular.html', {
        "questions": questions,
    })

# View for work with specific question
def question_details(request, id = None):
    question = get_object_or_404(Question, id = id)
    answers = question.answer_set.all()
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            answer = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AnswerForm(initial = {'question': id})
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        'form': form,
    })

# View for ask new question
def ask_question(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'baseform.html', {
        'form': form,
    })