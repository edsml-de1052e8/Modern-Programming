# Lecture 5: Cloud computing 
## Part 1. Python Web Apps



What is the cloud:

Cloud computing is on-demnd availability of computer system resources, especially data storage and computing power without direct active management by the user. Lowers operating costs, increases efficiency.
(Wikipedia)

Other definition: Set of networks of computers accessed via internet.

Public cloud: srvices are bought as needed, infrastructure shared with other users and data is not shared. Providers include Micorosft Azure, Alibaba Cloud, Google Cloud Services.
Private Cloud: computers are bought and put off-site and run by you or the company using a network. If done private you have full control over the computers. Example the college HPC clusters are available to Imperial researchers from a data centre in Slough, West of London.

Hybrid Cloud: company that runs a private data centre, but also buys more public cloud services as needed. In theory, best of both world, but in practice it migh tmean duplication of efforts. Currently how ICT operates.

**Why use the Cloud:**
- Availability: online & supported 24/7 (by someone else lol)
- Scalability: spend more, get more
- Reach: Access across the world
- Agility: rapid development and deployment
- Disaster mitigation: natural backups
- Fault tolerance: fallback to alternative machines/locations. If one breaks you can easily switch to another computer in the data center.
- Elasticity: ract dynamically to demand.

**Why not use the Cloud?**
- Latency issues: want large data transfers local. Particularly a problem withe the hybrid cloud
- Costs: data transfer, machine hire
- Security: handing data to someone else eg. hospital data wouldn't be put on the cloud.
- Control: less personal oversight
- Intellectual property concerns: legal or contractual constraints


**Infrastructure, Platform and Software as a Service**

- As a service == available to rent eg. hiring a taxi
- Infrastructure as a service (IaaS): 
Most basic model: purchase time on entire computer, but you set up the entire system (software, apps,...)
Good point: max control of the environment and the operating system, few constraints.
Bad point: keep responsibilities on things such as updates, scaling, often higher costs than other models.

- Platform As A Service (PaaS): intermediate model
Provider sets up OS/environment, you set the actual code, example: departmental Jupyter

- Software As A Service (SaaS): least effort model
Provider supplies both the infrastructure, provider sets up application software, you just do the data eg. Google Outlook.
















