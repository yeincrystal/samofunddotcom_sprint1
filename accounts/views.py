from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def sign_up(request):
    context = {}
    #POST Method 
    if request.method == "POST":
        #if문 여러줄로 표현하려면 괄호를 꼭 써주기 !! 
        if(request.POST['username'] and
        request.POST['password'] and 
        request.POST['password'] == request.POST['password_check']):
            #User라는 클래스에다가 한 줄 추가하는 게 다야, 근데 User모델은 조금 다름 
            #암호화나 보안강화를 위해서 별도의 방법을 통해서 User 테이블에 사용자 추가해줘야 함 .
            new_user = User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password'],
            )
            #save도 따로 필요없음!! 

            #회원가입이 끝나면 바로 로그인 시켜주는 기능 
            #auth안에 로그인 기능이 들어있음.
            auth.login(request, new_user)
            return redirect('portfolio:index')

        else:
            context['error'] = "아이디와 비밀번호를 다시 확인해주세요"
    #어차피 return하면 이프 문이 끝나버리니까 else생략하고 이렇게 끝! 
    return render(request, 'accounts/sign_up.html', context)

def login(request):
    context = {}

    if request.method == "POST":
        if request.POST['username'] and request.POST['password']:
            #User가 이미 등록된 사용자인지 확인하는 코드 -> User를 리턴해줌 
            user = auth.authenticate(
                request,
                username=request.POST['username'],

                password=request.POST['password']
            )
#POST 방식으로 accouts/login으로 request가 날아가고 Request.body 안에 데이터가 담겨서 보내집니다. 

            #User가 성공적으로 리턴되고 나면 로그인 시켜주기 
            if user is not None:
                auth.login(request, user)
                return redirect('portfolio:index')
            else:
                context['error']="아이디와 비밀번호를 다시 확인해주세요"
        else:
            context['error']="아이디와 비밀번호를 모두 입력해주세요"
    return render(request, 'accounts/login.html', context)


def logout(request):
    if request.method == "POST":
        auth.logout(request)

    return redirect('portfolio:index')
