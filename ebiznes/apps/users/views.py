from django.shortcuts import render

def base_view(request):
    return render(request, 'base.html')


def base_view_id(request, id):
    return render(request, 'base.html')
