from django.shortcuts import render
import markdown
# 导入 HttpResponse 模块
from django.http import HttpResponse
from .models import Lab
from .models import Member
from .models import Opportunity
# 视图函数
def about(request):
    lab = Lab.objects.all()[0]
    members = Member.objects.all()
    
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
    for member in members:
        member.interests = md.convert(member.interests)
        if member.homepage:
            member.homepage = md.convert(member.homepage)
    
    opportunities = Opportunity.objects.all()
    context = { 'lab': lab, 'members': members, 'opportunities': opportunities}
    return render(request, 'about.html', context)