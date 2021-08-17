# STYLESAGE TEST

## Goal
The objective of this API is to provide information on a database related to artists.

**Table of Contents**

1. [SetUp](#SetUp)
2. [Create new user to access the API](#Create new user to access the API)
3. [Structure](#Structure)
4. [Method](#Method)
5. [Tests](#Tests)
6. [Command](#Tests)
   
## SetUp

### Basic requirements

A basic requirement to execute this project is to have a miniconda installed.

### Instalation
The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/adjitta/stylesage_api.git
```
Create and active a virtual environment to install dependencies and activate it:
```sh
$ conda create -n stylesage_api_env
$ conda activate stylesage_api_env
```
Then install the dependencies:
```sh
(env)$ conda install --file requirements.txt
```  
When you finish installing the dependencies navigate to the project folder: 
```sh
(stylesage_api_env)$ cd stylesage_api/stylesage_api
``` 
Now make the django migrate and create a super user
```sh
(stylesage_api_env)$ cd stylesage_api/stylesage_api
(stylesage_api_env)$ manage.py migrate
(stylesage_api_env)$ manage.py createsuperuser
``` 
First, we have to start up Django's development server.
``` sh
(stylesage_api_env)$ python manage.py runserver
```
Now you can access the django administrator.

```
http://127.0.0.1:8000/admin/ 
```
## Create new user to access the API

This API have a  endpoints that only authenticated users can use the API services, for this reasons is necessary to access the django admin select in the users section ‘Add’ and create a new user and password. these will be your credentials to access the API
![Alt text](/home/adja/stylesage_api/screenshots/image.png "Django admistration")
![Alt text](/home/adja/stylesage_api/screenshots/image2.png "Django admistration")

## Structure
In  API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have many resource, `songs,albums and artists`.

Endpoint |HTTP Method | Authentication | Result
-- | -- |-- |--
`artists/` | GET | No | Get all artists
`albums/` | GET | Basic | Get albums informations
`passphrase/basic/ `| GET | No | Get count of valid basic passphrases.
`passphrase/advanced/ ` | GET | No |Get count of valid advanced passphrases.

The albums/ endpoints accepts filter and also allows you to select the fields you want to include.

Filter
--|
`artist_id`

Fields
--|
`songs`
`artist_name`
`track_count`
`album_duration`
`longest_track_duration`
`shortest_track_duration`

### Method
Request:

List of artists
```
curl --location --request GET 'http://127.0.0.1:8080/artists/' \
--data-raw ''
```

Response

If response is ok, the API response is :

```
HTTP/1.1 200 OK
< Date: Tue, 17 Aug 2021 14:28:34 GMT
< Server: WSGIServer/0.2 CPython/3.9.6
< Content-Type: application/json
< X-Frame-Options: DENY
< Content-Length: 464
< X-Content-Type-Options: nosniff
< Referrer-Policy: same-origin


[
   {
       "artist_id": 1313,
       "artist_name": "Amaral",
       "media_url": "https://rovimusic.rovicorp.com/image.jpg?c=wooGclVQX1HQRLANB6YAXj6KsMttLlyBmmVTZ6_CLs0=&f=2"
   },
]
```
Other response
```
200: The request was successfully
400: Bad request
401: Unauthorized.The response must include a WWW-Authenticate header field containing a challenge applicable to the requested resource.
500: Server Error
```

## Tests
To run the tests in this project you will have to execute the following command:
```sh
(stylesage_api_env)$ python manage.py test
```
## Command

To have the artists 'images available in the database, I have created a django command whose main function is to scrape the urls with the artists' images and save that information in the database in the media_url field.
```sh
(stylesage_api_env)$ python manage.py add_images
```
![Alt text](/home/adja/stylesage_api/screenshots/url.png "add image")
