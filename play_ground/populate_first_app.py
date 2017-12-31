import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','play_ground.settings')


import django
django.setup()


#Fake pop script

import random

from first_app.models import AccessRecord, WebPage, Topic

from faker import Faker
fakegen = Faker()
topics=['Search', "Social","MarketPlace", "News", "Games"]

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):
        # GEe the topic or the entry

        top = add_topic()

        #Crate Fake databases
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #Create new Webpage entry
        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]


        # Create a Fake access Record for the Webpage
        acc_rec= AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating Script!")
    populate(20)
    print("Populatin Complete!")
