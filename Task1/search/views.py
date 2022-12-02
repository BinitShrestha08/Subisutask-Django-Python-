# views, functions that takes http requests and returns http response

from django.shortcuts import render
import requests

def search(request):
    return render(request, 'index.html')


def get_asn(request):
    url="https://stat.ripe.net/data/announced-prefixes/data.json?resource="
    ASN = request.GET.get('asn')
    response= requests.get(url+ASN).json()
    return render(request, 'asn.html', {'response': response})
