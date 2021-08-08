from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util
from django.http import HttpResponse
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    markdowner = Markdown()
    getentry = util.get_entry(entry)
    if getentry:
        return render(request, "encyclopedia/entry.html" , {
            "title": entry.capitalize(),
            "content": markdowner.convert(getentry),
            "entry": entry
    })
    else:
        return render(request, "encyclopedia/entrynotfound.html")
        
def search(request):
    markdowner = Markdown()
    new_list = []
    allentries = util.list_entries()
    q = request.GET["q"]
    res = [i for i in allentries if str.capitalize(q) in i]
    getentry = util.get_entry(q)
    if getentry:
        return render(request, "encyclopedia/entry.html" , {
            "title": q.capitalize(),
            "content": markdowner.convert(getentry),
            "entry": q
    })
    else:
        return render(request, "encyclopedia/index.html", {
        "entries": res
    })

def new(request):
    allentries = util.list_entries()
    markdowner = Markdown()
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        message = "Entry already exists"
        if title in allentries:
            return render(request, "encyclopedia/error.html" , {
                "message": message
            }) 
        else:    
            save_entry = util.save_entry(title, content)
            getentry = util.get_entry(title)
            if getentry:
                return render(request, "encyclopedia/entry.html" , {
                    "title": title.capitalize(),
                    "content": markdowner.convert(getentry),
                    "entry": title    
    })
        
    else:
        return render(request, "encyclopedia/new.html")


def edit(request, entry):
    getentry = util.get_entry(entry)
    if request.method == "POST":
        content = request.POST.get("content")
        save_entry = util.save_entry(entry, content)
        
        return render(request, "encyclopedia/entry.html" , {
            "title": entry.capitalize(),
            "content": content, 
            "entry": entry
    })
    else:
        return render(request, "encyclopedia/edit.html" , {
            "title": entry.capitalize(),
            "content": getentry,
            "entry": entry   
    })
    
def randome(request):
    markdowner = Markdown()
    entries_list = util.list_entries()
    randomizer = random.choice(entries_list)
    getentry = util.get_entry(randomizer)
    return render(request, "encyclopedia/entry.html" , {
        "title": randomizer.capitalize(),
        "content": markdowner.convert(getentry),
        "entry": randomizer
    })
            



    
    
     
        

