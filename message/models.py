from django.db import models

# timezone 用于处理时间相关事务。
from django.utils import timezone

class Message(models.Model):
    qid=models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="姓名")
    email = models.EmailField(max_length=100, null=True, blank=False, verbose_name="邮箱")
    subject = models.CharField(max_length=100, null=True, blank=True,verbose_name="主题")  
    created = models.DateTimeField(default=timezone.now)
    message = models.TextField()
    state = models.CharField(max_length=10,default="unread", choices=(("unread", u"未读"), ("read", u"已读"),("solved", u"已解决"),("replied", u"已回复"), ("processing", u"处理中")), null=True, blank=True, verbose_name="处理情况更新")    
    def __str__(self):
        return self.name+self.subject+self.email
    class Meta:
        ordering = ('-created',)
        
class Banner(models.Model):
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    body=models.TextField(null=True, blank=True,verbose_name="内容（支持Markdown）")  
    class Meta:
        ordering = ('-updated',)
    def __str__(self):
        return self.body