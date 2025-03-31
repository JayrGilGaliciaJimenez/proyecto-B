from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer

from .serializers import CustomUser, CustomUserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import logging

logger = logging.getLogger(__name__)


# Hacer las vistas del api rest
class UserViewSets(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    renderer_classes = [JSONRenderer]
    # Podemos agregar la autenticacion
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    # Especificar los metodos que se pueden usar
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAuthenticated()]
        return []


# hacer una vista que devulva el token
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class CustomUserFormAPI(APIView):

    def get(self, request, *args, **kwargs):
        form = CustomUserCreationForm()
        fields = {
            field: {
                'label': form[field].label,
                'input': form[field].field.widget.attrs,
                'type': form[field].field.widget.input_type,
            }
            for field in form.fields
        }
        return Response(fields)

    def post(self, request, *args, **kwargs):
        logger.debug("Received data: %s", request.data)
        form = CustomUserCreationForm(request.data)
        if form.is_valid():
            user_data = form.cleaned_data
            User = get_user_model()
            user = User.objects.create_user(
                email=user_data['email'],
                password=user_data['password1'],
                name=user_data['name'],
                surname=user_data['surname'],
                control_number=user_data['control_number'],
                age=user_data['age'],
                tel=user_data['tel'],
            )
            return Response({'message': 'Usuario creado con éxito'}, status=status.HTTP_201_CREATED)
        logger.error("Form errors: %s", form.errors)

        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)