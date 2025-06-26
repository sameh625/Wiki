import random
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from . import util
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    content = util.get_entry(title)
    if content is not None:
        content = markdown2.markdown(content)
    return render(request, 'encyclopedia/title.html', {
        "title": title.upper(),
        "content": content
    })

def search(request):
    query = request.GET.get('q')
    entries = util.list_entries()
    if query in entries:
        return title(request, query) 
    else:
        results = [entry for entry in entries if query.lower() in entry.lower()]
        return render(request, 'encyclopedia/search.html', {
            "query": query,
            "results": results
        })
    
def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if util.get_entry(title):
            return render(request, "encyclopedia/create.html",{
                "error": "An entry with this title already exists.",
                "title": title,
                "content": content
            })
        else:
            util.save_entry(title,content)
            return redirect('encyclopedia:title', title=title)
    else: 
        return render(request,'encyclopedia/create.html')
    
def edit(request, title):
    if request.method == "POST":
        content = request.POST.get("content")
        util.save_entry(title, content)
        return redirect('encyclopedia:title', title=title)
    else:
        content = util.get_entry(title)
        return render(request, 'encyclopedia/edit.html', {
            'title': title,
            'content': content
        })
    
def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return redirect('encyclopedia:title', title=random_entry)