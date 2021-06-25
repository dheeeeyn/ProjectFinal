from django.shortcuts import redirect, render
from VApp.models import User, Volunteer, Donation, Profile, Contact
# from django.http import HttpResponse

def Home(request):
	return render(request, 'home.html')

def Donate(request):
	return render(request, 'donate.html')

def Volunteer(request):
	return render(request, 'volunteer.html')

def Your_Profile(request):
	return render(request, 'profile.html')

def Login(request):
	return render(request, 'login.html')


# sign in
def Your_sign(request):
	return render(request, 'signup.html')
	if request.method == 'POST':
		User.objects.create(YName=request.POST['YName'], email=request.POST['email'], password1=request.POST['password1'])
		return redirect('/VApp/login/')
	signup = User.objects.all()
	return render(request, 'login.html')

# def Add_sign(request):
# 	User.objects.create(YName=request.POST['YName'], email=request.POST['email'], password1=request.POST['password1'])
# 	return redirect(f'usesign/')

# def Use_sign(request):
# 	signup = User.objects.all()
# 	return render(request, 'login.html')


# contact
def Your_Contact(request):
	return render(request, 'contact.html')

def addContact(request):
	Contact.objects.create(name=request.POST['name'], email=request.POST['email'], message=request.POST['message'])
	return redirect(f'tyu/')
	
def thankyou(request):
	message = Contact.objects.all()
	return render(request,'thankyou.html')


# def VolunteerForm(request):
# 	return render(request, 'volunteerform.html')
	# if request.method == 'POST':
	# 	Item.objects.create(text=request.POST['Vinterest'])
	# 	#return redirect('/')
	# 	return redirect('/VApp/viewList_url/')
	# items = Item.objects.all()
	#return render(request, 'volunteerform.html',{'vInterest': items})
	


# def ViewList(request,VolId):
# 	vId = Volunteer.objects.get(id=VolId)
# 	#items = Item.objects.all()
# 	#items = Item.objects.filter(VolId=vId)
# 	return render(request, 'volunteerinfo.html',{'vId': vId,'Dsched':'Sched', 'Tsched': 'schedT'})

# def NewList(request):
# 	newVolunteer = Volunteer.objects.create()
# 	Item.objects.create(VolId=newVolunteer, text=request.POST['Vinterest'], Sched=request.POST['Dsched'], schedT=request.POST['Tsched'])
# 	return redirect(f'/VApp/{newVolunteer.id}/')

# def VolList(request,VolId):
# 	vId = Volunteer.objects.get(id=VolId)
# 	Item.objects.create(VolId=vId, text=request.POST['Vinterest'], Sched=request.POST['Dsched'],schedT=request.POST['Tsched'])
# 	return redirect(f'/VApp/{vId.id}/')


# def VolunteerForm(request):
# 	if request.method == 'POST':
# 		Item.objects.create(text=request.POST['Vinterest'])
# 		return redirect('/')
# 	return render(request, 'volunteerform.html')



# def VolunteerForm(request):
# 	if request.method == 'POST':
# 		newItem = request.POST['Vinterest']
# 		Item.objects.create(text=newItem)
# 	else:
# 		newItem = ''
# 	return render(request, 'volunteerform.html', {'vInterest': newItem,})


# def VolunteerForm(request):
# 	item = Item()
# 	item.text = request.POST.get('Vinterest', '')
# 	item.save()
# 	return render(request, 'volunteerform.html', {'vInterest': item.text})
	#return render(request, 'volunteerform.html', {'vInterest': request.POST.get('Vinterest'),'dSched': request.POST.get('Dsched'),'tSched': request.POST.get('Tsched'''),})

# def VolunteerForm(request):
# 	return render(request, 'volunteerform.html', {'vInterest': request.POST.get('Vinterest'),'dSched': request.POST.get('Dsched'),'tSched': request.POST.get('Tsched'''),})


# def VolunteerForm(request):
# 	return render(request, 'volunteerform.html', {'firstName': request.POST.get('Fname'),'lastName': request.POST.get('Lname'),'Municipality': request.POST.get('Maddress'),'City': request.POST.get('Caddress',''),})


# def VolunteerForm(request):
# 	return render(request, 'volunteerform.html', {'vInterest: request.POST['Vinterest'],})

# def VolunteerForm(request):
# 	if request.method == 'POST':
# 		return HttpResponse(request.POST['Vinterest'])
# 	return render(request, 'volunteerform.html')


# def VolunteerForm(request):
# 	return render(request,'volunteerform.html')


# VolunteerForm = None
# def VolunteerForm(request):
# 	# pass
# 	return HttpResponse('<html><head><title>VOLUNTEER</title></head><body><h1> Be one of Us! </h1><div class="volunteer"><div class="volunteer-container"><div class="volunteer-box"><form><label for="name"> Name:</label><br><input type="text" id="Fname" name="Fname" placeholder="Your first name" required><input type="text" id="Lname" name="Lname" placeholder="Your last name" ><br><br><label for="address"> Address</label><br><input type="text" id="Maddress" name="Maddress" placeholder="Municipality"required><input type="text" id="Caddress" name="Caddress" placeholder="City"required><br><br></div><input type="submit"  id="btnRegister" value="Register"></form></div></div></div></body></html>')                  