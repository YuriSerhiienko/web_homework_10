from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, QuoteForm
from .models import Author, Quote, Tag
from django.contrib.auth.decorators import login_required
from django.db.models import Count


def main(request):
    return render(request, "app_hm10/index.html", context={"title": "Homework 10"})


@login_required(login_url="users:login")
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app_hm10:add_author")
    else:
        form = AuthorForm()
    return render(request, "app_hm10/add_author.html", {"form": form})


@login_required(login_url="users:login")
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_hm10:quote_list')
    else:
        form = QuoteForm()

    authors = Author.objects.all().order_by('fullname')  # Отримати список авторів

    context = {
        'form': form,
        'authors': authors,  # Передати список авторів у контекст
    }
    return render(request, 'app_hm10/add_quote.html', context)


def quote_list(request):
    authors = Author.objects.all()
    quotes = Quote.objects.all()
    tags = Tag.objects.annotate(usage_count=Count("quote")).order_by("-usage_count")[
        :10
    ]
    context = {
        "quotes": Quote.objects.all(),
        "tags": tags,
    }
    return render(request, "app_hm10/quote_list.html", context)


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, "app_hm10/author_detail.html", {"author": author})


def tag_detail(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    context = {
        "tag": tag,
    }
    return render(request, "app_hm10/tag_detail.html", context)
