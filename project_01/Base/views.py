from django.shortcuts import render

# Create your views here.
def all_chai(request):
    return render(request, 'Base/all_base.html')