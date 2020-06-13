import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres', 'postgres', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):
        res = self.client().get('/categories')
        self.assertEqual(res.status_code, 200)

    def test_not_found_categories(self):
        res = self.client().get('/categories')
        self.assertEqual(res.status_code, 404)

    def test_get_questions(self):
        res = self.client().get('/questions')
        self.assertEqual(res.status_code, 200)

    def test_not_found_questions(self):
        res = self.client().get('/questions')
        self.assertEqual(res.status_code, 404)

    def test_get_question(self):
        res = self.client().get('/questions/20')
        self.assertEqual(res.status_code, 200)

    def test_not_found_get_question(self):
        res = self.client().get('/questions/2000')
        self.assertEqual(res.status_code, 404)

    def test_create_question(self):
        res = self.client().post('/questions', json={"question": "What's your age?", "answer": "30", "difficulty": "1", "category": 2})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['id'])

    def test_delete_question(self):
        res = self.client().delete('/questions/2')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['total_count'])

    def test_get_category_questions(self):
        res = self.client().get('/categories/2/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['questions'])

    def test_not_found_category_questions(self):
        res = self.client().get('/categories/2000/questions')
        self.assertEqual(res.status_code, 200)

    def test_search_questions(self):
        res = self.client().post('/questions/search')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['questions'])

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
