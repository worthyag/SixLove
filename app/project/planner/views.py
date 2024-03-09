import json

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest


from tennis import models as TennisModels
from tennis import forms as TennisForms

# Create your views here.


@login_required
def calendar(request):
    """"""
    tennis_sessions = TennisModels.TennisSession.objects.filter(
        users=request.user
    )

    # Convert the QuerySet to a list of dictionaries
    tennis_sessions_data = [{'category': session.category,
                            'title': session.title, 'date': session.date.strftime("%Y-%m-%d"),
                             'notes': session.notes, 'isCompleted': str(session.is_completed),
                             'id': session.id} for session in tennis_sessions]

    json_data = json.dumps(tennis_sessions_data)

    if request.method == "POST":
        print(request.POST)  # testing

        session_id = request.POST.get("session-id")

        if session_id is not None:

            if (session_id != "X"):
                # Editing Tennis Session
                try:
                    selected_session = get_object_or_404(TennisModels.TennisSession,
                                                         id=int(session_id),
                                                         users=request.user)
                except:
                    return HttpResponseBadRequest("Invalid request")
                form = TennisForms.TennisSessionForm(request.user, request.POST,
                                                     instance=selected_session)

                if form.is_valid():
                    session = form.save(commit=False)

                    # Returning a list of users.
                    users = form.cleaned_data.get("users", [])

                    # Checking if the request user is not already in the list before appending.
                    if request.user not in users:
                        # Setting the current user as one of the users.
                        users.append(request.user)

                    session.save()

                    # Adding the users to the session's many-to-many relationship.
                    session.users.set(users)

                    return redirect("planner:calendar")
                else:
                    return HttpResponseBadRequest("Invalid form data")
            else:
                # Adding Tennis Session
                form = TennisForms.TennisSessionForm(
                    request.user, request.POST)

                if form.is_valid():
                    session = form.save(commit=False)

                    # Returning a list of users.
                    users = form.cleaned_data.get("users", [])

                    # Checking if the request user is not already in the list before appending.
                    if request.user not in users:
                        # Setting the current user as one of the users.
                        users.append(request.user)

                    session.save()

                    # Adding the users to the session's many-to-many relationship.
                    session.users.set(users)

                    return redirect("planner:calendar")
                else:
                    return HttpResponseBadRequest("Invalid form data")

        else:
            # Delete Tennis Session
            if (request.POST["delete-id"] != "delete"):
                try:
                    selected_session = get_object_or_404(TennisModels.TennisSession,
                                                         id=int(
                                                             request.POST["delete-id"]),
                                                         users=request.user)
                except:
                    return HttpResponseBadRequest("Invalid request")

                selected_session.delete()
                return redirect("planner:calendar")
    else:
        # Initialising a new form.
        form = TennisForms.TennisSessionForm(request.user)

    return render(
        request,
        "./planner/calendar.html",
        {
            "title": "Calendar",
            "tennis_sessions": json_data,
            "form": form
        }
    )
