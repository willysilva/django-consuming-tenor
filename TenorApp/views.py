from django.shortcuts import render,get_object_or_404,redirect
import requests
from django.http import JsonResponse
import json
import urllib
from .models import Tenor
from django.template.loader import render_to_string
# Create your views here.
def home(request):
    tenors=Tenor.objects.order_by('votes')
    return render(request,'TenorApp/home.html',{'tenors':tenors})

def listing(request):
    if request.method=='POST':
        Rdata=dict()
        data=request.POST.get('data')
        hacker_ids=data.split(',')
        for hack_id in hacker_ids:
            try:
                hacker=Tenor.objects.get(id=hack_id)
            except Tenor.DoesNotExist:
                Tenor.objects.create(id=hack_id)
            else:
                pass
        tenors_dict=[]
        tenors=Tenor.objects.order_by('-votes')
        # order by more upvotes desc
        for i in tenors:
            print(i.id)
            tenors_dict+=[[i.id,i.votes,i.downvotes]]
        return JsonResponse(tenors_dict,safe=False)

def upvote(request,pk):
    tenor=get_object_or_404(Tenor,pk=pk)
    tenor.votes=tenor.votes+1
    tenor.save()
    return redirect('TenorApp:home')

def downvote(request,pk):
    tenor=get_object_or_404(Tenor,pk=pk)
    tenor.downvotes=tenor.downvotes+1
    tenor.save()
    return redirect('TenorApp:home')


