from django.db import models
from django.conf import settings
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=250, blank=True)
    title_body1 = models.TextField(max_length=1000, blank=True)
    title_body2 = models.TextField(max_length=1000, blank=True)
    title_body3 = models.TextField(max_length=1000, blank=True)

    sub1 = models.CharField(max_length=200, blank=True)
    sub1_child1 = models.CharField(max_length=500, blank=True)
    sub1_child1_body = models.TextField(max_length=1000, blank=True)
    sub1_child2 = models.CharField(max_length=500, blank=True)
    sub1_child2_body = models.TextField(max_length=1000, blank=True)
    sub1_child3 = models.CharField(max_length=500, blank=True)
    sub1_child3_body = models.TextField(max_length=1000, blank=True)
    sub1_child4 = models.CharField(max_length=500, blank=True)
    sub1_child4_body = models.TextField(max_length=1000, blank=True)
    sub1_child5 = models.CharField(max_length=500, blank=True)
    sub1_child5_body = models.TextField(max_length=1000, blank=True)

    sub2 = models.CharField(max_length=200, blank=True)
    sub2_child1 = models.CharField(max_length=500, blank=True)
    sub2_child1_body = models.TextField(max_length=1000, blank=True)
    sub2_child2 = models.CharField(max_length=500, blank=True)
    sub2_child2_body = models.TextField(max_length=1000, blank=True)
    sub2_child3 = models.CharField(max_length=500, blank=True)
    sub2_child3_body = models.TextField(max_length=1000, blank=True)
    sub2_child4 = models.CharField(max_length=500, blank=True)
    sub2_child4_body = models.TextField(max_length=1000, blank=True)
    sub2_child5 = models.CharField(max_length=500, blank=True)
    sub2_child5_body = models.TextField(max_length=1000, blank=True)

    sub3 = models.CharField(max_length=200, blank=True)
    sub3_child1 = models.CharField(max_length=500, blank=True)
    sub3_child1_body = models.TextField(max_length=1000, blank=True)
    sub3_child2 = models.CharField(max_length=500, blank=True)
    sub3_child2_body = models.TextField(max_length=1000, blank=True)
    sub3_child3 = models.CharField(max_length=500, blank=True)
    sub3_child3_body = models.TextField(max_length=1000, blank=True)
    sub3_child4 = models.CharField(max_length=500, blank=True)
    sub3_child4_body = models.TextField(max_length=1000, blank=True)
    sub3_child5 = models.CharField(max_length=500, blank=True)
    sub3_child5_body = models.TextField(max_length=1000, blank=True)

    sub4 = models.CharField(max_length=200, blank=True)
    sub4_child1 = models.CharField(max_length=500, blank=True)
    sub4_child1_body = models.TextField(max_length=1000, blank=True)
    sub4_child2 = models.CharField(max_length=500, blank=True)
    sub4_child2_body = models.TextField(max_length=1000, blank=True)
    sub4_child3 = models.CharField(max_length=500, blank=True)
    sub4_child3_body = models.TextField(max_length=1000, blank=True)
    sub4_child4 = models.CharField(max_length=500, blank=True)
    sub4_child4_body = models.TextField(max_length=1000, blank=True)
    sub4_child5 = models.CharField(max_length=500, blank=True)
    sub4_child5_body = models.TextField(max_length=1000, blank=True)

    sub5 = models.CharField(max_length=200, blank=True)
    sub5_child1 = models.CharField(max_length=500, blank=True)
    sub5_child1_body = models.TextField(max_length=1000, blank=True)
    sub5_child2 = models.CharField(max_length=500, blank=True)
    sub5_child2_body = models.TextField(max_length=1000, blank=True)
    sub5_child3 = models.CharField(max_length=500, blank=True)
    sub5_child3_body = models.TextField(max_length=1000, blank=True)
    sub5_child4 = models.CharField(max_length=500, blank=True)
    sub5_child4_body = models.TextField(max_length=1000, blank=True)
    sub5_child5 = models.CharField(max_length=500, blank=True)
    sub5_child5_body = models.TextField(max_length=1000, blank=True)



    def __str__(self):
        return self.title

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type


