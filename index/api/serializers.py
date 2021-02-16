
from index.models import Subscriber
from rest_framework import serializers
from rest_framework.authtoken.models import Token



# class UserDetailSerializer(serializers.ModelSerializer):
#     token = serializers.SerializerMethodField()
    

#     class Meta:
#         model = User
#         fields = (
#             'first_name',
#             'last_name',
#             'username',
#             'email',
#             'tel_numb',
#             'birthday_data',
#             'gender',
#             'date_joined',
#             'last_login',
#             'token'


#         )

#     def get_token(self, user):
#         token, created = Token.objects.get_or_create(user=user)
#         return token.key


class SubscribeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subscriber
        fields = (
            'email',

        )

    def validate_email(self, value):
        if Subscriber.objects.filter(email=value.lower()).exists(): 
            raise serializers.ValidationError("subscriber with this email already exists.") 
        return value.lower()



# from incidents.models import Site, Update, Incident, Uptime, Subscriber

# class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
    
    
#     class Meta:
#         model = Subscriber
#         fields = ('email',)