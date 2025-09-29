from django.shortcuts import render
from .serializers import UserRegisterSerializer, BlogSerializer, UpdateUserProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Blog


@api_view(["POST"])
def register_user(request):
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_blog(request):
    user = request.user
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(author=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def list_blogs(request):
    try:
        blogs = Blog.objects.filter(is_draft=False)
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    except Blog.DoesNotExist:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    if blog.author == request.user:
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error":"You are not allowed to edit this blog"}, status=status.HTTP_403_FORBIDDEN)



@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    if blog.author == request.user:
        blog.delete()
        return Response({"message":"Blog deleted successfuly"}, status=status.HTTP_202_ACCEPTED)
    return Response({"error":"You are not allowed to delete this blog"}, status=status.HTTP_403_FORBIDDEN)



@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = request.user
    serializer = UpdateUserProfileSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)