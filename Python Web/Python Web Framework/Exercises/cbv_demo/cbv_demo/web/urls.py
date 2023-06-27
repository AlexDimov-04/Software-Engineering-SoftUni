from django.urls import path
from cbv_demo.web.views import ArticlesListView, RedirectArticlesView
from cbv_demo.web.views import list_articles


urlpatterns = [
    path('', list_articles, name='list_articles'),
    path('cbv/', ArticlesListView.as_view(), name='list_articles_cbv'),
    path('cbv/<int:pk>/', ArticlesListView.as_view(), name='list_articles_cbv'),
    path('redirect-to-articles/', RedirectArticlesView.as_view(), name='redirect_to_articles'),
]