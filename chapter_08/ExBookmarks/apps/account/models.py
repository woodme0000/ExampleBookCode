# -*- coding:utf-8 -*-

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """
    定义用户属性，和User 一对一关联
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    class Meta:
        verbose_name = u'用户属性'
        verbose_name_plural = verbose_name


class Contact(models.Model):
    """
    关注表
    """
    user_from = models.ForeignKey(User, related_name='rel_from_set', verbose_name=u'关注')

    user_to = models.ForeignKey(User, related_name='rel_to_set', verbose_name=u'被关注')

    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=u'时间')

    class Meta:
        verbose_name = u'粉丝'
        verbose_name_plural = verbose_name
        ordering = ('-created', )

    def __str__(self):
        return '{} follows {}'.format(self.user_from,
                                      self.user_to)


# Add following field to User dynamically 自己表用户关注自己表用户，这句话很关键
User.add_to_class('following',
                  models.ManyToManyField('self',
                                         through=Contact,
                                         related_name='followers',
                                         symmetrical=False))
