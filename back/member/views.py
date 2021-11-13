from django.http import request
from rest_framework.views   import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import Members
from .serializers import MemberDetailSerializer, MemberSerializer

# Create your views here.
class MemberDetail(APIView):
    def get(self, request, format=None):
        pk = request.GET['id']
        queryset = Members.objects.get(members_id=pk)
        serializer = MemberDetailSerializer(queryset)
        return Response(serializer.data)

class SignUp(APIView):
    def post(self, request, format=None):
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"],
                password = request.POST["password1"],
                first_name = request.POST["firstname"],
                last_name = request.POST["lastname"],
                email_address = request.POST["email"]
            )
            birth = request.POST["birth"]
            Qtype = request.POST["Qtype"]
            Qans = request.POST["Qans"]
            member = Members(user=user, birth = birth, question_type = Qtype, question_ans = Qans)
            member.save()