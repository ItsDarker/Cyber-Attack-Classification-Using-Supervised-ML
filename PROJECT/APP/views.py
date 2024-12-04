from django.shortcuts import render, redirect
from . models import UserPersonalModel
from . forms import UserPersonalForm, UserRegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np
import joblib


def Landing_1(request):
    return render(request, '1_Landing.html')

def Register_2(request):
    form = UserRegisterForm()
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('Login_3')

    context = {'form':form}
    return render(request, '2_Register.html', context)


def Login_3(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home_4')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_Login.html', context)

def Home_4(request):
    return render(request, '4_Home.html')

def Teamates_5(request):
    return render(request,'5_Teamates.html')

def Domain_Result_6(request):
    return render(request,'6_Domain_Result.html')

def Problem_Statement_7(request):
    return render(request,'7_Problem_Statement.html')
    

def Per_Info_8(request):
    if request.method == 'POST':
        fieldss = ['firstname','lastname','age','address','phone','city','state','country']
        form = UserPersonalForm(request.POST)
        if form.is_valid():
            print('Saving data in Form')
            form.save()
        return render(request, '4_Home.html', {'form':form})
    else:
        print('Else working')
        form = UserPersonalForm(request.POST)    
        return render(request, '8_Per_Info.html', {'form':form})
    
Model1 = joblib.load(r'D:\CODE\DEPLOYMENT\PROJECT\APP\RFC.pkl')  
  
def Deploy_9(request): 
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        final_features = [np.array(int_features, dtype=object)]
        print(final_features)
        prediction = Model1.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(output)
        if output == 3:
            A = "THE MQTT_PUBLISH ATTACK MIGHT BE OCCUR IN THIS CONDITIONS."
            B = "PREVENTIONS : Firewalls: Use firewalls to control incoming and outgoing traffic based on predetermined security rules.Intrusion Detection Systems (IDS) and Intrusion Prevention Systems (IPS): Deploy IDS/IPS to monitor network traffic for suspicious activity and block potential threats."
            image_url =  "C:\\Users\\dhara\\Music\\MAIN_PROJECT\\CODE\\DEPLOYMENT\\PROJECT\\static\\images\\MQTT_PUBLISH.png"
        elif output == 10:
            A = "THE NONE OF ATTACK MIGHT BE OCCUR IN THIS CONDITIONS."
            B = "PREVENTIONS : NO NEED PREVENTIONS"
            image_url = "C:\\Users\\dhara\\Music\\MAIN_PROJECT\\CODE\\DEPLOYMENT\\PROJECT\\static\\images\\DOS_SYN_HPING.jpg"
        elif output == 11:
            A = "THE WIBPRO PULP ATTACK MIGHT BE OCCUR IN THIS CONDITIONS."
            B = "PREVENTIONS : Patch Management: Regularly update and patch software, operating systems, and network devices to address known vulnerabilities.Network Segmentation: Divide the network into smaller segments to limit the impact of a potential breach and control access to sensitive resources."
            image_url ="C:\\Users\\dhara\\Music\\MAIN_PROJECT\\CODE\\DEPLOYMENT\\PROJECT\\static\\images\\DOS_SYN_HPING.jpg"
        elif output == 0:
            A = "THE ARP_POISIONING ATTACK MIGHT BE OCCUR IN THIS CONDITIONS."
            B = "PREVENTIONS : Strong Authentication: Enforce strong authentication mechanisms such as multi-factor authentication (MFA) to prevent unauthorized access.Encryption: Use encryption protocols (e.g., SSL/TLS) to secure data in transit and ensure confidentiality."
            image_url = "C:\\Users\\dhara\\Music\\MAIN_PROJECT\\CODE\\DEPLOYMENT\\PROJECT\\static\\images\\DOS_SYN_HPING.jpg"
        elif output == 1:
            A = "THE DDOS_SLOWLORIS ATTACK MIGHT BE OCCUR IN THIS CONDITIONS."
            B = "PREVENTIONS : Access Control Lists (ACLs): Implement ACLs to restrict access to network resources based on user roles and permissions.Least Privilege Principle: Grant users the minimum level of access required to perform their tasks to reduce the risk of privilege escalation."
            image_url = "C:\\Users\\dhara\\Music\\MAIN_PROJECT\\CODE\\DEPLOYMENT\\PROJECT\\static\\images\\DOS_SYN_HPING.jpg"
        elif output == 2:
            A = "THE DOS_SYN_HPING ATTACK MIGHT BE OCCUR IN THIS CONDITIONS."
            B = "PREVENTIONS : Network Monitoring: Continuously monitor network traffic and logs to detect anomalies and potential security breaches.User Awareness Training: Educate users about security best practices, such as avoiding phishing emails and practicing good password hygiene."
            image_url = "https://www.indusface.com/wp-content/uploads/2021/03/syn6.png"
            prevention_img ="https://www.opensourceforu.com/wp-content/uploads/2011/11/SYN-prevention-practice.jpg"
        elif output == 4:
            A =  "THE METASPLOIT_BRUTE_FORCE_SSH ATTACK MIGHT BE OCCUR IN THIS CONDITIONS."
            B = "PREVENTIONS : Regular Security Audits and Assessments: Conduct periodic security audits and assessments to identify vulnerabilities and weaknesses in the network infrastructure.Denial-of-Service (DoS) Protection: Implement DoS protection mechanisms to mitigate the impact of DoS attacks and ensure service availability."
            image_url = "C:\\Users\\dhara\\Music\\MAIN_PROJECT\\CODE\\DEPLOYMENT\\PROJECT\\static\\images\\DOS_SYN_HPING.jpg"
        elif output == 5:
            A = "THE NMAP_FIN_SCAN ATTACK MIGHT BE OCCUR IN THIS CONDITIONS."
            B = "PREVENTIONS : Network Access Control (NAC): Use NAC solutions to enforce security policies and ensure that only authorized devices can connect to the network.Endpoint Security: Deploy endpoint protection tools, such as antivirus software and host-based firewalls, to secure individual devices."
            image_url = "C:\\Users\\dhara\\Music\\MAIN_PROJECT\\CODE\\DEPLOYMENT\\PROJECT\\static\\images\\DOS_SYN_HPING.jpg"
        elif output == 6:
            A = "THE NMAP_OS_DETECTION ATTACK MIGHT BE OCCUR IN THIS CONDITIONS."
            B = "PREVENTIONS : Secure Configuration Management: Follow secure configuration guidelines for network devices, servers, and other infrastructure components.Vulnerability Management: Use vulnerability scanning tools to identify and remediate vulnerabilities in the network environment."
            image_url = "C:\\Users\\dhara\\Music\\MAIN_PROJECT\\CODE\\DEPLOYMENT\\PROJECT\\static\\images\\DOS_SYN_HPING.jpg"
        elif output == 7:
            A =  "THE NMAP_TCP_SCAN ATTACK MIGHT BE OCCUR IN THIS CONDITIONS."
            B = "PREVENTIONS : ncident Response Plan: Develop and regularly update an incident response plan to effectively respond to security incidents and minimize their impact.Data Backup and Recovery: Implement regular data backups and establish robust recovery procedures to restore operations in the event of a security breach or data loss."
            image_url ="C:\\Users\\dhara\\Music\\MAIN_PROJECT\\CODE\\DEPLOYMENT\\PROJECT\\static\\images\\DOS_SYN_HPING.jpg"
        elif output == 8:
            A =  "THE NMAP_UDP_SCAN ATTACK MIGHT BE OCCUR IN THIS CONDITIONS."
            B = "PREVENTIONS : Network Traffic Analysis: Use network traffic analysis tools to detect and investigate suspicious behavior and potential security threats.Third-Party Risk Management: Assess the security posture of third-party vendors and service providers to ensure they meet your organization's security standards."
            image_url = "C:\\Users\\dhara\\Music\\MAIN_PROJECT\\CODE\\DEPLOYMENT\\PROJECT\\static\\images\\DOS_SYN_HPING.jpg"
        elif output == 9:
            A =  "THE NMAP_XMAS_TREE_SCAN ATTACK MIGHT BE OCCUR IN THIS CONDITIONS."
            B = "PREVENTIONS : Regular Security Audits and Assessments: Conduct periodic security audits and assessments to identify vulnerabilities and weaknesses in the network infrastructure.Endpoint Security: Deploy endpoint protection tools, such as antivirus software and host-based firewalls, to secure individual devices."
            image_url = "C:\\Users\\dhara\\Music\\MAIN_PROJECT\\CODE\\DEPLOYMENT\\PROJECT\\static\\images\\DOS_SYN_HPING.jpg"
        return render(request, '9_Deploy.html', {
            "prediction_text": A, 
            "B": B, 
            "image_url": image_url, 
            "prevention_img": prevention_img,
            "show_result": True
        })

    else:
        return render(request, '9_Deploy.html', {"show_result": False})
    #     return render(request, '9_Deploy.html', {"prediction_text": A, "B":B, "image_url": image_url, "prevention_img": prevention_img })

    # else:
    #     return render(request, '9_Deploy.html')
    
def Per_Database_10(request):
    models = UserPersonalModel.objects.all()
    return render(request, '10_Per_Database.html', {'models':models})

def Logout(request):
    logout(request)
    return redirect('Landing_1')
