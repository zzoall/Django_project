from django.db import models

# 모델 변경시에는 마이그레이션 해줘야함.
# Create your models here.
# DB의 테이블을 좀 더 쉽게 꺼내오기 위해 클래스 형식으로 바꿈 (mysql의 테이블 가져오기 기능)

class Post(models.Model):
    # 게시글에 필요한 필드 : 제목, 내용, 작성일, 수정일, 작성일
    title = models.CharField(max_length=50)
    content = models.TextField()
    # upload_to=경로
    # 어딘가 똑같은 폴더에 저장해주면 좋겠습니다.
    # 많이사용하는 서버는 warm,  잘 안쓰는 서버는 cold라 함. -> 출신/년/월/일 경로로 처음에 지정을 해줄게요.
    # blank=True :  SQL쿼리문으로 변환시 Null 기능
    header_img = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    # django model 이 save 될 때마다 현재날짜(date.today()) 로 갱신됨, 최종수정된 날짜시간(수정할때마다 update)
    created_at = models.DateTimeField(auto_now=True)
    # django model 이 최초 저장(insert) 시에만 현재날짜(date.today()) 를 적용 즉, 최초생성한 날짜시간
    # 아예 값 자체가 지금 시간으로 입력되어 들어감(우리가 변경할 필요 없음)
    updated_at = models.DateTimeField(auto_now_add=True)
    # 작성자는 추후 작성 예정


    def __str__(self):
        return f'[[{self.pk}] {self.title}]'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'