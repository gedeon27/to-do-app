from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapped_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('mainapp:home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapped_func
