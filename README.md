# marketplace
Django practice application that offers a venue marketplace to event organizers

# preinstall requirements
python 2.x  @ path: /usr/bin/python

virtualenv

# installation
run

``source ./setup.sh``

# post installation
You will know if the virtualenv is activated by noting (venv) appended to your terminal prompt

When no (venv), To activate the virtualenv, run

``source ./venv/bin/activate``

 or

 ``. ./venv/bin/activate``

to deacivate it, run

``deactivate``


#Client-side Dev

To build things for the client side, we have React and hot-reloading to make our lives easier

navigate to the marketplace/marketplace/client and run commands

``npm install``
``npm run build``
``npm run watch``

make sure that your django server is running in a separate terminal window

``./manage.py runserver``

You can now navigate to localhost:8000/client and watch the page reload live while you edit your components

#SASS

We're also making use of SASS. You can import .scss files directly into your React components and they will also be live reloaded with each edit
