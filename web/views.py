from django.shortcuts import render
from django.http import JsonResponse
from .tools import *
from .models import *
import json


# Create your views here.
def index(request):
    if request.method == 'GET':

        return render(request, 'web/main.html',
            {
            'projects': Projects.objects.all().order_by('-date'),
        })

    elif request.method == 'POST':  

        content = json.loads(request.body)
        if content is None:
            return JsonResponse({'status': 'error', 'message': 'No data received'}, status=402)

        name = str(content['name'])
        email = str(content['email'])
        subject = str(content['subject'])
        message = str(content['message'])

        if name == '' or email == '' or subject == '' or message == '':
            return JsonResponse({'status': 'error', 'message': 'Fill all entries'})

        #funcion para comprobar que es un correo valido con expresion regular
        if es_correo_valido(email):
            # Si el correo es válido, se crea un nuevo objeto de tipo Contacto
            try:  
                db = Contact(name = name, email = email, subject = subject, message = message)
                db.save()
            except:
                return JsonResponse({'error': 'Error saving data'}, status=402)
            # Se envía el correo
            try:
                send_mail(email, name, subject, message)
            except:
                return JsonResponse({'error': 'Error sending email'}, status=402)

            return JsonResponse({"ok": "The mail is send."}, status=200)

        else:
            return JsonResponse({"error": "The message could not be sent"}, status=400)




