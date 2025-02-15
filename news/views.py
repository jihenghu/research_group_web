from django.shortcuts import render,get_object_or_404
# 引入markdown模块
import markdown
import os
# 引入分页模块
from django.core.paginator import Paginator
# 导入 HttpResponse 模块
from django.http import HttpResponse

from .models import News

#News列表
def list(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.system('chmod -R 777 '+BASE_DIR+'/media/news/')
    articles = News.objects.all()
    articles = articles.order_by('-created')
    # 每页显示 1 篇文章
    paginator = Paginator(articles, 8)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 news
    news_list = paginator.get_page(page)
    
    context = { 'news_list': news_list}
    return render(request, 'news/list.html', context)
    

# News详情
def detail(request, id):
    # 取出相应的文章
    news = get_object_or_404(News, id=id)
    # 相邻发表文章的快捷导航
    pre_article = News.objects.filter(created__lt=news.created).order_by('-created')
    next_article = News.objects.filter(created__gt=news.created).order_by('created')
    if pre_article.count() > 0:
        pre_article = pre_article[0]
    else:
        pre_article = None

    if next_article.count() > 0:
        next_article = next_article[0]
    else:
        next_article = None

    # Markdown 语法渲染
    md = markdown.Markdown(
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        # 目录扩展
        'markdown.extensions.toc',
        ]
    )
    news.body = md.convert(news.body)

    # 需要传递给模板的对象
    context = { 
        'news': news,
        'toc': md.toc,
        'pre_article': pre_article,
        'next_article': next_article,
    }
    # 载入模板，并返回context对象
    return render(request, 'news/detail.html', context)
