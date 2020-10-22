from django.contrib import admin
from .models import UserInfo
from .models import Post

admin.site.register(Post)

admin.site.register(UserInfo)
# Register your models here.
