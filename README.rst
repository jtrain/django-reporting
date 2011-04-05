================
Django-Reporting
================


A reporting application for django that provides interactive table based views
for any django queryset data.

Now for a summary of how to install, configure and use.

Introduction
============

Django Reporting System allows you to create dynamic reports for your models, consolidating and aggregating data, filtering and sorting it.

It requires Django 1.1, because it uses Django's ORM aggregation. 


Installation
============

settings.py:: 

  INSTALLED_APPS = (
    # [...]
    'reporting',
    # admin has to go after reporting in order to have links to the
    # reports from the admin site.
    'django.contrib.admin', 

urls.py::

  from django.conf.urls.defaults import *
  from django.contrib import admin
  import reporting

  admin.autodiscover()
  # autodiscover reports in applications
  reporting.autodiscover()

  urlpatterns = patterns('',
    # [...]
    (r'^reporting/', include('reporting.urls')),
  )

For a working example see the 'samples' directory inside the repository.

Configure report
================

Let's say you have the following schema:

models.py::

  class Department(models.Model):
    # [...]
    
  class Occupation(models.Model):
    # [...]

  class Person(models.Model):
    # we won't use it in a summary report
    name = models.CharField(max_length=255) 

    # we'll be able to group and to filter by both occupation and country
    occupation = models.ForeignKey(Occupation)

    # we'll be able to group and to filter by department and it leader
    department = models.ForeignKey(Department)
    country = models.ForeignKey(Country)

    # we'll be able to filter by year
    birth_date = models.DateField()

    # we'll sum and calculate average for salary and expenses 
    salary = models.DecimalField(max_digits=16, decimal_places=2)   
    expenses = models.DecimalField(max_digits=16, decimal_places=2)

in your application create a *reports.py*

reports.py::

  import reporting
  from django.db.models import Sum, Avg, Count
  from models import Person

  class PersonReport(reporting.Report):
    model = Person
    verbose_name = 'Person Report'
    annotate = (                    # Annotation fields (tuples of field, func, title)
        ('id', Count, 'Total'),     # example of custom title for column 
        ('salary', Sum),            # no title - column will be "Salary Sum"
        ('expenses', Sum),
    )

    # columns that will be aggregated (syntax is the same as for annotate)
    aggregate = (                   
        ('id', Count, 'Total'),
        ('salary', Sum, 'Salary'),
        ('expenses', Sum, 'Expenses'),
    )

    # list of fields and lookups for group-by options
    group_by = [                   
        'department',
        'department__leader', 
        'occupation', 
    ]

    # This are report filter options (similar to django-admin)
    list_filter = [                
       'occupation',
       'country',
    ]
    
    # if detail_list_display is defined user will be able to see how rows was grouped.
    detail_list_display = [        
        'name', 
        'salary',
        'expenses', 
    ]

    # the same as django-admin.
    date_hierarchy = 'birth_date' 

  # Do not forget to 'register' your class in reports
  reporting.register('people', PersonReport) 

For more details see the project in the 'samples' directory in the repository.
