<img src="https://github.com/Nitesh-Singh-5/E-Nursery/blob/master/screenshots/E-nurser2.png" align="left" height="350" width="400" >
<img src="https://github.com/Nitesh-Singh-5/E-Nursery/blob/master/screenshots/E-nurser3.png" align="left" height="350" width="400" >
<img src="https://github.com/Nitesh-Singh-5/E-Nursery/blob/master/screenshots/E-nurser5.png" align="left" height="350" width="400" >

<br>
## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Nitesh-Singh-5/E-Nursery.git
$ cd clg-project-blog
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv E-nursery
$ E-nursery\Scripts\activate      # for windows
$ source E-nursery/bin/activate   # Mac OS/Linux
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(E-nursery)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(E-nursery)$ cd project
(E-nursery)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

For working with databases or getting the data from databases:
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

For entering admin panel:
```sh
$ python manage.py createsuperuser
```
