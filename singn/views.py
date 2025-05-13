from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SendOTPSerializer, VerifyOTPSerializer
from .models import OTPCode, User
from .utils import send_message_to_telegram
import random
from django.utils import timezone
from datetime import timedelta


# OTP yuborish uchun view
class SendOTPView(APIView):
    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        if serializer.is_valid():
            chat_id = serializer.validated_data['chat_id']

            # OTP yaratish
            code = str(random.randint(100000, 999999))
            expiration_time = timezone.now() + timedelta(minutes=5)

            # Yangi OTP ni saqlash
            otp = OTPCode.objects.create(
                chat_id=chat_id,
                code=code,
                expiration_time=expiration_time
            )

            # Telegramga OTP yuborish
            send_message_to_telegram(chat_id, f"Sizning OTP kodingiz: {code}")

            return Response({"message": "Kod yuborildi"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            chat_id = serializer.validated_data['chat_id']
            code = serializer.validated_data['code']

            try:
                otp = OTPCode.objects.get(chat_id=chat_id)
            except OTPCode.DoesNotExist:
                return Response({"message": "Kod topilmadi"}, status=status.HTTP_404_NOT_FOUND)

            if otp.expiration_time < timezone.now():
                otp.delete()
                return Response({"message": "Kod muddati tugagan"}, status=status.HTTP_400_BAD_REQUEST)

            if otp.code == code:
                # ✅ Foydalanuvchi mavjudmi – tekshiramiz
                user, created = User.objects.get_or_create(user_chat=chat_id, defaults={
                    "user_chat": f"user_{chat_id}",  # username unique bo'lishi kerak
                })

                # Kodni o‘chirib tashlaymiz
                otp.delete()

                return Response({
                    "message": "Kod tasdiqlandi",
                    "user_id": user.id,
                    "created": created  # yangi user yaratildimi yoki mavjudmi
                }, status=status.HTTP_200_OK)

            return Response({"message": "Noto‘g‘ri kod"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
