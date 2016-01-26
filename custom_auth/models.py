from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.

# Creates and saves a user with the given email, first name, last name and password.
class MyUserManager(BaseUserManager):
	def create_user(self, email, first_name, last_name, password = None):
		# If the user did not provide an email or a password raise the errors.
		if not email:
			raise ValueError('Users must have an email address.')
		if not password:
			raise ValueError('Users must have a password.')

		# Save the newly created user.
		# normalize_email means lowercasing the domain part of the email address.
		user = self.model(email = self.normalize_email(email),
							first_name = first_name,
							last_name = last_name,)
		user.set_password(password)
		user.save(using = self.db)
		return user

	# Creates a superuser that can login to the django admin site.
	def create_superuser(self, email, first_name, last_name, password):
		user = self.create_user(email,
									password = password,
									first_name = first_name,
									last_name = last_name)
		# Set the superuser privileges.
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using = self.db)
		return user


class MyUser(AbstractBaseUser):
	email = models.EmailField(max_length = 256, unique = True, verbose_name = 'email address')
	first_name = models.CharField(max_length = 32)
	last_name = models.CharField(max_length = 32)
	is_active = models.BooleanField(default = True)
	is_admin = models.BooleanField(default = False)
	is_staff = models.BooleanField(default = False)
	is_superuser = models.BooleanField(default = False)

	objects = MyUserManager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name','last_name']

	# Users are identified by his/her email address.
	def __unicode__(self):
		return self.email
	# Users are identified by his/her email address.
	def get_full_name(self):
		return self.email
	# Users are identified by his/her email address.
	def get_short_name(self):
		return self.email
	# User has specific permission? always true.
	def has_perm(self, perm, obj = None):
		return True
	# User has permission to view the app_label? always true.
	def has_module_perms(self, app_label):
		return True