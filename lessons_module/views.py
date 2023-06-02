from django.http import HttpRequest
from django.views.generic import DetailView, TemplateView
from django.views.generic.list import ListView

from exercise_module.models import IsSolve
from .models import Lessons, IsRead


class ListLessons(ListView):
    template_name = 'lessons_module/lessons_list.html'
    model = Lessons
    context_object_name = 'lessons'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListLessons, self).get_context_data(object_list=None, **kwargs)
        context['is_read'] = IsRead.objects.filter(user=self.request.user)
        context['is_solve'] = IsSolve.objects.filter(user=self.request.user)
        return context


class DetailLesson(DetailView):
    template_name = 'lessons_module/detail_lesson.html'
    model = Lessons
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        context = super(DetailLesson, self).get_context_data()
        request: HttpRequest = self.request
        is_read = IsRead.objects.filter(user=request.user, lesson=context['lesson']).first()
        if is_read is None:
            new_read = IsRead(user=request.user, lesson=context['lesson'])
            new_read.save()
        lessons = Lessons.objects.all()
        context['lessons'] = lessons
        next_exercise = lessons.filter(pk=self.kwargs.get('pk')).first().exercises_set.first()
        context['next_exercise'] = next_exercise

        return context


class ListLessonComponentView(TemplateView):
    template_name = 'lessons_module/component/list_lesson_component.html'

    def get_context_data(self, **kwargs):
        context = super(ListLessonComponentView, self).get_context_data(**kwargs)
        context['lessons'] = Lessons.objects.all()
        context['is_read'] = IsRead.objects.filter(user=self.request.user)
        context['is_solve'] = IsSolve.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
