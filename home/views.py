from django.shortcuts import render,get_object_or_404
import markdown
import os
from django.core.paginator import Paginator
from django.http import HttpResponse
from news.models import News
from research.models import Publication,Focus
from products.models import Product
from about.models import Lab
import colorsys
import PIL.Image as Image
import logging
import os

# logg=logging.getLogger('django')
# logg.info('iam a info level log')
# logg.error('iam a error level log')
# logg.warning('iam a warning level log')
# Home页视图
def index(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.system('chmod -R 777 '+BASE_DIR+'/media/news/')
    lab = Lab.objects.all()[0]
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
    lab.desc = md.convert(lab.desc)
    
    news_list_all = News.objects.all().filter(shown='Y')
    num_news=min(len(news_list_all),4)
    news_list = news_list_all[:num_news]    
    
    focus_list = Focus.objects.all()
    products = Product.objects.all() 
    
    
    publications_all = Publication.objects.all() 
    num_pubs=min(len(publications_all),4)
    publications= publications_all[:num_pubs]  

    
    context = {'news_list':news_list,'focus_list':focus_list,'products':products,'publications':publications,'lab':lab}
    return render(request, 'home/index.html', context)


