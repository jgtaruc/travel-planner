from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from custom_auth.models import MyUser


# Register your models here.

# Form for creating new users, includes all required fields
# with password confirmation.
class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
	password2 = forms.CharField(label = 'Password Confirmation', widget = forms.PasswordInput)

	class Meta:
		model = MyUser
		fields = ('email', 'first_name', 'last_name')

	# Check that password1 and password2 matches.
	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2") 
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match.")
		return password2

	# Save the password in hashed format
	def save(self, commit = True):
		user = super(UserCreationForm, self).save(commit = False)
		user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user


# Form for updating user information.
class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = MyUser
		fields = ('email', 'first_name', 'last_name', 'is_active', 'is_admin')

	# Regardless of what the user provides, return the initial value.
	def clean_password(self):
		return self.initial["password"]


# Forms to add or change user instances
class MyUserAdmin(UserAdmin):
	change_form = UserChangeForm
	add_form = UserCreationForm

	list_display = ('email', 'last_name', 'first_name', 'is_admin', 'is_superuser', 'is_staff')
	list_filter = ('is_admin',)
	fieldsets = (
				(None,		{'fields': ('email', 'password')}),
				('Name',	{'fields': ('first_name', 'last_name')}),
				('Permission',{'fields': ('is_admin', 'is_staff', 'is_superuser')}),
				)

	add_fieldsets = (
					(None,	{'classes': ('wide'), 'fields': ('email', 'password1', 'password2')}),
					)
	search_fields = ('email',)
	ordering = ('last_name',)
	filter_horizontal = ()


admin.site.register(MyUser, MyUserAdmin)
admin.site.unregister(Group)