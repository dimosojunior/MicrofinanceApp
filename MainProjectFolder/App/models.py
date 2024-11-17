from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser
import random
from datetime import timedelta
# Create your models here.



class MyUserManager(BaseUserManager):
    def create_user(self, email, username,phone, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")

        


        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, phone, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            phone=phone,

        )
        user.is_admin=True
        user.is_staff=True
        user.is_cashier=True
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

    

  
class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="user name", max_length=100, unique=True)
    middle_name=models.CharField(verbose_name="middle name", max_length=100, unique=False)
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    company_name=models.CharField(verbose_name="company name",blank=True,null=True, max_length=500, unique=False)
    phone=models.CharField(verbose_name="phone", max_length=10)
    Location=models.CharField(verbose_name="Mahali", max_length=200, blank=True, null=True)
    
    
    
    profile_image = models.ImageField(upload_to='media/',verbose_name="Picha Ya Mtu", blank=True, null=True)
    #profile_image = models.ImageField(upload_to='media/',verbose_name="Picha Ya Mtu", blank=True, null=True, default='mtu.jpg')
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    # Role_Choices = (
    #         ('MULTI TEACHER', 'MULTI TEACHER'),
    #         ('PHYSICS TEACHER', 'PHYSICS TEACHER'),
    #         ('CHEMISTRY TEACHER', 'CHEMISTRY TEACHER'),
    #         ('BIOLOGY TEACHER', 'BIOLOGY TEACHER'),
    #         ('ENGLISH TEACHER', 'ENGLISH TEACHER'),
    #         ('CIVICS TEACHER', 'CIVICS TEACHER'),
    #         ('MATHEMATICS TEACHER', 'MATHEMATICS TEACHER'),
    #         ('HISTORY TEACHER', 'HISTORY TEACHER'),
    #         ('GEOGRAPHY TEACHER', 'GEOGRAPHY TEACHER'),
    #         ('KISWAHILI TEACHER', 'KISWAHILI TEACHER'),
    #     )

    # role=models.CharField(verbose_name="role", choices=Role_Choices, max_length=50)
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_cashier=models.BooleanField(default=True)

    hide_email = models.BooleanField(default=True)

    
    


    USERNAME_FIELD="username"
    REQUIRED_FIELDS=['email','phone']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # Method to update push token
    def update_push_token(self, token):
        self.expo_push_token = token
        self.save()






class OTP(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.otp:
            self.otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        super().save(*args, **kwargs)

    def is_valid(self):
        from django.utils import timezone
        return self.created_at >= timezone.now() - timezone.timedelta(minutes=10)














class WatejaWote(models.Model):
    
    
    JinaKamiliLaMteja = models.CharField(verbose_name="Jina Kamili La Mteja", max_length=500,blank=True,null=True)
    SimuYaMteja = models.IntegerField(verbose_name="Namba Ya Simu Ya Mteja", blank=True,null=True)
    EmailYaMteja = models.EmailField(verbose_name="Email Ya Mteja", max_length=500,blank=True,null=True)
    Mahali = models.CharField(verbose_name="Mahali Anapoishi", max_length=500,blank=True,null=True)
    MaelezoYaMteja = models.TextField(verbose_name="Maelezo Ya Mteja", max_length=10000,blank=True,null=True)

    KiasiAnachokopa = models.IntegerField(verbose_name="Kiasi Kiasi Anachokopa", blank=True,null=True, default=0)
    KiasiAlicholipa = models.IntegerField(verbose_name="Kiasi Alicholipa Mpaka Sasa", blank=True,null=True, default=0)
    RejeshoKwaSiku = models.IntegerField(verbose_name="Rejesho Kwa Siku", blank=True,null=True, default=0)
    JumlaYaDeni = models.IntegerField(verbose_name="Jumla Ya Deni Analodaiwa", blank=True,null=True, default=0)
    Riba = models.IntegerField(verbose_name="Riba", blank=True,null=True, default=0)

    AmesajiliwaNa = models.CharField(verbose_name="Amesajiliwa Na ?", max_length=500,blank=True,null=True)

    
    PichaYaMteja = models.ImageField(verbose_name="Picha Ya Mteja", upload_to='media/PichaZaVyakula/',blank=True,null=True)

    #if created is greater than 30 inakuwa false
    Ni_Mteja_Hai = models.BooleanField(default=True, blank=True, null=True)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    
    
    class Meta:
        verbose_name_plural = "Wateja Wote"
        
    
    def __str__(self):
        return f" {self.JinaKamiliLaMteja} "




class WatejaWoteCart(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    JinaKamiliLaMteja = models.CharField(verbose_name="Jina Kamili La Mteja", max_length=500,blank=True,null=True)
    ordered = models.BooleanField(default=False)
    total_price = models.IntegerField(verbose_name="Jumla Ya Kiasi Alicholipa", default=0, blank=True, null=True)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "WatejaWote  Cart"

    def __str__(self):
        return str(self.JinaKamiliLaMteja) + " " + str(self.total_price)
         


class WatejaWoteCartItems(models.Model):
    cart = models.ForeignKey(WatejaWoteCart, on_delete=models.PROTECT) 
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    JinaKamiliLaMteja = models.CharField(verbose_name="Jina Kamili La Mteja", max_length=500,blank=True,null=True)
    
    Mteja = models.ForeignKey(WatejaWote,on_delete=models.PROTECT)
    KiasiChaRejeshoChaSiku = models.FloatField(default=0, blank=True,null=True)
    KiasiChaFainiChaSiku = models.FloatField(default=0, blank=True,null=True)
    #Customer = models.ForeignKey(ProductsCustomers,on_delete=models.PROTECT,blank=True,null=True)
    quantity = models.IntegerField(default=1, blank=True,null=True)
    #table = models.ForeignKey(ProductsTables,on_delete=models.PROTECT,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "WatejaWote  Cart Items"
    
    def __str__(self):
        return f" {self.Mteja.JinaKamiliLaMteja}"
        
    

# @receiver(pre_save, sender=WatejaWoteCartItems)
# def Wateja__correct_price(sender, **kwargs):
#     cart_items = kwargs['instance']
#     price_of_product = WatejaWote.objects.get(id=cart_items.Mteja.id)
#     cart_items.KiasiChaRejeshoChaSiku = cart_items.quantity * float(price_of_product.price)
#     # total_cart_items = CartItems.objects.filter(user = cart_items.user )
#     # cart = Cart.objects.get(id = cart_items.cart.id)
#     # cart.total_price = cart_items.price
#     # cart.save()
