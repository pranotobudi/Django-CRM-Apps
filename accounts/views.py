from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect 
from django.urls import reverse
from .forms import AccountForm
from contacts.models import Contact
from communications.models import Communication


from .models import Account

class AccountList(ListView):
    model = Account
    paginate_by = 12
    template_name = 'accounts/account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        try:
            a = self.request.GET.get('account',)
        except KeyError:
            a = None
        if a:
            account_list = Account.objects.filter(
                name__icontains=a,
                owner=self.request.user
            )
        else:
            account_list = Account.objects.filter(owner=self.request.user)
        return account_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AccountList, self).dispatch(*args, **kwargs)

@login_required
def account_detail(request, uuid):

    account = Account.objects.get(uuid=uuid)
    if account.owner != request.user:
            return HttpResponseForbidden()
    #print (f"BISMILLAH======{account.uuid} {account.city} {account.address_one}=================BISMILLAH")
    contacts = Contact.objects.filter(account=account)
    communications = Communication.objects.filter(
        account=account).order_by('-created_on')

    variables = {
        'account': account,
        'contacts': contacts,
        'communications': communications,

    }
    return render(request, 'accounts/account_detail.html', variables)

@login_required
def account_cru(request, uuid=None):

    if uuid:
        account = get_object_or_404(Account, uuid=uuid)
        if account.owner != request.user:
            return HttpResponseForbidden()
    else:
        account = Account(owner=request.user)

    if request.POST:
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            redirect_url = reverse(
                'account_detail',
                args=(account.uuid,)
            )
            return HttpResponseRedirect(redirect_url)
    else:
        form = AccountForm(instance=account)

    variables = {
        'form': form,
        'account':account
    }

    if request.is_ajax():
        template = 'accounts/account_item_form.html'
    else:
        template = 'accounts/account_cru.html'

    return render(request, template, variables)
