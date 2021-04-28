from django.shortcuts import render
#from django.http import HttpResponse


#try
def VolunteerForm(request):
	return render(request, 'volunteerform.html', {'vInterest': request.POST.get('Vinterest'),'dSched': request.POST.get('Dsched'),'tSched': request.POST.get('Tsched'''),})

#orig
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