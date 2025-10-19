from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView
from django.contrib import messages

ARTICLES = {
    "django-views": {"title": "Django Views 101", "body": "FBV, CBV, render/redirect, контекст и шаблоны."},
}

def index(request):
    context = {"title": "Главная", "today": "Сегодня вы изучаете Django Views"}
    return render(request, "pages/index.html", context)

def calc(request):
    a = request.GET.get("a")
    b = request.GET.get("b")
    op = request.GET.get("op", "add")
    result = None; error = None
    try:
        if a is not None and b is not None:
            x, y = float(a), float(b)
            if op == "add": result = x + y
            elif op == "sub": result = x - y
            elif op == "mul": result = x * y
            elif op == "div":
                if y == 0: error = "Деление на ноль"
                else: result = x / y
            else: error = "Неизвестная операция"
    except ValueError:
        error = "Введите числа в поля A и B"
    return render(request, "pages/calc.html", {"a": a, "b": b, "op": op, "result": result, "error": error})

def feedback(request):
    if request.method == "POST":
        name = (request.POST.get("name") or "").strip()
        msg  = (request.POST.get("message") or "").strip()
        if len(name) < 2:
            messages.error(request, "Имя должно быть не короче 2 символов")
        elif len(msg) < 5:
            messages.error(request, "Сообщение должно быть не короче 5 символов")
        else:
            # тут могли бы сохранить в БД/отправить email
            messages.success(request, f"Спасибо, {name}! Сообщение получено.")
            return redirect("feedback")  # PRG
    return render(request, "pages/feedback.html")

class ArticleDetail(DetailView):
    template_name = "pages/article_detail.html"
    context_object_name = "article"
    def get_object(self):
        slug = self.kwargs["slug"]
        data = ARTICLES.get(slug)
        if not data:
            from django.http import Http404
            raise Http404("Статья не найдена")
        return {"slug": slug, **data}
