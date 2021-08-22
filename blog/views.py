from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Chapter,Arc,Author,Comment
from django.views.generic import ListView , DetailView
# from django.views.generic.edit import FormMixin
from django.urls import reverse


from django.core import serializers

# from .forms import CommentForm

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

        author = Author.objects.get(user=context['chapter'].author)


        context['arcs'] = Arc.objects.all().annotate(chapter_count=Count('chapter_arc'))
        context['recent_chapters'] = Chapter.objects.all()[:3]
        context['author'] = author
        context['comments'] = Comment.objects.filter(chapter=self.get_object())
        # context['replies'] = Comment.objects.filter(chapter=self.get_object(), replaying_to = not None)
        return context


        return redirect(reverse('blog:chapter_detail' , kwargs={'slug':self.get_object().slug}))




def add_comment(request):
    print('==========================================================================yes')
    print(request.GET.get('chapter_id'))
    if request.is_ajax and request.method == 'GET':
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++yes')
        comment = Comment.objects.create(
            chapter = Chapter.objects.get(id = int(request.GET.get('chapter_id'))),
            name = request.GET.get('name'),
            email = request.GET.get('email'),
            body = request.GET.get('comment')

        )
        comment.save()
        com = {'id': comment.id, 'name': comment.name, 'body': comment.body, 'created_on': comment.created_on}
        return JsonResponse({'comment': com}, status=200)
    return JsonResponse({'error': error}, status=500)
