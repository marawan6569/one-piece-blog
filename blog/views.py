from django.shortcuts import render
from .models import Chapter
from django.views.generic import ListView , DetailView

# Create your views here.

class ChapterList(ListView):
    model = Chapter
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chapter_list"] =  Chapter.objects.filter(active=True)

        return context


# views increment
def update_views_count(chapter_id):
    views_count = int(Chapter.objects.get(id=chapter_id).views)
    new_views_count = views_count + 1
    chapter = Chapter(id=chapter_id)
    chapter.views = new_views_count
    chapter.save()

class ChapterDetail(DetailView):
    model = Chapter


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        self.object.add_view()
        self.object.save()



        # context['categories'] = Category.objects.all().annotate(post_count=Count('post_category'))
        # context['recent_posts'] = Post.objects.all()[:3]
        return context



# def all_chapters(request):
#     chapters = Chapter.objects.filter(active=True)
#     context = {'chapters': chapters}
#     return render(request, 'blog/all_chapters.html', context)

#
# def chapter_detail(request, id):
#     pass
