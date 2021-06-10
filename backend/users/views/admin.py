from django.http.response import JsonResponse
from django.views.decorators.http import require_GET
from loans.models import Loan
from users.decorators import authenticate_req
from users.models import User


@authenticate_req(roles=["Admin"])
def addagent(request, user):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        agent = User(name=name, email=email)
        agent.set_password(password)
        agent.save_agent()
    return JsonResponse(status=200)


@authenticate_req(roles=["Admin"])
@require_GET
def agentlist(request, user):
    context = {"agents": list(User.objects.filter(role="Agent").values())}
    return JsonResponse(context, status=200)


@authenticate_req(roles=["Admin"])
def deleteagent(request, user):
    if request.method == "POST":
        id = request.POST.get("agent_id")
        User.objects.filter(user_id=id).delete()
        return JsonResponse(
            {"result": "success", "message": "deleted Successfully"}, status=200
        )


@authenticate_req(roles=["Admin"])
def loanlist(request, user):
    context = {
        "rejected": list(Loan.filter(status="Rejected").values()),
        "approved": list(Loan.filter(status="Approved").values()),
        "awaited": list(Loan.filter(status="Awaited").values()),
        "new": list(Loan.filter(status="New").values()),
    }
    return JsonResponse(context, status=200)


@authenticate_req(roles=["Admin"])
def customerlist(request, user):
    context = {"agents": list(User.objects.filter(role="Customer").values())}
    return JsonResponse(context, status=200)


@authenticate_req(roles=["Admin"])
def agentloanlist(request, user, pk):
    Loans = Loan.objects.filter(agent__user_id=pk)
    context = {
        "rejected": list(Loans.filter(status="Rejected").values()),
        "approved": list(Loans.filter(status="Approved").values()),
        "awaited": list(Loans.filter(status="Awaited").values()),
    }
    return JsonResponse(context, status=200)
