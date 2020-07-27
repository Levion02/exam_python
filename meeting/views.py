from django.shortcuts import render
from .models import Room, Meeting
# Create your views here.
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {
        'rooms' :
            rooms
    })

def meeting_list(request):
    meetings = Meeting.objects.all()
    return render(request, 'meeting_list.html', {
        'meetings' :  meetings
    })