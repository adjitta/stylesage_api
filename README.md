![Portada](/screenshots/portada.png)

## About this proyect 💬
StyleSage API build with Django that provides music data and passphrase validation support

**Table of Contents**
1. [Setup :arrow_forward:](#Setup)
   * [Requirements 📋](#requirements)
   * [Installation 🔧](#installation)
2. [Create new user to access the API 📝](#create-new-user-to-access-the-API)
3. [Database population :computer:](#data-base-population)
4. [API :page_with_curl:](#API)
   * [Examples with curl](#example-with-curl)
      * [List of artists](#list-of-artists)
      * [List of albums](#list-of-albums)
      * [Basic passphrase validation](#basic-passphrase-validation)
      * [Advanced passphrase validation](#advanced-passphrase-validation)
5. [Tests ⚙](#Tests)
6. [Web scrapping to get artists images :robot:](#web-scraping-to-get-artists-images)
   
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

Now you can access the Django administrator.
```
http://127.0.0.1:8000/admin/ 
```

## Create new user to access the API 📝
This API has an endpoints that only authenticated users can use the API services, for these reasons is necessary to access the Django admin select in the users section ‘Add’ and create a new user and password. these will be your credentials to access the API

![Admin Django](/screenshots/image.png)
![Admin Django](/screenshots/image2.png)

## Database population :computer:
Django admin can be used to add data in to database.

## API :page_with_curl:
Endpoint |HTTP Method | Authentication | Result | Filters (Optional) | Fields (Optional)
-- | -- |-- |-- |-- |--
`artists/` | GET | No | Get all artists
`albums/` | GET | Basic | Get albums information | `artist_id` |`songs`<br />`artist_name`<br />`track_count`<br />`album_duration`<br />`longest_track_duration`<br />`shortest_track_duration`
`passphrase/basic/ `| GET | No | Get count of valid basic passphrases.
`passphrase/advanced/ ` | GET | No |Get count of valid advanced passphrases.

### Examples with curl

#### List of artists
```
curl --request GET 'http://127.0.0.1:8080/artists/'
```

```
HTTP/1.1 200 OK

[
   {
       "artist_id": 1313,
       "artist_name": "Amaral",
       "media_url": "https://rovimusic.rovicorp.com/image.jpg?c=wooGclVQX1HQRLANB6YAXj6KsMttLlyBmmVTZ6_CLs0=&f=2"
   },
]
```

#### List of albums
To add the autorization you need to encode in Base64 your credentials (in the format 'user:password'). You could do it online with [Base64](https://www.base64encode.org/)
```
curl --request GET 'http://127.0.0.1:8080/albums?artist_id=1414&fields=songs,artist_name,track_count,album_duration' \
--header 'Authorization: Basic c3R5bGVzYWdlOkNvY29sb2NvMTk5NCoqKio=' \
```

```
HTTP/1.1 200 OK
[
    {
        "album_id": 2020,
        "artist_id": 1414,
        "album_name": "cuidate",
        "songs": [
            {
                "album_id": 2020,
                "track_id": 3737,
                "name_track": "temblando",
                "milliseconds": 8
            },
            {
                "album_id": 2020,
                "track_id": 4040,
                "name_track": "brown",
                "milliseconds": 3
            }
        ],
        "artist_name": "Rosalia",
        "track_count": 2,
        "album_duration": 11
    }
]
```

#### Basic passphrase validation

```
curl --request GET 'http://127.0.0.1:8080/passphrase/basic/' \
--header 'Content-Type: text/plain' \
--data-raw 'aa bb cc dd
aa bb cc dd aa
aa bb cc dd aaa aa
uu aa'
```

```
HTTP/1.1 200 OK
2
```

#### Advanced passphrase validation

```
curl --request GET 'http://127.0.0.1:8080/passphrase/advanced/' \
--header 'Content-Type: text/plain' \
--data-raw 'abcde fghij
abcde xyz
a ab abc abd abf abj abj
iiii oiii ooii oooi oooo'
```

```
HTTP/1.1 200 OK
3
```

## Tests ⚙
To run the tests in this project you will have to execute the following command:
```sh
(stylesage_api_env)$ python manage.py test passphrase_validation.tests
```
They are unit tests that ensure the passphrase validation algorithms implementatione_api_env)$ python manage.py test

## Web scrapping to get artists images :robot:
To have the artists images available in the database, there is available a Django command whose main function is to scrape the media urls with the artists images from https://www.allmusic.com and save them in the database, in the media_url field, which is also available into artist API resource.
```sh
(stylesage_api_env)$ python manage.py add_images
Adding https://rovimusic.rovicorp.com/image.jpg?c=wooGclVQX1HQRLANB6YAXj6KsMttLlyBmmVTZ6_CLs0=&f=4 to Amaral
```


