from django.contrib import admin
#我们需要告诉管理站点Question 对象要有一个管理界面
#在管理站点中注册了Question对象，Django应该把它显示在管理站点的首页面上：
#自定义管理后台的表单:你会想要自定义管理界面中表单的外观和功能。 你可以通过在注册对象的时候告知Django一些你想要的选项来完成
from .models import Question,Choice
# 当管理有许多字段的表单时，选择一个直观的排序方式是一个重要而实用的细节。
# 说到有许多字段的表单，你可能想把表单分割成字段集：
#添加关联对象，在创建Question对象的同时可以直接添加一组Choice将会更好
#这告诉Django：“Choice对象在Question的管理界面中编辑。 默认提供足够3个Choice的空间。”
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
#fieldsets中每个元组的第一个元素是字段集的标题
      search_fields = ['question_text']
      fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
      inlines = [ChoiceInline]
      #使用display显示字段名称的元组，在对象的变更列表上作为列显示
      list_display = ('question_text', 'pub_date')
#admin.site.register(Question)
#任何时候你需要更改模型的管理选项，你将遵循此模式 — 创建一个模型管理类，然后将其作为第二个参数传递给admin.site.register()
admin.site.register(Question, QuestionAdmin)