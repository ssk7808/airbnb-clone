from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer

from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


""" class Categories(APIView): 
    def get(self, request):
        all_categories = Category.objects.all()  # 모든 카테고리 가져와서
        serializer = CategorySerializer(all_categories, many=True)  # 시리얼라이징
        return Response(serializer.data)
        # 하고 전부 다 보여줌

    def post(self, request):
        serializer = CategorySerializer(data=request.data)  # request.data : 유저가 보낸 데이터
        if serializer.is_valid():
            # CategorySerializer에 적어놓은 형식이랑 유저가 보낸 데이터의 형식이 같은지 검증
            new_category = (
                serializer.save()
            )  # 검증된 정보를 가지고 save (create메서드) 를 통해 새로운 Category 생성
            return Response(CategorySerializer(new_category).data)  # 생성된 Category 보여줌
        else:
            return Response(serializer.errors) """


""" @api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()  # 모든 카테고리 가져와서
        serializer = CategorySerializer(all_categories, many=True)  # 시리얼라이징
        return Response(
            serializer.data,  # 하고 전부 다 보여줌
        )
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)  # request.data : 유저가 보낸 데이터
        if serializer.is_valid():
            # CategorySerializer에 적어놓은 형식이랑 유저가 보낸 데이터의 형식이 같은지 검증
            new_category = (
                serializer.save()
            )  # 검증된 정보를 가지고 save (create메서드) 를 통해 새로운 Category 생성
            return Response(CategorySerializer(new_category).data)  # 생성된 Category 보여줌
        else:
            return Response(serializer.errors) """


""" class CategoryDetail(APIView):
    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound
        return category

    def get(self, request, pk):
        serializer = CategorySerializer(self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = CategorySerializer(
            self.get_object(pk),
            data=request.data,
            partial=True,
        )
        # 원래 있는 데이터와 유저가 있는 데이터 모두를 가지고 CategorySerializer 를 만든다.
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT) """


""" 
def category(request, pk):
    # 먼저 category pk 가 있는지 확인한 후 없으면 에러 띄움
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = CategorySerializer(
            category,
            data=request.data,
            partial=True,
        )
        # 원래 있는 데이터와 유저가 있는 데이터 모두를 가지고 CategorySerializer 를 만든다.
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)
    elif request.method == "DELETE":
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT) """
