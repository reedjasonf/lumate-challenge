from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.core.urlresolvers import reverse

from guestbook.models import Signature

# Create your views here.
def index(request, signed_val):
    context = {'signed_val': signed_val}
    return render(request, 'guestbook/index.html', context)

def sign(request):
    s = Signature(first_name=request.POST['firstname'], last_name=request.POST['lastname'], sign_date=timezone.now(), ip=request.META.get('REMOTE_ADDR'))
    s.save()
    return HttpResponseRedirect(reverse('guestbook:signed_guestbook', kwargs={'signed_val': True}))

def view(request):
    sig_list = Signature.objects.order_by('-sign_date')[0:]
    context = {'sig_list': sig_list}
    #output = ', '.join([p.first_name+" "+p.last_name for p in sig_list])
    return render(request, 'guestbook/gb_view.html', context)
