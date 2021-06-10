from django.http.response import JsonResponse
from django.views.decorators.http import require_GET
from loans.models import Loan
from users.decorators import authenticate_req


@authenticate_req(roles=["Agent"])
@require_GET
def agentloanlist(request, user):
    Loans = Loan.objects.filter(agent__user_id=user.user_id)
    context = {
        "rejected": list(Loans.filter(status="Rejected").values()),
        "approved": list(Loans.filter(status="Approved").values()),
        "awaited": list(Loans.filter(status="Awaited").values()),
        "new": list(Loan.filter(status="New").values()),
    }
    return JsonResponse(context, status=200)


@authenticate_req(roles=["Agent"])
@require_GET
def requestloan(request, user, pk):
    loan = Loan.objects.get(loan_id=pk)
    loan.status = "Awaited"
    loan.agent = user
    return JsonResponse(
        {"result": "success", "message": "applied for this loan by agent"}
    )
