# sca-day-4-project
 A simple blog application

This allows users to  navigate through all published posts and read single posts

I also create a simple administration interface to manage and publish posts


1. Define the database models in the models.py file of the application
2. Create an initial migration for the model. This generates a file (0001_initial.py) that contains the SQL statments to create the database table for the Post model
    - python manage.py makemigrations appname
3. Inspect the SQL output of your first migration without executing it
    - python manage.py sqlmigrate appname 0001
4. Sync the database with the new model
    - python manage.py migrate
Note: If you edit your models, you will have to create a new migration (makemigrations) and sync(migrate) again.
5. Create a simple administration site to 
manage data (in this case, blog posts). This is automatically done by django (django.contrib.admin)
6. Create a super user and follow the prompt
7. Run your server and open http://127.0.0.1:8000/admin/ in your browser
8. Login to the administration site with the credentials you just created
9. Add your models to the administration site (blog/admin.py)


Now, to read and write content to the database programmatically.
- Customize your model managers to retrieve all objects in the database in models.py <!--PublishedManager-->
- Create a view to dislay the list of posts (blog/views.py)
- Add URL patterns for your view (blog/urls.py)
- Include the URL patterns of the blog application in the main URL patterns of the project (mysite/urls.py)
- Create your templates directory
- Run your server


<!-- python manage.py shell allows you to test model values in the terminal -->
