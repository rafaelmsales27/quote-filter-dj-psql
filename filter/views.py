from django.shortcuts import get_object_or_404, render
from .models import Question

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("You are at filter")


def form(request):
    active_questions = Question.objects.filter(active=True).order_by("order")
    context = {"questions": active_questions}
    return render(request, "filter/form.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "filter/detail.html", {"question": question})
