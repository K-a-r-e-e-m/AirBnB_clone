# AirBnB clone - The console project



This is the first step towards building our first full web application: the AirBnB clone. This first step is very important because we will use what we build during this project with all other following projects:

- [x] Command interpreter `cmd`
- [x] HTML/CSS templating
- [ ] database storage
- [ ] API
- [ ] front-end integration…



## Command Interpreter
- In this project we are tasked to write a command interpreter to manage our AirBnB objects.
 
***What is Command Interpreter?***

*Command interpreter or* `cmd` *is like a shell It's exactly the same but limited to a specific using, In this project we need a Command interpreter to able to manage the objects of our project like:* 


- [x] Create a new object (ex: a new User or a new Place)
- [x] Retrieve an object from a file, a database etc…
- [x] Do operations on objects (count, compute stats, etc…)
- [x] Update attributes of an object
- [x] Destroy an object

#### How to start it
To start the command interpreter, run the following command in your terminal:
```shell
python3 console.py
```

#### How to use it
Once the command interpreter is running, you can use the following commands:
```

create <class>: Creates a new instance of the specified class and saves it to the JSON file.

show <class> <id>: Retrieves the instance of the specified class with the given ID.

all <class>: Retrieves all instances of the specified class, or all instances if no class is specified.

update <class> <id> <attribute> <value>: Updates the attribute of the specified class instance with the given ID.

destroy <class> <id>: Deletes the instance of the specified class with the given ID.
```
#### Examples
Here are some examples of how to use the command interpreter:
```
(mycmd) create User
(mycmd) show User 1234-5678-9012
(mycmd) all User
(mycmd) update User 1234-5678-9012 name "John Doe"
(mycmd) destroy User 1234-5678-9012
(mycmd) quit
```

# Contributors 👨‍💻

**Kareem Hany**

- [Github](https://github.com/Kareem1715)
- [Linkedin](https://www.linkedin.com/in/kareem-hany-%F0%9F%87%B5%F0%9F%87%B8-352bb8230/)
