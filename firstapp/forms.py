from django import forms
from firstapp.models import SiteUser,UserRole,Image


class SiteUserForm(forms.ModelForm):
    class Meta:
        model = SiteUser
        exclude = ["roleId",
                 "userFullName",
                 "userEmail",
                 "userPassword",
                 "userMobile",
                 "isActive"

                  ]
class UserRoleForm(forms.ModelForm):
    class Meta:
        model =UserRole
        exclude = [ "roleId",
                    "roleName",
                    "isActive"

                  ]
class ImageForm(forms.ModelForm):
    class Meta:
        model =Image
        exclude = [ "roleId",
                 "userFullName",
                 "userEmail",
                 "userPassword",
                 "userMobile",
                 "userImage",
                 "isActive"

                  ]