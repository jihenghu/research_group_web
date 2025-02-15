from django.db import models
from django.utils import timezone
#journal articles
class Publication(models.Model):
    title = models.CharField(max_length=200, null=True, blank=False, verbose_name="标题")
    authors = models.CharField(max_length=200, null=True, blank=False,default="unknown,unknown" ,verbose_name="作者(至少两位，使用逗号隔开)")
    journal = models.CharField(max_length=100,null=True, blank=True, verbose_name="期刊")
    accept = models.DateTimeField(default=timezone.now,null=True, blank=False, verbose_name="接收日期(Accepted Date)")
    abstract = models.TextField(null=True, blank=True, verbose_name="摘要(支持Markdown语法)")
    summary = models.TextField(null=True, blank=True, verbose_name="概述")
    url=models.URLField(null=True, blank=True, verbose_name="链接")
    doi=models.URLField(null=True, blank=True, verbose_name="DOI")
    avatar = models.ImageField(upload_to='publications/avatar/', blank=True , verbose_name="封面")
    graph = models.ImageField(upload_to='publications/graph/', blank=True , verbose_name="图表(多图建议先拼接再上传)")
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-accept' 表明数据应该以倒序排列
        ordering = ('-accept',)
    def __str__(self):
        return self.title
        
#full publications list
class Publist(models.Model):
    reference = models.TextField(max_length=500, null=True, blank=False, verbose_name="Reference/Title")
    type = models.CharField(max_length=20, choices=(("journal", u"Journal Articles"), ("patent", u"Patent/Monographs"),("conference", u"Conference Articles&Abstracts")),default="journal", verbose_name="类型")  
    accept = models.DateTimeField(default=timezone.now,null=True, blank=False,verbose_name="接收日期(Accepted Date)")
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-accept' 表明数据应该以倒序排列
        ordering = ('-accept',)
    def __str__(self):
        return self.reference
        
#research Focus
class Focus(models.Model):
    title = models.CharField(max_length=200, null=True, blank=False, verbose_name="Research Focus")
    field = models.CharField(max_length=200, null=True, blank=False, verbose_name="所属研究领域")
    body = models.TextField(null=True, blank=False,verbose_name="正文(支持Markdown语法)")  
    graph = models.ImageField(upload_to='focus/', blank=True , verbose_name="图表(多图建议先拼接再上传)")
    graph_desc = models.TextField(null=True,blank=True,verbose_name="图片说明")
    order = models.IntegerField(null=True,blank=False,default="0" , verbose_name="列表顺序(小值显示在前)")
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-order' 表明数据应该以倒序排列
        ordering = ('order',)
    def __str__(self):
        return self.title 
        
#popular links
class Poplink(models.Model):
    title = models.CharField(max_length=20, null=True, blank=False, verbose_name="标题")
    desc = models.TextField(null=True, blank=True, verbose_name="描述")
    url=models.URLField(null=True, blank=True, verbose_name="链接")
    class Meta:
        ordering = ('title',)
    def __str__(self):
        return self.title
        
#Image Gallery
class GalleryImage(models.Model):
    title = models.CharField(max_length=50, null=True, blank=False, verbose_name="图片名称")
    desc = models.TextField(null=True, blank=False,verbose_name="图片描述")  
    image = models.ImageField(upload_to='imagegallery/', blank=False , verbose_name="图片")
    created = models.DateTimeField(default=timezone.now,null=True, blank=False,verbose_name="创建日期")
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.title 