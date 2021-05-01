from django.shortcuts import redirect, render
from VApp.models import Item
#from django.http import HttpResponse


def VolunteerForm(request):
	# if request.method == 'POST':
	# 	Item.objects.create(text=request.POST['Vinterest'])
	# 	#return redirect('/')
	# 	return redirect('/VApp/viewList_url/')
	# items = Item.objects.all()
	#return render(request, 'volunteerform.html',{'vInterest': items})
	return render(request, 'volunteerform.html')


def ViewList(request):
	items = Item.objects.all()
	return render(request, 'volunteerinfo.html',{'vInterest': items})

def NewList(request):
	Item.objects.create(text=request.POST['Vinterest'])
	return redirect('/VApp/viewList_url/')


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