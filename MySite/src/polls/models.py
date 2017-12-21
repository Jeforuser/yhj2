from django.db import models
#创建两个模型，Question和Choice
#每个模型都有一些类变量，在模型中每个类变量都代表了数据库中的一个字段，类型
#某些Field 类具有必选的参数。 例如，CharField要求你给它一个max_length
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
# 注意我们使用ForeignKey定义了一个关联。 它告诉Django每个Choice都只关联一个Question。
# Django支持所有常见的数据库关系：多对一，多对多和一一对应
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
#主键（id）是自动添加的(也可以重写这个功能)
#模型变更的三个步骤
# 修改模型（在models.py文件中）
# 运行make migrations,为这些修改创建迁移文件
# 运行migrate,将这些修改更新到数据库中