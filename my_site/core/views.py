from django.shortcuts import render
def home(request):
    return render(request, 'core/home.html')
def about(request):
    context = {
        'team_members':['Ahumuza','Sharif','Ben']
    }
    return render(request, 'core/about.html', context)

# Create your views here.
