# Problem Statement

A 3-tier environment is a common setup. Use a tool of your choosing/familiarity create these resources. Please remember we will not be judged on the outcome but more focusing on the approach, style and reproducibility. 

# Proposed Approach

Three-tier architecture is a well-established software application architecture that organizes applications into three logical and physical computing tiers: 
* the presentation tier, or user interface; 
* the application tier, where data is processed;
* and the data tier, where the data associated with the application is stored and managed.

Here's a diagram that shows layers in a common N-tier architecture. Each layer handles one aspect of the application. The business layer manages communication between the user interface layer and the data access layer.
![picture alt]()

## What do we need

In simple term, 3 tier environment means frontend (presentation logic), backend (business logic), database (datastore)

I will be setting up resources of the 3 tier environment in Azure Cloud to showcase my proficiency in it.

I order to do so we will be doing the following steps :

1: Create single vnet

2: Create 3 subnets in that vnet
*Each 1 for webtier subnet,  app tier and for db tier 


4: Setup 3 nsg(network security group) to restrict the VM access

For the quickstart, we can refer the Azure Docs (https://docs.microsoft.com/en-us/azure/virtual-network/quick-create-portal)
This will be the basic setup. Based on the complexity of the project we need to have other considerations too .

## Other considerations

* You can add or remove VMs in each tier based on your scaling requirements. Because this scenario uses load balancers, you can add more VMs to a tier without affecting application uptime.

* We can use autoscaling in VM to add or remove VMs in each tier.As using autoscaling it will handle the  changes in load.

* All the virtual network traffic into the front-end application tier is protected by network security groups. Rules limit the flow of traffic so that only the front-end application tier VM instances can access the back-end database tier. No outbound internet traffic is allowed from the business tier or database tier. To reduce the attack footprint, no direct remote management ports are open. For more information, see Azure network security groups.


* Configuring disaster recovery for Azure VMs using Azure Site Recovery will incur the following charges on an ongoing basis.
  * Azure Site Recovery licensing cost per VM.
  * Network egress costs to replicate data changes from the source VM disks to another Azure region. Azure Site Recovery uses built-in compression to reduce the data transfer requirements by approximately 50%.
  * Storage costs on the recovery site. This is typically the same as the source region storage plus any additional storage needed to maintain the recovery points as snapshots for recovery.

* With the security isolation between subnets in place, you want to ensure that your publicly exposed front end is secure, and only allows access to what is needed. Only your presentation tier should be exposed to inbound internet traffic, and a web application firewall (WAF) technology in front of your presentation tier will enhance the security at this tier. WAFs inspect traffic for malicious activity, ensure communications are encrypted, and alert you if something is out of the ordinary. In Azure, Application Gateway is an HTTP load balancer that has a built-in WAF that you can enable.


## DevOps Consideration 

Since all the main resources and their dependencies are in the same virtual network, they are isolated in the same basic workload, that makes it easier to associate the workload's specific resources to a team, so that the team can independently manage all aspects of those resources. This isolation enables DevOps to perform continuous integration and continuous delivery (CI/CD).

## Benefits

With the application separated into tiers, each tier can be scaled, updated, or upgraded independently. If requests for our website increase, we can add more web servers to the load without impacting the other tiers. Similarly, if requests against our data tier increase, we can scale our database to have more capacity to handle the requests.

Network separation is a natural byproduct of this architecture. Because the application is separated into tiers, we should isolate each tier, and only allow necessary network access. The presentation tier can be exposed to the internet, the database can be fully secured behind multiple network tiers, and our application functions just the same. By securing network access between tiers, we reduce the attack surface of the application, and increase its security.
