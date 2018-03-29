#! /usr/bin/env python
# -*-coding: utf-8-*-

from flask import current_app, render_template,request, redirect, url_for, flash
from . import auth
from forms import LoginForm, RegisterForm
from ..models import  User
from flask_login import login_user, login_required, logout_user, current_user
from ..email import send_mail
from .. import db

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('auth/login.html',form=form)


@login_required
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@auth.route('/register',methods=['GET','POST'])
def register():
    app = current_app._get_current_object()
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_mail(user.email, u'确认账户',
                  'mail/confirm',user=user,token=token)
        db.session.add(user)
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@login_required
@auth.route('/confirm/<token>')
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash(u'确认成功')
    else:
        flash(u'确认失败')
    return redirect(url_for('main.index'))

