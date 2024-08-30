from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import ShortURL
from .forms import ShortURLForm

def home_view(request):
    
    template = "main/templates/home.html"
    
    context = {}
    
    context['form'] = ShortURLForm()
    
    if request.method == 'GET':
        return render(request, template, context)
        
    elif request.method == 'POST':
        
        form = ShortURLForm(request.POST)
        
        if form.is_valid():
            short_obj = form.save()
            
            new_url = request.build_absolute_uri('/') + short_obj.short_url
            org_url = short_obj.org_url
            
            context['new_url'] = new_url
            context['org_url'] = org_url
            
            return render(request, template, context)
        
    context['error'] = form.errors
    
    return render(request, template, context)

def redirect_view(request, short_part):
    try:
        shorturl = ShortURL.objects.get(short_url=short_part)
        
        shorturl.times_followed += 1
        
        shorturl.save()
        
        return HttpResponseRedirect(shorturl.org_url)
    
    except:
        raise Http404("URL does not exist")
