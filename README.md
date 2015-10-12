# Gwaith-demo

This is a collection of demo apps showing usage of [gwaith](https://github.com/bartekbrak/gwaith) - 
a library to download European Central Bank foreign exchange reference rates.
The collection currently numbers... one app, in Django. Flask planned.

This is a simple demo code for a prospective employer, no production use intended. 

## Django implementation

The app was meant to be kept über-minimal to make browsing code faster, no auth or security was 
implemented, this is left to prospective users should they find this code useful. 

The app consists of one managment command `getrates` (see its help for usage) 
meant to be run as a cron job or similar and a restful API.

### Install and demo run

```shell
git clone git@github.com:bartekbrak/gwaith-demo.git
cd django
pip install -r requirements.txt
./manage.py migrate
./migrate getrates
./manage.py runserver
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/rates/
# or navigate to http://127.0.0.1/ and browse manually
```

## Flask implementation

WIP

# LICENSE

Do what you wish with the code. MIT.

:wq ;P
