# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## API Reference
### Getting Started
* Base URL: at present this API can only be run locally and is not hosted as a based URL. The backend app os hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration
* Authentication: This version of the API does not require authentication or API keys.
### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": false,
    "error": 405,
    "message": "Method not allowed"
}
```
The API will return the following error types when requests fail:
* 400: Bad Request
* 404: Not Found
* 405: Method Not Allowed
* 422: Unproceesable Request
* 500: Internal Server Error
### Endpoints
#### GET /categories
* General:
    * Returns list of category objects, success value, and total number of categories
* Sample: `curl http://127.0.0.1:5000/catgories`
```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "success": 1,
    "totalCategories": 6
}
```
#### GET /questions
* General:
    * Returns list of question objects, success value, total number of questions, and list of category objects
    * Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1
* Sample: `curl http://127.0.0.1:5000/questions`
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": 1,
  "total_questions": 21
}
```
#### GET /questions/<question_id>
* General:
    * Returns a question object, and success value
* Sample: `curl http://127.0.0.1:5000/questions/5`
```
{
    "question": {
        "answer": "Apollo 13",
        "category": 5,
        "difficulty": 4,
        "id": 2,
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    "success": 1
}
```    
#### GET /categories/<category_id>/questions
* General:
    * Returns a list of category's question objects, success value, total number of questions and the current category object.
* Sample: `curl http://127.0.0.1:5000/categories/2/questions`
```
{
    "currentcategory": {
        "id": 2,
        "type": "Art"
    },
    "questions": [
        {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        },
        {
            "answer": "Mona Lisa",
            "category": 2,
            "difficulty": 3,
            "id": 17,
            "question": "La Giaconda is better known as what?"
        },
        {
            "answer": "One",
            "category": 2,
            "difficulty": 4,
            "id": 18,
            "question": "How many paintings did Van Gogh sell in his lifetime?"
        },
        {
            "answer": "Jackson Pollock",
            "category": 2,
            "difficulty": 2,
            "id": 19,
            "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
        }
    ],
    "success": 1,
    "totalQuestions": 4
}
```
#### POST /questions
* General:
    * Create a new question object by posting question, answer, category, and difficulty data
* Sample:
```
curl -X POST http://127.0.0.1:5000/questions

{
    "question": "What is the most famous painting of picasso?",
    "answer": "GUERNICA",
    "category": 2,
    "difficulty": 4
}
```
```
{
    "success": 1,
    "total_count": 20,
    "id": 26
}
```
#### DELETE /questions/<question_id>
* General:
    * Delete an existing question object.
* Sample: `curl https://127.0.0.1:5000/questions/5`
```
{
    "success": 1,
    "total_count": 19
}
```
#### POST /questions    
* General:
    * Search for question object by a search term sent in the request body.
* Sample:
```
curl -X POST http://127.0.0.1:5000/questions

{
    "searchTerm": "picasso"
}
```
```
{
    "questions":[
        {
            "answer": "GUERNICA",
            "category": 2,
            "difficulty": 4,
            "id": 26,
            "question": "What is the most famous painting of picasso?"
        }
    ],
    "success": 1,
    "totalQuestions": 1
}
```
#### POST /quizzes
* General:
    * Get question objects to play the quiz. This endpoint takes category ID and previous questions IDs and return a random questions within the given category.
* Sample:
```
curl -X POST http://127.0.0.1:5000/quizzes

{
    "quiz_category": {
        "id": 2
    },
    "previous_questions": [16, 18]
}
```
```
{
    "question":{
        "answer": "Jackson Pollock",
        "category": 2,
        "difficulty": 2,
        "id": 19,
        "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    "success": 1
}
```
## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```