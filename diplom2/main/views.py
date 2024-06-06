from django.shortcuts import render, redirect
from django.http import  HttpResponse
from .models import Review
from .forms import ReviewForm

def index(request):
    return render(request,'main/index.html')

def reviews(request):

    review = Review.objects.all()
    return render(request,'main/reviews.html', {'review': review})

def rate(request):
    error = ''
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма не верна!"
    else:
        form = ReviewForm()
    context = {'form': form,
               'error': error}
    return render(request, 'main/rate.html', context)

def contact(request):
    return render(request,'main/contact.html')

def documents(request):
    return render(request,'main/documents.html')

