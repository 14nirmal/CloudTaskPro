import requests
res = requests.post("http://localhost:8000/auth/login", json={"email": "nirmalpatel93280@gmail.com", "password": "Nirmal1234!"})
print("Login status:", res.status_code, res.json())
