from django.shortcuts import render


def About(request):

    return render(request, 'company/about.html')


def Contact(request):

    return render(request, 'company/contact.html')