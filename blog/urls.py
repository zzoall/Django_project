from django.urls import path, include
from . import views

# blog 앱 내부 경로를 지정하는 부분
# urlpatterns = [
#     path('', views.index),# /blog 뒤에 달린 주소가 없음.
#     path('index2/', views.index2)
# ]

urlpatterns = [
    # path('', views.index), # FBV
    path('', views.PostList.as_view()),  # CBV post_list.html을 기본 템플릿으로 찾게 됩니다
    path('<int:pk>/', views.PostDetail.as_view()), # 어디출신인지 -> views, 사용할클래스-> PostDetail , 내가 만든 포스트1, 포스트2 ... 5까지 다나옴.
]

