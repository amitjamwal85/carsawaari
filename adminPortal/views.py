from django.shortcuts import render,HttpResponse
from requests import Response
from datetime import date
from .models import UserInfo, CarDetails, TripDetails, RiderDetails, UserGroup, GroupMaster, AdminUser
from datetime import timedelta
from .General import send
from django.db.models import Q
from datetime import date
from datetime import datetime
import urllib.request
import urllib.parse
import urllib
import json
# Create your views here.

# ----------------------------------------------------Home View---------------------------------#
def index(request):
    if request.session.has_key('name'):
        return admin(request)
    else:
        return render(request, "login.html",)

# ----------------------------------------------------UsersDetails View---------------------------------#
def users(request):
    if request.session.has_key('name'):
        getvaule=UserInfo.objects.all().order_by("-reg_datetime")
        return render(request, "users.html",{'getlist':getvaule})
    else:
        return render(request, "login.html",)

# ----------------------------------------------------User Trip Details View---------------------------------#
def tripRequest(request):
    if request.session.has_key('name'):
        id = request.GET.get('id')
        username = request.GET.get('name')
        phone = request.GET.get('phone')
        getvaule=TripDetails.objects.filter(user_id=id)
        #getvaule = CarDetails.objects.raw('SELECT T.rider_id,T.trip_id,T.rider_id,user_info.phone_no,user_info.name FROM trip_details  T INNER JOIN user_info  on T.user_id=%s and user_info.user_id=T.rider_id',id)

        return render(request, "tripInfo.html",{'getlist':getvaule,'username':username})
    else:
        return render(request, "login.html",)


# ----------------------------------------------------Group Info View---------------------------------#
def groupInfo(request):
    if request.session.has_key('name'):
        id = request.GET.get('id')
        username = request.GET.get('name')
        phone = request.GET.get('phone')
        getinfo = GroupMaster.objects.filter(rider_id=id)


        #.filter(group_id__in=UserGroup.objects.filter(user_id=id))
        #getinfo=UserGroup.objects.raw('select * from GroupMaster where group_id in (select group_id from UserGroup where user_id=%s)',id)
        #getvaule = CarDetails.objects.raw('SELECT T.rider_id,T.trip_id,T.rider_id,user_info.phone_no,user_info.name FROM trip_details  T INNER JOIN user_info  on T.user_id=%s and user_info.user_id=T.rider_id',id)

        return render(request, "groupDetails.html",{'getlist':getinfo,'username':username})
    else:
        return render(request, "login.html",)



# ----------------------------------------------------Group Info View---------------------------------#
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
def groupall(request):
    if request.session.has_key('name'):
        grpcnt = GroupMaster.objects.all().count()
        usercnt = UserGroup.objects.all().count()
        page = request.GET.get('page', 1)
        getinfo = GroupMaster.objects.all()
        paginator = Paginator(getinfo, 8)
        try:
            gamelist = paginator.page(page)
        except PageNotAnInteger:
            gamelist = paginator.page(1)
        except EmptyPage:
            gamelist = paginator.page(paginator.num_pages)



        return render(request, "groupDetails.html",{'getlist':gamelist,'grpcnt':grpcnt,'usercnt':usercnt})
    else:
        return render(request, "login.html",)


# ----------------------------------------------------Offer Trip Details View---------------------------------#
def offer(request):
    if request.session.has_key('name'):
        id = request.GET.get('id')
        username = request.GET.get('name')
        phone = request.GET.get('phone')
        getvaule=RiderDetails.objects.filter(rider_id=id)
        #getvaule = CarDetails.objects.raw('SELECT T.rider_id,T.trip_id,T.rider_id,user_info.phone_no,user_info.name FROM trip_details  T INNER JOIN user_info  on T.user_id=%s and user_info.user_id=T.rider_id',id)

        return render(request, "offerDetails.html",{'getlist':getvaule,'username':username})
    else:
        return render(request, "login.html",)

# ----------------------------------------------------User Trip Details View---------------------------------#
def tripRequest(request):
    if request.session.has_key('name'):
        id = request.GET.get('id')
        username = request.GET.get('name')
        phone = request.GET.get('phone')
        getvaule=TripDetails.objects.filter(user_id=id)
        print("getvaule",getvaule)
        #getvaule = CarDetails.objects.raw('SELECT T.rider_id,T.trip_id,T.rider_id,user_info.phone_no,user_info.name FROM trip_details  T INNER JOIN user_info  on T.user_id=%s and user_info.user_id=T.rider_id',id)

        return render(request, "tripInfo.html",{'getlist':getvaule,'username':username})
    else:
        return render(request, "login.html",)

# ----------------------------------------------------userinfo Details View---------------------------------#
def userinfo(request):
    if request.session.has_key('name'):
        id = request.GET.get('id')
        getvaule=UserInfo.objects.filter(user_id=id)
        totalGroup = UserGroup.objects.filter(user_id=id).count()
        totalJoin = UserGroup.objects.filter(Q(user_id=id) & ~Q(rider_id=id)).count()
        TotalCreated = UserGroup.objects.filter(Q(user_id=id) & Q(rider_id=id)).count()

        #getvaule = CarDetails.objects.raw('SELECT T.rider_id,T.trip_id,T.rider_id,user_info.phone_no,user_info.name FROM trip_details  T INNER JOIN user_info  on T.user_id=%s and user_info.user_id=T.rider_id',id)
        return render(request, "userinfo.html",{'getlist':getvaule,'username':id,'totalGroup':totalGroup,'totalJoin':totalJoin,'TotalCreated':TotalCreated})
    else:
        return render(request, "login.html",)

# ----------------------------------------------------userinfo Details View---------------------------------#
def tripInfo(request):
    if request.session.has_key('name'):
        id = request.GET.get('id')
        getvaule=TripDetails.objects.filter(trip_id=id)
        #getvaule = CarDetails.objects.raw('SELECT T.rider_id,T.trip_id,T.rider_id,user_info.phone_no,user_info.name FROM trip_details  T INNER JOIN user_info  on T.user_id=%s and user_info.user_id=T.rider_id',id)
        return render(request, "tripDetails.html",{'getvaule':getvaule})
    else:
        return render(request, "login.html",)



# ----------------------------------------------------Admin View---------------------------------#
def admin(request):
    if request.session.has_key('name'):
        upcoming = RiderDetails.objects.filter(ride_status='active').count()
        print("upcoming ",upcoming)
        lastdate = date.today() - timedelta(days=7)
        today=datetime.combine(lastdate, datetime.min.time())
        print("last week date ",today)
        #lastweek = RiderDetails.objects.filter(ride_status='completed',ride_com_datetime__gte=today).count()
        lastweek = RiderDetails.objects.filter(ride_status='completed').count()
        print("lastweek ",lastweek)
        #totalBook =TripDetails.objects.filter(Q(trip_status='completed')|Q(trip_status='accepted')).count()
        totalBook = TripDetails.objects.all().count()
        print("totalBook ",totalBook)
        totalRide = RiderDetails.objects.all().count()
        print("totalRide ",totalRide)
        totalUsers = UserInfo.objects.all().count()
        print("totalUsers ", totalUsers)
        return render(request, "admin.html",{'upcoming':upcoming,'lastweek':lastweek,'totalbook':totalBook,'totalRide':totalRide,'totalUsers':totalUsers} )
    else:
        error = "Please Login Again"
        return render(request, "login.html", {'error': error})




# ----------------------------------------------------Login View---------------------------------#
def login(request):
    username = ''
    password = ''
    try:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(password)
            error = ''
            getvalue = AdminUser.objects.filter(username=username).filter(password=password)
            print("getvalue.exists()",getvalue.exists())
            if( getvalue.exists()):
                print("success")
                #get = AdminUser.objects.filter(username=username).filter(password=password)[0]
                #name=get.username
                request.session['name']='Admin'
                print("setting sesssion...")
                return admin(request)
            else:
                print("Failed")
                error = 'Invalid Credentials. Please try again.'
                return render(request,"login.html", {'error': error})
        return render(request,"login.html")
    except Exception :
        print("error")


# ----------------------------------------------------Logout View---------------------------------#
def logout(request):
    error = "You are logged out"
    try:
        del request.session['name']
    except:
        pass
    return render(request,"login.html", {'error': error})


# ----------------------------------------------------approve/dis View---------------------------------#
def appDis(request):
    if request.session.has_key('name'):
        getvalue=request.GET.get('get')
        id=request.GET.get('id')
        phone=request.GET.get('phone')
        userdata = UserInfo.objects.get(user_id=id)
        print(id)
        if getvalue=="approve":
            msg = "Your ID has successfully Verified. Now you can enjoy CarSawaari rides."
            print("approve")
            UserInfo.objects.filter(user_id=id).update(profile_status='Verified',user_bio='')
            result=sendMessage(msg,userdata.phone_no)
            print("Result :: ",result)
            sendNotification(msg, userdata.fcm_token, "Verified")
            return verfiyID(request)
        else:
            print("dis approve")
            msg = "Your ID has been rejected. Please fill details again."
            result = sendMessage(msg, userdata.phone_no)
            print("Result :: ", result)
            sendNotification(msg, userdata.fcm_token, "Not Verified")
            UserInfo.objects.filter(user_id=id).update(profile_status='Not Verified',user_bio='rejected',user_doc_url='http://5.189.166.153:8080/CarSawaari/img/govt.png')
            #send(phone,"Your ID has been Rejected","Profile Verfication")
            return verfiyID(request)
    else:
        return render(request, "login.html",)
    return render(request,"login.html", {'error': error})


def sendMessage(msg,number):
    msg =  urllib.parse.quote_plus(msg)
    urlhit = "http://198.24.149.4/API/pushsms.aspx?loginID=genrosysapi&password=Qwert2ab@123&mobile="+str(number)+"&text="+str(msg)+"&senderid=CARSWR&route_id=2&Unicode=0"
    print("urlhit",urlhit)
    contents = urllib.request.urlopen(urlhit).read()
    print(contents)
    return contents

def sendNotification(msg,token,subject):
    notificationObj = dict()
    notificationObj['subject'] = subject
    notificationObj['message'] = msg

    obj = dict()
    obj['data'] = notificationObj
    obj['to'] = token
    print(obj)

    myurl = "https://fcm.googleapis.com/fcm/send"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    req.add_header('Authorization',
                   'key=AAAAAXK20Cc:APA91bHDCJImUpz-aWAOCk_ale2XVfR0FiRV0VjmBgeXbFUVyzDCIKH27Va7IXDbHjflt6AI2rHHmpZle0yxUn9fb63DulbH_K7oNlNSokfljgip_Z7pcE0tVq4b569ihd7EGpwvi-gM')

    jsondata = json.dumps(obj)
    jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    #print(jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
    html = response.read()
    print(html)



# ----------------------------------------------------Verfiy View---------------------------------#

def Promotion(request):
    if request.session.has_key('name'):
        print("*****Promotion*****")
        return render(request, "Promotion.html",{})
    else:
        error = "Please Login Again"
        return render(request, "login.html", {'error': error})


def SendNotification(request):
    if request.session.has_key('name'):
        caption = request.GET.get('caption')
        subject = request.GET.get('subject')
        type = request.GET.get('type')
        if type=="all":
            users = UserInfo.objects.filter(user_id__isnull=False);
            sendPromo(caption, users,subject)
            print("caption : ", caption, " type : ", type)
            resp = "Notification sent successfully to " + str(users.count()) + " Users"
            return HttpResponse(resp)
        elif type=="notverified":
            users = UserInfo.objects.filter(
            ~Q(user_doc_url__icontains='http://5.189.166.153:8080/CarSawaari/img/govt.png'))
            sendPromo(caption, users,subject)
            print("caption : ", caption, " type : ", type)
            resp = "Notification sent successfully to " + str(users.count()) + " Users"
            return HttpResponse(resp)
        elif type == "verified":
            users = UserInfo.objects.filter(
            Q(profile_status='Verified')|Q(profile_status__icontains='Approve'))
            sendPromo(caption, users,subject)
            print("caption : ", caption, " type : ", type)
            resp = "Notification sent successfully to " + str(users.count()) + " Users"
            return HttpResponse(resp)
        elif type == "rejected":
            users = UserInfo.objects.filter(
            Q(profile_status__icontains='rejected'))
            sendPromo(caption, users,subject)
            print("caption : ", caption, " type : ", type)
            resp = "Notification sent successfully to " + str(users.count()) + " Users"
            return HttpResponse(resp)
        elif type == "upcoming":
            today = date.today()
            print("date.today()",today.year,"  ",today.month,"  ",today.day)
            riders = RiderDetails.objects.filter(rider_start_date__year=today.year,rider_start_date__month=today.month,rider_start_date__day=today.day,offer_type='book',ride_status='active')
            print("getdata : ",riders.count())
            for rider in riders:
                print("rider:",rider.rider_id)
                user = UserInfo.objects.get(user_id=rider.rider_id)
                sendNotification(caption, user.fcm_token, subject)
            triper = TripDetails.objects.filter(user_date__year=today.year,user_date__month=today.month,user_date__day=today.day, trip_type ='book',                                           trip_status='active')
            print("getdata : ", triper.count())
            for trip in triper:
                user = UserInfo.objects.get(user_id=trip.user_id)
                sendNotification(caption, user.fcm_token, subject)
            print("caption : ", caption, " type : ", type)
            resp = "Notification sent successfully to " + str(riders.count()+triper.count()) + " Users"
            return HttpResponse(resp)
        elif type == "offer":
            today = date.today()
            daybefore = today+ timedelta(days=-7)
            print("date.today()",today)
            print("date.today()", today+timedelta(days=-7))
            riders = RiderDetails.objects.filter(rider_start_date__lte=daybefore,offer_type='book',ride_status='active')
            print("getdata : ",riders.count())
            for rider in riders:
                print("rider:",rider.rider_id)
                user = UserInfo.objects.get(user_id=rider.rider_id)
                sendNotification(caption, user.fcm_token, subject)
            triper = TripDetails.objects.filter(user_date__lte=daybefore, trip_type ='book',                                           trip_status='active')
            print("getdata : ", triper.count())
            for trip in triper:
                user = UserInfo.objects.get(user_id=trip.user_id)
                sendNotification(caption, user.fcm_token, subject)
            print("caption : ", caption, " type : ", type)
            resp = "Notification sent successfully to " + str(riders.count()+triper.count()) + " Users"
            return HttpResponse(resp)

    else:
        error = "Please Login Again"
        return render(request, "login.html", {'error': error})


def sendPromo(caption,users,subject):
    for user in users:
        print("user : ", user.name)
        sendNotification(caption, user.fcm_token, subject)

# ----------------------------------------------------Verfiy View---------------------------------#

def verfiyID(request):
    if request.session.has_key('name'):
        print("**********")
        noprofile = UserInfo.objects.filter(
            Q(user_doc_url__icontains='http://5.189.166.153:8080/CarSawaari/img/govt.png')).count()
        notverified = UserInfo.objects.filter(~Q(user_doc_url__icontains='http://5.189.166.153:8080/CarSawaari/img/govt.png'),profile_status='Not Verified').count()
        verified = UserInfo.objects.filter(
            Q(profile_status='Verified')|Q(profile_status__icontains='Approve')).count()
        rejected = UserInfo.objects.filter(
            Q(user_bio='rejected')).count()
        print("noprofile",noprofile)
        print("notverified", notverified)
        print("verified", verified)
        print("rejected", rejected)

        getvalue = UserInfo.objects.filter(~Q(user_doc_url__icontains='http://5.189.166.153:8080/CarSawaari/img/govt.png'),profile_status='Not Verified').order_by("profile_status")
        print("getvalue*****",getvalue.count())
        return render(request, "verifyID.html", {'getlist': getvalue,'noprofile':noprofile,'notverified':notverified,'verified':verified,'rejected':rejected})
    else:
        error = "Please Login Again"
        return render(request, "login.html", {'error': error})

# ----------------------------------------------------Verfiy View---------------------------------#

def verfiyCar(request):
    if request.session.has_key('name'):
        verified = CarDetails.objects.filter(status='Verified').count()
        notverified = CarDetails.objects.filter(status='Not Verified',car_rc_url__isnull=False).count()
        rejected = CarDetails.objects.filter(status='rejected').count()
        print("verified",verified)
        print("notverified", notverified)
        print("rejected", rejected)
        getvalue = CarDetails.objects.filter(status__icontains='Not Verified',car_rc_url__isnull=False).order_by("-status")
        print("test....................",getvalue.count())
        return render(request, "verifyCar.html", {'getlist': getvalue,'verified':verified,'notverified':notverified,'rejected':rejected})
    else:
        error = "Please Login Again"
        return render(request, "login.html", {'error': error})


# ----------------------------------------------------approve/dis Car View---------------------------------#

def CarVer(request):
    if request.session.has_key('name'):
        getvalue=request.GET.get('get')
        id=request.GET.get('id')
        cardata = CarDetails.objects.get(car_id=id)
        userdata = UserInfo.objects.get(user_id=cardata.rider_id)
        print("value :: ",id)
        if getvalue=="approve":
            msg = "Your Car ID verification done successfully. Thank you"
            upd=CarDetails.objects.filter(car_id=id)
            upd.update(status='Verified')
            result = sendMessage(msg, userdata.phone_no)
            sendNotification(msg, userdata.fcm_token, "Verified")
            print("Result :: ", result)
            return verfiyCar(request)
        else:
            msg = "Your Car ID has been rejected. Please fill details again."
            result = sendMessage(msg, userdata.phone_no)
            print("Result :: ", result)
            sendNotification(msg, userdata.fcm_token,"Not Verified")
            CarDetails.objects.filter(car_id=id).update(status='rejected')
            return verfiyCar(request)
    else:
        return render(request, "login.html",)
    return render(request,"login.html", {'error': error})


