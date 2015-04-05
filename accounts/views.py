from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

# Create your views here.
@login_required
def user_profile(request):
  context = RequestContext(request, {'user': request.user})
  return render_to_response('accounts/user_profile.html', context_instance=context)
