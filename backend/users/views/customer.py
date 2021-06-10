from django.http.response import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET
from loans.models import Loan, ProductMapping
from users.decorators import authenticate_req
from users.models import User


@authenticate_req(roles=["Customer"])
def applyloan(request, user):
    if request.method == "GET":
        products = ProductMapping.objects.all()
        return render(request, "customer/applyloan.html", {"product": products})
    if request.method == "POST":
        amount = request.POST.get("amount")
        product_id = request.POST.get("product_id")
        tenure = request.POST.get("product_id")
        product = ProductMapping.get_product_from_id(product_id)
        loan_object = Loan(amount=amount, tenure=tenure, product=product, user=user)
        loan_object.save()
        return redirect("customerloanlist")


@authenticate_req(roles=["Customer"])
def customerloanlist(request, user):
    if request.method == "GET":
        Loans = Loan.objects.filter(user__user_id=user.user_id)
        context = {
            "rejected": list(Loans.filter(status="Rejected").values()),
            "approved": list(Loans.filter(status="Approved").values()),
            "new": list(Loans.filter(status="New").values()),
        }
        return render(request, "customer/customerloanlist.html", context=context)


@authenticate_req()
@require_GET
def loanview(request, user, pk):
    loan = Loan.objects.get(loan_id=pk)
    if loan.user.user_id != user.user_id:
        return HttpResponseForbidden()
    return render(request, "customer/loan.html", {"loan": loan})
