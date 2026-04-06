import jwt
from .models import User

SECRET_KEY = "SECRET_KEY_FOR_JWT"

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.custom_user = None  # 👈 используем своё поле

        auth = request.headers.get('Authorization')

        if auth:
            try:
                token_type, token = auth.split()
                if token_type.lower() == "bearer":
                    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
                    user_id = payload.get("user_id")
                    request.custom_user = User.objects.get(id=user_id, is_active=True)
            except Exception:
                request.custom_user = None

        return self.get_response(request)
