# Prerequisite
We can create Virtual network in Azure cloud using 4 ways:
1: AzurePortal
2: Powershell
3: Azure CLI
4: ARM

In this challenge I will be creating Virtal natwork using Azure portal and Powershell to showcase my proficiency.

## Creating Virtal Network and subnet : Portal
### Prerequisites
An Azure account with an active subscription.
### Sign in to Azure
Sign in to the Azure portal.

### Create a virtual network
1: Select Create a resource in the upper left-hand corner of the portal.

2: In the search box, enter Virtual Network. Select Virtual Network in the search results.

3: In the Virtual Network page, select Create.

4: In Create virtual network, enter or select this information in the Basics tab:
* Project details as : 

    Subscription --> Select your subscription.

    Resource group -->	Select Create new.

    Enter --> myResourceGroup.

    Select --> OK.

* Instance details	as:

    Name -->	Enter myVNet.

    Region--> Select (US) East US.


Thus, Create virtual network Azure portal

5: Select the IP Addresses tab, or select the Next: IP Addresses button at the bottom of the page.

6: In IPv4 address space, select the existing address space and change it to 10.1.0.0/16.

7: Select + Add subnet, then enter MySubnet for Subnet name and 10.1.0.0/24 for Subnet address range.

8: Select Add.

9: Select the Security tab, or select the Next: Security button at the bottom of the page.

10: Under BastionHost, select Enable. Enter this information:

* Setting	Value as: 
    Bastion name	--> Enter myBastionHost

    AzureBastionSubnet address space--> 	Enter 10.1.1.0/24

    Public IP Address	--> Select Create new.

    For Name, enter myBastionIP.

Select OK.

Select the Review + create tab or select the Review + create button.

11 : Select Create

Similarly, create 2 more subnets as mySubnet1 and mySubnet2 by +Add Subnet as in mentioned in step 7.

## Creating Virtal Network and subnet : Powershell
### Prerequisite
An Azure account with an active subscription. Create an account for free.
Azure PowerShell installed locally or Azure Cloud Shell
If you choose to install and use PowerShell locally, this article requires the Azure PowerShell module version 5.4.1 or later. Run Get-Module -ListAvailable Az to find the installed version. If you need to upgrade, see Install Azure PowerShell module. If you're running PowerShell locally, you also need to run Connect-AzAccount to create a connection with Azure.

### Create the resource group
Before you can create a virtual network, you have to create a resource group to host the virtual network. Create a resource group with New-AzResourceGroup. This example creates a resource group named CreateVNetQS-rg in the Eastus location:

```
$rg = @{

    Name = 'CreateVNetQS-rg'
    
    Location = 'EastUS'
    
}

New-AzResourceGroup @rg 
```

### Create the virtual network

Create a virtual network with New-AzVirtualNetwork. This example creates a default virtual network named myVNet in the EastUS location:

```
$vnet = @{
    Name = 'myVNet'
    ResourceGroupName = 'CreateVNetQS-rg'
    Location = 'EastUS'
    AddressPrefix = '10.0.0.0/16'    
}
$virtualNetwork = New-AzVirtualNetwork @vnet
```

### Add a subnet
Azure deploys resources to a subnet within a virtual network, so you need to create a subnet. Create a subnet configuration named default with Add-AzVirtualNetworkSubnetConfig:

```
$subnet = @{
    Name = 'MySubnet'
    VirtualNetwork = $virtualNetwork
    AddressPrefix = '10.0.0.0/24'
}
$subnetConfig = Add-AzVirtualNetworkSubnetConfig @subnet
```

#### Associate the subnet to the virtual network
You can write the subnet configuration to the virtual network with Set-AzVirtualNetwork. This command creates the subnet:

```
$virtualNetwork | Set-AzVirtualNetwork
```
Similarly, create 2 more subnets as mySubnet1 and mySubnet2 as mentioned in above step
