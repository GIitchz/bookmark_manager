from django.shortcuts import render, redirect
from django.http import HttpResponse
import random

# Create your views here.
def home_view(response):
    if response.method == "GET":
        if response.user.is_authenticated:
            name = response.user.username
            not_completed = response.user.bookmark_set.all().filter(isComplete=False)
            if len(not_completed):
                rand_bm = random.choice(not_completed)
                return render(response, 'main/home.html', {"name":name, "bookmark":rand_bm, "is_empty":False})
            else:
                return render(response, 'main/home.html', {"name":name, "is_empty":True})
        else:
            return render(response, 'main/home.html')
    else:
        form = response.POST
        bookmark_id = int(list(form.keys())[1][1:])
        bookmark = response.user.bookmark_set.get(id=bookmark_id)
        bookmark.isComplete = True
        bookmark.save()
        return redirect("/")


def bookmark_list_view(response):
    if response.method=="GET":
        completed = response.user.bookmark_set.all().filter(isComplete=True)
        not_completed = response.user.bookmark_set.all().filter(isComplete=False)
        return render(response, 'main/bookmark_list.html', {"completed":completed, "not_completed":not_completed})
    else:
        bookmark = response.user.bookmark_set.create(url="new bookmark", description="description")
        return redirect(f'../edit/{bookmark.id}', {"bm": bookmark})

def edit_bookmark_view(response, id):
    if response.method == "POST":
        form = response.POST
        print(id, list(form.keys()), form.values)
        bookmark = response.user.bookmark_set.get(id=id)
        if form.get('save') == 'save':
            bookmark.url = form.get('url')
            bookmark.description = form.get('description')
            if form.get('isComplete')=='on':
                bookmark.isComplete = True
            else:
                bookmark.isComplete = False
            bookmark.save()
        elif form.get('delete') == 'delete':
            bookmark.delete()
        completed = response.user.bookmark_set.all().filter(isComplete=True)
        not_completed = response.user.bookmark_set.all().filter(isComplete=False)
        return redirect('../list', {"completed":completed, "not_completed":not_completed})
    else:
        bookmark = response.user.bookmark_set.get(id=id)
        return render(response, 'main/edit_bookmark.html', {"bm":bookmark})