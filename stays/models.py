from django.db import models

# Create your models here.

class LabUser(models.Model):
    user_name = models.CharField(max_length=32) # ユーザ名
    user_state = models.CharField(max_length=32) # ユーザの状態
    user_grade = models.CharField(max_length=32) # ユーザの学年
    user_login_date = models.DateTimeField() # 最終操作時間
