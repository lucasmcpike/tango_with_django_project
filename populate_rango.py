import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    # 1. Define the data
    python_pages = [
        {'title': 'Official Python Tutorial', 'url':'http://docs.python.org/3/tutorial/'},
        {'title':'How to Think like a Computer Scientist', 'url':'http://www.greenteapress.com/thinkpython/'},
        {'title':'Learn Python in 10 Minutes', 'url':'http://www.korokithakis.net/tutorials/python/'} 
    ]

    django_pages = [
        {'title':'Official Django Tutorial', 'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title':'Django Rocks', 'url':'http://www.djangorocks.com/'},
        {'title':'How to Tango with Django', 'url':'http://www.tangowithdjango.com/'} 
    ]

    other_pages = [
        {'title':'Bottle', 'url':'http://bottlepy.org/docs/dev/'},
        {'title':'Flask', 'url':'http://flask.pocoo.org'} 
    ]

    cats = {
        'Python': {'pages': python_pages,"views":128,"likes":64},
        'Django': {'pages': django_pages,"views":64,"likes":32},
        'Other Frameworks':{'pages': other_pages,"views":32,"likes":16} 
    }

    
    for cat, cat_data in cats.items():
        # Pass the views and likes from the dictionary to the function
        c = add_cat(cat, views=cat_data.get('views', 0), likes=cat_data.get('likes', 0))
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    # 3. Print the results so you know it worked
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

# This starts the execution
if __name__ == '__main__':
    print('Starting Rango population script...') 
    populate()