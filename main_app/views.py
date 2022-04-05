from dbm.ndbm import library
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Comment
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
from .models import File
from django.shortcuts import redirect

# Create your views here.
#HOME VIEW
class Home(TemplateView):#home page, when you sign in you land here
    template_name = "home.html"

#UPLOADING FUNCTION
def upload(request): 
        context = {}   
        if request.method == 'POST':
            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name, uploaded_file)
            context['url'] = fs.url(name)     
        return render(request, 'upload.html', context)

#FILE LIST FUNCTION
def file_list(request):
    files = File.objects.all()
    return render(request, 'file_list.html', { 'files' : files })

#FILE UPLOAD #getting required bug from this 
def file_upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')#redirects to list of files
    else:
        form = FileForm()
    return render(request, 'file_upload.html', { 'form' : form })
    

    


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





                