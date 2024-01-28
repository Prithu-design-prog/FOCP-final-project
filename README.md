
# FOCP-final-project
**#task 1**

This task is about creating a program that can calculate the price of a pizza order from Beckett Pizza Plaza (BPP). The program should ask the user for the number of pizzas, the delivery option, and the app usage. The program should also check if it is Tuesday, as there are different discounts on that day. The program should then apply the appropriate discounts and display the total price in pounds.
This code is a program that calculates the total price of a pizza order based on the following factors:

The number of pizzas ordered, which is obtained from the user by calling the get_input function, which validates that the input is a positive integer.
The day of the week, which is obtained from the user by calling the get_yes_no_input function, which accepts only “y” or “n” as answers. If it is Tuesday, the base price of a pizza is reduced by 50%.
The delivery option, which is also obtained from the user by calling the get_yes_no_input function. If delivery is required, there is an additional charge of 2.5 units, unless the order size is 5 pizzas or more, in which case delivery is free.
The app usage, which is also obtained from the user by calling the get_yes_no_input function. If the customer used the app, there is a discount of 0.75 units applied to the total price.
The code prints a welcome message at the beginning and then prompts the user for the necessary inputs. It then calculates the total price by multiplying the number of pizzas by the base price, adding the delivery cost, and subtracting the app discount. It then prints the total price to the user.

**#task 2 **

This code is a solution to a programming assignment that involves analysing the usage of a cat shelter that has a security system to deter intruders. The cat shelter is equipped with a camera, a motion detector, and an RFID reader that detects a chip in a tag attached to the cat’s collar. The cat shelter is connected via WiFi to a laptop in the house, where a program creates a log of when the cat enters and leaves the shelter. If the chip is not detected, but motion is, it can be assumed that the neighbour’s cat has trespassed into the shelter. In this case, a loud siren plays automatically, and jets of ice cold water are directed at the intruder.

The code reads a file that contains the entry and exit times of the cats, and whether they are the owner’s cat or not. The file has one line for every cat activity, with the format CAT,ENTRY,EXIT, where CAT is either OURS or THEIRS, ENTRY is the time when the cat entered the shelter, and EXIT is the time when the cat left the shelter. Times are stored as minutes, with a start of midnight. The file ends with the word END.



**#task 3**

1.adduser.py

The code imports two modules: hashlib, which provides cryptographic hashing functions, and getpass, which allows secure input of passwords. The code defines four functions:

write_user_data takes a list of user data and a file path as arguments, and writes the user data to the file in a colon-separated format. Each user is represented by a list of three elements: username, full name, and hashed password. This function overwrites the existing content of the file.
read_user_data takes a file path as an argument, and reads the user data from the file. It returns a list of user data, where each user is represented by a list of three elements: username, full name, and hashed password. If the file does not exist, it returns an empty list.
hash_password takes a password as an argument, and hashes it using the SHA-256 algorithm. It returns a hexadecimal string representing the hashed password.
add_user takes a username, a full name, a password, and a file path as arguments, and adds a new user to the user database. It reads the existing user data from the file, checks if the username already exists, and appends the new user’s information if the username is unique. The password is hashed using the SHA-256 algorithm before being stored.


2.deluser.py
This code is a part of a program that implements the deluser command, which deletes a user from the user database. The code imports the hashlib module, which provides cryptographic hashing functions. The code defines four functions:

write_user_data takes a list of user data and a file path as arguments, and writes the user data to the file in a colon-separated format. Each user is represented by a list of three elements: username, full name, and hashed password. This function overwrites the existing content of the file. If the file does not exist, it prints an error message.
read_user_data takes a file path as an argument, and reads the user data from the file. It returns a list of user data, where each user is represented by a list of three elements: username, full name, and hashed password. If the file does not exist, it prints an error message and returns an empty list.
hash_password takes a password as an argument, and hashes it using the SHA-256 algorithm. It returns a hexadecimal string representing the hashed password.
delete_user takes a username and a file path as arguments, and deletes the user by username from the user database. It reads the existing user data from the file, and removes the user’s information if the username matches. It then writes the updated user data to the file. It prints a confirmation message if the user is deleted, or an error message if the username is empty or not found.
The code also gets the user input for the username and the file path, and calls the delete_user function with those arguments.


3.passwd.py
This code is a program that implements the passwd command, which allows a user to change their password in the user database. The code does the following:

- It imports the hashlib module, which provides cryptographic hashing functions, and the getpass module, which allows secure input of passwords.
- It defines four functions:
    - `read_user_data` takes a file path as an argument, and reads the user data from the file. It returns a list of user data, where each user is represented by a list of three elements: username, full name, and hashed password. If the file does not exist, it returns an empty list.
    - `write_user_data` takes a list of user data and a file path as arguments, and writes the user data to the file in a colon-separated format. Each user is represented by a list of three elements: username, full name, and hashed password. This function overwrites the existing content of the file.
    - `hash_password` takes a password as an argument, and hashes it using the SHA-256 algorithm. It returns a hexadecimal string representing the hashed password.
    - `update_user` takes a username, an old password, a new password, and a file path as arguments, and updates the password for the user in the user database. It reads the existing user data from the file, and checks if the username and the old password match. If they do, it replaces the old password with the new hashed password, and writes the updated user data to the file. It prints a confirmation message if the password is changed, or an error message if the username, the old password, or the new password is empty or invalid.
- It gets the user input for the username, the old password, the new password, and the confirm password, and strips any whitespace from them.
- It checks if the new password and the confirm password match. If they do, it calls the `update_user` function with the user input and the file path. If they don't, it prints an error message.



4.login.py
This code is a program that implements the login command, which allows a user to access the system if their username and password match the user database. The code does the following:

It imports the hashlib module, which provides cryptographic hashing functions, and the getpass module, which allows secure input of passwords.
It defines three functions:
read_user_data takes a file path as an argument, and reads the user data from the file. It returns a list of user data, where each user is represented by a list of three elements: username, full name, and hashed password. If the file does not exist or is empty, it returns an empty list and prints an error message.
hash_password takes a password as an argument, and hashes it using the SHA-256 algorithm. It returns a hexadecimal string representing the hashed password.
login takes a username, a password, and a file path as arguments, and checks if the username and password match the user data in the file. It reads the user data from the file, and compares the username and the hashed password with the stored values. It prints a confirmation message if the access is granted, or an error message if the access is denied or the username or password is empty.
It gets the user input for the username, the password, and the file path, and strips any whitespace from them.
It calls the login function with the user input.
This task is about creating a program that can calculate the price of a pizza order from Beckett Pizza Plaza (BPP). The program should ask the user for the number of pizzas, the delivery option, and the app usage. The program should also check if it is Tuesday, as there are different discounts on that day. The program should then apply the appropriate discounts and display the total price in pounds.
This code is a program that calculates the total price of a pizza order based on the following factors:

The number of pizzas ordered, which is obtained from the user by calling the get_input function, which validates that the input is a positive integer.
The day of the week, which is obtained from the user by calling the get_yes_no_input function, which accepts only “y” or “n” as answers. If it is Tuesday, the base price of a pizza is reduced by 50%.
The delivery option, which is also obtained from the user by calling the get_yes_no_input function. If delivery is required, there is an additional charge of 2.5 units, unless the order size is 5 pizzas or more, in which case delivery is free.
The app usage, which is also obtained from the user by calling the get_yes_no_input function. If the customer used the app, there is a discount of 0.75 units applied to the total price.
The code prints a welcome message at the beginning and then prompts the user for the necessary inputs. It then calculates the total price by multiplying the number of pizzas by the base price, adding the delivery cost, and subtracting the app discount. It then prints the total price to the user.

#task 2 

This code is a solution to a programming assignment that involves analysing the usage of a cat shelter that has a security system to deter intruders. The cat shelter is equipped with a camera, a motion detector, and an RFID reader that detects a chip in a tag attached to the cat’s collar. The cat shelter is connected via WiFi to a laptop in the house, where a program creates a log of when the cat enters and leaves the shelter. If the chip is not detected, but motion is, it can be assumed that the neighbour’s cat has trespassed into the shelter. In this case, a loud siren plays automatically, and jets of ice cold water are directed at the intruder.

The code reads a file that contains the entry and exit times of the cats, and whether they are the owner’s cat or not. The file has one line for every cat activity, with the format CAT,ENTRY,EXIT, where CAT is either OURS or THEIRS, ENTRY is the time when the cat entered the shelter, and EXIT is the time when the cat left the shelter. Times are stored as minutes, with a start of midnight. The file ends with the word END.



#task 3

1.adduser.py

The code imports two modules: hashlib, which provides cryptographic hashing functions, and getpass, which allows secure input of passwords. The code defines four functions:

write_user_data takes a list of user data and a file path as arguments, and writes the user data to the file in a colon-separated format. Each user is represented by a list of three elements: username, full name, and hashed password. This function overwrites the existing content of the file.
read_user_data takes a file path as an argument, and reads the user data from the file. It returns a list of user data, where each user is represented by a list of three elements: username, full name, and hashed password. If the file does not exist, it returns an empty list.
hash_password takes a password as an argument, and hashes it using the SHA-256 algorithm. It returns a hexadecimal string representing the hashed password.
add_user takes a username, a full name, a password, and a file path as arguments, and adds a new user to the user database. It reads the existing user data from the file, checks if the username already exists, and appends the new user’s information if the username is unique. The password is hashed using the SHA-256 algorithm before being stored.


2.deluser.py
This code is a part of a program that implements the deluser command, which deletes a user from the user database. The code imports the hashlib module, which provides cryptographic hashing functions. The code defines four functions:

write_user_data takes a list of user data and a file path as arguments, and writes the user data to the file in a colon-separated format. Each user is represented by a list of three elements: username, full name, and hashed password. This function overwrites the existing content of the file. If the file does not exist, it prints an error message.
read_user_data takes a file path as an argument, and reads the user data from the file. It returns a list of user data, where each user is represented by a list of three elements: username, full name, and hashed password. If the file does not exist, it prints an error message and returns an empty list.
hash_password takes a password as an argument, and hashes it using the SHA-256 algorithm. It returns a hexadecimal string representing the hashed password.
delete_user takes a username and a file path as arguments, and deletes the user by username from the user database. It reads the existing user data from the file, and removes the user’s information if the username matches. It then writes the updated user data to the file. It prints a confirmation message if the user is deleted, or an error message if the username is empty or not found.
The code also gets the user input for the username and the file path, and calls the delete_user function with those arguments.


3.passwd.py
This code is a program that implements the passwd command, which allows a user to change their password in the user database. The code does the following:

- It imports the hashlib module, which provides cryptographic hashing functions, and the getpass module, which allows secure input of passwords.
- It defines four functions:
    - `read_user_data` takes a file path as an argument, and reads the user data from the file. It returns a list of user data, where each user is represented by a list of three elements: username, full name, and hashed password. If the file does not exist, it returns an empty list.
    - `write_user_data` takes a list of user data and a file path as arguments, and writes the user data to the file in a colon-separated format. Each user is represented by a list of three elements: username, full name, and hashed password. This function overwrites the existing content of the file.
    - `hash_password` takes a password as an argument, and hashes it using the SHA-256 algorithm. It returns a hexadecimal string representing the hashed password.
    - `update_user` takes a username, an old password, a new password, and a file path as arguments, and updates the password for the user in the user database. It reads the existing user data from the file, and checks if the username and the old password match. If they do, it replaces the old password with the new hashed password, and writes the updated user data to the file. It prints a confirmation message if the password is changed, or an error message if the username, the old password, or the new password is empty or invalid.
- It gets the user input for the username, the old password, the new password, and the confirm password, and strips any whitespace from them.
- It checks if the new password and the confirm password match. If they do, it calls the `update_user` function with the user input and the file path. If they don't, it prints an error message.



4.login.py
This code is a program that implements the login command, which allows a user to access the system if their username and password match the user database. The code does the following:

It imports the hashlib module, which provides cryptographic hashing functions, and the getpass module, which allows secure input of passwords.
It defines three functions:
read_user_data takes a file path as an argument, and reads the user data from the file. It returns a list of user data, where each user is represented by a list of three elements: username, full name, and hashed password. If the file does not exist or is empty, it returns an empty list and prints an error message.
hash_password takes a password as an argument, and hashes it using the SHA-256 algorithm. It returns a hexadecimal string representing the hashed password.
login takes a username, a password, and a file path as arguments, and checks if the username and password match the user data in the file. It reads the user data from the file, and compares the username and the hashed password with the stored values. It prints a confirmation message if the access is granted, or an error message if the access is denied or the username or password is empty.
It gets the user input for the username, the password, and the file path, and strips any whitespace from them.
It calls the login function with the user input.
