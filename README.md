##### Temporary repo demonstrating a gevent+django runserver problem

This is a standard django project, only changes are:
- manage.py has been monkeypatched with gevent
- added a line to urls.py for the view
- added a views.py to hold the view `gdc`
- added a large `gdc.html` template (1.8MB), the last line displayed should be '5235225'

###### Steps:

1. clone repo
2. mkvirtualenv with python3
3. `pip install -r requirements.txt`
4. `python manage.py runserver`
5. load http://localhost:8000/ in a browser (I used Chrome)
6. notice that the data is cut off (the last line displayed should be '5235225')
7. comment `monkey.patch_all()` in "manage.py"
8. try step 5 again, notice the page fully loads as expected
 
