# from django.shortcuts import render #FBV방식
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
from django.views.generic import ListView #게시판형으로 데이터를 가지고 오는 클래스
from django.views.generic.detail import DetailView
from .models import Post

class PostDetail(DetailView): # 디테일뷰를 상속받은 클래스.import 필수,  post_detail.html을 불러옴.
    model = Post

class PostList(ListView):
    model = Post 
    # template_name = 'blog/index.html' # 지정안해줘도 같은이름의 post_list의 templeate와 model을 조합, 지정해주고 싶을때만 사용.
    ordering = '-pk' # post_list 가 역순으로 정렬이 됨.