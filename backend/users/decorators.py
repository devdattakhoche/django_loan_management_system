from functools import wraps

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def authenticate_req(func, roles):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        user = request.user
        if not request.user.is_authenticated:
            return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))
        if user.roles not in roles:
            raise PermissionDenied
        return func(request, user, *args, **kwargs)

    return wrapper
