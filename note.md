# Requests

- request.data returns the parsed content of the request body. This is similar to the standard request.POST and request.FILES attributes except that.

- use request.query_params instead of the Django's standard request.GET

- the response object consists of the following

1. data
2. status
3. template_name
4. headers
5. content_type

# Views

- When using class based views,  we inherit from the APIVIEW class

- Throttling reduces the number of calls that can be made to an api at a specific time.

- To override default settings, REST framework provides a set of additional decoartors which can be added to your views. These must come after (below)) the @api_view decorator.

These decorators correspond to the attributes set on APIView subclasses, described above.

The available decorators are:

@renderer_classes(...)
@parser_classes(...)
@authentication_classes(...)
@throttle_classes(...)
@permission_classes(...)
Each of these decorators takes a single argument which must be a list or tuple of classes.

