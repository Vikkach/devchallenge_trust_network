# Online Round Task 
# Backend | DEV Challenge XIX

## Trust network

Trust network is a community of people who know each other and can assign each other a trust level.  We usually use trust networks in real life when donating money,  searching for healthcare professionals or expertise: we search between friends, friends of friends, etc.  

Let's model information flow in our computer.  The main entities are

Person, which has the next attributes:
Id.  
Set of expertise topics [strings]
Set of relations to other peoples:  pairs 
Id    -  contact id,
trustLevel  - number between 1 or 10

We can build a model of trust network using straightforward REST API:  

Description of input data

You should implements server with the next endpoints:

Request POST /api/people
	{
                "id": "Garry",
                “topics”: [“books”, “magic”, “movies”]
            }

Response 201
 	{
  	   “id”: “Garry”,
  	    “topics”: [“books”, “magic”, “movies”]
}

Also we can update or create trust connections:

Request POST /api/people/Garry/trust_connections
Hash pair with person_id - trust level
{
   “Ron”: 10,
   “Hermione”: 10,
}


Response 201

Request POST /api/people/Garry/trust_connections
{
     “Snape”: 4,
    “Voldemort”: 1
}

Response 201

Should  add  contacts 8 and 12 with trust level 1 and 5 accordingly

The main work is a sending messages (question, search for expertise, etc), which should have form:

Request POST  api/messages
Request:
{
	“text”: “Voldemort is alive!”,
            “topics”: [“magic”],
	“from_person_id”: “Garry”,
“min_trust_level”: 5
}

*all fields are required

Response should trace message delivery through the network based on people topics and trust connection levels. Each person should receive this message only one time and not be spammed.  All persons who receive a message must have appropriate topics.


Note, that message is send broadcasted to all 

Response 201
{
      "Garry": ["Hermione", “Rone”]
}


Bonus – implement delivery of non-broadcast message, where 

    Receiver should have topics listed in requests,
    Intermediate nodes can not have topics, listed in request

Request POST api/path
  Request: {
      "text": "need to find an expertise in magic",
      "topics":  ["books",",magic"],
      “from_person_id”: “Garry”,
      “min_trust_level”: 5
  }

Response 201

This message should  find an receiver, which have appropriate topics in attributes.  All participants in the path should be connected with a trust level of 5 or more.

As a result, we should receive back:
{
  from: "Garry"
  path: ["Hermione"]
}

     - the path from the message sender to the message receiver, including all intermediate agents.  When we have more than one variant, we should return a shorter variant.


## Instruction

From root path of project (trust_network)

```bash
docker-compose build
docker-compose up db
docker-compose up web
```
If you get an error

```bash
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) 
FATAL:  database "test_db" does not exist
```

```bash
docker ps
docker exec -it ##container_id## bash
psql -U postgres
```

1. Login, setting Server as localhost and Port as 5432 (usually they are defaults)
2. CREATE DATABASE test_db;
3. CREATE USER test_user WITH ENCRYPTED PASSWORD 'password';
4. GRANT ALL PRIVILEGES ON DATABASE test_db TO test_user;

And run
```bash
docker-compose up web
```