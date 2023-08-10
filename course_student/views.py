from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer



@api_view(['GET'])
def post_list(request):
    queryset = Student.objects.all()
    print(queryset)
    serializer = StudentSerializer(queryset, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST'])
def create_post(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Good job!', status=201)
    else:
        return Response('Nooo', status=400)
    
@api_view(['PUT'])
def update_post1(request, id):
    post = get_object_or_404(Student, id=id) 
    serializer = StudentSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('Ok')
    return Response(serializer.errors, status=400)
    
    
    
@api_view(['PATCH'])
def update_post2(request, id):
    post = get_object_or_404(Student, id=id) 
    serializer = StudentSerializer(post, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

    
@api_view(['DELETE'])
def delete_post(request, id):
    post = get_object_or_404(Student, id=id)
    post.delete()
    return Response('Good delete!', status=204)