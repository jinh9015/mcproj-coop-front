#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'choe', # DB이름
#        'USER': 'root', # DB 유저 아이디
#        'PASSWORD': 'ssd78603183', # 비밀번호
#        'HOST': 'localhost', # 또는 자신이 설정한 호스트
#        'PORT': '3306', # db가 연결된 포트(여기서는 기본 포트)
#    }
#}

SECRET_KEY = 's!e!su8fn9ydb4m7hbkm07*d6y_@5ljhge$uiz)qx@b=3nm95m'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'coop-mysql',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '172.31.23.7',
        'PORT': '3307',
    }
}
