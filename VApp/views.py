from django.shortcuts import redirect, render
from VApp.models import Item, Volunteer
#from django.http import HttpResponse


def VolunteerForm(request):
	return render(request, 'volunteerform.html')
	# if request.method == 'POST':
	# 	Item.objects.create(text=request.POST['Vinterest'])
	# 	#return redirect('/')
	# 	return redirect('/VApp/viewList_url/')
	# items = Item.objects.all()
	#return render(request, 'volunteerform.html',{'vInterest': items})
	


def ViewList(request,VolId):
	vId = Volunteer.objects.get(id=VolId)
	#items = Item.objects.all()
	#items = Item.objects.filter(VolId=vId)
	return render(request, 'volunteerinfo.html',{'vId': vId,'Dsched':'Sched', 'Tsched': 'schedT'})

def NewList(request):
	newVolunteer = Volunteer.objects.create()
	Item.objects.create(VolId=newVolunteer, text=request.POST['Vinterest'], Sched=request.POST['Dsched'], schedT=request.POST['Tsched'])
	return redirect(f'/VApp/{newVolunteer.id}/')

def VolList(request,VolId):
	vId = Volunteer.objects.get(id=VolId)
	Item.objects.create(VolId=vId, text=request.POST['Vinterest'], Sched=request.POST['Dsched'],schedT=request.POST['Tsched'])
	return redirect(f'/VApp/{vId.id}/')


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