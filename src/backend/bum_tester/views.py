import json
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.template import loader
from django.conf import settings
import os
from .models import *
from . import *

@csrf_exempt
def index(request):
	latest_question_list = Question.objects.all()
	template = loader.get_template(os.path.join(settings.BASE_DIR,"bum_tester/templates/tester.html"))
	context = {
		"latest_question_list": latest_question_list,
	}
	return HttpResponse(template.render(context, request))

@csrf_exempt
def questions(request):
	product = Question.objects.all()
	result = []
	for i in product:
		result.append({
				'id': 		i.document_id,
				'question':	i.question,
				})
	return JsonResponse(result, safe=False)

@csrf_exempt
def question(request, id):
	product = Question.objects.get(pk=id)
	result = {
			'id': 		product.document_id,
			'question':	product.question,
			}
	return JsonResponse(result, safe=False)

@csrf_exempt
def pair(request, id):
	product = Question.objects.get(pk=id)
	answer = Answer.objects.get(pk=id)
	result = {
			'id': 		product.document_id,
			'question':	product.question,
			'answer':	answer.answer,
			'images':   [i.source  for i in Image.objects.filter(answer=answer)]
			}
	return JsonResponse(result, safe=False)

@csrf_exempt
def pairs(request):
	question = Question.objects.all()
	answer = Answer.objects.all()
	result = []
	for i in zip(question, answer):
		result.append({
				'id': 		i[0].document_id,
				'question':	i[0].question,
				'answer':	i[1].answer,
				'images':   [j.source for j in Image.objects.filter(answer=i[1])]
				})
	return JsonResponse(result, safe=False)