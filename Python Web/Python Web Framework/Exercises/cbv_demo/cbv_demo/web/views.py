from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from cbv_demo.web.models import Article


def list_articles(request):
    context = {
        'articles': Article.objects.all()
    }

    return render(request, 'articles/list.html', context=context)

# class ArticlesListView(views.View) :
#     def get(self, request):
        # context = {
        #     'articles': Article.objects.all()
        # }

        # return render(self.request, 'articles/list.html', context=context)
    
# class ArticlesListView(views.TemplateView):
#     template_name = 'articles/list.html'
#     extra_context = {
#         'articles': Article.objects.all()
#     }

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['articles'] = Article.objects.all()
    #     return context

class RedirectArticlesView(views.RedirectView):
    url = reverse_lazy('list_articles_cbv')

class ArticlesListView(views.ListView):


    template_name = 'articles/list.html'
    model = Article

    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get('search', '')
        queryset = queryset.filter(title__icontains=search)
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context
    
class ArticleDetailView(views.DetailView):
    model = Article
    template_name = 'articles/detail.html'
