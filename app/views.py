from django.shortcuts import render, redirect


def album_list(request):
    return render("album_list.html")


def album_detail(request):
    return render()


def new_song(request):
    return redirect("album_list.html")
