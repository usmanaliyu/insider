from django.shortcuts import render,get_object_or_404,redirect




from django.conf import settings
import redis


r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db = settings.REDIS_DB)


# Create your views here.

def AdGuidline(request):
    return render(request, 'ad/guidelines.html')