from django.urls import path

from users.views import agent, customer
from .views import auth, admin

# auth

urlpatterns = [
    path("registration", auth.customerRegistration, name="register"),
    path("login", auth.userlogin, name="login"),
    path("home", auth.home, name="home"),
    path("logout", auth.logoutView, name="logout"),
]


admin
urlpatterns += [
    path("addagent", admin.addagent, name="addagent"),
    path("agentlist", admin.agentlist, name="agentlist"),
    path("deleteagent", admin.deleteagent, name="deleteagent"),
    path("loanlist", admin.loanlist, name="loanlist"),
    path("customerlist", admin.customerlist, name="customerlist"),
    path("agentloanlist/<int:id>", admin.agentloanlist, name="agentloanlist"),
    path("uploadfiles", admin.upload_files, name="uploadfiles"),
    path("getfiles", admin.get_files, name="getfile"),
]

# agent
urlpatterns += [
    path("requestloan/<int:pk>", agent.requestloan, name="requestloan"),
    path("agentloanlist", agent.agentloanlist, name="agentloanlist"),
]

# user
urlpatterns += [
    path("applyloan", customer.applyloan, name="applyloan"),
    path("customerloanlist", customer.customerloanlist, name="customerloanlist"),
    path("viewloan/<int:pk>", customer.loanview, name="individualloan"),
]
