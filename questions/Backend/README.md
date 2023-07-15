# 100 Python Interview Questions in Backend

## 1- What are python frameworks for web development?

1. **Django**: A high-level, open-source web framework that follows the model-view-controller (MVC) architectural pattern. It's a batteries-included framework that provides a lot of built-in functionality and is known for its robust and scalable approach to web development.

2. **Flask**: A lightweight, micro web framework that is easy to use and great for small to medium-sized web applications. It is easy to learn and start with and gives developers more control over the application's structure and behavior.

3. **Pyramid**: A web framework designed for small and large web applications. It provides a lot of flexibility and can be used for a wide range of applications, from small personal blogs to large enterprise applications.

4. **Tornado**: A web framework for building web applications that are highly concurrent and perform well under heavy loads. It is ideal for building real-time applications, such as web sockets and long polling applications.

5. **FastAPI**: A modern, fast, web framework for building APIs with Python 3.6+ based on standard Python type hints. FastAPI is built on top of Starlette for web parts and Pydantic for data parts.

6. **Flask-RESTful**: A simple but flexible extension for Flask that makes it easy to handle RESTful API requests.

7. **Sanic**: A Flask like Python 3.5+ web server that's written to go fast. It allows the usage of the async/await syntax added in Python 3.5, which makes your code non-blocking and speedy.

## 2- Write an API using Django REST

```Python
# myapp/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

# myapp/serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'published_date', 'price')

# myapp/views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

This example defines a simple `Book` model with fields for (`title, author, published date, and price`). The `BookSerializer` class is used to convert the `Book` model into a format that can be returned by the API. The `BookViewSet` class is a view that handles the logic for creating, reading, updating, and deleting books. The URL routing is handled by the `DefaultRouter` class, which automatically generates the appropriate URLs for the API based on the views and models.

You can now run the development server and access the API endpoints at `http://localhost:8000/books/`. The API will support `GET, POST, PUT and DELETE` methods and you can use them to list, create, update, and delete books respectively.

## 3- What are the differences between Django Framework and Django REST Framework?

Django Framework and Django REST Framework are both web frameworks built on top of the Python programming language. However, they have different purposes and use different approaches to building web applications. **Django Framework** is a general-purpose web framework that can be used to build any type of web application.  
**Django REST Framework** is a framework specifically designed for building RESTful APIs. It provides a number of features that make it easy to build APIs that follow the REST architectural style.

A code sample using `Django Framework`:

```Python
from django.core.serializers import serialize
from django.http import HttpResponse


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = MyObj.objects.all()
        json_data = serialize("json", qs, fields=('my_field', 'my_other_field'))
        return HttpResponse(json_data, content_type='application/json')
```

A code sample using `Django REST Framework`:

```Python
from rest_framework import generics


class MyObjListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MyObjSerializer
```
