from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import api_view
from Blog.models import Post
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter


# @api_view(["GET", "POST"])
# def api_homepage(request):
#     if request.method == "GET":
#         all_posts = Post.objects.all()
#         serializer = PostSerializer(all_posts, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     else:
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"success": "Nice Work!!",
#                             "data": serializer.data}, status=status.HTTP_201_CREATED)



# @api_view(["GET", "PUT", "DELETE"])
# def api_detailpage(request, id):
#     if request.method == "GET":
#         detail = Post.objects.get(id=id)
#         new_serializer = PostSerializer(detail)
#         return Response(new_serializer.data, status=status.HTTP_200_OK)
#     elif request.method == "PUT":
#         detail = Post.objects.get(id=id)
#         serializer = PostSerializer(detail, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         detail = Post.objects.get(id=id)
#         detail.delete()
#         return Response("Post has been deleted", status=status.HTTP_204_NO_CONTENT)



# class api_homepage(APIView):
#     def get(self, request, id):
#          detail = Post.objects.get(id=id)
#          new_serializer = PostSerializer(detail)
#          return Response(new_serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#           serializer = PostSerializer(data=request.data)
#           if serializer.is_valid():
#             serializer.save()
#             return Response({"success": "Nice Work!!",
#                             "data": serializer.data}, status=status.HTTP_201_CREATED)
#           return Response("invalid data entered")
    


# class api_detailpage(APIView):
#     def get(self, request, id):
#          detail = Post.objects.get(id=id)
#          new_serializer = PostSerializer(detail)
#          return Response(new_serializer.data, status=status.HTTP_200_OK)

#     def put(self,request, id):
#         detail = Post.objects.get(id=id)
#         serializer = PostSerializer(detail, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
#     def delete(self,request, id):
#         detail = Post.objects.get(id=id)
#         detail.delete()
#         return Response("Post has been deleted", status=status.HTTP_204_NO_CONTENT)


# class api_homepage(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



# class api_detailpage(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = "id"


class api_commenthome(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ["post__title", "name", "message"]


class api_commentdetail(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "id"

# @api_view(["GET", "POST"])
# def api_commenthome(request):
#     if request.method == "GET":
#         all_posts = Comment.objects.all()
#         serializers = CommentSerializer(all_posts, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)
#     else:
#         serializers = CommentSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    


# @api_view(["GET", "PUT", "DELETE"])
# def api_commentdetail(request, id):
#     if request.method == "GET":
#         detail = Comment.objects.get(id=id)
#         serializers = CommentSerializer(detail)
#         return Response(serializers.data, status=status.HTTP_200_OK)
#     elif request.method == "PUT":
#         detail = Comment.objects.get(id=id)
#         serializers = CommentSerializer(detail, data=request.data, partial=True)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_202_ACCEPTED)
#         return Response("not accepted")
    #   else:
    #     serializers = Comment.objects.get(id=id)
    #     serializers.delete()
    #     return Response("deleted successfully")



# class api_commenthome(APIView):
#     pagination_class = PageNumberPagination
#     def get(self, request):
#            all_posts = Comment.objects.all()
#            serializers = CommentSerializer(all_posts, many=True)
#            return Response(serializers.data, status=status.HTTP_200_OK)
#     def post(self,request):
#         serializers = CommentSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class api_commentdetail(APIView):
#      def get(self, request, id):
#               detail = Comment.objects.get(id=id)
#               serializers = CommentSerializer(detail)
#               return Response(serializers.data, status=status.HTTP_200_OK)
#      def put(self, request, id):
#         detail = Comment.objects.get(id=id)
#         serializers = CommentSerializer(detail, data=request.data, partial=True)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_202_ACCEPTED)
#         return Response("not accepted")
#      def delete(self, request, id):
#         serializers = Comment.objects.get(id=id)
#         serializers.delete()
#         return Response("deleted successfully")
     


    

