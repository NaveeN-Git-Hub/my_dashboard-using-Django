from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
import os
import time


# Create your views here.
def profile(request):
		
	if request.method == "POST":
		name = request.POST.get("name", "")
		phone = request.POST.get("phone", "")
		email = request.POST.get("email", "")
		your_place = request.POST.get("your_place", "")
		blog = request.POST.get("blog", "")
		skills = request.POST.get("skills", "")
		summary = request.POST.get("summary", "")
		languages = request.POST.get("languages", "")
		hobbies = request.POST.get("hobbies", "")


		school_name = request.POST.get("school_name", "")
		school_board = request.POST.get("school_board", "")
		school_year = request.POST.get("school_year", "")

		degree_name = request.POST.get("degree_name", "")
		degree_university = request.POST.get("degree_university", "")
		degree_year = request.POST.get("degree_year", "")
		

		experience1_role = request.POST.get("experience1_role", "")
		experience1_company = request.POST.get("experience1_company", "")
		experience1_year = request.POST.get("experience1_year", "")
		experience1_summary = request.POST.get("experience1_summary", "")

		experience2_role = request.POST.get("experience2_role", "")
		experience2_company = request.POST.get("experience2_company", "")
		experience2_year = request.POST.get("experience2_year", "")
		experience2_summary = request.POST.get("experience2_summary", "")

		experience3_role = request.POST.get("experience3_role", "")
		experience3_company = request.POST.get("experience3_company", "")
		experience3_year = request.POST.get("experience3_year", "")
		experience3_summary = request.POST.get("experience3_summary", "")

		experience4_role = request.POST.get("experience4_role", "")
		experience4_company = request.POST.get("experience4_company", "")
		experience4_year = request.POST.get("experience4_year", "")
		experience4_summary = request.POST.get("experience4_summary", "")
		

		profile = Profile(name=name, phone=phone, email=email, your_place=your_place, blog=blog, 
			skills=skills,summary=summary, languages=languages, hobbies=hobbies, school_name=school_name, 
			school_board=school_board, school_year=school_year,  degree_name=degree_name, degree_university=degree_university,
			degree_year=degree_year, experience1_role=experience1_role, experience1_company=experience1_company,
			experience1_year=experience1_year,  experience1_summary=experience1_summary, experience2_role=experience2_role,
			experience2_company=experience2_company, experience2_year=experience2_year, experience2_summary=experience2_summary,
			experience3_role=experience3_role, experience3_company=experience3_company, experience3_year=experience3_year,
			experience3_summary=experience3_summary, experience4_role=experience4_role, experience4_company=experience4_company,
			experience4_year=experience4_year, experience4_summary=experience4_summary) 
		profile.save()

	return render(request, 'profile.html')

import sys
import subprocess
import platform



def resume(request,id):
	print("I am in views.py-resume")

	user_profile = Profile.objects.get(pk=id)

	template = loader.get_template('resume.html')

	print(user_profile.name)
	print(user_profile.your_place)

	skills_list = []  # skills
	for skill in user_profile.skills.split(',')[:4]:  # maximum 4 skills
		skills_list.append(skill.strip())
	user_profile.skills = skills_list

	hobbies_list = []  # hobbies 
	for hobby in user_profile.hobbies.split(',')[:4]: # maximum 4 hobbies
		hobbies_list.append(hobby.strip())
	user_profile.hobbies = hobbies_list

	languages_list = []  # languages

	for language in user_profile.languages.split(',')[:3]:
		languages_list.append(language.strip())
	user_profile.languages = languages_list


	html = template.render({'user_profile':user_profile})
	options ={
		'page-size':'Letter',
		'encoding':"UTF-8",
		'javascript-delay':5000,
		'enable-local-file-access': None,
	}


	if platform.system() == "Windows":
		pdfkit_config = pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY', 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
	else:
		os.environ['PATH'] += os.pathsep + os.path.dirname(sys.executable) 
		WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf')], 
			stdout=subprocess.PIPE).communicate()[0].strip()
		pdfkit_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)
		
	pdf = pdfkit.from_string(html,False,options, configuration=pdfkit_config)
	response = HttpResponse(pdf,content_type='application/pdf')
	response['Content-Disposition'] ='attachment'; 
	filename = str(user_profile.id) + "_" + user_profile.name + "_resume.pdf"
	print(filename)
	return response

def profiles_list(request):
	print("I am in views.py-profiles_list")
	profiles = Profile.objects.all()
	return render(request, 'profiles_list.html', {'profiles': profiles})