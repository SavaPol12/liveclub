from django.shortcuts import render, redirect
from .models import note
from .models import place
from .forms import noteForm


def index(request):
    notes = note.objects.order_by('-id')
    return render(request, 'index.html', {'title': 'Главная страница', 'notes': notes})


def about(request):
    return render(request, 'about.html')


def about_us(request):
    return render(request, 'about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = noteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Запись была некорректна'
    form = noteForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)


