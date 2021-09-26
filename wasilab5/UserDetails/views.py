from django.shortcuts import render
import stripe
from .models import UserPersonalInformation, DnsInformation, IcannModel
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def UploadData(request):
        if request.method == "POST":
                FirstName = request.POST['FirstName']
                LastName = request.POST['LastName']
                CompanyName = request.POST['CompanyName']
                JobTitle = request.POST['JobTitle']
                Address = request.POST['Address']
                City = request.POST['City']
                State = request.POST['State']
                Country = request.POST['Country']
                PhoneNumber = request.POST['PhoneNumber']
                Email = request.POST['Email']

                UserName = request.POST['UserName']
                DnsName = request.POST['DnsName']

                SavedUserData = UserPersonalInformation(UserName= UserName, DnsName=DnsName, FirstName= FirstName, LastName = LastName, CompanyName= CompanyName, JobTitle= JobTitle, Address = Address, 
                                        City= City, State = State, Country= Country, PhoneNumber = PhoneNumber, Email=Email)
                SavedUserData.save()
                return render(request, 'UserDetails/DataSecurity.html', {'DnsName': DnsName})
        else:
                return render(request, 'UserDetails/DataSecurity.html')

@login_required
def UploadDataView(request):
        DomainSearch = request.POST['DomainSearch']
        return render(request, 'UserDetails/UploadData.html', {'DomainSearch': DomainSearch})


@login_required
def UploadDnsInformation(request):
        NameServer1 = request.POST['NameServer1']
        NameServer2 = request.POST['NameServer2']
        DnsName = request.POST['DnsName']
        UserName = request.POST['UserName']

        DomainAutoRenew = request.POST['DomainAutoRenew']
        DnsStatus = request.POST['status']
        DomainSsl = request.POST['DomainSsl']
        DomainPremium = request.POST['DomainPremium']
        DomainYear = request.POST['DomainYear']

        SavedDnsInformation = DnsInformation(DomainYear = DomainYear, DomainAutoRenew=DomainAutoRenew, DomainSsl=DomainSsl, DomainPremium=DomainPremium , DnsStatus = DnsStatus, NameServer1 = NameServer1, NameServer2=NameServer2, DnsName= DnsName, UserName= UserName)
        SavedDnsInformation.save()

        return render(request, 'UserDetails/DnsBuy.html', {'DnsName': DnsName})


@login_required
def DnsIcann(request):
        DnsName = request.POST['DnsName']
        
        return render(request, 'UserDetails/DnsIcann.html' , {'DnsName': DnsName})


@login_required
def DnsCongratulations(request, args):
        DnsName = args

        obj1 = UserPersonalInformation.objects.get(DnsName = DnsName)
        obj2 = DnsInformation.objects.get(DnsName=DnsName)
        CName= obj1.CompanyName

        DnsName = obj1.DnsName
        UserName = obj1.UserName
        FirstName = obj1.FirstName
        LastName = obj1.LastName
        CompanyName = obj1.CompanyName
        JobTitle = obj1.JobTitle
        Address = obj1.Address
        City = obj1.City
        State = obj1.State
        Country = obj1.Country
        PhoneNumber = obj1.PhoneNumber
        Email = obj1.Email

        DomainYear = obj2.DomainYear
        DomainAutoRenew = obj2.DomainAutoRenew
        DnsStatus = obj2.DnsStatus
        DomainSsl = obj2.DomainSsl
        DomainPremium = obj2.DomainPremium
        NameServer1 = obj2.NameServer1
        NameServer2 = obj2.NameServer2


        SavedIcann= IcannModel(DomainYear=DomainYear , DnsName=DnsName, UserName=UserName, FirstName=FirstName, LastName=LastName, CompanyName=CompanyName,
                                        JobTitle=JobTitle, Address=Address, City=City, State=State, Country=Country, PhoneNumber=PhoneNumber, Email=Email,
                                         DomainAutoRenew= DomainAutoRenew, DnsStatus=DnsStatus, DomainSsl=DomainSsl, DomainPremium= DomainPremium , NameServer1=NameServer1, NameServer2=NameServer2)
        SavedIcann.save()

        return render(request, 'UserDetails/DnsCongratulations.html', {'DnsName': DnsName, 'CName': CName})
