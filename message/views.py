from django.shortcuts import render
from .models import Banner,Message
import markdown
from django.http import HttpResponse

def contactus(request):
    ##获取最新的banner
    banner=Banner.objects.first()
    # Markdown 语法渲染
    md = markdown.Markdown(
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        ]
    )    
    banner.body = md.convert(banner.body)
    return render(request, 'contactus/contactus.html',{'banner':banner})



def submit_message(request):
    # 解析参数
    name = request.POST['name'] # daily/month/year   
    email = request.POST['email'] # 所属产品集
    subject = request.POST['subject'] # 日期   
    message = request.POST['message'] # 日期   
   
    try:
        bmessage = Message(name=name,email=email,subject=subject,message=message)
        bmessage.save()
        return HttpResponse("success")     
    except Exception as e:
        return HttpResponse("失败Failed，联系运维contact（胡继恒/1831743701@qq.com/(+86) 13637059562)")               
   