  
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.utils.safestring import mark_safe
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible
from ckeditor_uploader.fields import RichTextUploadingField
@deconstructible
class PathAndRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(uuid4().hex, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)



class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError(_("The username is must be set"))
        username = self.normalize_email(username)
        user = self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password,**extra_fields):
        """Create and save Super user with given email address"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Supperuser must have is_staff=True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Supperuser must have is_superuser=True"))

        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(null=True,max_length=200,verbose_name='Утас',unique=True,blank=True)
    name = models.CharField(_('Нэр'), unique=False, max_length=200, blank=True, null=True)

    password = models.CharField(max_length=7000)
    confirm_password = models.CharField(max_length=7000)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username


class Order(models.Model):
    STATUS = (
        ('N', 'Шинэ'),
        ('F', 'Цуцалсан'),
        ('D', 'Дууссан'),
        ('B', 'Буцаагдсан'),
        ('O', 'Захиалсан'),
        ('C', 'Үнэ бодогдсон'),
        ('P', 'Төлбөр төлөгдсөн'),
        ('Q', 'Мэдээлэл буруу'),
    )
    link = models.URLField(_('Холбоос'),max_length=2000, null=True)
    name = models.CharField(_('Нэр'),  max_length=200, blank=True, null=True)
    quantity = models.IntegerField(_('Тоо ширхэг'), null=True)
    size = models.CharField(_('Размер'),  max_length=50, blank=True, null=True)
    color = models.CharField(_('Өнгө'),  max_length=100, blank=True, null=True)
    description = models.TextField(
        _('Тайлбар'), default='', null=True, blank=True,)
    address = models.TextField(
        _('Хаяг'), default='', null=True, blank=True,)
    
    status = models.CharField(max_length=1, choices=STATUS, default='N')

    admin_description = models.TextField(
        _('Хэрэглэгчид илгээх тайлбар'), default='', null=True, blank=True,)
    hansh = models.FloatField(_('Ханш'),  blank=True, null=True)
    cost = models.FloatField(_('Үнэ'),  blank=True, null=True)
    shipping_cost = models.FloatField(_('Хятад доторх тээврийн зардал'),default=0,  blank=True, null=True)
    delivery_cost = models.FloatField(_('Хүргэлтийн үнэ'),  default=0, blank=True, null=True)
    service_fee = models.FloatField(_('Үйлчилгээний хураамж'), default=0, blank=True, null=True)

    created_at = models.DateTimeField(_('Бүртгэгдсэн'),auto_now_add=True)
    updated_at = models.DateTimeField(_('Засагдсан'),auto_now=True)
    deleted_at = models.DateTimeField(_('Устгасан'),blank=True, null=True)

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name=_("User"), blank=True,
                             related_name="order")
  
    def get_link(self):
        if self.link:
            html = f'<a target="_blank" href="{self.link}"><img src="/media/picture/link-icon.png" width="23" /></a>'
            return mark_safe(html)
        return '-'
    get_link.short_description ='Холбоос'

    class Meta:
        db_table = 'order'
        verbose_name = _("Захиалга")
        verbose_name_plural = _("Захиалга")




class MessageRequest(models.Model):
    name = models.CharField(_('Нэр'), null=True,  max_length=200, blank=True)
    phone = models.CharField(_('Утас'), null=True,max_length=200, blank=True)
    message = models.TextField(_('Санал хүсэлт'), default='', null=True, blank=True,)
    created_at = models.DateTimeField(_('Илгээсэн огноо'),auto_now_add=True)
    class Meta:
        db_table = 'message_request'
        verbose_name = _("Санал хүсэлт")
        verbose_name_plural = _("Санал хүсэлт")

class News(models.Model):
    picture =  models.ImageField(_("Зураг"), upload_to=PathAndRename(
        'picture/'),null=True,  blank=True, max_length=2500)
    link = models.URLField(_('Холбоос'),null=True, blank=True,max_length=1000)
    title = models.CharField(_('Гарчиг'), null=True,max_length=1000, blank=True)
    text = models.TextField(_('Текст'), default='', null=True, blank=True,)
    sequence = models.IntegerField(_('Дараалал'), null=True)
    created_at = models.DateTimeField(_('Илгээсэн огноо'),auto_now_add=True)
    deleted_at = models.DateTimeField(_('Устгасан'),blank=True, null=True)
    
    def photo(self):
        return ''
        if self.picture ==None:
            return ''
        return mark_safe('<img src="{}" width="100" />'.format(self.picture.url))
    
    def get_link(self):
        if self.link:
            html = f'<center><a target="_blank" href="{self.link}"><img src="/media/picture/link-icon.png" width="23" /></a></center>'
            return mark_safe(html)
        return mark_safe(f'<center>-</center>')
    photo.short_description = 'Зураг'
    get_link.short_description ='Холбоос'
    class Meta:
        db_table = 'news'
        verbose_name = _("Мэдээ мэдээлэл")
        verbose_name_plural = _("Мэдээ мэдээлэл")


class BaseInfo(models.Model):
    phone = models.CharField(_('Утас'), null=True,max_length=1000, blank=True)
    email = models.CharField(_('Имэйл'), null=True,max_length=1000, blank=True)
    address = models.TextField(_('Хаяг'), default='', null=True, blank=True)
    small_description = models.TextField(_('Богино мэдээлэл'), default='', null=True, blank=True)
    fb = models.CharField(_('Фэйсбүүк линк'), null=True,max_length=1000, blank=True)
    insta = models.CharField(_('Инста линк'), null=True,max_length=1000, blank=True)
    class Meta:
        db_table = 'base_info'
        verbose_name = _("Үндсэн мэдээлэл")
        verbose_name_plural = _("Үндсэн мэдээлэл")




class Help(models.Model):
    title = models.CharField(_('Гарчиг'), null=True,max_length=1000, blank=True)
    sequence = models.IntegerField(_('Дараалал'), null=True)
    class Meta:
        db_table = 'help'
        verbose_name = _("Тусламж")
        verbose_name_plural = _("Тусламж")
    def __str__(self):
        return self.title

class HelpStep(models.Model):
    title = models.CharField(_('Гарчиг'), null=True,max_length=1000, blank=True)
    body = RichTextUploadingField(verbose_name=_("Контент"),blank=True, null=True, )
    help = models.ForeignKey(Help, null=True, on_delete=models.CASCADE, verbose_name=_("Тусламж"), blank=True,
                             related_name="help_step")
    
    sequence = models.IntegerField(_('Дараалал'), null=True)

    class Meta:
        db_table = 'help_step'
        verbose_name = _("Тусламж алхам")
        verbose_name_plural = _("Тусламж алхам")

    def __str__(self):
        return self.title



class AboutUs(models.Model):
    title = models.CharField(_('Гарчиг'), null=True,max_length=1000, blank=True)
    body = RichTextUploadingField(verbose_name=_("Контент"),blank=True, null=True, )
    sequence = models.IntegerField(_('Дараалал'), null=True)

    class Meta:
        db_table = 'about_us'
        verbose_name = _("Бидний тухай")
        verbose_name_plural = _("Бидний тухай")

    def __str__(self):
        return self.title

class UseOfTerms(models.Model):
    title = models.CharField(_('Гарчиг'), null=True,max_length=1000, blank=True)
    body = RichTextUploadingField(verbose_name=_("Контент"),blank=True, null=True, )
    sequence = models.IntegerField(_('Дараалал'), null=True)

    class Meta:
        db_table = 'use_of_terms'
        verbose_name = _("Үйлчилгээний нөхцөл")
        verbose_name_plural = _("Үйлчилгээний нөхцөл")

    def __str__(self):
        return self.title
    
    
class Hansh(models.Model):
    hansh = models.FloatField(_('Ханш'),  blank=True, null=True)

    class Meta:
        db_table = 'hansh'
        verbose_name = _("Ханш")
        verbose_name_plural = _("Ханш")

    def __str__(self):
        return str(self.hansh)