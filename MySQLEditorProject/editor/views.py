from django.shortcuts import render, redirect
from .models import CodeSnippet

# Create your views here.
def query_form(request):
    # Your code here
    return render(request, 'editor/query_form.html')
def query_list(request):
    # Your code here
    return render(request, 'editor/query_list.html')
def code_snippet_list(request):
    snippets = CodeSnippet.objects.all()
    return render(request, 'snippet_list.html', {'snippets': snippets})

def code_snippet_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        snippet = CodeSnippet(title=title, content=content)
        snippet.save()
        return redirect('snippet_list')
    return render(request, 'snippet_create.html')

def code_snippet_detail(request, snippet_id):
    snippet = CodeSnippet.objects.get(id=snippet_id)
    return render(request, 'snippet_detail.html', {'snippet': snippet})

def code_snippet_edit(request, snippet_id):
    snippet = CodeSnippet.objects.get(id=snippet_id)
    if request.method == 'POST':
        snippet.title = request.POST.get('title')
        snippet.content = request.POST.get('content')
        snippet.save()
        return redirect('snippet_detail', snippet_id=snippet.id)
    return render(request, 'snippet_edit.html', {'snippet': snippet})

def code_snippet_delete(request, snippet_id):
    snippet = CodeSnippet.objects.get(id=snippet_id)
    snippet.delete()
    return redirect('snippet_list')
