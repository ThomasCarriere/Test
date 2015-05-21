from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
import datetime
from django.core.urlresolvers import reverse

from .models import TicketIncident

def Accueil(request):
    Liste_Incidents = TicketIncident.objects.order_by('-id')
    context = {'Liste_Incidents': Liste_Incidents}
    return render(request, 'Incidents/Accueil.html', context)
    
def Detail(request, TicketIncident_id):
    ticketIncident = get_object_or_404(TicketIncident, pk=TicketIncident_id)
    return render(request, 'Incidents/Detail.html', {'ticketIncident': ticketIncident})

def Ajout(request, error_message=""):
    return render(request, 'Incidents/Ajout.html')

def Ajouter(request):
    now = timezone.now()
    description=request.POST.get('description')
    mail=request.POST.get('mail')

    if not description and mail:
        return  render(request, 'Incidents/Ajout.html', {'error_message': "Veuillez entrer une description"})
    elif (not mail and description):
     return render(request, 'Incidents/Ajout.html', {'error_message': "Veuillez entrer une adresse mail"})
    elif (not mail and not description):
     return render(request, 'Incidents/Ajout.html', {'error_message': "Veuillez entrer une description ainsi qu'une adresse mail"})
        

    obj = TicketIncident.objects.create(pub_date=now, Description = description, Mail = mail)

    return HttpResponseRedirect(reverse('Incidents:Accueil'))
    

