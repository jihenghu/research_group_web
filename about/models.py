from django.db import models
# 导入内建的User模型。
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone

# 博客文章数据模型
class Lab(models.Model):
    # Lab标题。models.CharField 为字符串字段，用于保存较短的字符串，比如标题
    title = models.CharField(max_length=200)

    # Lab标题。models.CharField 为字符串字段，用于保存较短的字符串，比如标题
    title_cn = models.CharField(null=True, blank=True,max_length=100 , verbose_name="中文名")

    # Lab介绍。保存大量文本使用 TextField
    desc = models.TextField()

    # Lab 封面图。URLField
    image = models.ImageField(upload_to='lab/', blank=True)

    # Lab 记录创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)

    # Lab 记录更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="姓名")
    title = models.CharField(max_length=20, choices=(("professor", u"教授"), ("postdoc", u"博士后"),("phd", u"博士研究生"),("graduate", u"硕士研究生"),("under", u"本科生"),("visit",u"访问/交流")),null=True, blank=True, verbose_name="头衔")
    avatar = models.ImageField(upload_to='members/', blank=True , verbose_name="头像")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女"),("nan", u"无")), default="nan", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    homepage = models.TextField(max_length=300, null=True, blank=True, verbose_name="个人主页")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
    office = models.CharField(max_length=20, null=True, blank=True, verbose_name="办公室")
    biography = models.TextField( null=True, blank=True, verbose_name="个人简介")
    interests = models.TextField( null=True, blank=True, verbose_name="研究领域")
    project = models.TextField( null=True, blank=True, verbose_name="主持项目")
    honor = models.TextField( null=True, blank=True, verbose_name="荣誉和奖项")
    nowwhere = models.CharField(max_length=200, null=True, blank=True, verbose_name="何地从事")
    start = models.DateField(null=True, blank=True, verbose_name="何日始")
    end = models.DateField(null=True, blank=True, verbose_name="何日止")
    state = models.CharField(max_length=6, choices=(("yes", u"在"), ("no", u"不在了")), null=True, blank=True, verbose_name="是否还在组内？")
    class Meta:
        ordering = ('start','-title')
    def __str__(self):
        return self.name
        
class Opportunity(models.Model):
    position = models.CharField(max_length=50, null=True, blank=True, verbose_name="岗位需求")
    desc = models.CharField(max_length=100,null=True, blank=True, verbose_name="简单说明")

    def __str__(self):
        return self.position