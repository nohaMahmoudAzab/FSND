import os
from flask import Flask, request, abort, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import not_
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def handle_pagination(all_objects, page):
  start = (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE
  objects = [object.format() for object in all_objects]
  selection = objects[start:end]
  return selection

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  Set up CORS. Allow '*' for origins.
  '''
  cors = CORS(app, resources={r"/*": {"origins": "*"}})

  @app.after_request
  def after_request_func(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
  '''
  GET endpoint to handle requests 
  for all available categories.
  '''
  @app.route('/categories')
  def get_categories():
    categories = Category.query.all()
    formated_categories = dict()
    for category in categories:
      formated_categories [category.id] = category.type

    if len(categories) == 0:
      abort(404)
    else:
      return jsonify({
        'success': 1,
        'totalCategories': len(categories),
        'categories': formated_categories
      })

  @app.route('/categories/<category_id>')
  def get_category(category_id):
    category = Category.query.get(category_id)

    if category is None:
      abort(404)
    else:
      return jsonify({
        'success': 1,
        'data': category.format()
      })

  '''
  GET endpoint to handle requests for questions, 
  including pagination (every 10 questions). 
  This endpoint returns a list of questions, 
  number of total questions, current category, categories. 
  '''
  @app.route('/questions')
  def get_questions():
    page = request.args.get('page', 1, type=int)
    questions = Question.query.all()
    page_questions = handle_pagination(questions, page)
    categories = Category.query.all()
    formated_categories = dict()
    for category in categories:
      formated_categories [category.id] = category.type

    if len(page_questions) > 0:
      return jsonify({
        'success': 1,
        'total_questions': len(questions),
        'questions': page_questions,
        'categories': formated_categories
      })
    else:
      abort(404)

  @app.route('/questions/<question_id>')
  def get_question(question_id):
    question = Question.query.get(question_id)

    if question is None:
      abort(404)
    else:
      return jsonify({
        'success': 1,
        'question': question.format()
      })

  '''
  An endpoint to DELETE question using a question ID.  
  '''
  @app.route('/questions/<question_id>', methods=["DELETE"])
  def delete_question(question_id):
    question = Question.query.get(question_id)

    if question is None:
      abort(404)
    else:
      question.delete()
      return jsonify({
        'success': 1,
        'total_count': len(Question.query.all())
      })

  '''
  POST endpoint to add a new question, 
  which will require the question and answer text, 
  category, and difficulty score.
  '''
  @app.route('/questions', methods=["POST"])
  def create_question():
    try:
      data = request.get_json()
      if 'searchTerm' in data:
        return search_questions(data['searchTerm'])
      else:
        question = Question(data['question'], data['answer'], data['category'], data['difficulty'])
        question.insert()

        return jsonify({
          "success": 1,
          "total_count": len(Question.query.all()),
          "id": question.id
        })
    except:
      abort(422)

  '''
  POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question.
  '''
  def search_questions(search_term):
    questions = Question.query.filter(Question.question.ilike('%'+search_term+'%')).all()

    if len(questions) > 0:
      return jsonify({
      'success': 1,
      'totalQuestions': len(questions),
      'questions': [question.format() for question in questions]
      })
    else:
      abort(404)

  '''
  GET endpoint to get questions based on category. 
  '''
  @app.route('/categories/<category_id>/questions')
  def get_category_questions(category_id):
    category = Category.query.get(category_id)
    questions = Question.query.filter(Question.category == category_id).all()

    if len(questions) > 0:
      return jsonify({
        'success': 1,
        'totalQuestions': len(questions),
        'questions': [question.format() for question in questions],
        'currentcategory': category.format()
      })
    else:
      abort(404)

  '''
  POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 
  '''
  @app.route('/quizzes', methods=["POST"])
  def quizzes():
    data = request.get_json()
    category_id = data['quiz_category']['id']
    if category_id != 0:
      query = Question.query.filter(Question.category == category_id)
    else:
      query = Question.query

    questions = query.filter(~Question.id.in_(data['previous_questions'])).all()

    if len(questions) > 0:
      random_question = (random.choice(questions)).format()
    else:
      random_question = None

    return jsonify({
      'success': 1,
      'question': random_question
    })

  '''
  Error Handlers:
  '''
  @app.errorhandler(400)
  def bad_request(e):
    return jsonify({
      'success': 0,
      'error': 400,
      'message': 'Bad request'
    }), 400

  @app.errorhandler(404)
  def not_found(e):
    return jsonify({
      'success': 0,
      'error': 404,
      'message': 'Not Found'
    }), 404

  @app.errorhandler(422)
  def unprocessable(e):
    return jsonify({
    'success': 0,
    'error': 422,
    'message': 'Unprocessable request'
    }), 422

  @app.errorhandler(500)
  def internal_server_error(e):
    return jsonify({
    'success': 0,
    'error': 500,
    'message': 'Internal Server Error'
    }), 500

  return app
