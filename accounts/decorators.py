from accounts.models import Subscriber
from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):     # this function take another function as parameter and add some additional functionality before that function call 
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func

def allowed_users(allowed_roles=[]): # allow users according to permission group defined in admin panel for that user
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request,*args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group != 'admin':
            return redirect('customerPage')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def allow_subscribe_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        user = request.user
        subscriber = Subscriber.objects.get(user=user)
        if request.user.is_authenticated and subscriber.subscribe:
            return redirect('process_subscription')
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func