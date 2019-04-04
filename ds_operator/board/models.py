from django.db import models


# Board Model
class Board(models.Model):
    updated_at = models.DateTimeField(auto_now=True) # 현재시각
    title = models.CharField(max_length=50) # 제목
    body = models.TextField() # 내용

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]
