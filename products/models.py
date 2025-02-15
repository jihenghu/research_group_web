from django.db import models
from django.utils import timezone
# Create your models here.

##数据集对象
class Product(models.Model):
    ##数据集标识，唯一
    slug=models.SlugField(max_length=10,unique=True, null=True, blank=False, verbose_name="数据集标识,大写缩写(如：ET,MLSE,EDVI,LH等)")
    longname = models.CharField(max_length=200, null=True, blank=True, verbose_name="完整名(如: microwave land surface emissivity)")
    desc = models.TextField(null=True, blank=True, verbose_name="数据简介")

    spatial_coverage = models.CharField(max_length=50, null=True, blank=True, verbose_name="覆盖范围(如: Global, China, East China, Anhui, US, Amazon等)")
    spatial_resolution = models.CharField(max_length=200, null=True, blank=True, verbose_name="空间分辨率(如: 25km, 0.25degree, 37 vertical layers 等信息)")
    date_start=models.DateTimeField(default=timezone.now,null=True, blank=True, verbose_name="数据集开始日期(只需要精确填写日期即可)")
    date_end=models.DateTimeField(default=timezone.now,null=True, blank=True, verbose_name="数据集结束日期(只需要精确填写日期即可)")
    temporal_resolution = models.CharField(max_length=200, null=True, blank=True, verbose_name="时间分辨率(如: daily, 3 hours, Monthly 等信息)")
    format=models.CharField(max_length=30,null=True, blank=True, verbose_name="数据格式(如：NetCDF, HDF5, GepTIFF, IMG, Binary, Ascii Formated等)")
    version=models.CharField(max_length=30,null=True, blank=True, verbose_name="版本")
    meta=models.TextField(null=True, blank=True, verbose_name="主要数据元(逗号隔开，如：Latent Heating, Rainfall Rate,CSH LH, SLH LH)")
    
    avatar=models.ImageField(upload_to = "products/avatar/", blank=True , verbose_name="上传封面"  )    
    access=models.FileField(upload_to = "products/download/", blank=True , verbose_name="上传示例数据"  )    
    document=models.FileField(upload_to = "products/documents/", blank=True , verbose_name="上传说明文档"  ) 
    citation=models.TextField(null=True, blank=True, verbose_name="引用") 
    faqs=models.TextField(null=True, blank=True, verbose_name="FAQ (支持Markdown语法)")     
    class Meta:
        ordering = ('slug',)
    def __str__(self):
        return "["+self.slug+"] "+self.longname

def sample_image_path(instance, filename):
    return 'products/productimage/{product}/{scale}/{file}'.format(product=instance.product.slug, scale=instance.scale, file=filename)


## 示例图片集
class ProductImage(models.Model):
    scale=models.CharField(max_length=10,null=True, blank=False, verbose_name="Level",
        choices=(("orbital", u"Orbit Level"),("daily", u"Daily"),("monthly", u"Monthly"),("seasonal", u"Seasonal"),("annual", u"Annual"),("multiyear", u"Multi-year")),default="daily")
    name=models.CharField(max_length=100, null=True, blank=False, verbose_name="文件名(不包含路径，包含拓展名)")
    date=models.CharField(max_length=8, null=True, blank=False, verbose_name="图片表示的日期(如 20040101,20051231)")
    image=models.ImageField(
        upload_to =sample_image_path, 
        blank=True , 
        verbose_name="图片")
    updated = models.DateTimeField(auto_now=True)
    product=models.ForeignKey(
        Product,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='product'
    )
    
    class Meta:
        ordering = ('product',)
    def __str__(self):
        return "["+self.product.slug+"_"+ self.scale +"] "+self.name