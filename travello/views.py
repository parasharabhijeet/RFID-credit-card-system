from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from pyzbar import pyzbar
import cv2

# Create your views here.
def index(request):
			
	return render(request,'index.html')

def timetable(request):
	
	return render(request,'timetable.html')

def addmoney(request):
	
	if request.method == 'GET':
		q = int(request.GET.get('quantity'))
		u = User.objects.get(username = request.user.username)
		p = u.profile
		bal = p.balance
		p.balance = bal + int(q)
		p.save()
		return redirect('/')
	else:
		return render(request,'add.html')
def pay(request):
	
	#if request.method == 'GET':
	#	img = request.GET.get('img')
	#	img = 'pics4barcode/'+img
	id = barcode()
	s = "'"
	q1 = id.index(s)+1
	q2 = id.rindex(s)
	usrn = id[q1:q2]
	usrn = usrn.lower()
	u = User.objects.get(username = request.user.username)
	if usrn == request.user.username:
		p = u.profile
		bal = p.balance
		p.balance = bal - 25
		p.save()
	else:
		messages.info(request,'invalid rfid')	
	return redirect('/')
	#else:
	#	return render(request,'scan.html')

def barcode():
    #function to control computer vision operations
    ret = True
    name = "Live Video Feed"
    cv2.namedWindow(name)
    cap = cv2.VideoCapture(0)
    while ret:
        ret, frame = cap.read()
        cv2.imshow(name, frame)
        s = decode(frame)
        if s != None:
            if s[0] == "1":
                ret = False
                id = s[1:]
        else:
            id = 0
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
    cap.release()
    return id


def decode(im):
    #barcode detection
        ids = pyzbar.decode(im)
        for obj in ids:
            #winsound.Beep(7000, 600)
            k = obj.data
            t = str(k)
            return "1" + t