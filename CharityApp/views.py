from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# DonationForm = None
def DonationForm(request):
	# pass
	return HttpResponse('<html><head><title>Donation Form</title><!-- padding-left: 25rem; --></head><body style="text-align:center; margin-top: 150px; margin-bottom: 300px; background-image: linear-gradient(to top, #9890e3 0%, #b1f4cf 100%);"><div class="contact" style="display: flex; align-items: center; justify-content: center;" ><div class="contact-box" style=" width:50%; border:black; border-width:3px; border-style:solid;"><h1 style="font-size: 3rem;"> Make Donations Now!!! </h1><hr style="width:30%;"><br><form><h3>Amount</h3><input type="radio" id="100" name="amount"  value="100" required><label for="100"> &#8369; 100</label><input type="radio" id=3300" name="amount" value="300" ><label for="100"> &#8369; 300</label><input type="submit"  id="btnSend" value="Donate"></form></div></div></body></html>')                  