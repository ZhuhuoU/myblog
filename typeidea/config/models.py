from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Link(models.Model):
    STATUS_ITEMS = [
        (0, '删除'),
        (1, '正常'),
    ]
    title = models.CharField(max_length=50, verbose_name='标题')
    href = models.URLField(verbose_name='链接')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    created_name = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6),
                                         range(1, 6)), verbose_name='搜索权重',
                                         help_text='权重越高，展示顺序越靠前')
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')

    class Meat:
        verbose_name = verbose_name_plural = '友链'


class SideBar(models.Model):
    STATUS_ITEMS = [
        (0, '隐藏'),
        (1, '展示'),
    ]
    TYPE_ITEMS = [
        (0, 'HTML'),
        (1, '最新文章'),
        (2, '最热文章'),
        (3, '最新评论'),
    ]
    title = models.CharField(max_length=50, verbose_name='标题')
    type = models.PositiveIntegerField(choices=TYPE_ITEMS, default=0, verbose_name='类型')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, default=1, verbose_name='栏目')
    content = models.CharField(max_length=500, blank=True, verbose_name='评论内容',
                               help_text='如果设置的不是HTML类型，评论可为空')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')

    class Meta:
        verbose_name = verbose_name_plural = '侧栏'