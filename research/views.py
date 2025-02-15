from django.shortcuts import render,get_object_or_404
# 引入markdown模块
import markdown
# 引入分页模块
from django.core.paginator import Paginator
# 导入 HttpResponse 模块
from django.http import HttpResponse

from .models import Publication,Publist,Focus,Poplink,GalleryImage
from products.models import Product


# research 主页视图
def index(request):
    focus_list = Focus.objects.all()
    publications=Publication.objects.all().order_by('-accept')[:2] 
    products=Product.objects.all()[:4] 
    context = { 'focus_list': focus_list,'products': products,'publications': publications}
    return render(request, 'research/index.html', context)



# 文章列表
def publications_list(request):
    articles = Publication.objects.all()
    articles = articles.order_by('-accept')
    #select the first 2 authors
    for pub in articles:
        if pub.authors:
            pub.authors=pub.authors.split(",")[0].strip()+", "+pub.authors.split(",")[1].strip()
        
    # 每页显示 1 篇文章
    paginator = Paginator(articles, 3)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 articles
    publications = paginator.get_page(page)

    publists=Publist.objects.all().order_by('-accept')
    md = markdown.Markdown(
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ]
    )
    
    for publist in publists:
        publist.reference= md.convert(publist.reference)

    context = { 'publications': publications,'publists': publists}
    return render(request, 'research/publications.html', context)
    



# 文章详情
def publication_detail(request, id):
    # 取出相应的文章
    publication = get_object_or_404(Publication, id=id)
    # publication = Publication.objects.get(id=id)

    # 相邻发表文章的快捷导航
    pre_article = Publication.objects.filter(accept__lt=publication.accept).order_by('-accept')
    next_article = Publication.objects.filter(accept__gt=publication.accept).order_by('accept')
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
    if publication.abstract:
        publication.abstract = md.convert(publication.abstract)

    # 需要传递给模板的对象
    context = { 
        'publication': publication,
        'toc': md.toc,
        'pre_article': pre_article,
        'next_article': next_article,
    }
    # 载入模板，并返回context对象
    return render(request, 'research/publication-detail.html', context)

# 文章列表
def focus(request):
    focus_list = Focus.objects.all()
    focus_list = focus_list.order_by('order')
    
    md = markdown.Markdown(
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ]
    )
    # Markdown 语法逐条渲染body
    for focus in focus_list:        
        focus.body = md.convert(focus.body)
    context = { 'focus_list': focus_list}
    return render(request, 'research/focus.html', context)
    
# resource 主页视图（popularlinks+galleryimage）
def resource(request):
    galleryimages = GalleryImage.objects.all()
    galleryimages = galleryimages.order_by('-created')     
    # 每页显示  12张图片
    paginator = Paginator(galleryimages, 12)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 galleryimages
    galleryimages = paginator.get_page(page)
    
    links = Poplink.objects.all()
    links = links.order_by('title')         
    context = { 'links': links,'galleryimages': galleryimages}
    return render(request, 'research/resource.html', context)
    
