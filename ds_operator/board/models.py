from django.db import models

class Board(models.Model):
    file = models.FileField(null=True)
    title = models.CharField(max_length=10, blank=True) # 제목
    updated_at = models.DateTimeField(auto_now=True) # 현재시각
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    blank=True,
                                    related_name='like_user_set',
                                    through='Like')
    pwd = models.CharField(max_length=10, null=False, default="0000") # 비밀번호

    def __str__(self):
        return self.title

    def like_count(self):
        return self.like_user_set.count()

class Like(models.Model):
    post = models.ForeignKey(Post)