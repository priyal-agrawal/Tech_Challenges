# Prerequisite
We can create Virtual network in Azure cloud using 4 ways:

1: AzurePortal

2: Powershell

3: Azure CLI

4: ARM

In this challenge I will be creating Virtal natwork using Azure portal and Powershell to showcase my proficiency.#  Create virtual machines : Portal

# Create three VMs in the virtual network:

## Create the first VM

1. On the upper-left side of the portal, select Create a resource > Compute > Virtual machine.

2. In Create a virtual machine, type or select the values in the Basics tab:

* Project Details	

  Subscription	--> Select your Azure subscription
  
  Resource Group -->	Select myResourceGroup
  
* Instance details	

  Virtual machine name	--> Enter myVM1
  
  Region	--> Select (US) East US
  
  Availability Options -->	Select No infrastructure redundancy required
  
  Image	--> Select Windows Server 2019 Datacenter
  
  Azure Spot instance -->	Select No
  
  Size --> Choose VM size or take default setting
  
* Administrator account	

  Username --> Enter a username
  
  Password -->	Enter a password
  
  Confirm password	--> Reenter password
  
  Inbound port rules
  
  Public inbound ports -->	Select None.
  

3. Select the Networking tab, or select Next: Disks, then Next: Networking.

4. In the Networking tab, select or enter:


* Setting	Value

  Network interface	as :
  
    Virtual network	--> Select myVNet.
    
    Subnet	--> Select mySubnet
    
    Public IP	--> Select None
    
    NIC network security group	--> Select Basic
    
    Public inbound ports network	--> Select None.
    
    
5. Select the Review + create tab, or select the blue Review + create button at the bottom of the page.

6. Review the settings, and then select Create.

## Create the second VM
1. Similarly on the upper-left side of the portal, select Create a resource > Compute > Virtual machine.

2. In Create a virtual machine, type or select the values in the Basics tab:

* Project Details	

  Subscription -->	Select your Azure subscription
  
  Resource Group	--> Select myResourceGroup
  
* Instance details	

  Virtual machine name	--> Enter myVM2
  
  Region -->	Select (US) East US
  
  Availability Options -->	Select No infrastructure redundancy required
  
  Image -->	Select Windows Server 2019 Datacenter
  
  Azure Spot instance -->	Select No
  
  Size	--> Choose VM size or take default setting
  
* Administrator account
	
  Username -->	Enter a username
  
  Password	 --> Enter a password
  
  Confirm password -->	Reenter password
  
  Inbound port rules	
  
  Public inbound ports	Select None.
  
3. Select the Networking tab, or select Next: Disks, then Next: Networking.

4. In the Networking tab, select or enter:

* Network interface	

  Virtual network	--> Select myVNet.
  
  Subnet	--> Select mySubnet1
  
  Public IP -->	Select None
  
  NIC network security group -->	Select Basic
  
  Public inbound ports network	--> Select None.
  
5. Select the Review + create tab, or select the blue Review + create button at the bottom of the page.

6. Review the settings, and then select Create.

> Similarly, we will create third Virtual Machine in third subnet mySubnet2 .

# Create virtual machines : Powershell
Create VMs in the virtual network.

## Create the first VM

Create the first VM with New-AzVM. When you run the next command, you're prompted for credentials. Enter a user name and password for the VM:

```
$vm1 = @{
    ResourceGroupName = 'CreateVNetQS-rg'
    Location = 'EastUS'
    Name = 'myVM1'
    VirtualNetworkName = 'myVNet'
    SubnetName = 'mySubnet'
}
New-AzVM @vm1 -AsJob
```
The -AsJob option creates the VM in the background. You can continue to the next step.

When Azure starts creating the VM in the background, you'll get something like this back:

```
Id     Name            PSJobTypeName   State         HasMoreData     Location             Command
--     ----            -------------   -----         -----------     --------             -------
1      Long Running... AzureLongRun... Running       True            localhost            New-AzVM
```
## Create the second VM

Create the second VM with this command:
```
$vm2 = @{
    ResourceGroupName = 'CreateVNetQS-rg'
    Location = 'EastUS'
    Name = 'myVM2'
    VirtualNetworkName = 'myVNet'
    SubnetName = 'mySubnet1'
}
New-AzVM @vm2
```

> Note: You'll have to create another user and password. Azure takes a few minutes to create the VM. You'll have to create another user and password. Azure takes a few minutes to create the VM.
  > Azure provides an ephemeral IP for Azure Virtual Machines which aren't assigned a public IP address, or are in the backend pool of an internal Basic Azure Load Balancer. The ephemeral IP mechanism provides an outbound IP address that isn't configurable.T
  > he ephemeral IP is disabled when a public IP address is assigned to the virtual machine or the virtual machine is placed in the backend pool of a Standard Load Balancer with or without outbound rules. If a Azure Virtual Network NAT gateway resource is assigned to the subnet of the virtual machine, the ephemeral IP is disabled.
  > For more information on outbound connections in Azure, see Using Source Network Address Translation (SNAT) for outbound connections. 



