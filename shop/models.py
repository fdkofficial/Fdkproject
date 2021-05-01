from django.db import models
class Categorie(models.Model):
    title=models.CharField(max_length=255)
    img=models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.title
class Product(models.Model):
    pr_id=models.AutoField
    pr_name=models.CharField(max_length=250)
    pr_date=models.DateField()
    pr_desc=models.CharField(max_length=500)
    pr_price=models.IntegerField()
    pr_img=models.ImageField(upload_to="shop/image")
    Model=models.CharField(max_length=266)
    color=models.CharField(max_length=266,default='Black')
    Categories=models.ForeignKey(Categorie,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.pr_name
class Book(models.Model):
    title=models.CharField(max_length=255)
    img_src=models.ImageField() 
    def __str__(self):
        return self.title
class Buy(models.Model):
    Productdet=models.CharField(max_length=255)
    Address=models.CharField(max_length=600)  
    Contact=models.CharField(max_length=600)  
    Username=models.CharField(max_length=600) 
    color=models.CharField(max_length=600) 
    size=models.CharField(max_length=600,null=True,blank=True) 
    model=models.CharField(max_length=600,null=True,blank=True) 
class Contact_us(models.Model):
    Name=models.CharField(max_length=255)
    Email=models.CharField(max_length=255)
    Contact=models.CharField(max_length=255)
    message=models.CharField(max_length=255)
    def __str__(self):
        return self.Name
class Moreimages(models.Model):
    products=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True,related_name='images')
    images=models.ImageField()
    def __str__(self):
        return self.products.pr_name
    
# Create your models here.
class review(models.Model):
    username=models.CharField(max_length=255)
    review=models.CharField(max_length=255)
    idr=models.CharField(max_length=255,null=True,blank=True)
class usercart(models.Model):
    username=models.CharField(max_length=255)
    pr_id=models.AutoField
    pr_name=models.CharField(max_length=250)
    pr_date=models.DateField()
    pr_desc=models.CharField(max_length=500)
    pr_price=models.IntegerField()
    pr_img=models.ImageField(upload_to="shop/image")
    Model=models.CharField(max_length=266)
    color=models.CharField(max_length=266,default='Black')
    