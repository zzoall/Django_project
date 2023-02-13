# from django.shortcuts import render
# from .models import Post

# Create your views here.
# V (view) - 화면에 출력되는 부분
 
# 1) Function Based View 방식
# def index(request):
#     return render(
#         request,
#         'blog/index.html' # request는 클라이언 상태(404, 200 등)
#     )

# def index(request):
#     posts = Post.objects.all() # 1. 쿼리로 데이터를 모두 가져옵니다
#     # 가져온 데이터는 어디에 뿌려야 하나요? Templates로 보내야겠죠
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts':posts,
#         }
#     )

# def index2(request):
#     return render(
#         request,
#         'index2.html'
#     )



# 2) Class Based Views 방식
from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post 
    # template_name = 'blog/index.html' # 지정안해줘도 같은이름의 post_list가 연결되어있으며, 지정해주고 싶을때만 사용.
    # ordering = '-pk' 