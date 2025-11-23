1) Problem Statement
The manual tracking of book inventory and circulation status in a small-scale library is inefficient, time-consuming, and prone to human error, leading to inaccurate records of book 
availability and potential loss of resources. This project addresses the need for a simple, automated, and centralized system to manage the core functions of a library, including inventory 
maintenance (adding, searching, listing) and circulation control (checking out and returning books), thereby improving operational efficiency and ensuring accurate status reporting.
2) Scope of the Project
The scope of this project is limited to developing a foundational, in-memory management system for books using Python.
Inclusions:
Inventory Management: Implementing the ability to add, list, and search for books based on title.
Circulation Logic: Implementing the ability to update the availability status of a book (is_checked_out flag) when it is checked out or returned.
Interface: A Command Line Interface (CLI) for interacting with the system.
Exclusions (Future Enhancements):
Data Persistence: The data is currently lost when the program closes. Saving/loading data to a file (CSV/JSON) is out of scope for this version.
Member Management: Tracking and storing user/member information is not included.
Advanced Features: Overdue fines, complex reporting, or barcode scanning are excluded.
3) Target Users
The primary and sole target user group for this system is:
Librarians and Library Staff: Personnel responsible for the daily operations of the library, including maintaining inventory records, processing check-outs, and handling returns.
The system is designed to be intuitive and easy for staff to use quickly and accurately.
