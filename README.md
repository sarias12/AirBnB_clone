
# the AirBnB clone project!

This project is about AirBnB. The goal is creates a program that add information from console 
that creates, update, destroy and show all information about City, Amenity, Place, Review, State and Users, 
with several information each models as date of creating and update, name, numbers, password and email.

[![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20200629%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200629T143519Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=096ecda1fb64c5f320bed0f1ac524642fa38c8cf3ed2982a618f6061ddc7e8f4)]

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
(hbnb) command [name class] [arguments, key, value]
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
| **show** | Show an instance based on the class name and id. | 


### How to use
Console should work like this in interactive mode:
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