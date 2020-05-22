from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Bug
from .forms import BugForm

# Create your views here.
def all_bugs(request):
    """ View all bug list
    """
    bugs = Bug.objects.all()
    return render(request, "bugs.html", {"bugs": bugs})

def bug_detail(request, pk):
    """
    Create a view that returns a single
    Bug object based on the bug ID (pk) and
    render it to the 'bugdetail.html' template.
    Or return a 404 error if the post is not found
    """
    bug = get_object_or_404(Bug, pk=pk)
    # bug.views += 1
    # bug.save()
    return render(request, "bugdetail.html", {'bug': bug})

@login_required
def create_or_edit_bug(request, pk=None):
    """
    Create a view that allows us to create
    or edit a bug depending if the Post ID
    is null or not
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.method == "POST":
        form = BugForm(request.POST, instance=bug)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.save()
            # Need to change the redirect to bug detail when I have created it.
            return redirect(all_bugs)
    else:
        form = BugForm(instance=bug)

    return render(request, 'bugform.html', {'form': form})