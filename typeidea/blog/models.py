from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    STATUS_ITEMS = [
        (0, '删除'),
        (1, '正常'),
    ]
    name = models.CharField(max_length=200, verbose_name='名称')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, default=1, verbose_name='状态')
    created_name = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    STATUS_ITEMS = [
        (0, '删除'),
        (1, '正常'),
    ]
    name = models.CharField(max_length=64, verbose_name='名称')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, default=1, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')

    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Post(models.Model):
    STATUS_ITEMS = [
        (0, '删除'),
        (1, '正常'),
        (2, '草稿'),
    ]
    title = models.CharField(max_length=200, verbose_name='标题')
    description = models.CharField(max_length=200, verbose_name='描述')
    content = models.TextField(verbose_name='正文')
    status = models.PositiveIntegerField(choices=STATUS_ITEMS, default=1, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='最后修改时间')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(Tag)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']
