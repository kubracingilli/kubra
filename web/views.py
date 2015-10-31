from django.shortcuts import render, redirect
from web.models import Web
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

login_url = '/login/'
# Create your views here.
def webindex(request):
    print(dir(request))
    pages=Web.objects.all()
    #return HttpResponse("Bu bir flewkflaewj")
    contents=[]
    #response=HttpResponse()
    #response['Text']=[]
    #print(type(response['Text']))
    for page in pages:
        contents.append(page.content)
    return HttpResponse(contents)

def page(request,content_id):
    #filter array döndürür get tek döndürür
    page= Web.objects.get(id=content_id)
    if not page:
        raise Http404
    page.view_count+=1
    #+1 ile view count arttırılıyor ama obje üzerne kayıt olmuyor. Save yaparak kayıt etmiş oluyoruz.
    page.save()
    return HttpResponse('Title: %s <br>View count:%s' %(page,page.view_count))
    #page= Web.objects.get(id=content_id)
    #return HttpResponse(page)

def weblogin(request):
    if request.method=='POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
        return redirect('/login')
    if request.user.is_authenticated:
        print(dir(request.user))
    return render(request, 'web/login.html')

#decorater
@login_required(login_url=login_url)
def webindex_html(request):
    #pages= Web.objects.all()
    pages= Web.objects.order_by('created_at')
    data = {
        'pages': pages,
    }
    return render(request, 'web/index.html',data)
    
@login_required(login_url=login_url)
def page_html(request,content_id):
    page=Web.objects.get(id=content_id)
    data={
        'page': page,
        'favorite_animal': 'Horse',
    }
    return render(request, 'web/page.html',data)
