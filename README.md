# Course App

## login and signup

### 1. signup as student

```
curl --location --request POST 'http://127.0.0.1:8002/auth/register/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=yv8k1AeYzjX0b9Ql1cIOvHB6wdHSsMK6O6coTCdj28ZYY5ZlxFKr8AbXSs4i41LT' \
--data-raw '{
    "username":"test1",
    "email":"test1@gmail.com",
    "password":"abcd1234",
    "user_type":"Student"
}'
```

### 2. signup as educator

```
curl --location --request POST 'http://127.0.0.1:8002/auth/register/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=yv8k1AeYzjX0b9Ql1cIOvHB6wdHSsMK6O6coTCdj28ZYY5ZlxFKr8AbXSs4i41LT' \
--data-raw '{
    "username":"test2",
    "email":"test2@gmail.com",
    "password":"abcd1234",
    "user_type":"Educator"
}'
```

### 3. login as student

```
curl --location --request POST 'http://127.0.0.1:8002/auth/login/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=yv8k1AeYzjX0b9Ql1cIOvHB6wdHSsMK6O6coTCdj28ZYY5ZlxFKr8AbXSs4i41LT' \
--data-raw '{
    "username":"test1",
    "password":"abcd1234",
}'
```

### 4. login as educator

```
curl --location --request POST 'http://127.0.0.1:8002/auth/login/' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=yv8k1AeYzjX0b9Ql1cIOvHB6wdHSsMK6O6coTCdj28ZYY5ZlxFKr8AbXSs4i41LT' \
--data-raw '{
    "username":"test2",
    "password":"abcd1234",
}'
```

### 5. Logout

Token would be in the response of signup and login API's

```
curl --location --request GET 'http://127.0.0.1:8002/auth/logout/' \
--header 'Authorization: Token 1a51d0a51f63aa57cddd2164b143945c68bdf378' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=yv8k1AeYzjX0b9Ql1cIOvHB6wdHSsMK6O6coTCdj28ZYY5ZlxFKr8AbXSs4i41LT'
```

## Course API (Require Token for Authorization)

Token would be in the response of signup and login API's

### 1. As Student (educator not allowed)

1. To list all courses

```
curl --location --request GET 'http://127.0.0.1:8002/course/' \
--header 'Authorization: Token 1a51d0a51f63aa57cddd2164b143945c68bdf378' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=yv8k1AeYzjX0b9Ql1cIOvHB6wdHSsMK6O6coTCdj28ZYY5ZlxFKr8AbXSs4i41LT'
```

2. To detail view of particular course. Example: course with id = 2

```
curl --location --request GET 'http://127.0.0.1:8002/course/2/' \
--header 'Authorization: Token 1a51d0a51f63aa57cddd2164b143945c68bdf378' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=yv8k1AeYzjX0b9Ql1cIOvHB6wdHSsMK6O6coTCdj28ZYY5ZlxFKr8AbXSs4i41LT'
```

3. To enroll in particular Course

```
curl --location --request POST 'http://127.0.0.1:8002/course/2/' \
--header 'Authorization: Token 1a51d0a51f63aa57cddd2164b143945c68bdf378' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=yv8k1AeYzjX0b9Ql1cIOvHB6wdHSsMK6O6coTCdj28ZYY5ZlxFKr8AbXSs4i41LT'
```

### As Educator (Students not allowed)

1. To upload a new course with title, description and image

```
curl --location --request POST 'http://127.0.0.1:8002/course/' \
--header 'Authorization: Token 1a51d0a51f63aa57cddd2164b143945c68bdf378' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=yv8k1AeYzjX0b9Ql1cIOvHB6wdHSsMK6O6coTCdj28ZYY5ZlxFKr8AbXSs4i41LT' \
--data-raw '{
    "title":"dff",
    "description":"aaaaa"
}'
```

2. To view student usernames in a particular course created by that educator only. Example course with id=2

```
curl --location --request POST 'http://127.0.0.1:8002/course/2/' \
--header 'Authorization: Token 1a51d0a51f63aa57cddd2164b143945c68bdf378' \
--header 'Cookie: csrftoken=yv8k1AeYzjX0b9Ql1cIOvHB6wdHSsMK6O6coTCdj28ZYY5ZlxFKr8AbXSs4i41LT'
```
