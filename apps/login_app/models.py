from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

# Create your models here.

class UserManager(models.Manager):
    def loginVal(self, postData):
        results = {'status': True, 'errors':[], 'user': None}
        users = self.filter(username = postData['username'])
        
        if len(users) < 1:
            results['status'] = False
        else:
            if bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
                results['user'] = users[0]
            else:
                results['status'] = False
        return results


    def creator(self, postData):
        user = self.create(name = postData['name'], username = postData['username'], password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
        return user
   
    # validate must take (self)
    def validate(self, postData):
        results = {'status': True, 'errors':[]}
        if len(postData['name']) < 3:
            results['errors'].append('Your name is too short.')
            results['status'] = False
        
        # check if first name is valid
        if not re.match("^[A-z][A-z|\.|\s]+$", postData['name']):
            results['errors'].append('Your name is not valid.')
            results['status'] = False
            
        if len(postData['username']) < 3:
            results['errors'].append('Your username is too short.')
            results['status'] = False

        if not re.match("^[A-z][A-z|\.|\s]+$", postData['username']):
            results['errors'].append('Your username is not valid.')
            results['status'] = False

        if postData['password'] != postData['c_password']:
            results['errors'].append('Your passwords do not match.')
            results['status'] = False

        if len(postData['password']) < 8:
            results['errors'].append('Your password is too short.')
            results['status'] = False

        if len(self.filter(username = postData['username'])) > 0:
            results['errors'].append('Username already exists.')
            results['status'] = False

        return results


class User(models.Model):
    name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    trips = models.ManyToManyField('self')
    objects = UserManager()
    