import time
import calendar
from datetime import date, datetime, timedelta

from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.core.context_processors import csrf
from django.forms.models import modelformset_factory
from django.template import RequestContext
from myproject.forms import RegistrationForm

from django.utils import simplejson

from myproject.models import *

mnames = "January February March April May June July August September October November December"
mnames = mnames.split()



def _show_users(request):
    """Return show_users setting; if it does not exist, initialize it."""
    s = request.session
    if not "show_users" in s:
        s["show_users"] = True
    return s["show_users"]

@login_required
def settings(request):
    """Settings screen."""
    s = request.session
    _show_users(request)
    if request.method == "POST":
        s["show_users"] = (True if "show_users" in request.POST else False)
    return render_to_response("cal/settings.html", add_csrf(request, show_users=s["show_users"]), context_instance=RequestContext(request))

def reminders(request):
    """Return the list of reminders for today and tomorrow."""
    year, month, day = time.localtime()[:3]
    reminders = Entry.objects.filter(date__year=year, date__month=month,
                                   date__day=day, creator=request.user, remind=True)
    tomorrow = datetime.now() + timedelta(days=1)
    year, month, day = tomorrow.timetuple()[:3]
    return list(reminders) + list(Entry.objects.filter(date__year=year, date__month=month,
                                   date__day=day, creator=request.user, remind=True))

@login_required
def main(request, year=None):
    """Main listing, years and months; three years per page."""
    # prev / next years
    if year: year = int(year)
    else:    year = time.localtime()[0]

    nowy, nowm = time.localtime()[:2]
    lst = []

    # create a list of months for each year, indicating ones that contain entries and current
    for y in [year, year+1, year+2]:
        mlst = []
        for n, month in enumerate(mnames):
            entry = current = False   # are there entry(s) for this month; current month?
            entries = Entry.objects.filter(date__year=y, date__month=n+1)
            if not _show_users(request):
                entries = entries.filter(creator=request.user)

            if entries:
                entry = True
            if y == nowy and n+1 == nowm:
                current = True
            mlst.append(dict(n=n+1, name=month, entry=entry, current=current))
        lst.append((y, mlst))

    return render_to_response("cal/main.html", dict(years=lst, user=request.user, year=year,
                                                   reminders=reminders(request)))

@login_required
def month(request, year=time.localtime()[0], month=time.localtime()[1], change=None):
    """Listing of days in `month`."""
    year, month = int(year), int(month)

    # apply next / previous change
    if change in ("next", "prev"):
        now, mdelta = date(year, month, 15), timedelta(days=31)
        if change == "next":   mod = mdelta
        elif change == "prev": mod = -mdelta

        year, month = (now+mod).timetuple()[:2]

    # init variables
    cal = calendar.Calendar()
    month_days = cal.itermonthdays(year, month)
    nyear, nmonth, nday = time.localtime()[:3]
    lst = [[]]
    week = 0

    # make month lists containing list of days for each week
    # each day tuple will contain list of entries and 'current' indicator
    for day in month_days:
        entries = current = False   # are there entries for this day; current day?
        form = None
        filled = False
        formset = 0
        if day:
            entries = Entry.objects.filter(date__year=year, date__month=month, date__day=day, creator=request.user)
            if not _show_users(request):
                entries = entries.filter(creator=request.user)
            if day == nday and year == nyear and month == nmonth:
                current = True
                
            if len(entries) == 0:
                form = modelformset_factory(Entry, extra=1, exclude=("creator", "date"), can_delete=True)
            else:
                form = modelformset_factory(Entry, extra=0, exclude=("creator", "date"), can_delete=True)
                filled = True
                
            formset = form(queryset=Entry.objects.filter(date__year=year,
            date__month=month, date__day=day, creator=request.user))

        lst[week].append((day, entries, current, formset, filled))
        if len(lst[week]) == 7:
            lst.append([])
            week += 1

    return render_to_response("cal/month.html", dict(year=year, month=month, user=request.user,
                        month_days=lst, mname=mnames[month-1], reminders=reminders(request)),
                        context_instance=RequestContext(request))

@login_required
def day(request, year, month, day):
    """Entries for the day."""
    entries = Entry.objects.filter(date__year=year, date__month=month,
                                         date__day=day, creator=request.user)
    if len(entries) == 0:
        EntriesFormset = modelformset_factory(Entry, extra=1, exclude=("creator", "date"), can_delete=True)
    else:
        EntriesFormset = modelformset_factory(Entry, extra=0, exclude=("creator", "date"), can_delete=True)
    
    other_entries = []
    if _show_users(request):
        other_entries = Entry.objects.filter(date__year=year, date__month=month,
                                       date__day=day).exclude(creator=request.user)
                                       
    year, month, origday = int(year), int(month), int(day)

    if request.method == 'POST':
        if request.is_ajax():
            formset = EntriesFormset(request.POST)
            if formset.is_valid():
                # add current user and date to each entry & save
                entries = formset.save(commit=False)
                for entry in entries:
                    entry.creator = request.user
                    entry.date = date(int(year), int(month), int(origday))
                    entry.save()
                    
                cal = calendar.Calendar()
                month_days = cal.itermonthdays(year, month)
                nyear, nmonth, nday = time.localtime()[:3]
                lst = [[]]
                week = 0
            
                # make month lists containing list of days for each week
                # each day tuple will contain list of entries and 'current' indicator
                # for day in month_days:
                entries = current = False   # are there entries for this day; current day?
                form = None
                filled = False
                formset = 0
                if day:
                    entries = Entry.objects.filter(date__year=year, date__month=month, date__day=day, creator=request.user)
                    if not _show_users(request):
                        entries = entries.filter(creator=request.user)
                    if day == nday and year == nyear and month == nmonth:
                        current = True
                        
                    if len(entries) == 0:
                        form = modelformset_factory(Entry, extra=1, exclude=("creator", "date"), can_delete=True)
                    else:
                        form = modelformset_factory(Entry, extra=0, exclude=("creator", "date"), can_delete=True)
                        filled = True
                        
                    formset = form(queryset=Entry.objects.filter(date__year=year,
                    date__month=month, date__day=day, creator=request.user))
        
                lst[week].append((day, entries, current, formset, filled))
                if len(lst[week]) == 7:
                    lst.append([])
                    week += 1
                
                return render_to_response("cal/cell.html", dict(year=year, month=month, user=request.user,
                            month_days=lst, mname=mnames[month-1], reminders=reminders(request)),
                            context_instance=RequestContext(request))
        else:
            formset = EntriesFormset(request.POST)
            if formset.is_valid():
                # add current user and date to each entry & save
                entries = formset.save(commit=False)
                for entry in entries:
                    entry.creator = request.user
                    entry.date = date(int(year), int(month), int(day))
                    entry.save()
                return HttpResponseRedirect(reverse("myproject.views.month", args=(year, month))) 

    else:
        # display formset for existing enties and one extra form
        formset = EntriesFormset(queryset=Entry.objects.filter(date__year=year,
            date__month=month, date__day=day, creator=request.user))
    
    return render_to_response("cal/day.html", add_csrf(request, entries=formset, year=year,
            month=month, day=day, other_entries=other_entries, reminders=reminders(request)),
            context_instance=RequestContext(request))


def add_csrf(request, **kwargs):
    """Add CSRF and user to dictionary."""
    d = dict(user=request.user, **kwargs)
    d.update(csrf(request))
    return d
    
def signup(request):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse("myproject.views.month"))
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = User.objects.create_user(username=form.cleaned_data['username'], password = form.cleaned_data['password'])
                user.save()
                greener = Greener(user=user, iNumber='i888888', name='NAH NALA')
                greener.save()
                new_greener = authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
                login(request, new_greener)
                return HttpResponseRedirect(reverse("myproject.views.month"))
            else:
                return render_to_response('cal/signup.html', {'form': form}, context_instance=RequestContext(request))
        else:
                ''' user is not submitting the form, show them a blank registration form '''
                form = RegistrationForm()
                context = {'form': form}
                return render_to_response('cal/signup.html', context, context_instance=RequestContext(request))
