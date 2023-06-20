from django.contrib import admin
from profiles.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django_paranoid.admin import ParanoidAdmin
from django.contrib.auth.models import Group
from django.contrib.admin.actions import delete_selected
from rangefilter.filters import DateRangeFilterBuilder, DateTimeRangeFilterBuilder, NumericRangeFilterBuilder
import datetime
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(ParanoidAdmin, BaseUserAdmin):
    list_display = ("name", "username", "is_admin")
    list_editable = ("is_admin",)
    list_filter = ("is_admin",)
    search_fields = ('username', 'name')
    readonly_fields = ('is_staff',)


    fieldsets = (
        (None, {'fields': ('name','username', 'password','is_admin')}),
           )

    add_fieldsets = (
         ('Personal Information', {
            'description': "",
            'classes': ('wide',),
            'fields': (
                'name', 'username')}),
        ('username and Password', {
            'description': "",
            'classes': ('wide',),
            'fields': ('password1', 'password2',)}
         ),
       
        ('Appointment Type', {'fields': ('is_admin', )}),
    )
    def save_model(self, request, obj, form, change):
        if obj.is_admin:
            obj.is_staff = True
            obj.is_superuser = True
            obj.is_active = True
        else:
            obj.is_staff = False
            obj.is_superuser = False
            
        super().save_model(request, obj, form, change)
    ordering = ('username',)
    filter_horizontal = ()


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('order_no','name', 'link', 'quantity','size','color','description', 'address','user',"status",'hansh','cost','shipping_cost','delivery_cost','service_fee','ub_shipping_cost',"admin_description")
    readonly_fields = ('order_no','hansh','user')
    list_display = ('order_no','name', 'get_link',"price","status", 'quantity','size','color','description','created_at', 'address',"user")
    list_filter = ("created_at","status",("created_at", DateRangeFilterBuilder()),)
    search_fields = ('order_no','name','link','user__username')
    actions = ['finish','paid','done']
    
    def price(self, obj):
        cost  = 0 if obj.cost ==None else obj.cost
        scost  = 0 if obj.shipping_cost ==None else obj.shipping_cost
        dcost  = 0 if obj.delivery_cost ==None else obj.delivery_cost
        fee  = 0 if obj.service_fee ==None else obj.service_fee
        ucost  = 0 if obj.ub_shipping_cost ==None else obj.ub_shipping_cost
        if obj.hansh ==None:
            return '0'
        else:
            price = (cost + scost + dcost + fee+ucost)*obj.hansh
            currency = "{:,.2f}".format(price)
            return str(currency)+"₮"


    def save_model(self, request, obj, form, change):
        if obj.order_no == None:
            count = Order.objects.last().id+1
            year = datetime.date.today().year
            order_no = str(year)[2:4]+ str(count).zfill(4)
            obj.order_no=order_no

        if obj.status == 'C':
            hansh = Hansh.objects.first()
            
            if hansh == None:
                h = 1.0
            else:
                h = hansh.hansh
            obj.hansh = h
            
        super().save_model(request, obj, form, change)


    def finish(self,request,queryset):
        queryset.update(status="O")
    def paid(self,request,queryset):
        queryset.update(status="P")
    def done(self,request,queryset):
        queryset.update(status="D")
   
      
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    price.short_description = 'Бодогдсон үнэ'
    finish.short_description = 'Захиалсан'
    paid.short_description = 'Төлбөр төлөгдсөн'
    done.short_description = 'Дууссан'
    delete_selected.short_description = u'Устгах'
    class Media:
        js = ('js/order_admin.js',)
   
   
@admin.register(MessageRequest)
class MessageRequestAdmin(admin.ModelAdmin):
    fields = ('name', 'phone', 'message',)
    list_display = ('name', 'phone', 'message','created_at')
    list_filter = ("created_at",("created_at", DateRangeFilterBuilder()),)
    search_fields = ('id','name','phone')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'picture', 'text','link','position','sequence','deleted_at')
    list_display = ('title', 'photo','get_link','text','sequence','position','created_at','deleted_at')
    list_filter = ("created_at","deleted_at")
    search_fields = ('id','title')

  

@admin.register(BaseInfo)
class BaseInfoAdmin(admin.ModelAdmin):
    fields = ('phone', 'email', 'address','small_description','fb','insta')
    list_display = ('phone', 'email', 'address','small_description','fb','insta')
    
@admin.register(Help)
class HelpStepAdmin(admin.ModelAdmin):
    fields = ('title','sequence')
    list_display = ('title',)

@admin.register(HelpStep)
class HelpStepAdmin(admin.ModelAdmin):
    fields = ('title', 'help', 'body','sequence')
    list_display = ('title', 'help')

    

    
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    fields = ('title','body','sequence')
    list_display = ('title', 'sequence')

    

    
@admin.register(UseOfTerms)
class UseOfTermsAdmin(admin.ModelAdmin):
    fields = ('title','body','sequence')
    list_display = ('title', 'sequence')

    
    
@admin.register(Hansh)
class HanshAdmin(admin.ModelAdmin):
    fields = ('hansh',)
    list_display = ('hansh',)

    