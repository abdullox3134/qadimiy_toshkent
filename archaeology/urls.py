from django.urls import path

from .views import (archaeology_list, archaeology_detail, items_list,
                    items_detail, news_list, news_detail)

urlpatterns = [

    path('arxiv/', archaeology_list),
    path('arxiv/<int:pk>/', archaeology_detail),
    path('items/', items_list),
    path('items/<int:pk>/', items_detail),
    path('news', news_list),
    path('news/<int:pk>/', news_detail),
]
