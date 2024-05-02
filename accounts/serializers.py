from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
    
    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None :
            #provide django, password will be hashing!
            instance.set_password(password)
        instance.save()
        return instance

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password"]

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","last_login","email","name","nickname","birth","sex","intro"]

class byeSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["password"]