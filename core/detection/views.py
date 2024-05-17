import json
import time
from datetime import datetime

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Company, Department, Employee, Sheet, ADModel, Image


# Create your views here.
def check_login(fn):
    def wrapper(request, *args, **kwargs):
        if request.session.get('isLogin', False):
            return fn(request, *args, *kwargs)
        else:
            resp = redirect('/detection/login/')
            return resp

    return wrapper


# @check_login
def dashborad(request):
    return render(request, "dashboard.html")


@csrf_exempt
def login(request):
    if request.method == 'GET':
        if request.session.get('isLogin', None):
            return redirect('/detection/')
        else:
            return render(request, "user/login.html")

    elif request.method == 'POST':
        company = request.POST.get('company', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        print(company, username, password)
        if company and username and password:
            company = Company.objects.filter(CID=company).first() or Company.objects.filter(Cname=company).first()
            if company is None:
                alert = '该企业或企业代号不存在!'
            else:
                try:
                    user = Employee.objects.get(CID=company, EID=username)
                    if user:
                        if user.Password == password:
                            request.session['uid'] = user.EID
                            request.session['cid'] = user.CID.CID
                            request.session['realName'] = user.Ename
                            request.session['role'] = user.Role
                            request.session['isLogin'] = True
                            request.session.set_expiry(24 * 60 * 60)
                            print(request.session.items())
                            # return render(request, "dashboard.html")
                            return redirect('/detection/')
                        else:
                            alert = '密码错误!'
                    else:
                        alert = '该用户不存在!'
                except Exception as e:
                    print(e)
                    alert = '网络错误，请稍后重试!'
        else:
            alert = '请完整输入登录信息!'
        return render(request, "user/login.html", {'alert': alert})


def logout(request):
    request.session.delete()
    request.session['isLogin'] = False
    return redirect('/detection/login/')


# User
def profile(request):
    if request.session.get('isLogin', None):
        user = Employee.objects.get(CID=request.session['cid'], EID=request.session['uid'])
        company = user.CID
        department = user.DID
        return render(request, 'user/profile.html', {'user': user, 'company': company, 'department': department})
    else:
        return redirect('/detection/login/')
    # return render(request, 'user/profile.html',)


def organization(request):
    if request.session.get('isLogin', None):
        user = Employee.objects.get(CID=request.session['cid'], EID=request.session['uid'])
        department = user.DID
        return render(request, 'user/organization.html', {'department': department})
    else:
        return redirect('/detection/login/')


def settings(request):
    pass


def authority(request):
    if request.session.get('isLogin', None):
        user = Employee.objects.get(CID=request.session['cid'], EID=request.session['uid'])
        return render(request, 'user/authority.html', {'role': user.Role})
    else:
        return redirect('/detection/login/')


# functions
def card(request):
    return render(request, "card.html")


@csrf_exempt
@check_login
def model(request):
    models_list = ADModel.objects.filter(MID__in=["STFPM", "SPADE", "PANDA"])
    models = {"STFPM": models_list[0], "SPADE": models_list[1], "PANDA": models_list[2]}
    current_model = request.session.get('current_model', None)
    if current_model:
        on_model = ADModel.objects.get(MID=current_model)
    else:
        on_model = None
    if request.method == 'GET':
        if on_model:
            return render(request, "work/model.html", {'on_model': on_model, 'models': models})
        else:
            return render(request, "work/model.html", {'on_model': None, 'models': models})
    elif request.method == 'POST':
        try:
            action = json.loads(request.body).get('action', None)
            material = json.loads(request.body).get('material', None)
        except Exception as e:
            action = request.POST.get('action', None)
            material = request.POST.get('material', None)
        if action == "detection":  # 执行图像检测模型
            if request.FILES['image']:
                pic_obj = request.FILES['image']
                pic_type = '.' + str(pic_obj.name).split('.')[-1]
                pic_name = request.session.get('uid', 'user') + "_" + str(int(round(time.time() * 1000))) + pic_type
                request.session['current_img'] = pic_name
                print(pic_name)
                image = Image(name=pic_name, img=pic_obj)
                image.save()
                return render(request, "work/model.html", {'on_model': on_model, 'models': models, 'image': image})
        elif action == "info":
            current_model = json.loads(request.body).get('current_model', None)
            on_model = ADModel.objects.filter(MID=current_model)
            if current_model:
                request.session['current_model'] = current_model
                return render(request, "work/model.html", {'on_model': on_model, 'models': models})
            else:
                return render(request, "work/model.html", {'on_model': None, 'models': models})


@csrf_exempt
@check_login
def sheet(request):
    user = Employee.objects.get(CID=request.session['cid'], EID=request.session['uid'])
    sheets = list(Sheet.objects.filter(EID=user.EID).order_by('Approval', '-OrderDate'))
    if request.method == 'GET':
        action = request.GET.get('sheet', None)
        if action == "review":  # 管理员审批
            juniors = list(Employee.objects.filter(DID=user.DID.DID))
            juniors.remove(user)
            sheets = list(
                Sheet.objects.filter(EID__in=[junior.EID for junior in juniors], Approval=False).order_by('-OrderDate'))
        elif action == "reviewed":  # 已审批
            sheets = list(Sheet.objects.filter(EID=user.EID, Approval=True).order_by('-OrderDate'))
        elif action == "reviewing":  # 未审批
            sheets = list(Sheet.objects.filter(EID=user.EID, Approval=False).order_by('-OrderDate'))
        else:
            pass
            # for sheet in sheets:
            #     sheet.setCNTime()
        return render(request, "work/sheet.html", {'sheet_list': sheets, 'action': action})
    elif request.method == 'POST':
        try:
            action = request.POST.get('action', None)
            if action == "create":
                SID = request.POST.get('SID', None)
                EID = user
                Task = request.POST.get('Task', None)
                Content = request.POST.get('Content', None)
                odate = str(request.POST.get('OrderDate', None)).split('/')
                tdate = str(request.POST.get('TargetDate', None)).split('/')
                OD = f'{odate[2]}-{odate[0]}-{odate[1]} 8:00:00'
                OrderDate = datetime.strptime(OD, '%Y-%m-%d %H:%M:%S')
                TD = f'{tdate[2]}-{tdate[0]}-{tdate[1]} 16:00:00'
                TargetDate = datetime.strptime(TD, '%Y-%m-%d %H:%M:%S')
                Approval = False
                print(TargetDate)
                if Task and Content:
                    Production = {'task': Task, 'content': Content}
                else:
                    Production = None
                sheet = Sheet(SID=SID, EID=EID, Production=Production,
                              OrderDate=OrderDate, TargetDate=TargetDate, Approval=Approval)
                print(type(sheet.Approval))
                sheet.save()
                alert = "创建信息成功"
            elif action == "update":
                pass
                alert = "修改信息成功"
            elif action == "delete":
                pass
                alert = "删除信息成功"
            else:
                pass
                alert = None
        except:
            alert = "操作失败，请稍后重试！"
        return render(request, "work/sheet.html", {'sheet_list': sheets, "alert": alert})


@check_login
@csrf_exempt
def sheet_op(request):
    if request.method == 'POST':
        action = request.GET.get('action', None)
        user = Employee.objects.get(CID=request.session['cid'], EID=request.session['uid'])
        if action == "create":
            SID = request.GET.get('SID', None)
            EID = request.session['uid']
            Task = request.GET.get('Title', None)
            Content = request.GET.get('Content', None)
            OrderDate = str(request.GET.get('OrderDate-year', None))
            TargetDate = str(request.GET.get('TargetDate-year', None))
            Approval = False
            if Task and Content:
                Production = json.dumps({"task": Task, "content": Content})
            else:
                Production = None
            sheet = Sheet(SID=SID, EID=EID, Production=Production,
                          OrderDate=OrderDate, TargetDate=TargetDate, Approval=Approval)
            print(sheet)
            # sheet.save()
        elif action == "update":
            pass
        elif action == "delete":
            pass


def chart(request):
    return render(request, "chart.html")


def shift(request, html: str):
    # route = html.split(".")[0]
    print(html)
    # return render(request, html)
    return redirect(reverse(html))


def vmodel(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass