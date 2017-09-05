# -*- coding:utf-8 -*-
"""
Django settings for EBookmarks project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# 因为我们把app都放到了apps,所以我们需要定义一下apps的搜索路径，使用 sys.path.insert
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 第一个参数是搜索位置，第二个参数是使用Base_DIR和app拼成一个路径
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(1, os.path.join(BASE_DIR, 'extra_apps'))

# 设置用户登录跳转相关
from django.core.urlresolvers import reverse_lazy
LOGIN_REDIRECT_URL = reverse_lazy('accounts:dashboard')
LOGIN_URL = reverse_lazy('accounts:login')  # 重定向用户登录的URL(例如:使用login_required装饰器 (decorator))
LOGOUT_URL = reverse_lazy('accounts:logout')  # 重定向用户登出的URL

# 设置认证后台，可以添加自定义的认证后台
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBacked',
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*97d0m9ab_wvggg$a+2h#ba!^)+y*4e+&8j-d7$y&1h_8&8z)p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'account',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',  # 用户消息框架
    'django.contrib.staticfiles',
    'images',
    'sorl.thumbnail',
    'pure_pagination',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'EBookmarks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'EBookmarks.wsgi.application'

# 配置用户验证方式为调用自己的UserProfile里面的验证方式

# 配置邮件发送服务器
EMAIL_HOST = 'smtp.aliyun.com'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'luojingen@aliyun.com'
EMAIL_HOST_PASSWORD = 'luo1380126'
EMAIL_USE_TLS = False
EMAIL_FROM = 'luojingen@aliyun.com'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ebookmarks',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
# 不使用全球时间，使用本
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# 配置图片文件上传的默认根路径，需要在setting里面加入如下配置文件，用户可以上传自己的图片
MEDIA_URL = '/media/'  # 管理用户上传的多媒体文件的主 URL
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 图片这些文件在本地保存的路径
