from django import forms
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

class ArticleForm(forms.ModelForm):
    pass

class ArticleCreateView(views.CreateView):
    model = Article
    template_name = 'articles/create.html'
    # fields = "__all__"
    success_url = reverse_lazy('list_articles_cbv')
    disabled_fields = ('title', 'content')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        for field in self.disabled_fields:
            form.fields[field].widget.attrs['disabled'] = 'disabled'

        return form

    form_class = forms.modelform_factory(Article, fields=('title', 'content'), widgets={
        'title': forms.TextInput(
            attrs={
                'class': 'abc',
            }
        )
    })

class ArticleUpdateView(views.UpdateView):
    pass

class ArticleDeleteView(views.DeleteView):
    model = Article
    template_name = 'articles/delete.html'
    form_class = forms.modelform_factory(Article, fields=('title', 'content'),)