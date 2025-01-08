from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World :)")
    return render(request, template_name='website/index.html')

def about(request):
    return render(request, template_name='website/about.html')
                        
def contact_us(request):
    return render(request, template_name='website/contact.html')