import datetime
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Otp
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .serializers import UserSerializer, OtpSerializer, OtpVerificationSerializer


# Create your views here.


class RegistrationView(APIView):

    def post(self, request):

        data = request.data
        serializer = UserSerializer(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "Registration successful. Please verify your email."}, status= status.HTTP_201_CREATED)

        return Response({"message": "Something went wrong, Please try again","error" :serializer.errors}, status= status.HTTP_400_BAD_REQUEST)


class OTPView(APIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def post(self, request):

        data = request.data
        serializer = OtpSerializer(data = data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.filter(email = email).first()

            if user:
                otp_code = Otp.generate_otp()
                expiration_time = timezone.now() + datetime.timedelta(minutes=10)
                Otp.objects.create(user = user, otp_code= otp_code, expires_at = expiration_time)

                #Mock sending mail
                send_mail(
                    'Otp code for Email Verification',
                    f"Your Otp code for {email} is {otp_code}",
                    "zecopcompanyltd@gmail.com",
                    [email],
                    fail_silently=False
                )

                return Response({"message": "OTP sent to registered email"}, status= status.HTTP_202_ACCEPTED)
            
            return Response({"message": "User not found"}, status= status.HTTP_404_NOT_FOUND)
        
        return Response({"message": "Something went wrong, Please try again","error" :serializer.errors}, status= status.HTTP_400_BAD_REQUEST)
    

class OtpVerificationView(APIView):

    def post(self, request):

        data = request.data
        serializer = OtpVerificationSerializer(data=data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp_code = serializer.validated_data['otp']
            user = User.objects.filter(email = email).first()

            if user:
                hashed_otp = Otp.hash_otp(otp_code)
                otp = Otp.objects.filter(user=user, otp_code=hashed_otp, expires_at__gte = timezone.now()).first()
                # if verification done 
                # than generate a JWT token  

                if otp:
                    user.is_verified = True
                    user.save()

                    refresh = RefreshToken.for_user(user)
                    access_token = str(refresh.access_token)
                    return Response({"message": "Login Sucessfull", "token": access_token}, status= status.HTTP_200_OK)
                
                return Response({"message": "Invalid or Expired Otp"}, status= status.HTTP_400_BAD_REQUEST)
            
            return Response({"message": "User not found"}, status= status.HTTP_404_NOT_FOUND)
        
        return Response({"message": "Something went wrong, Please try again","error" :serializer.errors}, status= status.HTTP_400_BAD_REQUEST) 
                