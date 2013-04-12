from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Entry(models.Model):
    title = models.CharField(max_length=40)
    snippet = models.CharField(max_length=100, blank=True)
    body = models.TextField(max_length=10000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date = models.DateField(blank=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    remind = models.BooleanField(default=False)

    def __unicode__(self):
        if self.title:
            return unicode(self.creator) + u" - " + self.title
        else:
            return unicode(self.creator) + u" - " + self.snippet[:40]

    def short(self):
        if self.snippet:
            return u'%s' % (self.snippet)
        #else:
         #   return self.title
    short.allow_tags = True

    class Meta:
        verbose_name_plural = "entries"
        
        
class Greener(models.Model):
        user            = models.OneToOneField(User)
        iNumber        = models.CharField(max_length=100)
        name            = models.CharField(max_length=100)

        def __unicode__(self):
                return self.name
    	


### Admin

class EntryAdmin(admin.ModelAdmin):
    list_display = ["creator", "date", "title", "snippet"]
    search_fields = ["title", "snippet"]
    list_filter = ["creator"]
