AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'allauth.account.auth_backends.AuthenticationBackend',) #all auth
SITE_ID = 3 #allauth - in the django admin under "sites" this refers to the site you are testing/using 
		# you can check by loading the page in admin and then looking up at the address bar for the number


# ACCOUNT_ADAPTER = 'project.users.allauth.AccountAdapter'  #allauth
APP_PATH = os.path.dirname(os.path.abspath(__file__))
 
# auth and allauth settings
ACCOUNT_LOGOUT_ON_GET = True
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
	'facebook': {
		'SCOPE': ['email', 'publish_actions'], # was 'publish_stream', now this 40 mins later
		'METHOD': 'js_sdk'  # instead of 'oauth2'
	}
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #allauth