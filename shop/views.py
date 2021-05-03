from django.shortcuts import render,redirect
from django.http import HttpResponse
from.forms import Bookform
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
import datetime
def index(request,id):
    product=Product.objects.filter(Categories=id)
    print(Product.objects.filter(Categories=id))
    allpr=Product.objects.all()
    return render(request,'shop/index.html',{'product':product,'allpr':allpr})
def allprod(request):
    allpr=Product.objects.all()
    return render(request,'shop/index.html',{'allpr':allpr})
def about(req):
    return render(req,'shop/about.html')
def contact(req):
    if req.method=='POST':
        Name=req.POST.get('name')
        Email=req.POST.get('email')
        Contact=req.POST.get('phone')
        Msg=req.POST.get('msg')
        saving=Contact_us(Name=Name,Email=Email,Contact=Contact,message=Msg)
        saving.save()
        messages.success(req,"Your details has been collected!")
        return redirect('/')
    return render(req,'shop/contact.html')
def search(req):
    return HttpResponse("search page")
def pv(req):
    return HttpResponse("product view page")
def tracker(req):
    return HttpResponse("tracker page")
def categ(request):
    cate=Categorie.objects.all()
    allpr=Product.objects.all()
    return render(request,'shop/categ.html',{'cate':cate,'allpr':allpr})
    #categvalue=request
def uploadf(request):
    if request.method=='POST':
        form = Bookform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/shop')
        else:
            form = Bookform()
        return render(request,'upload_img.html',{'form':form})
    return render(request,'upload_img.html',{'form':form})
def vp(request,id):
    product=Product.objects.filter(id=id)
    if request.method == 'POST':
        Username=User.objects.get(username=request.user)
        review1=request.POST.get('review')
        id1=id
        save1=review(username=Username,review=review1,idr=id1)
        save1.save()
    vir=review.objects.filter(idr=id)
    return render(request,'shop/viewproduct.html',{'product':product,'vir':vir})
def buy(request):
    if request.method=='POST':
        Address=request.POST.get('Address')
        Contact=request.POST.get('Contact')
        Username=User.objects.get(username=request.user)
        product=request.POST.get('Product')
        color=request.POST.get('color')
        model=request.POST.get('model')
        size=request.POST.get('size')
        save2=Buy(Productdet=product,Address=Address,Contact=Contact,Username=Username,size=size,model=model,color=color)
        save2.save()
        messages.success(request,'Your Order has been placed')
    return redirect('/')
def cart(request):
    if request.method=='POST':
        Username=User.objects.get(username=request.user)
        name=request.POST.get('pr_name')
        desc=request.POST.get('pr_desc')
        pr_date=datetime.datetime.now()
        pr_price=request.POST.get('pr_price')
        pr_img=request.POST.get('pr_img')
        Model=request.POST.get('model')
        color=request.POST.get('color')
        save3=usercart(pr_name=name,pr_img=pr_img,Model=Model,pr_date=pr_date,pr_desc=desc,pr_price=pr_price,color=color,username=Username)
        save3.save()
    cruser=User.objects.get(username=request.user)
    product=usercart.objects.filter(username=cruser)
    return render(request,'shop/cart.html',{'product':product})
def cartview(request,id):
    product=usercart.objects.filter(id=id)
    if request.method == 'POST':
        Username=User.objects.get(username=request.user)
        review1=request.POST.get('review')
        id1=id
        save1=review(username=Username,review=review1,idr=id1)
        save1.save()
    vir=review.objects.filter(idr=id)
    return render(request,'shop/cartviewprd.html',{'product':product,'vir':vir})
def search(request):
    if request.method == 'POST':
        query=request.POST.get('query')
        product1=Product.objects.filter(pr_name__icontains=query)
        product2=Product.objects.filter(pr_desc__icontains=query)
        product = product1.union(product2)
    return render(request,'shop/search.html',{'product':product})
# def reviews(request):
#     if request.method == 'POST':
#         Username=User.objects.get(username=request.user)
#         review1=request.POST.get('review')
#         save1=review(username=Username,review=review1)
#         save1.save()
#     return redirect('/')
# Create your views here.
