# Авторизация
* Роут - POST:api/user/login/
* Пример запроса: 
```json
{
	"username": "testmail@mail.com",
	"password": "strongpassword321"
}
```
* Ответ запроса:
```json
{
	"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NzM2NDM5MiwianRpIjoiYWU2N2E4MGE3Y2I3NDI4ZmI4NDYzNTI3NWIwMDE3ODAiLCJ1c2VyX2lkIjoxfQ.4teKUPT7GOzrLFoVc006-SprkGE5vq6jH1E3ldqkvqU",
	"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU3MzIxMTkyLCJqdGkiOiJjOGZkYmY2ZTk4N2Y0ZGNjOWRhOTc0ODZhYjkwZDgwZSIsInVzZXJfaWQiOjF9.m0tMWO5jNx9ylJdTexl4DuZ_fXvjSjjtaOsi3sHckGU"
}
```