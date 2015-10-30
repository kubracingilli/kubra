from django.db import models
from django.contrib import auth
# Create your models here.
class Web(models.Model):
    """
    Web project for base page
    """
    #key,value gibi. Slug. VeritabanındaTutulan, KullanıcınınGöreceği
    TYPES = (
        ('wiki','Wiki Page'),
        ('general','Gneric Page Type'),
        ('personal','My Custom Personel Content'),
    )
    title =models.CharField(max_length=255)
    content =models.TextField() #TextField sınırı yok
    #halil.author dersek halilin yazıları geliyor
    author =models.ForeignKey('auth.User', related_name='author')
    content_type= models.CharField(max_length=8, choices = TYPES,default='general',null=True)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    #kljdhcdskvndszv
    def __str__(self):
        return self.title
