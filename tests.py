import unittest
from urllib import response

from flask_login import current_user
from project import app, db
from flask_testing import TestCase

from project.models import BlogPost, User

class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("admin", "admin@admin.com", "admin"))
        db.session.add(User("admin2", "admin2@admin.com", "admin2"))
        db.session.add(BlogPost("Test post", "This is a test. Only a test.", 1))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):

    # Ensure that main page requires user login
    def test_main_route_requires_login(self):
        response =  self.client.get('/', follow_redirects=True)
        self.assertIn(b'Please log in to access this page.', response.data)

    # Ensure that posts show up on the main page
    def test_posts_show_up_on_main_page(self):
         
        response =  self.client.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'This is a test. Only a test', response.data)

    def test_posts_get_added(self):
        with self.client:
            response =  self.client.post(
                '/login',
                data=dict(username="admin2", password="admin2"),
                follow_redirects=True
            )

            response = self.client.post(
                '/', 
                data=dict(title='testing title', description='added...', author_id=current_user.id),
                follow_redirects=True
            )

            self.assertIn(b"testing title", response.data)
            self.assertIn(b"added...", response.data)
            self.assertIn(b"admin2", response.data)


class AuthViewsTests(BaseTestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        response =  self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        response =  self.client.get('/login')
        self.assertIn(b'Please login', response.data)

    # Ensure login behaves correctly with correct credentials
    def test_correct_login(self):
        with self.client:
            response =  self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            self.assertIn(b'You were logged in', response.data)
            self.assertTrue(current_user.name == "admin")
            self.assertTrue(current_user.is_active)

    # Ensure login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
         
        response =  self.client.post(
            '/login',
            data=dict(username="wrong", password="wrong"),
            follow_redirects=True
        )
        self.assertIn(b'Invalid username or password', response.data)

    # Ensure logout behaves correctly
    def test_logout(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            response =  self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'You were just logged out', response.data)
            self.assertFalse(current_user.is_active)
    
    # Ensure that logout page requires user login
    def test_logout_route_requires_login(self):
         
        response =  self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)

    # Ensure user can register
    def test_user_registeration(self):
        response = self.client.post('/register', data=dict(
            username='Michael', email='michael@realpython.com',
            password='python', confirm_password='python'
        ), follow_redirects=True)
        self.assertIn(b'login', response.data)
        self.client.get('/logout', follow_redirects=True)
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="Michael", password="python"),
                follow_redirects=True
            )
            self.assertIn(b'You were logged in', response.data)
            self.assertTrue(current_user.name == "Michael")
            self.assertTrue(current_user.is_active())

if __name__ == '__main__':
    unittest.main()