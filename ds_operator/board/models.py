from django.db import models

class Board(models.Model):
    file = models.FileField(null=True)
    title = models.CharField(max_length=10, blank=True) # 제목
    updated_at = models.DateTimeField(auto_now=True) # 현재시각

    def __str__(self):
        return self.title