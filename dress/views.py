from django.shortcuts import render


def dress_list(request):
    return render(request, 'dress/dress_list.html', {})
