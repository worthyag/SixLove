from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.utils import timezone
from django.db.models import Exists, OuterRef, Q, Count, Max, F

# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, authenticate

from tennis import models as TennisModels

from .forms import CustomUserCreationForm
# Create your views here.


def home(request):
    """
    The view for the home page. Displays two different pages depending
    on the status of is_authenticated:
        - Landing Page: gives potentials user the chance to learn about SixLove.
        - Stats Page: where users can view their stats and progress.
    """
    # Only displays the user's stats if they are authenticated.
    if request.user.is_authenticated:
        # Getting all the request user's tennis sessions.
        tennis_sessions = TennisModels.TennisSession.objects.filter(
            user=request.user
        )

        # CHART 1
        # ========

        # To allow the user to filter the chart.
        filter_option = request.GET.get("filter", "")

        # Applying filters based on the filter_option.
        if filter_option == "completed":
            tennis_sessions = tennis_sessions.filter(is_completed=True)

        elif filter_option == "not_completed":
            tennis_sessions = tennis_sessions.filter(is_completed=False)

        elif filter_option == "upcoming":
            tennis_sessions = tennis_sessions.filter(
                date__gt=timezone.now().date())

        elif filter_option == "past":
            tennis_sessions = tennis_sessions.filter(
                date__lt=timezone.now().date())

        forehand_sessions = tennis_sessions.filter(category="forehand")
        backhand_sessions = tennis_sessions.filter(category="backhand")
        serve_sessions = tennis_sessions.filter(category="serve")
        volley_sessions = tennis_sessions.filter(category="volley")
        slice_sessions = tennis_sessions.filter(category="slice")
        smash_sessions = tennis_sessions.filter(category="smash")
        drop_shot_sessions = tennis_sessions.filter(category="drop-shot")
        agility_sessions = tennis_sessions.filter(category="agility")
        stamina_sessions = tennis_sessions.filter(category="stamina")
        other_sessions = tennis_sessions.filter(category="other")

        tennis_sessions_per_month = TennisModels.TennisSession.objects.filter(
            user=request.user
        )

        # CHART 2
        # ========

        # To allow the user to filter the chart.
        filter_monthly = request.GET.get("filter-monthly", "")

        # Applying filters based on the filter_option.
        if filter_monthly == "forehand":
            tennis_sessions_per_month = tennis_sessions_per_month.filter(
                category="forehand")

        elif filter_monthly == "backhand":
            tennis_sessions_per_month = tennis_sessions_per_month.filter(
                category="backhand")

        elif filter_monthly == "serve":
            tennis_sessions_per_month = tennis_sessions_per_month.filter(
                category="serve")

        elif filter_monthly == "volley":
            tennis_sessions_per_month = tennis_sessions_per_month.filter(
                category="volley")

        elif filter_monthly == "slice":
            tennis_sessions_per_month = tennis_sessions_per_month.filter(
                category="slice")

        elif filter_monthly == "smash":
            tennis_sessions_per_month = tennis_sessions_per_month.filter(
                category="smash")

        elif filter_monthly == "drop-shot":
            tennis_sessions_per_month = tennis_sessions_per_month.filter(
                category="drop-shot")

        elif filter_monthly == "agility":
            tennis_sessions_per_month = tennis_sessions_per_month.filter(
                category="agility")

        elif filter_monthly == "stamina":
            tennis_sessions_per_month = tennis_sessions_per_month.filter(
                category="stamina")

        elif filter_monthly == "other":
            tennis_sessions_per_month = tennis_sessions_per_month.filter(
                category="other")

        current_year = timezone.now().year

        jan_sessions = tennis_sessions_per_month.filter(
            date__year=current_year, date__month=1)
        feb_sessions = tennis_sessions_per_month.filter(
            date__year=current_year, date__month=2)
        mar_sessions = tennis_sessions_per_month.filter(
            date__year=current_year, date__month=3)
        apr_sessions = tennis_sessions_per_month.filter(
            date__year=current_year, date__month=4)
        may_sessions = tennis_sessions_per_month.filter(
            date__year=current_year, date__month=5)
        jun_sessions = tennis_sessions_per_month.filter(
            date__year=current_year, date__month=6)
        jul_sessions = tennis_sessions_per_month.filter(
            date__year=current_year, date__month=7)
        aug_sessions = tennis_sessions_per_month.filter(
            date__year=current_year, date__month=8)
        sep_sessions = tennis_sessions_per_month.filter(
            date__year=current_year, date__month=9)
        oct_sessions = tennis_sessions_per_month.filter(
            date__year=current_year, date__month=10)
        nov_sessions = tennis_sessions_per_month.filter(
            date__year=current_year, date__month=11)
        dec_sessions = tennis_sessions_per_month.filter(
            date__year=current_year, date__month=12)

        return render(
            request,
            "./registration/index.html",
            {
                "title": f"{request.user} - Home",
                "tennis_sessions": tennis_sessions,
                "filter_option": filter_option,
                "filter_monthly": filter_monthly,
                "forehand_sessions": forehand_sessions,
                "backhand_sessions": backhand_sessions,
                "serve_sessions": serve_sessions,
                "volley_sessions": volley_sessions,
                "slice_sessions": slice_sessions,
                "smash_sessions": smash_sessions,
                "drop_shot_sessions": drop_shot_sessions,
                "agility_sessions": agility_sessions,
                "stamina_sessions": stamina_sessions,
                "other_sessions": other_sessions,
                "jan_sessions": jan_sessions,
                "feb_sessions": feb_sessions,
                "mar_sessions": mar_sessions,
                "apr_sessions": apr_sessions,
                "may_sessions": may_sessions,
                "jun_sessions": jun_sessions,
                "jul_sessions": jul_sessions,
                "aug_sessions": aug_sessions,
                "sep_sessions": sep_sessions,
                "oct_sessions": oct_sessions,
                "nov_sessions": nov_sessions,
                "dec_sessions": dec_sessions,
            }
        )
    else:
        return render(
            request,
            "./registration/index.html",
            {
                "title": "Home"
            }
        )


def signup(request):
    """"""
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()

    return render(
        request,
        "./registration/signup.html",
        {
            "title": "Sign Up",
            "form": form
        }
    )


def user_login(request):
    """"""
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(
        request,
        "./registration/login.html",
        {
            "title": "Login",
            "form": form
        }
    )
