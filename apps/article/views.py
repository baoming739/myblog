# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Article,Tag


# Create your views here.

class HomeView(View):
    def get(self,request):
        articles=Article.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        #objects = ['john', 'edward', 'josh', 'frank']

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(articles,5, request=request)

        article = p.page(page)

        return render(request,"home.html",
                      context={
                          "articles":articles,
                          "article":article
                      }
                      )


class ArticleView(View):
    def get(self,request):
        articles = Article.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # objects = ['john', 'edward', 'josh', 'frank']

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(articles, 5, request=request)

        article = p.page(page)
        return render(request,"article.html",context={
            "article":article
        })

class ArticleDetialView(View):
    def get(self,request,article_id):
        article = Article.objects.get(id=article_id)

        return render(request,"article_detail.html",context={
            "article":article,
            "article_id":article_id
        })

class TagsView(View):
    def get(self,request):
        tags = Tag.objects.all()
        # articles_nums = Tag.get_article_nums()
        # print articles_nums
        return render(request,"tags.html",context={
            "tags":tags,
            # "articles_nums":articles_nums
        })


class TagsDetialView(View):
    def get(self,request,tags_id):
        articles = Article.objects.filter(tags__name=tags_id)

        print articles
        return render(request,"tags_detail.html",context={
            "articles":articles,
            "tags_id":tags_id
        })
