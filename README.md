WAS E-commerce Website 
AWS WAF web application firewall that helps protect web applications and APIs from attacks. 
Route 53 highly available and scalable Domain Name System (DNS) web service. 
Cognito Customers can add user sign-up and sign-in features and control access to your web and mobile applications. 
Application Load Balancer After you enable an Availability Zone, the load balancer starts routing requests to the registered targets in that Availability Zone. 
                   99.999% availability Multi regions (three regions)   
Frontend: Public Subnet  Fargate  to pick the instance types, manage the scheduling of the containers, and optimize cluster utilization. 
Amazon ElasticCache to cache static content and orchestrated backend API responses. 
EC2 table persists the user sessions and frontend application configurations 
Backend: Private Subnet 
Lambda, DynamoDB and S3 provide the ecommerce application data store, storing data products, customers, and customer transactions. 
Backup Centralize backup and recovery with a fully managed, policy-based service. 
API Gateway APIs act as the "front door" for applications to access data 
EvenBridge  to connect application components together, making it easier for you to build scalable event-driven applications.   
Elastic File System (Amazon EFS) to share common code and files such as properties and configurations, JavaScript, CSS, and JSON templates.  
SQS Send requests from backend to the payment and send message to the customers 
Payment Cryptography to secure data in payment processing in accordance with various PCI standards. 
Transit Gateway To connect between VPCs 

 

                                                                                                                                           
