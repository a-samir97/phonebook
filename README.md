# Description
Building a simple phonebook application using Python Django

- we have two entities ( `Contact`, `ContactNumber`)
- Each `Contact` has more than one `ContactNumber`
- Each `ContactNumber` has only one `Contact`

# Database schema 
![alt text](https://github.com/a-samir97/phonebook/blob/main/docs/db_schema.png)

# how to run the project 
- you need to run this command only `docker-compose up`


# API Endpoints 

- `/api/contants` GET
- `/api/contacts/<contact_id>` GET
- `/api/contants` POST
  - request body {"name": "test"}
- `/api/numbers/` POST
  - request body {"number": "+2012121212, "contact": contact_id}    


# Swagger Page
![alt text](https://github.com/a-samir97/phonebook/blob/main/docs/swagger.png)
