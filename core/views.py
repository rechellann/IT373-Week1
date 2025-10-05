from django.shortcuts import render, get_object_or_404
from .models import Announcement


# Create your views here.
 
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def announcements_list(request):
    announcements = Announcement.objects.order_by('-created_at')
    return render(request, "announcements_list.html", {'announcements': announcements})


def announcement_detail(request, id):
    announcement = get_object_or_404(Announcement, id=id)
    return render(request, "announcement_detail.html", {'announcement': announcement})
