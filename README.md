<p align="center">
  <img src="https://static.thenounproject.com/png/182706-200.png" height="150" />
</p>
<h2 align="center">
    A Thousand Notes <a href="https://a-thousand-notes.herokuapp.com/app">(Demo)</a>
</h2>
<p align="center">
  🖼️<em> Because a picture is worth more than just words</em> 🖼️</br>
</p>
<p align="center">
<img alt="React" src="https://badges.aleen42.com/src/react.svg" />
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/fastapi" />
<img alt="Tests" src="https://github.com/awtkns/fastapi-crudrouter/workflows/Python%20application/badge.svg" />
<img alt="docker" src="https://badges.aleen42.com/src/docker.svg" />
</p>

---

# About
A Thousand Notes is a full stack web application created for the Fall 2021 - Shopify Developer Intern Challenge. It is an app that aims to help bring your pictures to life. Within the app, you can upload images along with their names and they will be displayed within the app and automatically linked to a relavant song on spotify. In doing this, users will be able to appreciate their pictures like never before because after all, <em>A picture is worth a thousand... notes</em>. 

### Backend features
You can view the backend api of the app <a href="https://a-thousand-notes.herokuapp.com/">here</a>. This api has been thoroughly tested with Pytest. Features include retriving images by id or retrieving all images, deleting an image by id or a list of ids, and adding one or more images. Image data such as spotify information is stored in postgreSQL while the images themselves are stored on Google's Firebase.

### Frontend features
You can view the front end of the app <a href="https://a-thousand-notes.herokuapp.com/app">here</a>. Features include uploading an image via the upload button, playing the Spotify preview of a linked song within your browser, a button to open a given song in spotify, selecting multiple songs to delete with a delete button, querying images by name via the search bar, and pagination of images via the buttons at the buttom of the page.

# Framework and tools
### Backend
- Python with FastAPI
- SQLAlchemy and Pydantic
- PostgreSQL for production and SQLite for testing
### Frontend
- React with Next.js
- Material UI
### General
- Docker
- Firebase
- Spotify API
- Git

# How songs are linked
Initially the plan was to create a randomly generated song based on images provided. I could only find one service online that did this and I even created a script in python linked <a href='https://github.com/asim-shrestha/a-thousand-notes/blob/main/misc/scraper.py'>here</a> that uses selenium to login to the service, drag an image to be run, wait for the AI to generate a song from the image, and return the url of the generated song. Unfortunately, a given user for this website (https://melobytes.com/en/app/ai_image2song) only gets a limited number of song generations before they hit a paywall. Because of this, I transitioned to using the spotify API to retrieve a random song from a constantly updated playlist of new music. In the future, one could also use AI to provide a description of uploaded images and use these descriptions to retrieve a song from spotify as maybe a search query. I unfortunately did not have time to implement this here, but it was an enjoyable project nonetheless and it was fun learning how to utilze Firebase and the Spotify API.

# Testing
```
cd backend
pip install -r requirements.txt
pip install pytest
cd tests
pytest
```

# Deployment
Note you must first use the available sample.docker.env file and fill out any missing values. Then you can simply run:
```
docker-compose up 
```
After the command finishes, you can travel to http://localhost:5001/ for the backend and http://localhost:3000/ for the frontend
