from django.shortcuts import render


def gdc(request):
    return render(request, 'gdc.html')