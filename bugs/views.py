from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Bug
from .forms import BugForm
from django.http import Http404

# Create your views here.
def all_bugs(request):
    """ View all bug list
    """
    bugs = Bug.objects.all()
    return render(request, "bugs.html", {"bugs": bugs})

def bug_detail(request, pk, slug):
    """
    Create a view that returns a single
    Bug object based on the bug ID (pk) and
    render it to the 'bugdetail.html' template.
    Or return a 404 error if the post is not found
    """
    bug = get_object_or_404(Bug, pk=pk, slug=slug)
    is_upvoted = False
    # Checks if current user had previously upvoted the bug
    if bug.upvotes.filter(id=request.user.id).exists():
        is_upvoted = True
    return render(request, "bugdetail.html", {'bug': bug, 'is_upvoted': is_upvoted})

@login_required
def create_or_edit_bug(request, pk=None, slug=None):
    """
    Create a view that allows us to create
    or edit a bug depending if the Post ID
    is null or not
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None

    # if the user is not equal to the creator of the bug post show error 404
    if bug is not None:
        if bug.author != request.user:
            raise Http404()

    if request.method == "POST":
        form = BugForm(request.POST, instance=bug)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.save()
            return redirect(bug.get_absolute_url())
    else:
        form = BugForm(instance=bug)

    return render(request, 'bugform.html', {'form': form})

@login_required
def upvote_bug(request):
    # Allow user to upvote or remove the vote from the bug. User have to be logged.
    bug = get_object_or_404(Bug, id=request.POST.get('bug_id'))
    if bug.upvotes.filter(id=request.user.id).exists():
        bug.upvotes.remove(request.user)
        is_upvoted = False
    else:
        bug.upvotes.add(request.user)
        is_upvoted = True
    return redirect(bug.get_absolute_url())