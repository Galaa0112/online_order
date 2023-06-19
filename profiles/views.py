from django.shortcuts import redirect, render
from  django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login , logout
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from profiles.models import  *
import datetime

# model import 
from django.db.models import CharField
from django.db.models.functions import Lower
from profiles.models import  User
from django.http import JsonResponse

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import serializers, generics, permissions, status

CharField.register_lookup(Lower)

# Class Index
class Index(View):
    def get(self, request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        news = News.objects.filter(deleted_at=None).order_by("sequence").all()
        base = BaseInfo.objects.first()
        helpData = []
        helps = Help.objects.order_by("sequence").all()
        for h in helps:
            hSteps = HelpStep.objects.filter(help = h).order_by("sequence").all()
            helpData.append({'id':h.id,'title':h.title,'step':hSteps})
        return render(request,'index.html',{'news':news,'base':base, 'help':helpData})
    


# class TestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HelpStep
#         fields = ['title', 'body']

# class IndexAPI(View):
#     def get(self,request):
#         serializer_class = TestSerializer(
#             HelpStep.objects, many=True)
       
#         return JsonResponse({"has_next":serializer_class.data})

    
class TermsView(View):
    def get(self,request):
        terms = UseOfTerms.objects.order_by("sequence").all()
        base = BaseInfo.objects.first()
        return render(request,'terms.html',{'terms':terms,'base':base})

class AboutUsView(View):
    def get(self,request):
        base = BaseInfo.objects.first()
        about = AboutUs.objects.order_by("sequence").all()
        return render(request,'about_us.html',{'about':about,'base':base})

    
class RegisterView(View):
    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        name = request.POST.get('name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone_check = User.objects.filter(username = username)

       

        if len(username)==8:
            prefx = username[0:2]
            if phone_check:
                messages.warning(request,'Бүртгэлтэй утасны дугаар байна!')
                return redirect('/login')
            elif password1 != password2:
                messages.warning(request,'Нууц үг таарахгүй байна')
                return redirect('/login')
            elif len(password1) < 5:
                messages.warning(request,'Нууц үг хэтэрхий богино байна. Дор хаяж 5-ын урттай байх хэрэгтэй.')
                return redirect('/login')
            elif prefx == "95" or prefx == "94" or prefx == "85" or prefx == "99" or prefx == "90" or prefx == "91" or prefx == "96" or prefx == "80" or prefx == "86"  or prefx == "88"  or prefx == "89"  or prefx == "83"  or prefx == "93"  or prefx == "97"  or prefx == "98":
                auth_info ={
                    'username':username,
                    'name':name,
                    'password':make_password(password1)
                }
                user = User(**auth_info)
                user.save()
                messages.success(request, 'Амжилттай бүртгэгдлээ. Та бүртгэлээрээ нэвтэрч орно уу')
                return redirect ('/login')
            else:
                messages.warning(request,"Утасны дугаар буруу байна.")
                return redirect('/login')
        messages.warning(request,"Утасны дугаар буруу байна")
        return redirect('/login')



class LoginView(View):
    def get(self,request):
        
        base = BaseInfo.objects.first()
        return render(request,'login.html',{'base':base})

    def post(self,request,*args,**kwargs):
        detect = request.POST.get('username')
        passowrd = request.POST.get('password')
        
        match = User.objects.filter(
            Q(username = detect)
        ).first()
        if match:
            user = authenticate(request,username=match.username, password=passowrd)
            if user is not None:
                login(request,user)
                return redirect('/')
        messages.warning(request,'Хэрэглэгчийн утасны дугаар эсвэл нууц үг буруу байна.')
        return redirect('/login')
    

class LogoutView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,request):
        logout(request)
        return redirect('/')
    

    
class ProfileView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    def get(self,request):
        user = request.user
        base = BaseInfo.objects.first()
        return render(request,'dashboard/profile.html',{'user':user, 'base':base})
    
    def post(self,request,*args,**kwargs):
        user = request.user
        name = request.POST.get('name')
        user.name = name
        user.save()
        messages.success(request, 'Амжилттай мэдээллээ шинэчиллээ.')
        return redirect ('/profile')
         
                  
class ChangePasswordView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    def get(self,request):
        user = request.user
        base = BaseInfo.objects.first()
        return render(request,'dashboard/change_password.html',{'user':user, 'base':base})
    
    def post(self,request,*args,**kwargs):
        user = request.user
        pw1 = request.POST.get('pw1')
        pw2 = request.POST.get('pw2')
        pw3 = request.POST.get('pw3')
        user = authenticate(request,username=user.username, password=pw1)
        if user is None:
            messages.success(request, 'Нууц үг буруу байна.')
            return redirect ('/password')
        elif pw2 != pw3:
            messages.success(request, 'Шинэ нууц үг хоорондоо таарахгүй байна.')
            return redirect ('/password')
        else:
            user.password = make_password(pw2)
            user.save()
            messages.success(request, 'Нууц үг амжилттай шинэчиллээ. Та шинэ нууц үгээрээ нэвтэрч орно уу.')
            return redirect ('/password')
                
    
class OrderView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    def get(self,request):
        user = request.user
        base = BaseInfo.objects.first()
        return render(request,'dashboard/order.html',{'user':user,'base':base})
    
    def post(self,request,*args,**kwargs):
        user = request.user
        link = request.POST.get('link') if request.POST.get('link')!=None else ''
        name = request.POST.get('name') if request.POST.get('name')!=None else ''
        quantity = request.POST.get('quantity') if request.POST.get('quantity')!=None else ''
        size = request.POST.get('size') if request.POST.get('size')!=None else ''
        color = request.POST.get('color') if request.POST.get('color')!=None else ''
        description = request.POST.get('description') if request.POST.get('description')!=None else ''
        address = request.POST.get('address') if request.POST.get('address')!=None else ''
        count = Order.objects.count()+1
        year = datetime.date.today().year
        order_no = str(year)[2:4]+ str(count).zfill(4)
    
        order_info ={
            "order_no":order_no,
            "user": user,
            "link": link,
            "name": name,
            "quantity":quantity,
            "size":size,
            "color": color,
            "description": description,
            "address": address
        }
        order = Order(**order_info)
        order.save()
        messages.success(request, 'Таны захиалга амжилттай бүртгэгдлээ.')
        return redirect ('/order')
                  
               
class OrderListView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    def get(self,request):
        user = request.user
        page = request.GET.get('page',1)
        query =Order.objects.filter(user = user)
        
        name = request.GET.get('name')
        date = request.GET.get('date')
        status = request.GET.get('status')
        if(status!=None and status!=""):
            query = query.filter(status =status )
        if(name!=None and name!=""):
            query = query.filter(name__lower__contains =name.lower() )
        if(date!=None and date!=""):
            date = str(date)
            year = date[0:4]
            month = date[5:7]    
            day = date[8:10]    
            query = query.filter(
                created_at__year =year,
                created_at__month =month,
                created_at__day =day
                )

        orders = query.order_by("-created_at").all()

        paginator = Paginator(orders,20)
        try:
            order_list = paginator.page(page)
        except PageNotAnInteger:
            order_list = paginator.page(1)
        except EmptyPage:
            order_list = paginator.page(paginator.num_pages)

        base = BaseInfo.objects.first()
        return render(request,'dashboard/order_list.html',{'orders':order_list,'base':base})
    
class OrderUpdateView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    
    def get(self, request,id):
        user = request.user
        order =Order.objects.filter(user = user, id= id).first()
        if order == None:
            messages.success(request, 'Захиалга олдсонгүй')
            return redirect ('/dashboard/order_list.html')
        return render(request,'dashboard/order_edit.html',{'order':order})
    
    def post(self,request,id,*args,**kwargs):
        if id == "" or id == None:
            messages.success(request, 'Захиалга олдсонгүй')
            return render(request,'dashboard/order_edit.html')
        order =Order.objects.filter(id= id).first()

        if order == "" or order == None:
            messages.success(request, 'Захиалга олдсонгүй')
            return render(request,'dashboard/order_edit.html')
        link = request.POST.get('link') if request.POST.get('link')!=None else ''
        name = request.POST.get('name') if request.POST.get('name')!=None else ''
        quantity = request.POST.get('quantity') if request.POST.get('quantity')!=None else ''
        size = request.POST.get('size') if request.POST.get('size')!=None else ''
        color = request.POST.get('color') if request.POST.get('color')!=None else ''
        description = request.POST.get('description') if request.POST.get('description')!=None else ''
        address = request.POST.get('address') if request.POST.get('address')!=None else ''

        order.link = link
        order.name = name
        order.quantity = quantity
        order.size = size
        order.color = color
        order.description = description
        order.address = address
        order.status = "N"
        order.save()
    
        messages.success(request, 'Таны захиалга амжилттай засагдлаа.')
        return render(request,'dashboard/order_edit.html',{'order':order})
       
class OrderCancelView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    def get(self, request,id):
        order =Order.objects.filter(id= id).first()
        if order == None:
            messages.success(request, 'Захиалга олдсонгүй')
            return redirect ('/dashboard/order_list.html')
        order.status = 'F'
        order.save()
        messages.success(request, 'Таны захиалга цуцдагдлаа.')
        return render(request,'dashboard/order_edit.html',{'order':order})
       

       
class MessageRequestView(View):
    def post(self,request,*args,**kwargs):
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        message = request.POST.get('message')
        if len(phone)==8:
            prefx = phone[0:2]
            if prefx == "95" or prefx == "94" or prefx == "85" or prefx == "99" or prefx == "90" or prefx == "91" or prefx == "96" or prefx == "80" or prefx == "86"  or prefx == "88"  or prefx == "89"  or prefx == "83"  or prefx == "93"  or prefx == "97"  or prefx == "98":
                message_info ={
                    'phone':phone,
                    'name':name,
                    'message':message
                }
                msg = MessageRequest(**message_info)
                msg.save()
                messages.success(request, 'Таны хүсэлтийг хүлээн авлаа')
                return redirect ('/#contact',{})
             
            else:
                messages.warning(request,"Утасны дугаар буруу байна.")
                return redirect('/#contact',{})
                  
        messages.warning(request,"Утасны дугаар буруу байна",{})
        return redirect('/#contact',{})

