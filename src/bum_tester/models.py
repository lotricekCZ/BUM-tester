from datetime import date
from django.db import models
# from django.utils.translation import gettext_lazy as gtl
# from django.contrib.auth.models import User as DjangoUser
# from django.core.exceptions import ValidationError
# from django.core.validators import MaxValueValidator, MinValueValidator




# Question and answer model
class Question(models.Model):
	document_id = models.BigIntegerField(primary_key=True)
	question = models.TextField(null=False)
	
class Answer(models.Model):
    document_id = models.BigIntegerField(primary_key=True)
    answer	 = models.TextField()

class Image(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    source = models.TextField()
	# answered = models.BooleanField(default=False) # unused until we don't have valid User class determined by at least some cookie