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

Accessing Azure Cloud Services:
Getting access: Azure student subscription, allows institutions 100$ of free credit a year activation is through student email. Can also sign up to other services like Google Cloud Services

**Web protocols**

- TCP/IP: now we use far long numbers with 8 blocks of hexadecimals (0370:7334), enough IP addresses for now, might need to be expanded
IP addresses only attaches to computer connected to the internet.

- HTTP/HTML: makes computer talk to each other, mark up language. eg. https://user:password
This web address can be broken down into several sections. 
- Leftmost part defines the protocol being used: either htpp or https (https is more secure)
Other common protocols: ftp or ssh

- SSH: Web browser checks that server you're talking to matches the signatgure inside your root certificate, then generates own key and you link it to your server via this unique key. People can still know you are interacting with a server but not the info being transmitted.

- Authentication: not often used, password and username

- Server: usually as a human-readable name and version eg. www.imperial.ac.uk but can be changed to IP address by ooking up name/servers (or DNS domain name server).
Starts from the right.

- Port number: communication address on single machine, some services have defaults.

- Path (sometimes endpoint):
For a static HTTP server this often a real path to a file, up to server to interpret, character set is limited 
Word endpoint is used repeatedly with reference to APIs but not every time.

- Parameters: optional list of query parameters, the text beyond the ? consists of a set of parameters, encoded in a key=value format, which is again passed on to the server application to use when generating its output. eg. val1=123

- HTTP Requests: server receives request message like: GET /test?message HTTP/1.1 request body
Also IP address to respond to & some metadata eg. beheaders, info to identify you or your IP address. 

- HTTP Methods: there are many methods/verbs to give specific usage through http standard. eg. GET (give me the thing) or POST ("here is some data yu asked for") but also HEAD ("servers repsonds headers"). 
NB: all requests are requests so possibility of requets being denied!!


**API**

- In general, these work by providing a set of http-based URLs (i.e., web addresses) which respond to requests by returning relevant database information. In this example we connect to.

This is one common pattern in which the path in the HTTP request encodes the question we want to ask. Fuller documentation on this API is available at the TFL Swagger API page which lists the various valid paths you can follow and explains the information you get back. Another common pattern uses the path to specify the basic resource you are interested in and then query parameters to modify the response, e.g.

https:/api.github.com/users/jrper/repos?sort=created
Following https://api.tfl.gov.uk/Occupancy/BikePoints/BikePoints_187 generates the response

[{"$type":"Tfl.Api.Presentation.Entities.BikePointOccupancy, Tfl.Api.Presentation.Entities","id":"BikePoints_187","name":"Queen's Gate (South), South Kensington","bikesCount":3,"emptyDocks":21,"totalDocks":25}]

Other common choices, APIs also work in: XML, CSV all have relevant Python modules available to process from the standard library (json, xml, csv).

If in Python there is a key-value pair that is a dictionary in Python but an object in JSON. If in Python yoi have a dynamic array then it is a list [] but an array in JSON []. In general JSON data is data stored in a string and Python data is live.

```json.loads(my_data) # convert JSON to Python```

The Python system module urllib.request can be used to handle transmitting and receiving the requests, although non-system packages with more features are also available, and usually recommended when accessible (the most famous is probably the requests package.). The json, xml and csv modules can also be used to provide basic data processing on responses although, for large data sets, a package such as pandas may be more appropriate.



http codes are baically error codes

Flask - Python Web Apps: initially an April Fools' Joke, third party app so must be installed.

```from flask imort Flask```
``` app= Flask(__name__) ```
``` @app.route("/hello") ```

```def my_func():```
   ```return "<b.Hello,/b> World!"```


Grabs flask module, creates a web app using the flask class, requires a name. @app is a decorator around the function. Whenever someone connects to Flask app and calls hello the result is calling that function.
Need to call the app ```app.py```
Set running (in simple test server) with ```flask run```.

The decorator is part of Python syntax and allows to apply one function to another to get the resulting name. So takes 2nd function as input and returns new function which we've done extra work on. Wraps the entir function so as to print the arguments.

Variables in path names for Flask:
- def my_func (input_name) can be added in the return section: 
```@app.route("/name/<input_name>/age/<int:input_age>")
def my_func(input_name, input_age):
    return f"<b>Hello</b> {input_name}! Looking good for {input_age}!"```

client_name= request.args.get(...default=) is a dictionary so use same syntax as for dictionary eg. default=

Similarly, information passed in in query parameters can be used via a dictionary lookup

from flask import request
clients = ["Tom Cruise", "Halle Berry"]

@app.route("/client")
def my_func():
    client_name = request.args.get('name', default=None)
    if client_name in clients:
        return f"<b>Hello</b> {client_name}"
    else:
        return f"Are you in the right place"
Have a look in the examples in the lecture04 folder, after which, it's time to start trying the exercises.

NB: you can have multiple .py files but really try to have everything as module.










