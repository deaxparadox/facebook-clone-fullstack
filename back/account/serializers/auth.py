from rest_framework import serializers

from django.contrib.auth.models import User



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def login(self) -> dict | None:
        """
        This function should be called after `is_valid()`.
        """
        username = self.validated_data.get("username")
        password = self.validated_data.get("password")
        
        print(username, password)
        
        user = User.objects.get(username=username)
        
        # check user password
        if user.check_password(password):
            return {
                "token": user.account.apitoken.key,
                "uid": user.account.uid.id
            }
        
        return 
    
    
class APITokenSerilizer(serializers.Serializer):
    token = serializers.CharField()