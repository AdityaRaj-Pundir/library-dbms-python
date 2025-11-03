# Online Library Database Management System
> [!NOTE]
> This project uses Python as its frontend and MySQL as its backend.

## Project Aim
The “Digital Library” project aims to computerize the front-end library management system. The software is designed to be user-friendly, simple, fast, and cost-effective.

Key features include user enrollment and book addition, authentication for administrators and users, book availability and check-out, login credentials, data management (only admins can add, delete, or update data), data retrieval, an intuitive user interface, data protection, and a notes facility. The system ensures personal data security and confidentiality.

Library management systems (LMS) are enterprise resource planning systems specifically designed for libraries. They serve as comprehensive tools to manage various aspects of a library’s operations, including tracking enrolled users, monitoring available books, recording book issues and returns, and handling fines and other related information.

The primary objective of an LMS is to enhance library efficiency and reduce operational costs. By automating numerous tasks, these systems streamline the library’s operations, eliminating the need for manual intervention and significantly reducing paperwork.

One of the key advantages of an LMS is its ability to save time for both users and librarians. Users can easily search for available books with just a click, while librarians can quickly access information about book availability. Additionally, the system simplifies the process of adding, removing, or editing the database, making it convenient for managing user registrations and cancellations.

In comparison to manual systems, the automated nature of an LMS results in substantial time savings. By eliminating the need for manual labor and paperwork, the system allows librarians to focus on more critical tasks and provides users with a more efficient and convenient library experience.

## Project Functions
- Home
    - Login
        - User Account
            - Issue Books
            - Return Books
            - View Issued Books
            - Search Books/Authors
                - Books
                    - By Keyword
                    - By Book ID
                    - By Author
                    - By Published Year
                - Authors
                    - By Name
                    - By Author ID
            - Update Account Information
                - Change Display Name
                - Change Password
                - Change E-Mail
                - Change Phone Number
            - Delete Account
            - Add to Wishlist
            - Logout
        - Admin Account
            - Delete Any User’s Account
            - Update Any Account Information
            - Display All User’s Information 
            - Search Users
            - Search Books/Authors
            - Issue Book
            - Return Book
            - View All Issued Books
            - Add Book to Library
            - Delete Book from Library
            - Assign/Revoke Admin Privileges
            - Export Table in CSV Format
            - Logout
    - Sign Up 

## Sample Output
### Home Page:
<img width="488" height="433" alt="image" src="https://github.com/user-attachments/assets/0be51eda-be41-4f1a-bc7f-efb7efff8c59" /><br />
The library system’s homepage is designed with a pixelated aesthetic, emphasizing user navigation. The primary options presented below include login or registration, access to the return policy, or exit. This intuitive layout prioritizes user experience, guiding visitors toward their desired actions with minimal visual distractions. A similar pattern is followed throughout the entire Library System’s experience.

### Return Policy:
<img width="488" height="359" alt="image" src="https://github.com/user-attachments/assets/46a7c5b2-56a2-4573-89d8-5253aab391e1" />

### Login and Sign-Up Page:
<img width="488" height="326" alt="image" src="https://github.com/user-attachments/assets/de5d0e98-f4c5-4eeb-b80c-ade48fd1895a" />

### Signing Up:
<img width="457" height="664" alt="image" src="https://github.com/user-attachments/assets/a00c4630-e8a9-412b-9cb9-db2d981483d6" />

### Logging In:
<img width="457" height="325" alt="image" src="https://github.com/user-attachments/assets/2ebe31c7-26bb-4f2d-ad0a-85e2703d1ea8" />

### User Panel:
<img width="457" height="219" alt="image" src="https://github.com/user-attachments/assets/2de7c6f7-c720-4d41-b1ec-985baa828527" />

### Updating Account Information:
<img width="457" height="473" alt="image" src="https://github.com/user-attachments/assets/812715e6-38ea-4580-aebe-cc30c5934307" /><br />
The standard user can change their Display Name, E-Mail, Phone Number or Password. The overall process for each remains the same, and the user is required to input their current password for each change.

### Searching Books (By Keyword):
<img width="488" height="433" alt="image" src="https://github.com/user-attachments/assets/bbf114ac-8968-4781-9334-10cfc0a49e95" /><br />
The user can search among the books available in the library on the basis of their Book ID, Year of Publication, Author, or a keyword in the book’s title. The overall process for each search function is the same, but searching by Book ID results in the most accurate search, since each book has a unique Book ID.

### Issuing a Book:
<img width="488" height="329" alt="image" src="https://github.com/user-attachments/assets/a88437d4-dd55-4b47-afeb-1459da411aa2" /><br />
Users can issue books by finding the book they want to issue in the shortlisted table, and use the given Book ID to Issue the book. Users can also view which books are already issued by other users.

### Viewing Issues:
<img width="488" height="254" alt="image" src="https://github.com/user-attachments/assets/683cf2d8-0da3-4078-882f-b3efea4c64fd" />

### Returning Issued Books:
<img width="488" height="255" alt="image" src="https://github.com/user-attachments/assets/5bec5fbe-4856-4f8c-a2bb-2a608191cd48" /><br />
Users return issued books by going to the ‘Return Books’ page, where they’re greeted with a list of their current issues. From here they’re prompted with the Book ID of the book they wish to return. The library system automatically calculates the number of days the book had been issued, and calculates the applicable fines (if any).

Users can check whether a book has been issued from the ‘Issue Books’ page or the ‘Search Books’ page.
<img width="488" height="274" alt="image" src="https://github.com/user-attachments/assets/519fa4b7-61d1-416a-a719-fef2c1fb94bc" />

### Wishlist Submissions:
<img width="455" height="178" alt="image" src="https://github.com/user-attachments/assets/26fb90e1-82e0-4c3a-abe8-8f52de34332e" /><br />

> [!NOTE]
> Logging Out brings the user back to the home page.

### Admin Panel:
<img width="455" height="272" alt="image" src="https://github.com/user-attachments/assets/1d6e6a32-563b-4f42-88d6-740d223f9b6c" /><br />
Admin accounts have the ability to do whatever a standard account can, and more. An admin account can delete, update and view any user’s account, issue and return books, view all user’s issue and return details, and Assign/Revoke admin privileges. Moreover, they can export tables in CSV format on their computer.

### Deleting an Account:
<img width="455" height="376" alt="image" src="https://github.com/user-attachments/assets/6b0018ac-b0bb-4c61-8d81-65dc0924a9ab" />

### Searching for an Account:
<img width="455" height="311" alt="image" src="https://github.com/user-attachments/assets/aa79d411-fe41-472c-935f-20ae61354aa6" />

### Adding a Book to the Library:
<img width="455" height="376" alt="image" src="https://github.com/user-attachments/assets/0c1a0dc9-ffc6-4f3d-a48b-5721dbfde1b2" /><br />
While adding books to the library, admins can view the library’s Wishlist in its current state. Thus, they have easy access to the user’s demands.

<img width="455" height="193" alt="image" src="https://github.com/user-attachments/assets/5e478343-b2f3-49f9-833c-da1fbcd2b051" /><br />
> Searching for Atomic Habits (after adding).

### Removing a Book from the Library:
<img width="455" height="239" alt="image" src="https://github.com/user-attachments/assets/c15865e1-f1f4-4cb5-b5f8-375abb28f927" />

### Assigning/Revoking Admin Privileges:
<img width="475" height="334" alt="image" src="https://github.com/user-attachments/assets/8388f458-3556-4c5a-b545-e4d9886e3f11" />

### Exporting a Table in CSV Format:
<img width="456" height="375" alt="image" src="https://github.com/user-attachments/assets/dddcf9f0-85ba-4061-a29f-ef0966626f5b" /><br />

> Exported CSV File:<br />
> <img width="312" height="218" alt="image" src="https://github.com/user-attachments/assets/17a78a01-0365-4a89-bcc2-094655d1201c" />

### Returning a Book Late (Being Fined):
<img width="472" height="260" alt="image" src="https://github.com/user-attachments/assets/f92402f1-ee38-4bbc-adb1-c707124f88c2" />

Admins can then view users who have been fined from the admin panel, by viewing all issues. 

Users are fined for keeping a book longer than 2 weeks. The users are charged 5 AED per day over 2 weeks that they keep the book. In this case, it had been 24 days since the user kept the book, i.e. 10 days over the limit. So, the total charges applicable would be 5 AED per extra day, or 5 AED for 10 days, which amounts to 50 AED.

### Displaying All Users:
<img width="456" height="388" alt="image" src="https://github.com/user-attachments/assets/ceece077-c9fe-4b7d-8d08-161a26dcbbd5" />

### Quitting Program:
<img width="456" height="251" alt="image" src="https://github.com/user-attachments/assets/9b54937a-9677-4960-917d-84797a2f695f" />

## Database Details
Once you have connected Python to MySQL (It should be done automatically on the first run of the `.py` file, the database should be created automatically.

### Library Database:
<img width="259" height="197" alt="image" src="https://github.com/user-attachments/assets/2cf0e1e4-43a3-4ba5-a008-fc71f9c64961" />

### Users Table:
<img width="430" height="144" alt="image" src="https://github.com/user-attachments/assets/494bc0b0-566b-41b8-8ffb-77f9f213bf21" />

### Books Table:
<img width="333" height="128" alt="image" src="https://github.com/user-attachments/assets/0daf96f4-899b-46f9-b1a4-3cf1220e467a" />

### Authors Table:
<img width="323" height="70" alt="image" src="https://github.com/user-attachments/assets/2c2d1aae-a780-49c0-b63d-edd8a54466b8" />

### Issues Table:
<img width="411" height="132" alt="image" src="https://github.com/user-attachments/assets/a91a99a0-4cfd-4cac-a421-7221fe43dd09" />

### Wishlist Table:
<img width="322" height="69" alt="image" src="https://github.com/user-attachments/assets/2f86d44e-e78f-42bd-8c6b-3e119d822e09" />

## Resources Used
The resources used for this project were:
 - 	[patorjk](patorjk.com/software/taag) – Used to create the pixelated headers for each page in the library management system.
 -	MySQL Connector – Used to edit MySQL database from Python as Front-end.
 -	Python – The entire project was done on Python.
 -	ANSI – ANSI Escape sequences were used to color the headers for each page in the library management system.
 -	CSV Module – Used to export tables in CSV format using file handling in Python.
 -	Date and Time module – Used to calculate number of days since a book was issued.
 -	OS Module – Used to identify the operating system of current device and execute the appropriate terminal clearing command.
 -	Prettytable Module – Used to display tables in user-friendly format.

### Thanks for Reading! Happy Hacking!











