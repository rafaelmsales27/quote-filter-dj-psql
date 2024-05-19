from django.shortcuts import get_object_or_404, render
from .models import Question
from .forms import QuestionForm

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("You are at filter")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "filter/detail.html", {"question": question})


def form(request):
    active_questions = Question.objects.filter(active=True).order_by('order')
    forms = []  # List to store form instances
    for question in active_questions:
        form = QuestionForm(question=question)  # Create form for each question
        forms.append(form)

    if all(form.is_valid() for form in forms):  # Check validity if submitting form
        # Handle form submission logic (optional)
        pass

    context = {'forms': forms}
    return render(request, "filter/form.html", context)
