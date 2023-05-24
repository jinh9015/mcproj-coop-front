from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm

def index(request):
    """
    coopplatform 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'coopplatform/question_list.html', context)

def detail(request, question_id):
    """
    coopplatform 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'coopplatform/question_detail.html', context)

def answer_create(request, question_id):
    """
    coopplatform 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():                         # 폼 유효성 검사
            answer = form.save(commit=False)        # commit=False =>임시저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('platform:detail', question_id=question.id)
    else:                                           # request.method 가 GET 인 경우
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'coopplatform/question_detail.html', context)

def question_create(request):
    """
    coopplatform 게시글 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():                         # 폼 유효성 검사
            question = form.save(commit=False)      # commit=False =>임시저장
            question.create_date = timezone.now()
            question.save()
            return redirect('platform:index')
    else:                                           # request.method 가 GET 인 경우
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'coopplatform/question_form.html', context)