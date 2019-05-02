import traceback


from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import urllib.request
import urllib.parse
import json
from adminPortal.models import GroupMaster, TblCities


def main(request):
    return render(request, "main.html", )

def test(request):
    return render(request, "test1.html", )

def carpool(request):
    try:
        fromsrc = request.GET.get('from')
        dest = request.GET.get('dest')

        fromsrc = fromsrc.split(",")[0]
        dest = dest.split(",")[0]

        print("fromsrc:",fromsrc)
        print("dest:", dest)
        page = request.GET.get('page', 1)
        group = GroupMaster.objects.filter(origin_name__icontains=fromsrc).filter(dest_name__icontains=dest)
        paginator = Paginator(group, 4)
        try:
            gamelist = paginator.page(page)
        except PageNotAnInteger:
            gamelist = paginator.page(1)
        except EmptyPage:
            gamelist = paginator.page(paginator.num_pages)
        print("group.count()::",group.count())
        return render(request, "car-pool.html",{'grouplist':gamelist,'fromsrc':fromsrc,'dest':dest,'countgrp':group.count()} )
    except:
        traceback.print_exc()
        raise Http404("Error in page. Please try again later")



def joinpool(request):
    try:
        phone_no = request.GET.get('phone_no')
        group_id = request.GET.get('group_id')
        country_code = request.GET.get('country_code')
        email_id = request.GET.get('email_id')
        finalurl = "http://5.189.166.153:8080/CarSawaari/BaseServlet?phone_no="+str(phone_no)+"&group_id="+str(group_id)+"&country_code="+str(country_code)+"&email_id="+str(email_id)+"&action=25"
        print("finalurl:",finalurl)
        with urllib.request.urlopen(
                finalurl) as response:
            html = response.read()
            print(html)
            j = json.loads(html)
            print(j['status'])
        return HttpResponse(j['status'])
    except:
        traceback.print_exc()
        return HttpResponse("0")


def getcity(request):
    try:
        search = request.GET.get('search')
        #searchobj = TblCities.objects.filter(name__startswith=search)
        searchobj = TblCities.objects.all()
        results = []
        for r in searchobj:
            results.append(r.name)
        data = {
            'list': results,
        }
        return JsonResponse(data)
    except:
        traceback.print_exc()
        return HttpResponse("0")
