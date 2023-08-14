from django.db import models
# 과제 1. 사용자 회원가입 엔드포인트
# 이메일과 비밀번호로 회원가입할 수 있는 엔드포인트를 구현해 주세요.
# 이메일과 비밀번호에 대한 유효성 검사를 구현해 주세요.
# 이메일 조건: @ 포함
# 비밀번호 조건: 8자 이상
# 비밀번호는 반드시 암호화하여 저장해 주세요.
# 이메일과 비밀번호의 유효성 검사는 위의 조건만으로 진행해 주세요. 추가적인 유효성 검사 조건은 포함하지 마세요.
class User(models.Model):
    user_email = models.CharField(max_length=32, unique=True)
    user_password = models.CharField(max_length=128)
