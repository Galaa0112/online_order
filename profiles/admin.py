from django.contrib import admin
from profiles.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django_paranoid.admin import ParanoidAdmin
from django.contrib.auth.models import Group
from django.contrib.admin.actions import delete_selected
from rangefilter.filters import DateRangeFilterBuilder, DateTimeRangeFilterBuilder, NumericRangeFilterBuilder

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


    ordering = ('username',)
    filter_horizontal = ()


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('name', 'link', 'quantity','size','color','description', 'address','user',"status",'hansh','cost','shipping_cost','delivery_cost','service_fee',"admin_description")
    readonly_fields = ('hansh','user')
    list_display = ('id','name', 'get_link',"status", 'quantity','size','color','description','created_at', 'address',"user")
    list_filter = ("created_at","status",("created_at", DateRangeFilterBuilder()),)
    search_fields = ('id','name','link','user__username')
    actions = ['finish','paid','done']
    def save_model(self, request, obj, form, change):
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

    finish.short_description = 'Захиалсан'
    paid.short_description = 'Төлбөр төлөгдсөн'
    done.short_description = 'Дууссан'
    delete_selected.short_description = u'Устгах'
    # def has_change_permission(self, request, obj=None):
    #     if request.user.is_admin == True:
    #         return True
    #     else:
    #         return False

    # def has_add_permission(self, request, obj=None):
    #     if request.user.is_admin == True:
    #         return True
    #     else:
    #         return False
    
    # def has_delete_permission(self, request, obj=None):
    #     if request.user.is_admin == True:
    #         return True
    #     else:
    #         return False

    # def has_view_permission(self, request, obj=None):
    #     if request.user.is_admin == True:
    #         return True
    #     else:
    #         return False

    
@admin.register(MessageRequest)
class MessageRequestAdmin(admin.ModelAdmin):
    fields = ('name', 'phone', 'message',)
    list_display = ('name', 'phone', 'message','created_at')
    list_filter = ("created_at",("created_at", DateRangeFilterBuilder()),)
    search_fields = ('id','name','phone')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'picture', 'text','link','sequence','deleted_at')
    list_display = ('title', 'photo','get_link','text','sequence','created_at','deleted_at')
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

    