from django.conf.urls.defaults import *
try:
    from django.views.generic.simple import direct_to_template
    imported = True
except:
    from django.views.generic import TemplateView
    imported = False

if imported:
    urlpatterns = patterns('',
        (r'^test/$', direct_to_template, {'template': 'original.html'}),
        (r'^other/$', direct_to_template, {'template': 'other.html'}),
        (r'^goal/$', direct_to_template, {'template': 'goal.html'}),
    )
else:
    urlpatterns = patterns('',
        (r'^test/$', TemplateView.as_view(template_name='original.html')),
        (r'^other/$', TemplateView.as_view(template_name='other.html')),
        (r'^goal/$', TemplateView.as_view(template_name='goal.html')),
    )
