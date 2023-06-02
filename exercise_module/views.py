from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from exercise_module.models import Exercises, IsSolve
from lessons_module.forms import CalculationForm
from lessons_module.models import Lessons


class ExerciseView(View):
    def get(self, request, pk):
        form = CalculationForm()
        context = {
            'exercise': Exercises.objects.filter(pk=pk).first(),
            'form': form
        }
        return render(request, 'exercise_module/exercise.html', context)

    def post(self, request: HttpRequest, pk):
        exercise = Exercises.objects.filter(pk=pk).first()
        form = CalculationForm(request.POST)
        context = {
            'exercise': exercise,
            'form': form,
        }
        if form.is_valid():
            result = form.cleaned_data.get('result')
            if result == exercise.result:
                context['is_True'] = 'yes'
                is_solve = IsSolve.objects.filter(user=request.user, exercise=exercise).first()
                if is_solve is None:
                    new_solve = IsSolve(user=request.user, exercise=exercise)
                    new_solve.save()
                context['form'] = None
                lesson = Lessons.objects.filter(exercises__pk=pk).first()
                next_exercise = lesson.exercises_set.filter(pk=pk + 1).first()
                if next_exercise is not None:
                    context['next_exercise'] = next_exercise
                else:
                    next_lesson = Lessons.objects.filter(pk=exercise.lesson.pk + 1).first()
                    if next_lesson is not None:
                        context['next_lesson'] = next_lesson
            else:
                context['is_True'] = 'no'
        return render(request, 'exercise_module/exercise.html', context)
