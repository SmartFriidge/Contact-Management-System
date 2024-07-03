# Contact Management System

The contact management program we have designed takes a modular approach towards the storage and manipulation of contacts stored using the json format. The functionality of the program includes loading, adding, searching, and deleting contacts, each of which is implemented as a seperate module.

## Modules

### Load Contacts
The load contacts function uses the os library to check if the file we use to store contacts exists and subsequently returns the data of the loaded file.

### Save Contacts
The save contacts function writes the contact information stored in the program as a dictionary back to the file used for storage of the information.
 
### Add Contacts  
The add contacts allows a new contact to be added to the dictionary of contacts by prompting the input of relevant information which includes the name, phone number, and network provider of the contact. This information is appended to the dictionary and the save contacts function is then used to update our contacts file.

### Search Contacts
Searching for contacts is implemented in three seperate modules, each allowing for a search using a different parameter than the others, namely the name of the contact, the phone number, and the network provider. Each search function prompts for the input of the search parameter and proceeds to loop through the contacts dictionary, if the searcg parameter is found, contact information is printed, otherwise the user is informed of the failure of the search.

### Delete Contacts
The delete contact function allows for the permanent removal of a contact. It searches for the given phone number in the contact dictionary, if found the contact is deleted and the file is updates using the save contacts function, otherwise the user is informed of the failure of the process.

### Main()
The main function allows for the user to access all these different features of the program implemented as modules by assigning each module a unique number which the user is prompted to input and thus the appropriate module is called.
