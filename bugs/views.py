from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Bug, Comment
from .forms import *
from django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def all_bugs(request):
    """ View all bug list"""
    bugs = Bug.objects.all()

    paginator = Paginator(bugs, 6)

    page = request.GET.get('page')

    # Avoid the error message 'That page number is not an integer'
    # Found the solution into Slack from jevgeni
    try:
        bugs = paginator.page(page)
    except PageNotAnInteger:
        bugs = paginator.page(1)
    except EmptyPage:
        bugs = paginator.page(paginator.num_pages)

    return render(request, "bugs.html", {"bugs": bugs})


def bug_detail(request, pk, slug):
    """
    Create a view that returns a single
    Bug object based on the bug ID (pk) and
    render it to the 'bugdetail.html' template.
    Or return a 404 error if the post is not found
    """
    bug = get_object_or_404(Bug, pk=pk, slug=slug)
    # Upvoted part
    is_upvoted = False
    # Checks if current user had previously upvoted the bug
    if bug.upvotes.filter(id=request.user.id).exists():
        is_upvoted = True

    # Comment part
    comments = Comment.objects.filter(bug=bug, reply=None).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            context = request.POST.get('context')
            reply_id = request.POST.get('comment_id')
            comment_qs = None

            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)

            comment = Comment.objects.create(
                bug=bug,
                author=request.user,
                context=context,
                reply=comment_qs)
            comment.save()
            return redirect(bug.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        'bug': bug,
        'is_upvoted': is_upvoted,
        'comments': comments,
        'comment_form': comment_form
        }

    return render(request, "bugdetail.html", context)


@login_required
def create_or_edit_bug(request, pk=None, slug=None):
    """
    Create a view that allows us to create
    or edit a bug depending if the Post ID
    is null or not
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None

    # if the user is not equal to the creator of the bug post
    # he will not be able to edit the post
    if bug is not None:
        if bug.author != request.user:
            messages.error(
                request,
                "This is not your post, you can't edit",
                extra_tags="alert alert-danger")
            return redirect(bug.get_absolute_url())

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
    """ Allow user to upvote or remove the vote from the bug.
         User have to be logged.
    """
    bug = get_object_or_404(Bug, id=request.POST.get('bug_id'))
    if bug.upvotes.filter(id=request.user.id).exists():
        bug.upvotes.remove(request.user)
        is_upvoted = False
    else:
        bug.upvotes.add(request.user)
        is_upvoted = True
    return redirect(bug.get_absolute_url())
