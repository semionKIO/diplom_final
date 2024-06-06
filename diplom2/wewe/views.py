from django.shortcuts import render
from .models import Services,Workers
from django.views.generic import DetailView

class WeDetailView(DetailView):
    model = Services
    template_name = 'wewe/new_page.html'

    context_object_name = 'we'

class WorkDetailView(DetailView):
    model = Workers
    template_name = 'wewe/work_detail.html'

    context_object_name = 'work'

def index_we(request):
    review = Services.objects.all()
    return render(request,'wewe/index_we.html', {'review': review})

def workers(request):
    work = Workers.objects.all()
    return render(request,'wewe/workers.html', {'work': work})