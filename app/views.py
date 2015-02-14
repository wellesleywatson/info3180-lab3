"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from app import app
from flask import render_template, flash, request, redirect, url_for
#app.secret_key = 'akunamatata'



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
  

@app.route('/contact',methods=['POST', 'GET']) 
def contact():
  #flash = 'Message successfully sent'
  if request.method == 'POST':
    fromaddr = request.form['email'] 
    fromname = request.form['name']
    toaddr  = 'nostaw7@gmail.com'
    toname = 'Wellesley Watson'
    subject = request.form['subject']
    msg = request.form['message']

    message = """From: {} <{}> 
    To: {} <{}> 
    Subject: {} 
     {} 
    """
    messagetosend = message.format(
                                 fromname,
                                 fromaddr,
                                 toname,
                                 toaddr,
                                 subject,
                                 msg)
    
    
    sendemail(fromaddr, toaddr, messagetosend)
    
  return render_template('contact.html')


def sendemail(faddr, taddr, msend):
  
  import smtplib
  #Credentials (if needed)
  username = 'nostaw7@gmail.com'
  password = 'cyrvtywxbbusnowj'

  # The actual mail send
  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.login(username,password)
  server.sendmail(faddr, taddr, msend)
  server.quit()

  
  
@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
