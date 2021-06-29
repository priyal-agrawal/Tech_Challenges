# Connect to myVM1 : Portal
1. Go to the Azure portal to manage your private VM. Search for and select Virtual machines.

2. Pick the name of your private virtual machine myVM1.

3. In the VM menu bar, select Connect, then select Bastion.

4. In the Connect page, select the blue Use Bastion button.
![picture alt](https://github.com/priyal-agrawal/Tech_Challenges/blob/67d0330d80c389acc76b69da5c077108d92594ce/Challenge%201/images/connect-to-virtual-machine.png)
5. In the Bastion page, enter the username and password you created for the virtual machine previously.

6. Select Connect

# Connect to a VM from the internet : PowerShell
To get the public IP address of the VM, use Get-AzPublicIpAddress.

This example returns the public IP address of the myVm1 VM:
```
$ip = @{
    Name = 'myVM1'
    ResourceGroupName = 'CreateVNetQS-rg'
}
Get-AzPublicIpAddress @ip | select IpAddress
```
Open a command prompt on your local computer. Run the mstsc command. Replace <publicIpAddress> with the public IP address returned from the last step:

``` 
  mstsc /v:<publicIpAddress>
  
```

1. If prompted, select Connect.

2. Enter the user name and password you specified when creating the VM.

3. Select OK.

4. You may receive a certificate warning. If you do, select Yes or Continue.


# Communicate between VMs
    
1. In the bastion connection of myVM1, open PowerShell.

2. Enter ping myvm2.

You'll receive a message similar to this output:
```
Pinging myvm2.cs4wv3rxdjgedggsfghkjrxuqf.bx.internal.cloudapp.net [10.1.0.5] with 32 bytes of data:
Reply from 10.1.0.5: bytes=32 time=3ms TTL=128
Reply from 10.1.0.5: bytes=32 time=1ms TTL=128
Reply from 10.1.0.5: bytes=32 time=1ms TTL=128
Reply from 10.1.0.5: bytes=32 time=1ms TTL=128

Ping statistics for 10.1.0.5:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 3ms, Average = 1ms
    
    
 ```
    
3. Close the bastion connection to myVM1.

4. Complete the steps in Connect to myVM1, but connect to myVM2.

5. Open PowerShell on myVM2, enter ping myvm1.

You'll receive something like this message:
```
Pinging myvm1.cs4wv3rxdjgedggsfghkjrxuqf.bx.internal.cloudapp.net [10.1.0.4] with 32 bytes of data:
Reply from 10.1.0.4: bytes=32 time=1ms TTL=128
Reply from 10.1.0.4: bytes=32 time=1ms TTL=128
Reply from 10.1.0.4: bytes=32 time=1ms TTL=128
Reply from 10.1.0.4: bytes=32 time=1ms TTL=128

Ping statistics for 10.1.0.4:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 1ms, Maximum = 1ms, Average = 1ms
    
```
6. Close the bastion connection to myVM2.
