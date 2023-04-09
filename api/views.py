from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import os
import json

@csrf_exempt
def generate_response(request):
    # Set up the OpenAI API credentials
    openai.api_key = "USE_YOUR_API"
    
    model_engine = "text-davinci-002"
  
    # Get the question from the POST payload
    data = json.loads(request.body)
    question = data.get("question")
    # Get the question from the request
    # question = request.POST.get("question")
    # return JsonResponse({"response": question})
    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine=model_engine,
        prompt=question,
        max_tokens=1000,
        n=1,
    )

    # Return the generated response as a JSON object
    return JsonResponse({"response": response.choices[0].text})