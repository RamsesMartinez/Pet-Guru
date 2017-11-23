from django.shortcuts import render
from chat.models import Room, Message
from home.models import Question
from home.forms import BaseForm

from django.contrib.auth.decorators import login_required


@login_required
def chat_room(request, label):    
    question_sel = Question.objects.get(pk=label)
    room, created = Room.objects.get_or_create(label=label, question=question_sel)
    messages = reversed(room.messages.order_by('-timestamp')[:50])
    if question_sel.status == 'OP':
        question_sel.status = 'RP'
        question_sel.user_response = request.user
        question_sel.save()

    if request.method == 'POST':                
        message = request.POST.get('message')        
        handler = request.POST.get('handler')
        new_mess = Message.objects.create(room=room,handle=handler,message=message)
        new_mess.save()
        
    
    return render(request, "room.html", {
        'label': label,
        'room': room,
        'messages': messages,
    })