# RestAPI_Flask_pymongo
In this repository I have created RestAPI using python, flask and mongodb on which we can do simple CRUD operation as well as some query params operation for limit, page, name and age.

Step1 : To run app.py install below setup
       -1) Python 3.9
       -2) Vs code editor (or any)
       -3) mongodb 
       -4) postman
       
Step2 : after downloading app.py run below command into that in cmd
    
     python -m pip install virtualenv
     python -m virtualenv env
     
     pip install flask
     pip install flask_pymongo
     
Step3 : start mongodb and create database Users on your localhost address and In that database create collection user and copy your localhost address paste in app.py file in place of app.config['MONGO_URI'] and save 
Step4:  click on run button after completing above steps successfully run app.py from run button
step5:  start postman and enter route and select your method like GET and click on send you will get all data which are in the USERS database or you can post data into user.
step6:  we can also perform /api/users?page=1&limit=10&name=James&sort=age this operation on url

thank you..
happycoding


     
