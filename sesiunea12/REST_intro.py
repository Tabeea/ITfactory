'''
REST - REpresentation State Transfer --> is an arhitectural style for providing standards between computer systems or the web
making it easier for systems to communicate with each other
REST - Compliant systems, also called RESTful systems are caracterized by how they are stateles s and separate the concerns of client and
server
For an API to be considered RESTful it must have the following contains:
    - client-server arhitecture
    - statelessness: the server does not store any client context between context, so each request contains all the
    information needed to complete it
    - cache ability: clients can cache response data, reducing the number of requests to the server and improving performance
    cashe = zona mica de memorie care stocheaza pentru o perioada foarte scurta date
    - use if http methods: GET, POST, PUT, DELETE
    - use of http status code: success(200), failure(400), not found(404)
'''
