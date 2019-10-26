from django.urls import path
from . import views

# 步骤3、配置应用命名空间
app_name = "myblog_app"

urlpatterns = [
    #步骤2、这是是二层路由配置
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('hello/',views.say_hello,name="hello"),

]

