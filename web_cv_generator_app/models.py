from django.db import models

# Create your models here.
# The model should include all these fields which actually help us to collect the details 
# of that specific user

class Profile(models.Model):
	print("I am in models.py-Profile")
	name = models.CharField(max_length=100, blank=False) # , default='anonymous', editable=True
	phone = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	your_place = models.CharField(max_length=200, null=True, blank=True)
	blog = models.CharField(max_length=200, null=True, blank=True)
	skills = models.TextField(max_length=200)
	summary = models.TextField(max_length=2000)
	languages = models.TextField(max_length=2000)
	hobbies = models.TextField(max_length=2000, null=True, blank=True)

	# education
	school_name = models.CharField(max_length=200, null=True, blank=True)
	school_board = models.CharField(max_length=200, null=True, blank=True)
	school_year = models.CharField(max_length=200, null=True, blank=True)

	degree_name = models.CharField(max_length=200, null=True, blank=True)
	degree_university = models.CharField(max_length=200, null=True, blank=True)
	degree_year = models.CharField(max_length=200, null=True, blank=True)
	
	# experience
	experience1_role = models.CharField(max_length=200, default='')
	experience1_company = models.CharField(max_length=200, default='')
	experience1_year = models.CharField(max_length=200, default='')
	experience1_summary = models.TextField(max_length=2000, default='')
	
	experience2_role = models.CharField(max_length=200, null=True, blank=True)
	experience2_company = models.CharField(max_length=200, null=True, blank=True)
	experience2_year = models.CharField(max_length=200, null=True, blank=True)
	experience2_summary = models.TextField(max_length=2000, null=True, blank=True)

	experience3_role = models.CharField(max_length=200, null=True, blank=True)
	experience3_company = models.CharField(max_length=200, null=True, blank=True)
	experience3_year = models.CharField(max_length=200, null=True, blank=True)
	experience3_summary = models.TextField(max_length=2000, null=True, blank=True)

	experience4_role = models.CharField(max_length=200, null=True, blank=True)
	experience4_company = models.CharField(max_length=200, null=True, blank=True)
	experience4_year = models.CharField(max_length=200, null=True, blank=True)
	experience4_summary = models.TextField(max_length=2000, null=True, blank=True)

	# Photo
	#photo = models.ImageField(null=True, blank=True, upload_to='images/', default='web_cv_photo.jpg')  # install it using 'python -m pip install Pillow'
	
	"""
	# once you've written the above Text fields then to create a table in db execute following commands
	python manage.py makemigrations
	python manage.py migrate

	Now Check if this table is actually created in the backend. To login and check in "http://127.0.0.1:8000/admin"
	# create a super user

	# So in order to create the super user you simply type in Python

	python manage.py createsuperuser

	Now check in http://127.0.0.1:8000/admin

	# Now as you can see there's no model here because we are yet to register that model in the admin.py file as below
	from .models import Profile
	admin.site.register(Profile)
	"""