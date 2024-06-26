import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Exists, OuterRef, Q, Max, Count

from . import forms
from . import models


# Create your views here.
@login_required
def tennis(request):
    """
    The view for the tennis page.
    """
    # Getting all the tennis sessions for the request user.
    tennis_sessions = models.TennisSession.objects.filter(
        user=request.user).order_by("date")

    # Filtering for tennis sessions today.
    today_sessions = [
        session for session in tennis_sessions if session.is_tennis_session_scheduled_today()
    ]
    is_today = "No tennis sessions scheduled for today." if len(
        today_sessions) == 0 else ""

    # Filtering for upcoming tennis sessions.
    upcoming_sessions = [session for session in tennis_sessions
                         if not session.is_tennis_session_scheduled_today() and
                         session.date > datetime.date.today()]

    # Filtering for past tennis sessions.
    past_sessions = [session for session in tennis_sessions
                     if not session.is_tennis_session_scheduled_today() and
                     session.date < datetime.date.today()]

    return render(
        request,
        "./tennis/tennis.html",
        {
            "title": "Tennis",
            "today_sessions": today_sessions,
            "is_today": is_today,
            "upcoming_sessions": upcoming_sessions,
            "past_sessions": past_sessions,
        }
    )


@login_required
def add(request):
    """
    The view for the add tennis session page.
    """
    # If the request method is post the form will be submitted if not
    # a new form will be created.
    if request.method == 'POST':
        form = forms.TennisSessionForm(request.POST)

        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            return redirect("tennis:success")
    else:
        # Initialising a new form.
        form = forms.TennisSessionForm()

    return render(
        request,
        "./tennis/add_tennis_session.html",
        {
            "title": "Add Tennis Session",
            "form": form,
        }
    )


@login_required
def edit_tennis_session(request, tennis_session_id):
    """
    The view for the edit tennis session page.
    """
    # Stops users from user navigating to the edit page for a tennis
    # session that doesn't exist or doesn't belong to them.
    try:
        selected_session = get_object_or_404(models.TennisSession,
                                             id=tennis_session_id,
                                             user=request.user)
    except models.TennisSession.DoesNotExist:
        return redirect("tennis:tennis")
    except:
        return redirect("tennis:tennis")

    if request.method == "POST":
        form = forms.TennisSessionForm(request.POST,
                                       instance=selected_session)

        if form.is_valid():
            form.save()
            return redirect("tennis:success")
    else:
        form = forms.TennisSessionForm(instance=selected_session)

    return render(
        request,
        "./tennis/edit_tennis_session.html",
        {
            "title": "Edit Tennis Session",
            "form": form
        }
    )


@login_required
def delete_tennis_session(request, tennis_session_id):
    """
    The view for the delete tennis session page.
    """
    # Stops users from user navigating to the delete page for a tennis
    # session that doesn't exist or doesn't belong to them.
    try:
        selected_session = get_object_or_404(models.TennisSession,
                                             id=tennis_session_id,
                                             user=request.user)
    except models.TennisSession.DoesNotExist:
        return redirect("tennis:tennis")
    except:
        return redirect("tennis:tennis")

    if request.method == "POST":
        selected_session.delete()
        return redirect("tennis:tennis")

    return render(
        request,
        "./tennis/delete_tennis_session.html",
        {
            "title": "Delete Tennis Session",
            "tennis_session": selected_session
        }
    )


@login_required
def success(request):
    """The view for the success page."""
    return render(
        request,
        "./tennis/success.html",
        {
            "title": "Success"
        }
    )


@login_required
def learn(request):
    """The view for the learn page."""
    # resources = models.Resource.objects.all().order_by("title")

    # To allow the user to search through the list of resources.
    # Getting the search query from the request.
    query = request.GET.get("resource-search", "")

    # To allow the user to filter the resources.
    filter_option = request.GET.get("filter", "")

    # Querying the data.
    resources = models.Resource.objects.filter(
        Q(title__icontains=query) | Q(tags__name__icontains=query)
    )

    # Applying additional filters based on the filter_option.
    if filter_option == "fundamentals":
        resources = resources.filter(
            tags__name__in={"forehand", "backhand", "serve"}
        ).order_by("title")

    elif filter_option == "fitness":
        resources = resources.filter(
            tags__name__in=["agility", "stretching"]
        ).order_by("title")

    elif filter_option == "stretch":
        resources = resources.filter(
            tags__name="stretching"
        ).order_by("title")

    elif filter_option == "forehand":
        resources = resources.filter(
            tags__name="forehand"
        ).order_by("title")

    elif filter_option == "backhand":
        resources = resources.filter(
            tags__name="backhand"
        ).order_by("title")

    elif filter_option == "volley":
        resources = resources.filter(
            tags__name="volley"
        ).order_by("title")
    elif filter_option == "slice":
        resources = resources.filter(
            tags__name="slice"
        ).order_by("title")

    return render(
        request,
        "./tennis/learn.html",
        {
            "title": "Learn",
            "resources": resources,
            "search_query": query,
            "filter_option": filter_option,
        }
    )


@login_required
def resource(request, resource_id):
    """The view for the resource page."""
    try:
        resource = get_object_or_404(models.Resource, id=resource_id)
        sections = resource.sections.all() if resource.resource_type == "article" else None

        # Splitting content for sections with type "bullet_points" or "paragraph".
        if sections is not None:
            for section in sections:
                if section.section_type in ["bullet_points", "paragraph"]:
                    section.split_content = section.content.split("\n")

        return render(
            request,
            "./tennis/resource.html",
            {
                "title": resource.title,
                "resource": resource,
                "sections": sections
            }
        )
    except:
        return render(
            request,
            "./tennis/resource.html",
            {
                "title": "Resource Not Found",
                "resource": None,
                "sections": None
            }
        )
