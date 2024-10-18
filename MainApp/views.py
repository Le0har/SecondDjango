from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist
from MainApp.forms import CommentForm, SnippetForm, UserRegistrationForm 
from django.contrib import auth


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == 'GET':
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form,
            }
        return render(request, 'pages/add_snippet.html', context)
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            if request.user.is_authenticated:
                snippet.user = request.user
                snippet.save()
            return redirect("snippets-list")
        return render(request,'pages/add_snippet.html', {'form': form})


def snippets_page(request):
    snippets = Snippet.objects.filter(public=True)
    context = {
            'pagename': 'Просмотр сниппетов',
            'snippets': snippets,
            }
    return render(request, 'pages/view_snippets.html', context)


def snippets_page_user(request):
    current_user = request.user
    snippets = Snippet.objects.filter(user__username=current_user)
    context = {
    'pagename': 'Просмотр моих сниппетов',
    'snippets': snippets,
    }
    return render(request, 'pages/view_snippets.html', context)


def snippet_detail(request, snippet_id):
    comment_form = CommentForm()
    context = {'pagename': 'Просмотр сниппета'}
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        return render(request, "pages/errors.html", context | {"error": f'Snippet with id={snippet_id} not found'})
    else:
        context['snippet'] = snippet
        context['comment_form'] = comment_form
        return render(request, 'pages/snippet_detail.html', context)
    

def snippet_delete(request, snippet_id):
    if request.method == 'GET' or request.method == 'POST':
        snippet = get_object_or_404(Snippet, id=snippet_id)
        snippet.delete()
    return redirect('snippets-list')


def snippet_edit(request, snippet_id): 
    context = {'pagename': 'Редактирование сниппета'}
    snippet = get_object_or_404(Snippet, id=snippet_id)
    if request.method == 'GET':
        form = SnippetForm(instance=snippet)
        return render(request,'pages/add_snippet.html', context | {'form': form})
    if request.method == 'POST':
        data_form = request.POST
        snippet.name = data_form['name']
        snippet.code = data_form['code']
        snippet.save()
        return redirect('snippets-list')


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            context = {
                'pagename': 'PythonBin',
                'errors': ['wrong username or password'],
            }
            return render(request, "pages/index.html", context)
    return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('home')


def create_user(request):
    context = {'pagename': 'Регистрация нового пользователя'}
    if request.method == 'GET':
        form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context['form'] = form
    return render(request, "pages/registration.html", context)


def comment_add(request):
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        print(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.POST.get("username")
            comment.snippet = Snippet.objects.prefetch_related('comments').get(id=1)
            comment.save()
            return redirect(f'/snippets/1')
        raise Http404


    