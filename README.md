AppEngine landing page app
==========================

Boilerplate project template for hosting a simple landing page on Google App Engine, created shamelessly using
https://github.com/kamalgill/flask-appengine-template/.

Setup/Configuration
-------------------
1. Download this repository via `git clone git@github.com:skorokithakis/landing-page.git` or download the tarball at
   <http://github.com/skorokithakis/landing-page/tarball/master>
2. Set the application id in `app.yaml`
3. Add the secret keys for CSRF protection by running the `generate_keys.py` script at `application/generate_keys.py`,
   which will generate the secret keys module at application/secret\_keys.py
4. Customize the main HTML template at `application/templates/index.html`.
5. Add your CSS and JS at `application/static/css/` and `application/static/js`.
6. Customize favicon at `application/static/img/favicon.ico`
7. Customize 404 page at `application/templates/404.html`

You can view the signed up users' emails at `/view_signups` (needs admin privileges).

Previewing the Application
--------------------------
To preview the application using App Engine's development server,
use [dev_appserver.py][devserver]

<pre class="console">
  dev_appserver.py .
</pre>

Assuming the latest App Engine SDK is installed, the test environment is
available at <http://localhost:8080>


Deploying the Application
-------------------------
To deploy the application to App Engine, use [appcfg.py update][appcfg]
<pre class="console">
  appcfg.py update .
</pre>

The application should be visible at http://{YOURAPPID}.appspot.com


License
-------
This software is provided under the MIT license.
