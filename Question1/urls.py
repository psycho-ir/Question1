from django.conf.urls import patterns, include, url

from django.contrib import admin
from user_management.views import RegisterView, LoginView, ActivateView

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Question1.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^register', RegisterView.as_view()),
                       url(r'^activate/(?P<activation_code>.*)', ActivateView.as_view()),
                       url(r'^', LoginView.as_view()),

)
