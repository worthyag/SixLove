import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from . import forms
from . import models


# Create your views here.
@login_required
def tennis(request):
    """"""
    tennis_sessions = models.TennisSession.objects.filter(
        user=request.user).order_by("date")

    today_sessions = [
        session for session in tennis_sessions if session.is_tennis_session_scheduled_today()
    ]
    is_today = "No tennis sessions scheduled for today." if len(
        today_sessions) == 0 else ""

    upcoming_sessions = [session for session in tennis_sessions
                         if not session.is_tennis_session_scheduled_today() and
                         session.date > datetime.date.today()]

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
    """"""
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
    return render(
        request,
        "./tennis/success.html",
        {
            "title": "Success"
        }
    )


@login_required
def learn(request):
    resources = models.Resource.objects.all().order_by("title")

    return render(
        request,
        "./tennis/learn.html",
        {
            "title": "Learn",
            "resources": resources,
        }
    )


@login_required
def resource(request, resource_id):
    try:
        resource = get_object_or_404(models.Resource, id=resource_id)
        sections = resource.sections.all() if resource.resource_type == "article" else None

        # Splitting content for sections with type "bullet_points" or "paragraph"
        if sections is not None:
            for section in sections:
                if section.section_type in ["bullet_points", "paragraph"]:
                    section.split_content = section.content.split("\n")

        # print(type(sections))

        # for section in sections:
        #     print("hello")

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
