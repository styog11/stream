import requests
import us.py
login_url="http://styogyt.byethost31.com/login_db.php"
home_url="http://styogyt.byethost31.com/home.php"
payload = {
    "username": us.username ,
    "password": us.password
}

r = requests.post(url=login_url , data=payload)
print(r.text)
