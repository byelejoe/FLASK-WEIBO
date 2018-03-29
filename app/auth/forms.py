# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField(u'邮箱', validators=[DataRequired(),Length(1,32), Email()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    remember = BooleanField(u'保持登录')
    submit = SubmitField(u'登录')

class RegisterForm(FlaskForm):
    email = StringField(u'邮箱', validators=[DataRequired(), Length(4,32),Email()])
    username = StringField(u'用户名', validators=[DataRequired(), Length(2,32),
                            Regexp('^[A-Za-z0-9_.]*$', 0, message=u'非法字符')])
    password = PasswordField(u'密码', validators=[DataRequired(),
                                                EqualTo('password2',message=u'两次输入必须一致')])
    password2 = PasswordField(u'重复密码', validators=[DataRequired()])
    submit = SubmitField(u'注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'邮箱已被注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'用户名已存在')