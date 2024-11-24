from django.shortcuts import render
from .models import License

# Create your views here.
def dashboard(request):
    licenses = License.objects.all()
    context = {'licenses': licenses}
    return render(request, 'core/dashboard.html', context)