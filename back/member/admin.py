from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Members

# Register your models here.
# class MemberInline(admin.StackedInline):
#   model = Members
#   can_delete = False
#   verbose_name_plural = 'Members'
#   fk_name = 'user'

# class CustomUserAdmin(UserAdmin):
#   # inlines = (MemberInline, )
#   list_display=('username', 'email', 'first_name', 'last_name')
#   list_select_related = ('members', )

#   #admin페이지에서 유저 수정할때 나타나는 입력폼 무엇으로 할건지
#   fieldsets = UserAdmin.fieldsets + (
#     (None, {'fields': ('members_id', 'birth', 'question_type', 'question_ans')}),
#   )
#   # admin 페이지에서 사용자 추가할때 입력폼
#   add_fieldsets = (
#     (None, {'fields' : ('members_id', 'birth', 'question_type', 'question_ans')}),
#   )

#   # def get_inline_instances(self, request, obj=None):
#   #   if not obj:
#   #     return list()
#   #   return super(CustomUserAdmin, self).get_inline_instances(request, obj)

# admin.site.unregister(User)
admin.site.register(Members)