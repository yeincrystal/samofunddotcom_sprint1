from django.db import models
from django.contrib.auth.models import User
import pandas as pd

class Samofund(models.Model):
    #author = models.CharField(max_length=100) #필요없음 
    #foreignKey로 사용되는 변수는 나중에 데이터 꺼내올 때 지정해주는 이름 (table column명과 다를 수 있어)
    #on_delete=models.CASCADE : User가 사라지면 그 유저에 연동되었는 모든 것들 CASCADE처럼 다 지워버림 ! (optional)
    company_name = models.TextField(null=True) #non-nullable이 defaul라서 nullable로 바꿔주기 
    fund_name = models.TextField(null=True)
    initial_date = models.DateTimeField(null=True)
    m_strategy = models.TextField(null=True)
    pbs = models.TextField(null=True)
    setting = models.TextField(null=True)
    total_net_profit = models.TextField(null=True)
    modified_base = models.TextField(null=True)
    june_perf = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    week_perf = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    pday_perf = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    perf_2019 = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    year_conv_perf = models.DecimalField(null=True, decimal_places=2, max_digits=5)
    cum_perf = models.DecimalField(null=True, decimal_places=2, max_digits=5)

    def __str__(self):
        return f'{self.fund_name},{self.pbs}'



# Create your models here.
class Portfolios(models.Model):
    #author = models.CharField(max_length=100) #필요없음 
    #foreignKey로 사용되는 변수는 나중에 데이터 꺼내올 때 지정해주는 이름 (table column명과 다를 수 있어)
    #on_delete=models.CASCADE : User가 사라지면 그 유저에 연동되었는 모든 것들 CASCADE처럼 다 지워버림 ! (optional)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False) #non-nullable이 defaul라서 nullable로 바꿔주기 
    body = models.TextField()
    image = models.ImageField(upload_to='portfolio',null=True) #이미지 자체를 다 저장하는 게 아니라(binary numbers), 이미지가 들어있는 '경로를' 저장해두는 것 
    created_at = models.DateTimeField()
    #포트폴리오 테이블에 추가하는 것처럼 보이지만, 별도의 테이블을 만드는 거야 
    #Portfolio.liked_users로 코딩해서 가져오려고 이름을 이렇게 지정한거지, 꼭 이 이름으로 할 필요 없엉 
    #User든지 Portfolio든지 어느 한 곳에만 추가하면 됨 (자동으로 다대다 )
    liked_users = models.ManyToManyField(User, related_name='liked_posts') #장고가 알아서 중간 테이블 만들어줌 -> User.liked_posts

    def __str__(self):
        #post.user인데 self가 instance니까 self.user 
        #이제 nullable이 되었으니까, 두가지 상황으로 나눠서 지정해줘야 함. 
        if self.user:
            return f'{self.user.get_username()}: {self.body}'
        #굳이 else 안써도 되니까 구태어 쓰지 않음 ! 
        return f'{self.body}'