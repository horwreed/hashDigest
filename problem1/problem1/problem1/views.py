from django.http import JsonResponse, HttpResponseNotFound, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from . import helper

digest_to_message_map = {}

@csrf_exempt
def messages_post(request):
    try:
        message = helper.parse_request_body(request.body)
        message_digest = helper.generate_message_digest(message)

        digest_to_message_map[message_digest] = message

        output = {}
        output['digest'] = message_digest
        return JsonResponse(output)
    except Exception as err:
        return HttpResponseServerError("Error while making request=%s, error=%s" % (request.build_absolute_uri(), err))

def messages_get(request, hash):
    try:
        message = digest_to_message_map[hash]
        output = {'message' : message}
        return JsonResponse(output)
    except KeyError:
        return HttpResponseNotFound("404 Error, no message with hash=%s" % hash)
    except Exception as err:
        return HttpResponseServerError("Error while making request=%s, error=%s" % (request.build_absolute_uri(), err))

