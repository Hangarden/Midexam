from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from usermgmt.models import Music

def list_music(request):
    musics = Music.objects.all()
    return render(request, 'usermgmt/list_music.html', {'musics' : musics})


from usermgmt.forms import MusicForm


def create_music(request):
    form = MusicForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_music')

    return render(request, 'usermgmt/music_form.html', {'form': form})


def update_music(request, id):
    music = Music.objects.get(id=id)
    form = MusicForm(request.POST or None, instance=music)

    if form.is_valid():
        form.save()
        return redirect('list_music')

    return render(request, 'usermgmt/music_form.html', {'form': form, 'music': music})


def delete_music(request, id):
    music = Music.objects.get(id=id)

    if request.method == 'POST':
        music.delete()
        return redirect('list_music')

    return render(request, 'usermgmt/music_delete_confirm.html', {'music': music})

