from django.shortcuts import render,get_object_or_404,redirect
import os
from django.conf import settings
import markdown
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.http import FileResponse 
from .models import Product,ProductImage
from django.contrib.auth.decorators import login_required
import base64
from django.utils.safestring import mark_safe
##引入表单类
# from .forms import ProductImageForm

# 文章列表
def products(request):
    products = Product.objects.all()
    products = products.order_by('slug')


    paginator = Paginator(products, 4)
    page = request.GET.get('page')   
    products = paginator.get_page(page)
              
    context = { 'products': products}
    return render(request, 'products/products.html', context)    
    
# 文章列表
def detail(request, slug):

    product = get_object_or_404(Product, slug=slug)
   
    # 相邻的快捷导航
    pre_article = Product.objects.filter(slug__lt=product.slug).order_by('-slug')
    next_article = Product.objects.filter(slug__gt=product.slug).order_by('slug')
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
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ]
    )
    
    if product.faqs:
        product.faqs = md.convert(product.faqs)
    
    if product.citation:
        product.citation=md.convert(product.citation)

    ##获取产品对应的图片集：
    productimages=ProductImage.objects.filter(product=product)
    scales=[]
    for productimage in productimages:
        if productimage.scale not in scales:
            scales.append(productimage.scale) 
    scales_length=len(scales)

    dates= [[] for i in range(scales_length)]
    iscale=-1
    for scale in scales:
        iscale=iscale+1
        scaleimages=ProductImage.objects.filter(product=product,scale=scale).order_by('date')        
        for scaleimage in scaleimages:
            if scaleimage.date not in dates[iscale]:
                dates[iscale].append(scaleimage.date) 
       
    # print(scales)
    # print(dates)
    imgurl="/media/utils/no-object-found.gif"
    if scales:
        if dates:
            firstimage=get_object_or_404(ProductImage,product=product,scale=scales[0],date=dates[0][0])
            imgurl=firstimage.image.url
    context = { 'product': product,'pre_article':pre_article,'next_article':next_article,'scales':mark_safe(scales),'dates':mark_safe(dates),"imgurl":imgurl}
    return render(request, 'products/detail.html', context)    

 
##提供文件下载
def access(request,slug):  
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    product = get_object_or_404(Product, slug=slug)
    url=product.access.url
    filename = str(url).split("/")[-1] 
    file=open(BASE_DIR+url,'rb')  
    response =FileResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
    return response  

##提供文档下载
def document(request,slug):  
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    product = get_object_or_404(Product, slug=slug)
    url=product.document.url
    filename = str(url).split("/")[-1] 
    file=open(BASE_DIR+url,'rb')  
    response =FileResponse(file)  
    response['Content-Type']='application/octet-stream'  
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
    return response 


##查看ProductImage
@login_required(login_url='/admin')
def product_images(request):
    images=ProductImage.objects.all()
    images = images.order_by('-updated')
    products=Product.objects.all()            
    context = { 'images': images,'products': products}
    return render(request, 'products/product-images.html', context)   
    
##实现批量上传
@login_required(login_url='/admin')
def batch_upload(request):
    if request.method == 'POST':
        files = request.FILES.getlist('images',None) # input 标签中的name值,后端逻辑不承认前端的id
        scale = request.POST['scale'] # daily/month/year
        slug = request.POST['product'] # 所属产品集
        product = get_object_or_404(Product, slug=slug)
        if not files:
            return HttpResponse('没有上传的文件')
        else:
            try:
                for file in files:
                    filename=str(file.name).split("/")[-1]##去除路径，包含后缀
                    # print(file.name)
                    # print(filename)
                    bearname=''.join(str(filename).split(".")[:-1])##文件名，去除后缀
                    # print(bearname)
                    filedate=bearname[-8:] ## 文件名最后的八位日期：xxx_20040101
                    # print(filedate)
                    img = ProductImage(image=file,scale=scale,product=product,name=filename,date=filedate)
                    img.save()
            except Exception as e:
                # print(e)
                return HttpResponse("批量失败，联系运维（胡继恒/1831743701@qq.com/13637059562)")
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            os.system('chmod 744 '+BASE_DIR+'/media/products/productimage/'+slug+'/'+scale+'/*')
            return redirect("/admin/products/productimage/")

    elif request.method == 'GET':
        products = Product.objects.all()
        context = { 'products': products }
        return render(request, 'products/batch_upload.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")

def ajaxpic(request):
    # 解析参数
    # requestData=dict(request.POST)['data']
    scale = request.POST['scale'] # daily/month/year
    csrf = request.POST['csrfmiddlewaretoken'] # daily/month/year
    slug = request.POST['product'] # 所属产品集
    date = request.POST['date'] # 日期   
   
    product = get_object_or_404(Product,slug=slug)    
    productimage=get_object_or_404(ProductImage,product=product,scale=scale,date=date) 

    img=productimage.image
    response = HttpResponse(img.url,content_type="text") 
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    
    # with open(BASE_DIR+img.url, "rb") as image_file:
        # encoded_string = base64.b64encode(image_file.read())
    # response = HttpResponse(encoded_string,content_type="text") 
    
    return response
