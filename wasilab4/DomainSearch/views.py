import re
from django.shortcuts import render
from .models import Dns, DnsTlds
from UserDetails.models import UserPersonalInformation

# Create your views here.

def DomainSearchResultPage(request):
        if request.method == 'POST':
                DomainSearch = request.POST['DomainSearch']
                # DnsTldsName = DnsTlds.objects.values_list('DnsTldsName')
                # DnsTldsNameStr = str(DnsTldsName)
                # DnsTldsNameStr = str(['.com', '.org', '.wasi', '.lab'])
                if ' ' in DomainSearch:
                        return render(request, 'DomainSearch/ResultPage.html')
                else:
                        if re.search(r'\.com\b', DomainSearch) or re.search(r'\.lab\b', DomainSearch) :
                                if  UserPersonalInformation.objects.filter(DnsName = DomainSearch ):
                                        return render(request, 'DomainSearch/ResultPage.html', {'DomainNameAlreadyRegistered': DomainSearch })
                                else:
                                        return render(request, 'DomainSearch/ResultPage.html', {'DomainSearch': DomainSearch})
                        else:
                                return render(request, 'DomainSearch/ResultPage.html')
        
        else:
                return render(request, 'DomainSearch/ResultPage.html')
