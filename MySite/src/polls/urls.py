from django.conf.urls import url

from . import views
#  Django区分不同APP的URL的名字
# 添加命名空间到你的URLconf。 
# 在polls/urls.py文件中，继续添加app_name来设置应用程序命名空间：
app_name='polls'#app的名称一致
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^echo_once$', views.echo_once, name='echo_once'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^NewFile/$', views.NewFile, name='NewFile'),
]
#url()传递的四个参数
# regex:正则表达式，匹配url，必须有
# view:请求访问的视图，必须有
# name:命名你的URL可让你从Django其他地方明确地引用它，特别是在模板中,可有可无