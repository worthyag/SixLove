from .models import UserProfile


def user_profile(request):
    # Return a dictionary with the user_profile
    return {'user_profile': request.user.userprofile if request.user.is_authenticated else None}
