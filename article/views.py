from django.shortcuts import render
from django.shortcuts import redirect

from article.models import Article


def list_article(request):
    articles = Article.objects.all()
    data = {
        "articles": articles,
    }

    return render(request, 'list.html', data)


def detail_article(request, pk):
    article = Article.objects.get(id=pk)
    data = {
        "article": article,
    }
    return render(request, 'detail.html', data)


def create_article(request):
    if request.method == "POST":
        title = request.POST.get('title', None)
        content = request.POST.get('content', None)
        article = Article.objects.create(
            title=title,
            content=content
        )
        return redirect(list)

    return render(request, 'create.html')
