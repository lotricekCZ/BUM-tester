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
    """
    This function is a view for the index page of the application.
    It renders the 'tester.html' template with the list of all questions
    from the 'Question' model.

    Args:
        request (HttpRequest): The request object representing the HTTP request.

    Returns:
        HttpResponse: The rendered HTML response.
    """

    # Fetch all questions from the 'Question' model
    latest_question_list = Question.objects.all()

    # Get the absolute path to the 'tester.html' template
    template_path = os.path.join(settings.BASE_DIR, "bum_tester/templates/tester.html")

    # Load the template
    template = loader.get_template(template_path)

    # Create the context
    context = {
        "latest_question_list": latest_question_list,
    }

    # Render the template with the context and return the response
    return HttpResponse(template.render(context, request))

@csrf_exempt
def questions(request):
    """
    This function is a view that returns all questions from the database as a JSON response.

    Args:
        request (HttpRequest): The request object representing the HTTP request.

    Returns:
        JsonResponse: A JSON response containing a list of dictionaries,
        each representing a question with 'id' and 'question' keys.
    """
    # Fetch all questions from the 'Question' model
    product = Question.objects.all()

    # Create a list of dictionaries containing 'id' and 'question' keys for each question
    result = [{'id': i.document_id, 'question': i.question} for i in product]

    # Return the list of dictionaries as a JSON response
    return JsonResponse(result, safe=False)

@csrf_exempt
def question(request, id):
    """
    This function is a view that returns a question from the database as a JSON response.

    Args:
        request (HttpRequest): The request object representing the HTTP request.
        id (int): The id of the question to retrieve.

    Returns:
        JsonResponse: A JSON response containing a dictionary representing a question with 'id' and 'question' keys.
    """
    # Fetch a question from the 'Question' model using the provided id
    product = Question.objects.get(pk=id)

    # Create a dictionary containing 'id' and 'question' keys for the question
    result = {
        'id': product.document_id,
        'question': product.question,
    }

    # Return the dictionary as a JSON response
    return JsonResponse(result, safe=False)


@csrf_exempt
def pair(request, pair_id):
    """
    Returns a pair of question and answer from the database as a JSON response.

    Args:
        request (HttpRequest): The request object representing the HTTP request.
        pair_id (int): The id of the pair to retrieve.

    Returns:
        JsonResponse: A JSON response containing a dictionary representing a pair with 'id', 'question' and 'answer' keys.
                      The 'images' key contains a list of image sources.
    """
    question = Question.objects.get(pk=pair_id)
    answer = Answer.objects.get(pk=pair_id)

    result = {
        'id': question.document_id,
        'question': question.question,
        'answer': answer.answer,
        'images': [image.source for image in Image.objects.filter(answer=answer)],
    }
    return JsonResponse(result, safe=False)

@csrf_exempt
def pairs(request):
    """
    Returns all pairs of questions and answers from the database as a JSON response.

    Args:
        request (HttpRequest): The request object representing the HTTP request.

    Returns:
        JsonResponse: A JSON response containing a list of dictionaries representing pairs with 'id', 'question', 'answer' and 'images' keys.
                      The 'images' key contains a list of image sources.
    """
    # Get all questions and answers from the database
    question = Question.objects.all()
    answer = Answer.objects.all()

    # Create a list to store the pairs
    result = [
        {
            'id': 		question_item.document_id,
            'question':	question_item.question,
            'answer':	answer_item.answer,
            'images':   [image.source for image in Image.objects.filter(answer=answer_item)]
        }
        for question_item, answer_item in zip(question, answer)
    ]

    # Return the list as a JSON response
    return JsonResponse(result, safe=False)
