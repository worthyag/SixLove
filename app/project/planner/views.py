from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def calendar(request):
    """"""
    return render(
        request,
        "./planner/tennis.html",
        {
            "title": "Calendar",
        }
    )
