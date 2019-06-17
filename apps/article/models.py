# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
# Create your models here.

class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=50,verbose_name="标签名称")
    add_time = models.DateTimeField(verbose_name="加入时间", auto_now_add=True)

    class Meta:
        verbose_name="标签"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

    def get_article_nums(self):

        return self.article_set.all().count()

    get_article_nums.short_description = '文章总数'

class Article(models.Model):
    author = models.ForeignKey(User,null=True,blank=True ,verbose_name='作者')
    title = models.CharField(max_length=140, verbose_name='文章标题')
    # body = models.TextField(verbose_name='文章内容')
    body = UEditorField(verbose_name=u"文章内容", imagePath="blog/body/images/", width=1000, height=300,
                        filePath="blog/files/", default='')
    tags = models.ManyToManyField(Tag, verbose_name='标签', null=True, blank=True, )
    update_date = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    add_time = models.DateTimeField(verbose_name="加入时间", auto_now_add=True)

    class Meta:
        verbose_name="文章"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title
