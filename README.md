# Financial
A Financial New wibsite

• You must read the file to the end to know everything about the program

• Objective of the program:
      Create an interface that allows managing financial transactions (add, view, edit, delete) in an organized and easy way using Django and the Django Rest Framework (DRF).

1. Create a database for financial transactions:
 •The program includes financial transactions such as paying or receiving money. Each transaction contains information such as:
    • Transaction date
    • Transaction description
    • Amount
    • The ID of the user who performed the transaction

2. Create API Endpoints:
 •Endpoints are URLs to which users can send requests to access or modify data. The program requires the establishment of the following points:
    1. GET and POST
       •This point allows users to:
         • View all stored financial transactions (GET).
         • Add a new transaction (POST).

    3.  GET, PUT, and DELETE:
        •This point allows users to:
          • View details of a specific transaction using its unique number (GET).
          • Modifying a specific transaction using its unique number (PUT).
          • Delete a specific transaction using its unique number (DELETE).

    4. The basic functions performed by the program:
         • Transaction Management: Users can add, modify or delete transactions.
         • Data retrieval: Users can review their own financial transactions or other transactions (if they have permission).
         • Identify specific transactions: Users can identify a specific transaction based on its identifier (transaction_id).

    4. Interaction with the program:
        • Users interact with the software by sending HTTP requests such as GET, POST, PUT, and DELETE.
        • POSTMAN or any other tool can be used to test sending these requests to the API and seeing the results.
    
    5. Improvements we will make:
        • You can expand the program to include features such as:
            Create financial reports (such as monthly or annual summaries of transactions).
    6. Test the interface using Postman:
        • After developing the interface, it requires testing all endpoints using a tool like Postman. You will submit requests and verify that the interface is working properly.

    7. How to test the program correctly:
        1. post: http://127.0.0.1:8000/api/transactions/ Go to the link and then fill out the information.
        2. get: http://127.0.0.1:8000/api/transactions/ Go to the link To show the operations you have performed.
        3. delete: http://127.0.0.1:8000/api/transactions/7/ Go to the link To delete the process,The number 7 indicates the id number.

       
