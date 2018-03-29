from flask_mail import Message
from flask import render_template, current_app
from . import mail
from threading import Thread

def send_sync_mail(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(subject+app.config['ZH_MAIL_SUBJECT_PREFIX'] ,
                  recipients=[to], sender=app.config['ZH_MAIL_SENDER'] ,charset='utf-8')
    msg.body = render_template(template+'.txt', **kwargs)
    msg.html = render_template(template+'.html', **kwargs)
    thr = Thread(target=send_sync_mail,args=[app,msg])
    thr.start()
    return thr