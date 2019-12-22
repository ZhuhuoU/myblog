from django.db import models

# Create your models here.
from blog.models import Post


class Comment(models.Model):
    STATUS_ITEMS = [
        (0, '删除'),
        (1, '正常'),
    ]
    target = models.ForeignKey(Post, on_delete=models.DO_NOTHING, verbose_name='评论目标')
    nickname = models.CharField(max_length=12, verbose_name='昵称')
    email = models.EmailField(verbose_name='邮箱')
    website = models.URLField(verbose_name='网站')
    content = models.CharField(max_length=500, verbose_name='内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '评论'
