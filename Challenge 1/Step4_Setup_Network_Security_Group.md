# Filter network traffic with a network security group using the Azure portal

You can use a network security group to filter network traffic inbound and outbound from a virtual network subnet. In 3 tier environment will use NSG on each subnet to secure the frontend,backend and database VMs as per required rules.

Network security groups contain security rules that filter network traffic by IP address, port, and protocol. Security rules are applied to resources deployed in a subnet.

## Prerequisites

An Azure subscription.

## Sign in to Azure

Sign in to the Azure portal at https://portal.azure.com

## Create application security groups

An application security group enables you to group together servers with similar functions, such as web servers.

1. Select Create a resource in the upper left-hand corner of the portal.

2. In the search box, enter Application security group. Select Application security group in the search results.

3. In the Application security group page, select Create.

4. In Create an application security group, enter or select this information in the Basics tab:

* Setting	Values as: 

  Project details	
  
    Subscription -->	Select your subscription.
    
    Resource group -->	Select myResourceGroup.
    
  Instance details	
  
    Name -->	Enter myAsgWebServers.
    
    Region -->	Select (US) East US.
    
5. Select the Review + create tab, or select the blue Review + create button at the bottom of the page.

6. Select Create.

7. Repeat step 4 again, specifying the following values:


* Setting	Values as :

  Project details	
  
    Subscription	--> Select your subscription.
    
    Resource group -->	Select myResourceGroup.
    
  Instance details
  
    Name -->	Enter myAsgMgmtServers.
    
    Region	--> Select (US) East US.
    
8. Select the Review + create tab, or select the blue Review + create button at the bottom of the page.

9. Select Create.

## Create a network security group
A network security group secures network traffic in your virtual network.

1. Select Create a resource in the upper left-hand corner of the portal.

2. In the search box, enter Network security group. Select Network security group in the search results.

3. In the Network security group page, select Create.

4. In Create network security group, enter or select this information in the Basics tab:


* Setting	Values as : 

  Project details	
  
    Subscription	--> Select your subscription.
    
    Resource group	--> Select myResourceGroup.
    
  Instance details	
  
    Name	--> Enter myNSG.
    
    Location	--> Select (US) East US.
    
5. Select the Review + create tab, or select the blue Review + create button at the bottom of the page.

6. Select Create.

## Associate network security group to subnet
In this section, we'll associate the network security group with the subnet of the virtual network we created earlier.

1. In the Search resources, services, and docs box at the top of the portal, begin typing myNsg. When myNsg appears in the search results, select it.

2. In the overview page of myNSG, select Subnets in Settings.

3. In the Settings page, select Associate:
![picture alt](https://github.com/priyal-agrawal/Tech_Challenges/blob/3e15941288df5c5e00e1790f9283a64938c80365/Challenge%201/images/associate-nsg-subnet.png)
4. Associate NSG to subnet.

5. Under Associate subnet, select Virtual network and then select myVNet.

6. Select Subnet, select default, and then select OK.

## Create security rules
1. In Settings of myNSG, select Inbound security rules.

2. In Inbound security rules, select + Add:
![picture alt] (https://github.com/priyal-agrawal/Tech_Challenges/blob/3e15941288df5c5e00e1790f9283a64938c80365/Challenge%201/images/add-inbound-rule.png)

3. Create a security rule that allows ports 80 and 443 to the myAsgWebServers application security group. In Add inbound security rule, enter or select the following information:

Source -->	Leave the default of Any.

Source port ranges -->	Leave the default of (*)

Destination	--> Select Application security group.

Destination application security group -->	Select myAsgWebServers.

Service -->	Leave the default of Custom.

Destination port ranges	--> Enter 80,443.

Protocol	--> Select TCP.

Action	--> Leave the default of Allow.

Priority	--> Leave the default of 100.

Name	--> Enter Allow-Web-All.


![picture alt](https://github.com/priyal-agrawal/Tech_Challenges/blob/3e15941288df5c5e00e1790f9283a64938c80365/Challenge%201/images/inbound-security-rule.png)
4. Complete step 2 again, using the following values:


Source	--> Leave the default of Any.

Source port ranges	--> Leave the default of (*)

Destination -->	Select Application security group.

Destination application security group	--> Select myAsgMgmtServers.

Service -->	Leave the default of Custom.

Destination port ranges -->	Enter 3389.

Protocol -->	Select TCP.

Action	--> Leave the default of Allow.

Priority	--> Leave the default of 110.

Name	--> Enter Allow-RDP-All.


Once you've completed steps 1-3, review the rules you created. Your list should look like the list in the following example:

![picture alt](https://github.com/priyal-agrawal/Tech_Challenges/blob/3e15941288df5c5e00e1790f9283a64938c80365/Challenge%201/images/inbound-security-rule.png)

# Associate network interfaces to an ASG
When the portal created the VMs, it created a network interface for each VM, and attached the network interface to the VM.

Add the network interface for each VM to one of the application security groups you created previously:

1. In the Search resources, services, and docs box at the top of the portal, begin typing myVMWeb. When the myVMWeb virtual machine appears in the search results, select it.

2. In Settings, select Networking.

3. Select the Application security groups tab, then select Configure the application security groups.

![picture alt](https://github.com/priyal-agrawal/Tech_Challenges/blob/3e15941288df5c5e00e1790f9283a64938c80365/Challenge%201/images/configure-app-sec-groups.png)


4. In Configure the application security groups, select myAsgWebServers. Select Save.

![picture alt](https://github.com/priyal-agrawal/Tech_Challenges/blob/3e15941288df5c5e00e1790f9283a64938c80365/Challenge%201/images/select-asgs.png)

5. Select application security groups.

6. Complete steps 1 and 2 again, searching for the myVMMgmt virtual machine and selecting the myAsgMgmtServers ASG.

# Test traffic filters
1. Connect to the myVMMgmt VM. Enter myVMMgmt in the search box at the top of the portal. When myVMMgmt appears in the search results, select it. Select the Connect button.

2. Select Download RDP file.

3. Open the downloaded rdp file and select Connect. Enter the user name and password you specified when creating the VM.

4. Select OK.

5. You may receive a certificate warning during the connection process. If you receive the warning, select Yes or Continue, to continue with the connection.

The connection succeeds, because port 3389 is allowed inbound from the internet to the myAsgMgmtServers application security group.

The network interface for myVMMgmt is associated with the myAsgMgmtServers application security group and allows the connection.

6. Open a PowerShell session on myVMMgmt. Connect to myVMWeb using the following example:

```
mstsc /v:myVmWeb
```

The RDP connection from myVMMgmt to myVMWeb succeeds because virtual machines in the same network can communicate with each over any port by default.

You can't create an RDP connection to the myVMWeb virtual machine from the internet. The security rule for the myAsgWebServers prevents connections to port 3389 inbound from the internet. Inbound traffic from the Internet is denied to all resources by default.

7. To install Microsoft IIS on the myVMWeb virtual machine, enter the following command from a PowerShell session on the myVMWeb virtual machine:
```
Install-WindowsFeature -name Web-Server -IncludeManagementTools
```
8. After the IIS installation is complete, disconnect from the myVMWeb virtual machine, which leaves you in the myVMMgmt virtual machine remote desktop connection.

9. Disconnect from the myVMMgmt VM.

10. In the Search resources, services, and docs box at the top of the Azure portal, begin typing myVMWeb from your computer. When myVMWeb appears in the search results, select it. Note the Public IP address for your VM. The address shown in the following example is 23.96.39.113, but your address is different:

![picture alt](https://github.com/priyal-agrawal/Tech_Challenges/blob/3e15941288df5c5e00e1790f9283a64938c80365/Challenge%201/images/public-ip-address.png)

11. To confirm that you can access the myVMWeb web server from the internet, open an internet browser on your computer and browse to http://<public-ip-address-from-previous-step>.

You see the IIS welcome screen, because port 80 is allowed inbound from the internet to the myAsgWebServers application security group.

The network interface attached for myVMWeb is associated with the myAsgWebServers application security group and allows the connection.

> Similarly,Associate the above security settings for two subnets and VMs.
  
> We can also route the network traffic by creating route tableand associate it to VMs.
  
