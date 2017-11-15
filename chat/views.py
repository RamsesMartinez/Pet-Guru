from django.shortcuts import render
from chat.models import Room
from home.models import Question
from django.contrib.auth.decorators import login_required


@login_required
def chat_room(request, label):    
    question_sel = Question.objects.get(pk=label)
    room, created = Room.objects.get_or_create(label=label,question=question_sel)
    messages = reversed(room.messages.order_by('-timestamp')[:50])
    
    return render(request, "room.html", {
        'room': room,
        'messages': messages,
    })