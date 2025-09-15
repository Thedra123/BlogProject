from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from . import data

# initialize repository and seed posts
repo = data.PostRepository()
repo.seed()


def post_list(request):
    """Display list of posts, optionally filtered by search query (?q=...)"""
    posts = repo.all()
    query = request.GET.get("q")

    if query:
        query_lower = query.lower()
        posts = [
            p for p in posts
            if query_lower in p.title.lower() or query_lower in p.content.lower()
        ]

    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, post_id: int):
    """Show a single post by ID, or render 404 page if not found."""
    post = repo.get(post_id)
    if not post:
        return render(request, "blog/not_found.html", status=404)
    return render(request, "blog/post_details.html", {"post": post})


@require_http_methods(["POST"])
def post_delete(request, post_id: int):
    """Delete a post and redirect to home, or return 404 if not found."""
    deleted = repo.delete(post_id)
    if not deleted:
        return HttpResponse("Post not found", status=404)
    return redirect("/")
