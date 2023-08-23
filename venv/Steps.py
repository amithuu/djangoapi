""" How to setup virtual envirnment for django"""

# Create a Directory
    '[mkdir directoryname]'

# Enter into the directory
    '[cd directoryname]'

# Create a virtual environment
    '[python3 -m venv virtual-env-name]'

# [if any error comes here, then install ["sudo apt install python3-venv"]]

# Activate the virtual environment
    '[source venv/bin/activate]'

# to deactivate the virtual environment
    '[deactivate]'

# to get all the files inside the venv
    '[pip freeze]'

# install django
    '[pip install django]'

# intsall restapiframework
    '[pip install djangorestframework]'

# check now what we have installed
    '[pip freeze]'
    '[  asgiref==3.7.2,
        Django==4.2.4,
        djangorestframework==3.14.0,
        pytz==2023.3,
        sqlparse==0.4.4,
        typing_extensions==4.7.1,
    ]'

# Now create a project in django
    '[django-admin startproject projectname]'

# Get into inside project
    '[cd projectname]'

# list the files
    '[now we get the manage.py file]'

# now go to editor and in settings as we hjave installed restframework, add it to apps list
    '['rest_framework',]'

# To add the database we need to migatre and makemigrations
    '[python3 manage.py makemigrations]'

# To make changes we need to migrate the databse
    '[python3 manage.py migrate]'

# Run the server and check now
    '[python3 manage.py runserver]'

# Create a new Project called as app in django 
    '[python3 manage.py createproject project-name]'

# Note: once u create an app or install an app [we need to add apps in settings]
    '[buildapi]'

# as we have added our project, now we need our file in web, so we need add the route of the file in ["urls.py"]
    '['include', we need to import this in restapi > urls.py ]'

# Add the same file in buildapi ,create a filename with [urls.py] as same as in the main app[restapi]


# Add the urls of the all the buildapi app routes in a single include import in restapi>urls.py
    'path('',include(appname.urls)),' [This line includes all the routes of the file ("buildapi")]

# Create an html file and add that in views.py, from where we can add get our pages into web.
    '[<!DOCTYPE html>
        <html>
            <head>

            <title> Learning RestAPi with django</title>

            </head>
            <body>
                <h1> hi i have created a django page using views, added urls to and added app in settings as well </h1>
            </body>
        </html>
]'

# i am creating am new model for the page, and added that to admin page,[admin.site.register(filename)]
[then i got this error]
[no such table: buildapi_courselist]
[beacuse as i have not migrated the files into the database]

  (python3 manage.py makemigrations)
  (python3 manage.py migrate)

[when migrated and registered is done we get to see [/home/chiku/Pictures/Screenshots/Screenshot from 2023-08-23 12-45-28.png]]
[but i need the name/title of the courselist to be name of the course[Course_Name]. for that we use dunder function in models.py]

[after adding the dunder __str__ function to the class [def __str__(self)   -> return self.CourseList], the name which has to be taken for the title]
[the result we get is [/home/chiku/Pictures/Screenshots/Screenshot from 2023-08-23 12-47-53.png]]


# AFTER THIS WE NEED TO CREATE A SERIALIZER WHICH TRANSLATES THE DATA FROM TO JSON

