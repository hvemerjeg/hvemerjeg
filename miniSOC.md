Hi, my name is Rafael. Welcome to my miniSOC documentation!

# 1. Installation

I decided to choose Splunk for my miniSOC environment. In my case I will be installing Splunk in Linux.
We go to the official page of Splunk, log in and download the version that fits our OS.


![[Pasted image 20230123102523.png]]

In my case I used downladed the .deb package. I used dpkg to install it.
![[Pasted image 20230123102955.png]]


# 2. Setting Splunk

We can choose to start or to enable splunk every time the system starts. I will choose to start it manually every time the system starts.
After the installation, the files were placed into /opt/splunk.
![[Pasted image 20230123103832.png]]

We will get some output and the port in which splunk is listening. So we can access it through visiting the localhost address in that port from the web browser. 

So visting the http://localhost:port form our web browser, we can see the splunk panel.

![[Pasted image 20230123104302.png]]

Log in with your credentials.

![[Screenshot from 2023-01-23 10-44-37.png]]

# 3. Forwarding the logs from my router to splunk

To forward the logs from the router to Splunk you need to enter into the admin panel of your router. It is important to note that some routers do not have that much logging functionalities, so maybe you are not able to forward the logs to Splunk. 

![[Pasted image 20230123111006.png]]

In my case, I was using a Zyxel router that had some logging functionalities. I set the syslog server address and the UDP port to send the logging. This address is were my Splunk software is installed. Now we need to configure Splunk to listen on that 9090 UDP port!

So in Splunk, we go to the **Add Data** option.

![[Pasted image 20230123111542.png]]

Then **Monitor**. And we choose **TCP/UDP**. Set the UDP port.

![[Pasted image 20230123111809.png]]

Then I set some options like the source type, Host, and App context.

![[Pasted image 20230123112232.png]]

After that we click review, we check everything is ok and then we are done! Let's see how the logging looks!

# 4. Searching

We click the option **Search & Reporting** at the home page, and we can start to perform some searches on the loggs that we have!

The first thing I did was to logg in into the router once again to see how the events look like

![[Screenshot from 2023-01-23 11-28-41.png]]

Nice! So, we will receive many events form the router. Now we can make searches and start to gain some hands on experience with Splunk!
The next step is going to be to add more logs from other sources to Splunk.