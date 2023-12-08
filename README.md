# Memory Transaction

This project emulates a transaction-based system and enables users to begin transactions to put/get key-value pairs to database, and commit and rollback the database. 

## How to Use Library

To run this project, install Python. You can then create a python file, and download memory.py and place it in the same directory as the Python file you created. Then, to access the memory database, use `from memory import Memory`. 

### Create a Memory Object `m = Memory()`
After doing so, you can then access the following functions to interact with database

### `m.begin_transaction()`
Starts transaction

### `m.put(key, value)`
Places key (string) and value (int) pair into current database transaction

### `m.get(key)`
Gets value of key from database transaction once key/value pair has been committed

### `m.commit()`
Commits in progress transactions to database

### `m.rollback()`
Rolls back current transactions of database

### How Assignment Can Be Modified
To make this a more effective assignment, there should be additional functions, such as `printDictionary()`, which would show the current dictionary to the user. There should also be a `printInProgress()` function, which would show the in progress transactions to the user. To make this easier to grade, there could be testing files to ensure functionality.