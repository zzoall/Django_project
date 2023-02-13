from django.db import models

# Create your models here.
# DB의 테이블을 좀 더 쉽게 꺼내오기 위해 클래스 형식으로 바꿈 (mysql의 테이블 가져오기 기능)

class Post(models.Model):
    # 게시글에 필요한 필드 : 제목, 내용, 작성일, 수정일, 작성일
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True) # 최종수정된 날짜시간(수정할때마다 update)
    updated_at = models.DateTimeField(auto_now_add=True) # 최초생성한 날짜시간
    # 작성자는 추후 작성 예정


    def __str__(self):
        return f'[[{self.pk}] {self.title}]'
    