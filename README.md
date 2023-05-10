# Random Password Generator and Password Manager

The project uses Quantum simulator to generate a random password which in comparison to classical methods is purely random.
In the classical methods a pseudorandom number is generated which is actually made by manipulating constants like date and time.
Here, we'll be using a hadamard gate on 7 qubits to generate a random number between 0-127. After that this number will be turned into its ascii value and a string with random characters will be generated.
The Project also has an interactive password manager which stores user Ids, domain and the randomly generated passwords.
The passwords are encrypted and can be accessed if the stored MAC address matches the system's MAC address.

Our project provides two layers of security to the user. Firstly, we use quantum computing to create an untraceable password for the user. Secondly, to access this set of passwords the software checks the MAC address of the device being used along with the user's registered password to decrypt the database. This ensures that even if the system is compromised, the data and stored passwords are safe.

In the project, we used a Hadamard gate on seven qubits to create a circuit with equal probability for every number. On measurement a random number between 0-127 is generated. Then, this number will be turned into the corresponding ascii value and a string with random characters will be generated.

Talking about the interface, the user needs to enter the name of the website/application for which the password needs to be created, the interface then generates the password, encrypts it and stores it in the database. To access the database, the user needs to enter the password of the database, followed by the name of the application/website they need to access the password for, the system decrypts it and returns it back to the user.
