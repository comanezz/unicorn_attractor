from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.db.models import Count

# Create your views here.
def all_features(request):
    """ View all feature list
    """
    features = Feature.objects.all()
    return render(request, "features.html", {'features': features})

def feature_detail(request, pk, slug):
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
    comments = Comment.objects.filter(bug=bug, reply=None).order_by('id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            context = request.POST.get('context')
            reply_id = request.POST.get('comment_id')
            comment_qs = None

            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)

            comment = Comment.objects.create(bug=bug, author=request.user, context=context, reply=comment_qs)
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