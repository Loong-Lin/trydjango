from django.shortcuts import render


def index(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "index.html", {})


def about_view(request, *args, **kwargs):
    my_list = [10, 100, 1000, "abc"]
    my_context = {
        "my_text": " This is a book.",
        "my_number": 100,
        "my_list": my_list
    }
    return render(request, "about.html", my_context)
