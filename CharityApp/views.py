from django.shortcuts import render
#from django.http import HttpResponse

def DonationForm(request):
	return render(request,'donationform.html')

# Create your views here.
# DonationForm = None
# def DonationForm(request):
# 	# pass
# 	return HttpResponse('<html><head><title>Donation Form</title><!-- padding-left: 25rem; --></head><body style="text-align:center; margin-top: 150px; margin-bottom: 300px; background-image: linear-gradient(to top, #9890e3 0%, #b1f4cf 100%);"><div class="contact" style="display: flex; align-items: center; justify-content: center;" ><div class="contact-box" style=" width:50%; border:black; border-width:3px; border-style:solid;"><h1 style="font-size: 3rem;"> Make Donations Now!!! </h1><hr style="width:30%;"><br><form><h3>Amount</h3><label style="font-weight: 900;" for="name"> Name:</label><br><br><input type="name" id="name" name="name" placeholder="Name" style="width:20rem;"required><br><br><label style="font-weight: 900;" for="email"> Email:</label><br><br><input type="email" id="email" name="email" placeholder="input valid email.." style="width:20rem;"required><br><br><label style="font-weight: 900;" for="message">Message:</label><br><textarea id="message" name="message" placeholder="Write something... (optional)" rows=15 style="height:8rem; width:20rem;"></textarea><br><br><input type="submit"  id="btnSend" value="Donate"></form></div></div></body></html>')                  