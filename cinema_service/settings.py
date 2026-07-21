# Certifique-se de remover qualquer linha solta como "from rest_framework import viewsets" ou similares no topo do settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "cinema",  # <-- ADICIONADO PARA RESOLVER O RUNTIME ERROR
]

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_THROTTLE_CLASSES": (
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ),
    "DEFAULT_THROTTLE_RATES": {
        "anon": "10/min",
        "user": "30/min",
    },
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Cinema API",
    "DESCRIPTION": "API for managing movies, cinema halls, movie sessions, orders and users.",
    "VERSION": "1.0.0",
}
