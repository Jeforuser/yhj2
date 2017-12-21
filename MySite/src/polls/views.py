from django.shortcuts import render
# Create your views here.
#要调用视图，我们需要将其映射到URL-为此我们需要一个URLconf
# 每个视图都是由一个简单的Python函数(或者是基于类的视图的方法)表示的。
# Django通过检查请求的URL来选择使用哪个视图
from django.http import HttpResponse
from .models import Question
from django.template import loader
#from dwebsocket import require_websocket

#@require_websocket
def echo_once(request):
    message = request.websocket.wait()
    request.websocket.send(message)
#视图载入方法一
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     #context是一个由(变量名,python对象)组成的字典(译者注：变量名对应html模板中的名称)。
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
#视图载入方法二
from django.shortcuts import render
from .models import Question
def index(request):
#     from PIL import Image
#     import matplotlib.pyplot as plt
#     img=Image.open(r'C:/Hydrangeas.jpg')
#     plt.figure("dog")
#     plt.imshow(img)
#     #plt.show()
#     img.save(r'MySite/src/polls/static/polls/images/2.jpg')
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
#处理详细页面的视图
def NewFile(request):
    from PIL import Image
    import matplotlib.pyplot as plt
#     img=Image.open(r'C:/Hydrangeas.jpg')
#     plt.figure("dog")
#     plt.imshow(img)
#     #plt.show()
#     img.save(r'MySite/src/polls/static/polls/images/2.jpg')
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/NewFile.html', context)
from django.http import Http404
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Choice, Question
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        #request.POST 是一个类似字典的对象，让你可以通过关键字的名字获取提交的数据
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 重新显示该问题的表单
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 始终在成功处理 POST 数据后返回一个 HttpResponseRedirect ，
        # （合并上句） 这样可以防止用户点击“后退”按钮时数据被发送两次。
        # （合并至上一句）
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))