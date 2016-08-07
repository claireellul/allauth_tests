
The aim of this demonstration is to set up a simple test showing how the django-allauth code can be used to associate multiple social media accounts with one user account.  

This code sample is based mainly on the code sample provided here: http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/ (Accessed 6th August 2016) but has also add additions of code from here: http://stackoverflow.com/questions/13140021/django-allauth-linking-multiple-social-accounts-to-a-single-user (Accessed 7th October 2016)


Bug fixes and changes made to the original code from Sarah Hangstrom

1. removed all references to {% load url from future %} as this is not needed in the version of Django being used: version 1.9.9 running under Python 2.7 (these are in the .html files)

2. added the twitter provider as follows (repeated for the other providers):
- create an App on the given provider and get a secret key and an application key (these may have different names)
- Run the following SQL to add the new app to the Django installation (you can add these values via the Django admin tools instead):
    INSERT INTO socialaccount_socialapp (provider, name, secret, client_id, key)
    VALUES ('twitter', 'Twitter', 'axm6JHiPd2qqnMWhFW4kpceTELGtWykP116JAPT7y1TQkDDzyY', 'MK9OLSo0f0oBAJTTjEVIQGiYF', '');

    INSERT INTO socialaccount_socialapp_sites (socialapp_id, site_id) VALUES (2,1);  (where 2 - the socialapp_id - is the ID of the new entry in socialaccount_socialapp and 1 is the site_id which you can find in django_site)

- in settings.py, under installed apps add:
      'allauth.socialaccount.providers.twitter'

- in allauth_settings.py, under SOCIAL_ACCOUNT_PROVIDERS add:
      'twitter': {
          'SCOPE': ['email', 'publish_stream'],
          'METHOD': 'oauth2'  # instead of 'oauth2'
      }

- in login.html add (under the identical statement for facebook that is already in the example): 
      <a href="/accounts/twitter/login/"><div class="tw"></div></a>


- modify style.css to add the tw class needed for the above, as follows:
      .tw {
          background: url('/static/img/tw.png') no-repeat center top;
          box-shadow: 2px 2px 8px rgba(0,0,0,.7);
          border-radius: 5px;
          width: 198px;
          height: 37px;
          margin: 80px auto;
          overflow: hidden;
      }


- add the required twitter logo to 
      /larb/static/img/

3.  Added the code to enable the linking of additional social media accounts to the index.html file
    

    <xmp>	{% load socialaccount %}
      <p><a href="{% provider_login_url "facebook" process="connect" %}">Connect a facebook account</a></p>
      <p><a href="{% provider_login_url "google" process="connect" %}">Connect a Google account</a></p>
    </xmp>


CHANGES TO DJANGO-ALLAUTH
The django-allauth master branch has not (as of 7th August 2016) been updated to automatically request the e-mail address from twitter. However this branch contains the code changes needed: https://github.com/pennersr/django-allauth/pull/1453/commits/28c90c3c5f42c7f8740d57819ad962fc7a504607

