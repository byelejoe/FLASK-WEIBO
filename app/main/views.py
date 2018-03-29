#! /usr/bin/env python
# -*-coding: utf-8-*-

from flask import render_template,session, redirect, url_for, abort, flash
from datetime import datetime
from . import main
from .forms import EditProfileForm, AskForm, AnswerForm
from .. import db
from ..models import User, Question, Answer
from flask_login import login_required, current_user

@main.route('/', methods=['GET', 'POST'])
def index():
    questions=Question.query.order_by(Question.timestamp.desc()).all()
    return render_template('index.html', questions=questions,
                           current_time=datetime.utcnow())

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is  None:
        abort(404)
    return render_template('user.html',user=user)

@main.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form= EditProfileForm()
    if form.validate_on_submit():
        current_user.location=form.location.data
        current_user.profession=form.profession.data
        current_user.about_me=form.about_me.data
        db.session.add(current_user)
        flash(u'已更新')
        return redirect(url_for('.user', username=current_user.username))
    return render_template('edit_profile.html',form=form)

@main.route('/ask', methods=['GET','POST'])
@login_required
def ask():
    form = AskForm()
    if form.validate_on_submit():
        ques = Question(body=form.body.data,
                        desc=form.desc.data,
                        author=current_user._get_current_object())
        db.session.add(ques)
        flash(u'发布成功')
        return redirect(url_for('.index'))
    return render_template('ask.html', form=form)

@main.route('/question/<int:id>',methods=['GET','POST'])
def question(id):
    question = Question.query.get_or_404(id)
    form = AnswerForm()
    if form.validate_on_submit():
        ans=Answer(body = form.body.data,
                   question = question,
                   author = current_user._get_current_object())
        db.session.add(ans)
        flash(u'发布成功')
        return redirect(url_for('.question', id=question.id))
    answers=question.answers.order_by(Answer.timestamp.desc())
    return render_template('answer.html',question=question, form=form, answers=answers)

