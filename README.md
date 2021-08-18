# STYLESAGE TEST

## Goal 
The objective of this API is to provide information on a database related to artists.

**Table of Contents**
1. [Setup](#Setup)
   * [Requirements](#requirements)
   * [Installation](#installation)
2. [Create new user to access the API](#create-new-user-to-access-the-API)
3. [Database population](#data-base-population)
4. [API](#API)
   * [Requirements](#requirements)
   * [Installation](#installation)
5. [Tests](#Tests)
6. [Web scrapping to get artists images](#web-scraping-to-get-artists-images)
   
## Setup :arrow_forward:

### Requirements 📋
We assume that you have [miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your computer.
### Installation 🔧
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
Now, run the Django migrate to create the tables into the database and create a super user to access the admin site:
```sh
(stylesage_api_env)$ python manage.py migrate
(stylesage_api_env)$ python manage.py createsuperuser
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
This API has an endpoints that only authenticated users can use the API services, for these reasons is necessary to access the django admin select in the users section ‘Add’ and create a new user and password. these will be your credentials to access the API

![Admin django](/screenshots/image.png)
![Admin django](/screenshots/image2.png)

## Database population

## API
Endpoint |HTTP Method | Authentication | Result | Filters | Fields
-- | -- |-- |--
`artists/` | GET | No | Get all artists
`albums/` | GET | Basic | Get albums information | `artist_id` | `songs`,`artist_name`,`track_count`,`album_duration`,`longest_track_duration`,`shortest_track_duration`
`passphrase/basic/ `| GET | No | Get count of valid basic passphrases.
`passphrase/advanced/ ` | GET | No |Get count of valid advanced passphrases.

#### Example with curl
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

## Tests ⚙
To run the tests in this project you will have to execute the following command:
```sh
(stylesage_api_env)$ python manage.py test passphrase_validation.tests
```
They are unit tests that ensure the passphrase validation algorithms implementatione_api_env)$ python manage.py test

## Web scrapping to get artists images
To have the artists images available in the database, there is available a Django command whose main function is to scrape the media urls with the artists images from https://www.allmusic.com and save them in the database, in the media_url field, which is also available into artist API resource.
```sh
(stylesage_api_env)$ python manage.py add_images
```

![Admin django](/screenshots/url.png)
