from django.db import models
from django.utils import timezone
#journal articles
class News(models.Model):
    title = models.CharField(max_length=200, null=True, blank=False, verbose_name="标题")
    authors = models.CharField(max_length=200, null=True, blank=True,default="ADMIN", verbose_name="作者(逗号隔开)")
    shown = models.CharField(max_length=1, choices=(("Y", u"显示"),("N", u"不显示")),default="Y", verbose_name="是否在首页轮播显示")  
    category = models.CharField(max_length=20, choices=(("research", u"研究动态"),("technical ", u"技术分享"), ("lecture", u"学术讲座及论坛"),("conference", u"外出会议"),("common", u"一般新闻")),default="common", verbose_name="类型")  
    created = models.DateTimeField(default=timezone.now,null=True, blank=False, verbose_name="时间")
    summary = models.TextField(null=True, blank=True, verbose_name="简述")
    body = models.TextField(null=True, blank=True, verbose_name="正文（支持Markdown语法）")
    url=models.URLField(null=True, blank=True, verbose_name="相关链接")
    image = models.ImageField(upload_to='news/image/%Y%m%d/',null=True,blank=True, verbose_name="文中图")
    avatar = models.ImageField(upload_to='news/avatar/%Y%m%d/', null=True,blank=False, verbose_name="封面（必填项）")
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)
    def __str__(self):
        return self.title
        
