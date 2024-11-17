from App.models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from App.models import *


# from rest_framework.validators import UniqueValidator
# from rest_framework_jwt.settings import api_settings



class OTPSerializer(serializers.Serializer):
    email = serializers.EmailField()

class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(max_length=128)

    def validate(self, data):
        try:
            user = MyUser.objects.get(email=data['email'])
        except MyUser.DoesNotExist:
            raise serializers.ValidationError("Mtumiaji mwenye email hii teyari yupo.")

        otp_instance = OTP.objects.filter(user=user, otp=data['otp']).last()
        if not otp_instance or not otp_instance.is_valid():
            raise serializers.ValidationError("OTP sio sahihi au imeshaisha muda wake.")
        return data

    def save(self):
        user = MyUser.objects.get(email=self.validated_data['email'])
        user.set_password(self.validated_data['new_password'])
        user.save()
        OTP.objects.filter(user=user).delete()
        return user

        


class MyUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyUser
        fields = '__all__'










class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('username', 'email','phone', 'password')




class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = (
            'username', 
            'email', 
            'phone',
            'company_name',
            
            'profile_image',
            
            'Location'
        )



#______________MWISHO HAPA DJANGO REACT AUTHENTICATION_________________





class UserDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyUser
        fields = '__all__'
        # fields = ['id', 'username', 'email','phone','first_name','profile_image']












# kwa ajili ya kumregister mtu bila kutumia token
class UserCreationSerializer(serializers.ModelSerializer):
	username=serializers.CharField(max_length=25)
	email=serializers.EmailField(max_length=50)
	password=serializers.CharField(max_length=50)


	class Meta:
		model= MyUser
		fields= ['username','email','password']
		#fields='__all__'

	def validate(self,attrs):
		username_exists = MyUser.objects.filter(username=attrs['username']).exists()
		if username_exists:
			raise serializers.ValidationError(detail="User with username already exists")


		email_exists = MyUser.objects.filter(email=attrs['email']).exists()
		if email_exists:
			raise serializers.ValidationError(detail="User with email already exists")

		return super().validate(attrs)






class WatejaWoteSerializer(serializers.ModelSerializer):
    # Unit = UnitZaWatejaWoteSerializer(many=False)
    # FoodGroup = MakundiYaWatejaWoteSerializer(many=False)
    class Meta:
        model = WatejaWote
        fields = '__all__'


#--------------------CART AND CART ITEMS--------------------
class WatejaWoteCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatejaWoteCart
        fields = '__all__'


class WatejaWoteCartItemsSerializer(serializers.ModelSerializer):
    cart = WatejaWoteCartSerializer()
    Mteja = WatejaWoteSerializer()

    #table = WatejaWoteTablesSerializer()
    class Meta:
        model = WatejaWoteCartItems
        fields = '__all__'


