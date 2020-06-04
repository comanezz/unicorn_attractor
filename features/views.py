from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
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
    feature object based on the feature ID (pk) and
    render it to the 'featuredetail.html' template.
    Or return a 404 error if the post is not found
    """
    feature = get_object_or_404(feature, pk=pk, slug=slug)
    # Upvoted part
    is_upvoted = False
    # Checks if current user had previously upvoted the feature
    if feature.upvotes.filter(id=request.user.id).exists():
        is_upvoted = True

    # Comment part
    comments = Comment.objects.filter(feature=feature, reply=None).order_by('id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            context = request.POST.get('context')
            reply_id = request.POST.get('comment_id')
            comment_qs = None

            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)

            comment = Comment.objects.create(feature=feature, author=request.user, context=context, reply=comment_qs)
            comment.save()
            return redirect(feature.get_absolute_url())
    else:
        comment_form = CommentForm()

    context = {
        'feature': feature,
        'is_upvoted': is_upvoted,
        'comments': comments,
        'comment_form': comment_form
        }

    return render(request, "featuredetail.html", context)

@login_required
def create_or_edit_feature(request, pk=None, slug=None):
    """
    Create a view that allows us to create
    or edit a feature depending if the Post ID
    is null or not
    """
    feature = get_object_or_404(Feature, pk=pk) if pk else None

    # if the user is not equal to the creator of the feature post he will not be able to edit the post
    if feature is not None:
        if feature.author != request.user:
            messages.error(request, "This is not your post, you can't edit", extra_tags="alert alert-danger")
            return redirect(feature.get_absolute_url())

    if request.method == "POST":
        form = FeatureForm(request.POST, instance=feature)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.author = request.user
            feature.save()
            # Uncomment once I set up feature detail view correctly
            # return redirect(feature.get_absolute_url())
            return redirect(all_features)
    else:
        form = FeatureForm(instance=feature)

    return render(request, 'featureform.html', {'form': form})