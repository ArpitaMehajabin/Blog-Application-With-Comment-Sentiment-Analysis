
# Blog Application with Sentiment Analysis

This is a Django-based Blog Application that includes a sentiment analysis feature. Users can write blog posts, comment on posts, and view the sentiment of comments (positive or negative). The project leverages natural language processing (NLP) techniques to analyze the tone of user comments.


## Features

- User registration and authentication (sign-up, login, logout)
- Create,  edit, and delete blog posts
- Manage user profile (change username, profile picture, password)
- Comment on blog posts
- Sentiment analysis of comments
- Admin panel for managing users and content


## Technologies Used
- Python
- Django
- HTML, CSS, Bootstrap
- JavaScript
- Natural Language Processing (NLP)
  - Hugging Face Transformers(using pre-trained model pipeline)
- SQLite (default database)
## Installation

1.Clone the repository:

```bash
 https://github.com/ArpitaMehajabin/Blog-Application-With-Comment-Sentiment-Analysis.git
```
2.Navigate to the project directory:
 ```bash
 cd blog_website
```
3.Create and activate a virtual environment:
 ```bash
 pip install virtualenv # if not already installed
```
Creating Virtual Environment:
```bash
virtualenv venv
```
Activating Virtual Environment: On Windows:
```bash
venv\Scripts\activate
```
4.Install the required dependencies:
 ```bash
 pip install -r requirements.txt
```
5.Run migrations:
 ```bash
 python manage.py makemigrations
python manage.py migrate
```
6.Start the development server:
 ```bash
 python manage.py runserver
```
