from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')


def contanct(request):
    return render(request, 'mainApp/basic.html', {'values': ['Если у вас\
    остались вопросы, то задавайте их мне по почте', 'silentdesu@gmail.com']})
