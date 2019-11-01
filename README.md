# Ebiznes

## INSTALLATION

### Prerequisites
```
Python 3.6
Node 10 or nvm(https://github.com/coreybutler/nvm-windows) with installed node 10
```

### VIRTUALENV
```
virtualenv env --python=python3
source env/bin/activate
pip install -r requirements/base.txt
```

### MIGRATIONS
Create database first and then
copy db.base.py into db.py and populate it with your settings and then run:

```
python manage.py migrate
```

### JAVASCRIPT
```
npm install
npm run build / npm run watch
```

### Run local server
```
python manage.py runserver
```

Then go to localhost:8000 in your browser.

### Admin
First create admin account with
```
python manage.py createsuperuser
```

Then go to localhost:8000/admin and login with created account.


### Assets
Main login images is from:
```
https://www.pexels.com/photo/man-in-green-polo-shirt-3084330/
Photo by Ekrulila from Pexels
```