from rest_framework import serializers


class UserDataSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    stack = serializers.CharField()


class ResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
    user = UserDataSerializer()
    timestamp = serializers.DateTimeField()
    fact = serializers.CharField()


class ErrorSerializer(serializers.Serializer):
    error = serializers.CharField(default="Too many requests.")


user_cat_data_schema = {
    'summary': 'Get user data and cat fact',
    'description': 'Returns the users name, email and dev stack and a random\
        cat fact fetched from a third party API service. You can only make 50 requests/hr.',
    'operation_id': 'user_cat_data',
    'request': None,
    'responses': {
        200: ResponseSerializer,
        429: ErrorSerializer
    }
}