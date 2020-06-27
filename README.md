
# the AirBnB clone project!

Description here!

![](Place for picture)

#### Clone Repository with HTTPS

Use Git or checkout with SVN using the web URL.
```
git clone https://github.com/LizethVictoria20/AirBnB_clone.git
```
#### Files and Directories
| Command  | Description |
| ------------- | ------------- |
| **models** | Directory that contain all classes used for the entire project. | 
| **tests** | Directory that contain all unit tests. | 
| **console.py** |This File is the entry point of our command interpreter. |
| **models/base_model.py** | This file is the base class of all our models. | 
| **models/engine** | Directory that contain all storage classes. | 
| **file_storage.py** | Prints all string representation of all instances based or not on the class name.|

#### Storage


#### The console


```
#cisfun$ command [-flag or -option] [arguments,  files or  directories]
```

| Command  | Description |
| ------------- | ------------- |
| **help or ?** | Shows the list of commands available. If the input includes a command name, the output is more verbose and restricted to details of that command, when available.  | 
| **Ctrl + D** | It's to exit the program (End of File).  | 
| **quit** |It's to exit the program |
| **create** |  Creates a new instance of class BaseModel | 
| **destroy** | Deletes an instance based on the class name and id. | 
| **all** | Prints all string representation of all instances based or not on the class name.| 
| **update** | Updates an instance based on the class name and id by adding or updating attribute. | 


### How to use
shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
all destroy EOF  create  help  show  quit update

(hbnb) 
(hbnb) 
(hbnb) quit
$


But also in non-interactive mode:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
all destroy EOF  create  help  show  quit update
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
all destroy EOF  create  help  show  quit update
(hbnb) 
$"
```

## Authors
Lizeth Victoria Franco [![alt text][1.1]][2]
Sergio Steben Arias Quintero [![alt text][1.1]][1]
<!-- links to social media icon -->
[1.1]: http://i.imgur.com/0o48UoR.png (Github)
<!-- links to your social media accounts -->
<!-- update these accordingly -->
[1]: https://github.com/sarias12
[2]: https://github.com/LizethVictoria20