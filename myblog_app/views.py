from django.shortcuts import redirect,reverse

# Create your views here.
from django.http import HttpResponse

def say_hello(request):
    if request.method == "GET":
        name = request.GET.get("name","")
        return HttpResponse("hello,%s!"%(name))


def index(request):
    username = request.GET.get("username","")
    if username:
        return HttpResponse("已登录")
    else:
        # 步骤4、这里用到了url反转
        login_url = reverse("myblog_app:login")
        print("="*30)
        print(login_url)
        print("="*30)
        redirect(login_url)

def login(request):
    return HttpResponse("您所在的页面是登录注册页！！")
