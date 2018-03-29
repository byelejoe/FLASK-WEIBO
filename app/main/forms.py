#! /usr/bin/env python
# -*-coding: utf-8-*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, Length

class EditProfileForm(FlaskForm):
    location = StringField(u'居住地',validators=[DataRequired()])
    profession = StringField(u'所在行业',validators=[DataRequired()])
    about_me= TextAreaField(u'个人介绍',validators=[DataRequired()])
    submit= SubmitField(u'更新')

class AskForm(FlaskForm):
    body = StringField(u'写下你的问题',validators=[DataRequired()])
    desc = TextAreaField(u'问题描述（可选）', default='')
    submit = SubmitField(u'提交')


class AnswerForm(FlaskForm):
    body = TextAreaField(u'写回答', validators=[DataRequired()])
    submit = SubmitField(u'提交')

