from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from common.forms import UserForm
# @csrf_token
def signup(request):
    """
    회원가입
    """
    if request.method == "POST":    # POST 요청 -> 입력받은 데이터로 새 사용자 생성
        form = UserForm(request.POST)
        # 회원가입 필드값 모두 입력, 비번 두개 동일, 비번 생성 규칙.. 검사
        if form.is_valid():
            form.save()
            # form.cleaned_data.get : 입력받은 값을 얻기 위한 함수
            # 로그인 시 필요한 아이디, 비번 얻기 위해 사용
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # authenticate,login 함수로 가입 후 자동로그인
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:   # GET 요청 -> commom/signup.html 화면 반환
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})