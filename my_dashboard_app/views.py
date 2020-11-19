from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def base(request):
	return render(request, 'base.html', {})

def about(request):
	return render(request, 'about.html', {})

def contact(request):
	print("I am in contact def")
	if request.method == 'POST':  # fill and send the form via email
		
		name = request.POST['name']
		print("Name: ", name)
		message_email = request.POST['email']
		message_subject = request.POST['msg_subject']
		message = request.POST['message']

		# send mail
		send_mail(
			message_subject,  # subject_name
			'Name - ' + name + '\n' + 'Mail ID: ' + message_email + '\n\n' + 'Content:\n' + message,  # content
			message_email,  # from email
			['youtoonaveen@gmail.com'],  # To email
			)
		return render(request, 'about.html', {'name': name})
	else:

		return render(request, 'about.html')