from django.shortcuts import render
from .models import Chapter,Arc
from django.views.generic import ListView , DetailView

from django.db.models import Count


# Create your views here.

class ChapterList(ListView):
    model = Chapter
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chapter_list"] =  Chapter.objects.filter(active=True)

        return context



class ChapterDetail(DetailView):
    model = Chapter


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        self.object.add_view()
        self.object.save()



        context['arcs'] = Arc.objects.all().annotate(chapter_count=Count('chapter_arc'))
        context['recent_arcs'] = Arc.objects.all()[:3]
        return context
