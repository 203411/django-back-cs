# Ambientación del back Django

## Instalación del recurso de restframework librerias
```bash 
pip install djangorestframework
```
```bash 
pip install markdown
```
```bash 
pip install django-filter
```
```bash
pip install virtualenv
```
```bash
pip install psycopg2
```
```bash
pip install python-dotenv
```
```bash
pip install django-cors-headers
```

## Agregar la libreria a INSTALLED_APPS en settings
```bash 
'rest_framework',
```
```bash
'rest_framework.authtoken',
```
```bash
'corsheaders',
```

## Agregar en MIDDLEWARE en settings
```bash
'corsheaders.middleware.CorsMiddleware',
```

## Agregar lo siguiente en settings
```bash
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]
```

## Tiempo de expiración de token, configuracion en setting
```bash
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=45),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=2),
}
```
