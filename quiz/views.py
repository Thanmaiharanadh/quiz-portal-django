from django.shortcuts import render, redirect
from .models import Quiz, Question


def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, "quiz/quizlist.html", {
        "quizzes": quizzes
    })


def quiz_detail(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.question_set.all()

    if request.method == "POST":
        score = 0

        for question in questions:
            selected = request.POST.get(f"question_{question.id}")

            if selected:
                if int(selected) == question.correct_option:
                    score += 1

        return render(request, "quiz/result.html", {
            "quiz": quiz,
            "score": score,
            "total": questions.count()
        })

    return render(request, "quiz/quiz_detail.html", {
        "quiz": quiz,
        "questions": questions
    })