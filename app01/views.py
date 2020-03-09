from django.shortcuts import render, redirect

# Create your views here.


from django.contrib import auth
from app01 import models
from functools import wraps


# def check_login(f):
#     @wraps(f)
#     def inner(request, *args, **kwargs):
#         if request.session.get('is_login') == '1':
#             return f(request, *args, **kwargs)
#         else:
#             return redirect('/login/')
#
#     return inner
#
#
# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = models.User.objects.filter(username=username, password=password)
#         if user:
#             # 登录成功
#             request.session["is_login"] = "1"
#             request.session["username"] = username
#             request.session['user_id'] = user[0].id
#             # 生成一个特殊的字符串
#             # 特殊字符串当初key，在数据库的session表中对应一个session value
#             # 在响应中向浏览器写了一个cookie，cookie的值就是特殊的字符串
#             return redirect('/index/')
#
#     return render(request, 'login.html')
#
#
# @check_login
# def index(request):
#     user_id = request.session.get('user_id')
#     # 根据id查询
#     user_obj = models.User.objects.filter(id=user_id)
#     if user_obj:
#         return render(request, 'index.html', {'user': user_obj[0]})
#     else:
#         return render(request, 'index.html', {'user': '匿名用户 '})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')    # lxw lxw12345
        pwd = request.POST.get('password')
        # 如何判断用户名和密码正确
        user = auth.authenticate(username=username, password=pwd)
        auth.login(request, user)
        if user:
            return redirect('/index/')
    return render(request, 'login.html')


def index(request):
    print('========================')
    print(request.user.username)
    return render(request, 'index.html')

