import os
import sys

# load a bunch of environment

DEBUG = os.getenv('DEBUG') in ['True', 'true', '1', 'yes']
if DEBUG:
    SQLALCHEMY_ECHO = True
TESTING = os.getenv('TESTING') in ['True', 'true', '1', 'yes']

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False

LOG_LEVEL = os.getenv('LOG_LEVEL') or 'debug'

SECRET_KEY = os.getenv('SECRET_KEY')
NONCE_SECRET = os.getenv('NONCE_SECRET')
HASHIDS_SALT = os.getenv('HASHIDS_SALT')

MONTHLY_SUBMISSIONS_LIMIT = int(os.getenv('MONTHLY_SUBMISSIONS_LIMIT') or 1000)
ARCHIVED_SUBMISSIONS_LIMIT = int(os.getenv('ARCHIVED_SUBMISSIONS_LIMIT') or 100)
EXPENSIVELY_WIPE_SUBMISSIONS_FREQUENCY = float(os.getenv('EXPENSIVELY_WIPE_SUBMISSIONS_FREQUENCY') or 0.2)
REDIS_URL = os.getenv('REDISTOGO_URL') or os.getenv('REDISCLOUD_URL') or 'redis://localhost:6379'

CDN_URL = os.getenv('CDN_URL')

SERVICE_NAME = os.getenv('SERVICE_NAME') or 'Forms'
UPGRADED_PLAN_NAME = os.getenv('UPGRADED_PLAN_NAME') or 'Gold'
SERVICE_URL = os.getenv('SERVICE_URL') or 'http://example.com'
CONTACT_EMAIL = os.getenv('CONTACT_EMAIL') or 'team@example.com'
NEWSLETTER_EMAIL = os.getenv('NEWSLETTER_EMAIL') or 'signup@example.com'
DEFAULT_SENDER = os.getenv('DEFAULT_SENDER') or 'Forms Team <submissions@example.com>'
ACCOUNT_SENDER = os.getenv('ACCOUNT_SENDER') or DEFAULT_SENDER
API_ROOT = os.getenv('API_ROOT') or '//example.com'

SENDGRID_USERNAME = os.getenv('SENDGRID_USERNAME')
SENDGRID_PASSWORD = os.getenv('SENDGRID_PASSWORD')

STRIPE_TEST_PUBLISHABLE_KEY = os.getenv('STRIPE_TEST_PUBLISHABLE_KEY')
STRIPE_TEST_SECRET_KEY = os.getenv('STRIPE_TEST_SECRET_KEY')
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY') or STRIPE_TEST_PUBLISHABLE_KEY
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY') or STRIPE_TEST_SECRET_KEY
STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')

GA_KEY = os.getenv('GA_KEY') or '123456'

RECAPTCHA_SECRET = os.getenv('RECAPTCHA_SECRET')
RECAPTCHA_KEY = os.getenv('RECAPTCHA_KEY')

RATE_LIMIT = os.getenv('RATE_LIMIT', '30 per hour')
REDIS_RATE_LIMIT = os.getenv('REDIS_URL')  # heroku-redis

CONTACT_FORM_HASHID = os.getenv('CONTACT_FORM_HASHID', CONTACT_EMAIL)

TYPEKIT_KEY = os.getenv('TYPEKIT_KEY', '1234567')
