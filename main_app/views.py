from dbm.ndbm import library
from pipes import Template
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import TemplateView
from .models import Comment
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
from .models import File
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
#HOME VIEW
class Home(TemplateView):#home page, when you sign in you land here
    template_name = "home.html"
    #come back to this if i want home page to render a list, it will need to have same logic as list view
  

#USER FUNCION
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    files = File.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'files': files})



#django auth
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            return render(request, 'signup.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/intro')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'login.html', {'form': form})
        else: 
            return render(request, 'signup.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
        
#CLASS FILE LIST
class FileListView(ListView):
    model = File
    template_name = 'class_file_list.html'
    context_object_name = 'files'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        file_name = self.request.GET.get("file_name")
        print(file_name)
        if file_name != None:
            context["files"] = File.objects.filter(file_name__icontains=file_name)#filters name 
            context["header"] = f"Searching for {file_name}"
        else:
            context['files'] = File.objects.all()
            context["header"] = "ALL FILES"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/class/files')

#CLASS FILE DETAIL VIEW
class FileDetail(DetailView):
    model = File
    template_name = "class_file_detail.html"
    #context_object_name = 'files'

#COMMENTING OUT CODE TO RENDER SINGULAR FILE IN THE DETAIL
'''
def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        file_name = self.request.GET.get("file_name")
        print(file_name)
        if file_name != None:
            context["files"] = File.objects.filter(file_name__icontains=file_name)#filters name 
            context["header"] = f"Searching for {file_name}"
        else:
            context['files'] = File.objects.all()
            context["header"] = "ALL FILES"
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/class/files/')

'''

    
#CLASS FILE UPDATE VIEW
class FileUpdate(UpdateView):
    model = File
    #form_class = FileForm
    fields = '__all__'
    template_name = 'file_upload.html'
    
    def form_valid(self, form):
            self.object = form.save(commit=False)
            #self.object.user = self.request.user
            self.object.save()
            return HttpResponseRedirect('/class/files')
  


#CLASS FILE UPLOAD
class UploadFileView(CreateView):
    model = File
    form_class = FileForm
    success_url = reverse_lazy('class_file_list')
    template_name = 'file_upload.html'


#FILE UPLOAD #getting required bug from this 
def file_upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('class_file_list')#redirects to list of files
    else:
        form = FileForm()
    return render(request, 'file_upload.html', { 'form' : form })



#FILE DELETE FUNCTION
def delete_file(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk=pk)
        file.delete()
    return HttpResponseRedirect('/class/files')



#FILE LIST FUNCTION
'''
def file_list(request):
    files = File.objects.all()
    return render(request, 'file_list.html', { 'files' : files })
'''









    


#INTRO VIEW
class Intro(TemplateView): #intro page that lets you learn about how to use app. may want to switch this to be the landing page later
    template_name = "intro.html"

#COMMENTS VIEW
class Comments(TemplateView):
    template_name= "comments.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.all() # Here we are using the model to query the database for us.
        return context

    
    


    






#DOES LIBRARY NEED TO BE ITS OWN MODEL?
#FAKEABASE
class Library:
    def __init__(self, file_name, category, season, date_created, ):
        self.file_name = file_name
        self.category = category
        self.season = season
        self.date_created = date_created

library = [
    Library('A0001', 'BOTTOMS', 'FALL 23', '10/22/22'),
    Library('A0001', 'BOTTOMS', 'FALL 23', '10/22/22'),
    Library('A0001', 'BOTTOMS', 'FALL 23', '10/22/22'),
    Library('A0001', 'BOTTOMS', 'FALL 23', '10/22/22'),
]
    
class My_Library(TemplateView):
    template_name = 'my_library.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["library"] = library 
        return context

        
#model has to be singular, class has to be uppercase





                