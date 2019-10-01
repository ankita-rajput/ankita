from firstapp import views
from django.conf.urls import url
app_name='firstapp'    #-----constant variable should be linked in urls files
urlpatterns=[
    url(r'^about/$',views.about,name="about"),
    url(r'^content1/$', views.content1,name="content1"),
    url(r'^content2/$',views.content2,name="content2"),
    url(r'^signup/$', views.signup, name="signup"),
    url(r'^login/$', views.login, name="login"),
    url(r'^viewdata/$', views.viewdata, name="viewdata"),
    url(r'^fetchingonevalue/$', views.fetchingonevalue, name="fetchdata"),
    url(r'^imageform/$', views.imageform, name="image"),
    url(r'^updateform/$', views.updateform, name="update"),
    url(r'^delete/$', views.deletedata, name="delete"),
    url(r'^updatedata/$', views.action, name="update"),
    url(r'^imageviewdata/$', views.imageviewdata, name="imagedata"),
    url(r'^imagedelete/$', views.deleteimageformdata, name="imagedelete"),
    url(r'^imageupdate/$', views.imageupdate, name="imageudate"),

]
