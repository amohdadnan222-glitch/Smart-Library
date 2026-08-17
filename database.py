import sqlite3

# Connect to the database (creates library.db if it doesn't exist)
conn = sqlite3.connect("library.db")

# Create a cursor object
cursor = conn.cursor()

# -----------------------------
# Books Table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    isbn TEXT UNIQUE,
    category TEXT,
    quantity INTEGER NOT NULL,
    available_quantity INTEGER NOT NULL
)
""")

# -----------------------------
# Students Table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    branch TEXT
)
""")

# -----------------------------
# Teachers Table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    department TEXT
)
""")

# -----------------------------
# Issued Books Table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS issued_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_type TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    issue_date TEXT,
    return_date TEXT,
    status TEXT DEFAULT 'Issued',
    fine INTEGER DEFAULT 0
)
""")

# -----------------------------
# Admin Table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS admin(

id INTEGER PRIMARY KEY AUTOINCREMENT,

username TEXT UNIQUE,

password TEXT

)
""")

cursor.execute("""
INSERT OR IGNORE INTO students
(name,email,password,branch)

VALUES
('Adnan',
'adnan@gmail.com',
'12345',
'CSE')
""")

cursor.execute("""
INSERT OR IGNORE INTO admin
(username,password)

VALUES
('admin','admin123')
""")




cursor.execute("""
INSERT OR IGNORE INTO students
(name,email,password,branch)

VALUES
('Adnan',
'adnan@gmail.com',
'12345',
'CSE')
""")


cursor.executemany("""
INSERT OR IGNORE INTO books
(title, author, isbn, category, quantity, available_quantity)
VALUES (?, ?, ?, ?, ?, ?)
""", [

    ("Python Programming", "Guido van Rossum", "ISBN101", "Programming", 10, 10),
    ("Flask Web Development", "Miguel Grinberg", "ISBN102", "Web Development", 8, 8),
    ("Learning SQL", "Alan Beaulieu", "ISBN103", "Database", 6, 6),
    ("Computer Networks", "Andrew S. Tanenbaum", "ISBN104", "Networking", 12, 12),
    ("Operating System Concepts", "Abraham Silberschatz", "ISBN105", "Operating System", 7, 7),
    ("Data Structures Using Python", "Narasimha Karumanchi", "ISBN106", "Programming", 9, 9),
    ("Artificial Intelligence", "Stuart Russell", "ISBN107", "AI", 5, 5),
    ("Machine Learning", "Tom M. Mitchell", "ISBN108", "Machine Learning", 4, 4),
    ("Clean Code", "Robert C. Martin", "ISBN109", "Software Engineering", 10, 10),
    ("Introduction to Algorithms", "Thomas H. Cormen", "ISBN110", "Algorithms", 15, 15),

    ("Java: The Complete Reference", "Herbert Schildt", "ISBN111", "Programming", 8, 8),
    ("Effective Java", "Joshua Bloch", "ISBN112", "Programming", 7, 7),
    ("C Programming Language", "Brian W. Kernighan", "ISBN113", "Programming", 11, 11),
    ("C++ Primer", "Stanley B. Lippman", "ISBN114", "Programming", 6, 6),
    ("Head First Java", "Kathy Sierra", "ISBN115", "Programming", 9, 9),
    ("Head First Python", "Paul Barry", "ISBN116", "Programming", 7, 7),
    ("Automate the Boring Stuff", "Al Sweigart", "ISBN117", "Python", 10, 10),
    ("Python Crash Course", "Eric Matthes", "ISBN118", "Python", 12, 12),
    ("Think Python", "Allen B. Downey", "ISBN119", "Python", 8, 8),
    ("Django for Beginners", "William S. Vincent", "ISBN120", "Web Development", 6, 6),

    ("HTML and CSS", "Jon Duckett", "ISBN121", "Web Development", 9, 9),
    ("JavaScript and JQuery", "Jon Duckett", "ISBN122", "Web Development", 8, 8),
    ("Eloquent JavaScript", "Marijn Haverbeke", "ISBN123", "Web Development", 7, 7),
    ("JavaScript: The Good Parts", "Douglas Crockford", "ISBN124", "Web Development", 5, 5),
    ("You Don't Know JS", "Kyle Simpson", "ISBN125", "JavaScript", 10, 10),
    ("Learning React", "Alex Banks", "ISBN126", "Web Development", 8, 8),
    ("React Up and Running", "Stoyan Stefanov", "ISBN127", "Web Development", 7, 7),
    ("Learning Node.js", "Marc Harter", "ISBN128", "Web Development", 6, 6),
    ("Node.js in Action", "Nathan Rajlich", "ISBN129", "Web Development", 9, 9),
    ("PHP and MySQL Web Development", "Luke Welling", "ISBN130", "Web Development", 11, 11),

    ("Database System Concepts", "Abraham Silberschatz", "ISBN131", "Database", 10, 10),
    ("Fundamentals of Database Systems", "Ramez Elmasri", "ISBN132", "Database", 8, 8),
    ("SQL Cookbook", "Anthony Molinaro", "ISBN133", "Database", 7, 7),
    ("SQL Pocket Guide", "Jonathan Gennick", "ISBN134", "Database", 5, 5),
    ("MySQL Cookbook", "Paul DuBois", "ISBN135", "Database", 9, 9),
    ("PostgreSQL Up and Running", "Regina Obe", "ISBN136", "Database", 6, 6),
    ("MongoDB: The Definitive Guide", "Kristina Chodorow", "ISBN137", "Database", 8, 8),
    ("Beginning MongoDB 7", "Dushan Petkovic", "ISBN138", "Database", 7, 7),
    ("Database Design for Mere Mortals", "Michael J. Hernandez", "ISBN139", "Database", 10, 10),
    ("NoSQL Distilled", "Pramod J. Sadalage", "ISBN140", "Database", 6, 6),

    ("Computer Networks", "James F. Kurose", "ISBN141", "Networking", 12, 12),
    ("Data Communications", "Behrouz A. Forouzan", "ISBN142", "Networking", 9, 9),
    ("Networking Essentials", "Jeffrey S. Beasley", "ISBN143", "Networking", 7, 7),
    ("TCP/IP Illustrated", "W. Richard Stevens", "ISBN144", "Networking", 8, 8),
    ("Network Security Essentials", "William Stallings", "ISBN145", "Networking", 6, 6),
    ("CCNA Routing and Switching", "Todd Lammle", "ISBN146", "Networking", 10, 10),
    ("Computer Networking: A Top-Down Approach", "James Kurose", "ISBN147", "Networking", 11, 11),
    ("Network Programming with Python", "John Goerzen", "ISBN148", "Networking", 5, 5),
    ("Wireless Communications", "Andrea Goldsmith", "ISBN149", "Networking", 7, 7),
    ("Internet Protocols", "Douglas E. Comer", "ISBN150", "Networking", 8, 8),

    ("Operating Systems: Internals and Design", "William Stallings", "ISBN151", "Operating System", 9, 9),
    ("Modern Operating Systems", "Andrew S. Tanenbaum", "ISBN152", "Operating System", 10, 10),
    ("Operating System Principles", "Andrew S. Tanenbaum", "ISBN153", "Operating System", 6, 6),
    ("Linux Kernel Development", "Robert Love", "ISBN154", "Operating System", 8, 8),
    ("The Linux Command Line", "William Shotts", "ISBN155", "Linux", 12, 12),
    ("Linux Bible", "Christopher Negus", "ISBN156", "Linux", 7, 7),
    ("UNIX Network Programming", "W. Richard Stevens", "ISBN157", "Operating System", 6, 6),
    ("Advanced Programming in the UNIX Environment", "W. Richard Stevens", "ISBN158", "Operating System", 5, 5),
    ("Windows Internals", "Pavel Yosifovich", "ISBN159", "Operating System", 8, 8),
    ("Operating Systems Made Easy", "R. K. Sharma", "ISBN160", "Operating System", 7, 7),

    ("Deep Learning", "Ian Goodfellow", "ISBN161", "AI", 6, 6),
    ("Hands-On Machine Learning", "Aurélien Géron", "ISBN162", "Machine Learning", 10, 10),
    ("Pattern Recognition and Machine Learning", "Christopher Bishop", "ISBN163", "Machine Learning", 7, 7),
    ("Machine Learning Yearning", "Andrew Ng", "ISBN164", "Machine Learning", 8, 8),
    ("The Elements of Statistical Learning", "Trevor Hastie", "ISBN165", "Machine Learning", 5, 5),
    ("Reinforcement Learning", "Richard S. Sutton", "ISBN166", "AI", 6, 6),
    ("Computer Vision", "Richard Szeliski", "ISBN167", "AI", 7, 7),
    ("Natural Language Processing", "Daniel Jurafsky", "ISBN168", "AI", 9, 9),
    ("Speech and Language Processing", "James H. Martin", "ISBN169", "AI", 5, 5),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "ISBN170", "AI", 10, 10),

    ("Software Engineering", "Ian Sommerville", "ISBN171", "Software Engineering", 12, 12),
    ("The Pragmatic Programmer", "David Thomas", "ISBN172", "Software Engineering", 9, 9),
    ("Code Complete", "Steve McConnell", "ISBN173", "Software Engineering", 8, 8),
    ("Software Testing Techniques", "Boris Beizer", "ISBN174", "Software Engineering", 6, 6),
    ("Agile Software Development", "Robert C. Martin", "ISBN175", "Software Engineering", 7, 7),
    ("User Story Applied", "Mike Cohn", "ISBN176", "Software Engineering", 5, 5),
    ("Design Patterns", "Erich Gamma", "ISBN177", "Software Engineering", 10, 10),
    ("Refactoring", "Martin Fowler", "ISBN178", "Software Engineering", 8, 8),
    ("Continuous Delivery", "Jez Humble", "ISBN179", "Software Engineering", 6, 6),
    ("DevOps Handbook", "Gene Kim", "ISBN180", "Software Engineering", 9, 9),

    ("The C++ Programming Language", "Bjarne Stroustrup", "ISBN181", "Programming", 7, 7),
    ("Effective C++", "Scott Meyers", "ISBN182", "Programming", 6, 6),
    ("C# in a Nutshell", "Joseph Albahari", "ISBN183", "Programming", 8, 8),
    ("Learning C#", "Jesse Liberty", "ISBN184", "Programming", 9, 9),
    ("Go Programming Language", "Alan A. A. Donovan", "ISBN185", "Programming", 5, 5),
    ("Programming Rust", "Jim Blandy", "ISBN186", "Programming", 6, 6),
    ("The Rust Programming Language", "Steve Klabnik", "ISBN187", "Programming", 8, 8),
    ("Kotlin in Action", "Dmitry Jemerov", "ISBN188", "Programming", 7, 7),
    ("Swift Programming", "Matt Neuburg", "ISBN189", "Programming", 5, 5),
    ("R Programming for Data Science", "Roger D. Peng", "ISBN190", "Programming", 9, 9),

    ("Engineering Mathematics I", "B. S. Grewal", "ISBN191", "Mathematics", 15, 15),
    ("Engineering Mathematics II", "B. S. Grewal", "ISBN192", "Mathematics", 12, 12),
    ("Higher Engineering Mathematics", "B. V. Ramana", "ISBN193", "Mathematics", 10, 10),
    ("Discrete Mathematics", "Kenneth H. Rosen", "ISBN194", "Mathematics", 8, 8),
    ("Linear Algebra Done Right", "Sheldon Axler", "ISBN195", "Mathematics", 7, 7),
    ("Probability and Statistics", "Miller", "ISBN196", "Mathematics", 9, 9),
    ("Numerical Methods", "S. S. Sastry", "ISBN197", "Mathematics", 11, 11),
    ("Graph Theory", "Douglas B. West", "ISBN198", "Mathematics", 6, 6),
    ("Calculus", "James Stewart", "ISBN199", "Mathematics", 10, 10),
    ("Differential Equations", "Dennis Zill", "ISBN200", "Mathematics", 8, 8),

    ("Engineering Physics", "H. K. Malik", "ISBN201", "Physics", 9, 9),
    ("Modern Engineering Physics", "A. S. Vasudeva", "ISBN202", "Physics", 7, 7),
    ("Concepts of Physics", "H. C. Verma", "ISBN203", "Physics", 12, 12),
    ("University Physics", "Young and Freedman", "ISBN204", "Physics", 8, 8),
    ("Introduction to Quantum Mechanics", "David J. Griffiths", "ISBN205", "Physics", 6, 6),
    ("Electromagnetism", "David J. Griffiths", "ISBN206", "Physics", 7, 7),
    ("Optics", "Ajoy Ghatak", "ISBN207", "Physics", 9, 9),
    ("Solid State Physics", "A. J. Dekker", "ISBN208", "Physics", 5, 5),
    ("Thermodynamics", "Yunus Cengel", "ISBN209", "Physics", 8, 8),
    ("Waves and Oscillations", "N. K. Bajaj", "ISBN210", "Physics", 6, 6),

    ("Digital Electronics", "R. P. Jain", "ISBN211", "Electronics", 10, 10),
    ("Microelectronic Circuits", "Adel S. Sedra", "ISBN212", "Electronics", 7, 7),
    ("Microprocessors and Microcontrollers", "A. K. Ray", "ISBN213", "Electronics", 8, 8),
    ("Embedded Systems", "Raj Kamal", "ISBN214", "Electronics", 9, 9),
    ("Digital Design", "Morris Mano", "ISBN215", "Electronics", 11, 11),
    ("Analog Electronics", "David A. Bell", "ISBN216", "Electronics", 6, 6),
    ("Electronic Devices", "Thomas Floyd", "ISBN217", "Electronics", 8, 8),
    ("Communication Systems", "Simon Haykin", "ISBN218", "Electronics", 7, 7),
    ("VLSI Design", "S. M. Sze", "ISBN219", "Electronics", 5, 5),
    ("Internet of Things", "Arshdeep Bahga", "ISBN220", "Electronics", 10, 10),

    ("Cloud Computing", "Rajkumar Buyya", "ISBN221", "Cloud Computing", 9, 9),
    ("AWS in Action", "Andreas Wittig", "ISBN222", "Cloud Computing", 7, 7),
    ("Learning AWS", "Mark Wilkins", "ISBN223", "Cloud Computing", 6, 6),
    ("Azure Fundamentals", "John Savill", "ISBN224", "Cloud Computing", 8, 8),
    ("Google Cloud Platform", "Ted Hunter", "ISBN225", "Cloud Computing", 5, 5),
    ("Cloud Security", "Ronald Krutz", "ISBN226", "Cloud Computing", 7, 7),
    ("Cloud Architecture Patterns", "Bill Wilder", "ISBN227", "Cloud Computing", 9, 9),
    ("Serverless Architectures", "Peter Sbarski", "ISBN228", "Cloud Computing", 6, 6),
    ("Docker Deep Dive", "Nigel Poulton", "ISBN229", "Cloud Computing", 10, 10),
    ("Kubernetes Up and Running", "Kelsey Hightower", "ISBN230", "Cloud Computing", 8, 8),

    ("Android Programming", "Bill Phillips", "ISBN231", "Mobile Development", 7, 7),
    ("Android App Development", "Neil Smyth", "ISBN232", "Mobile Development", 9, 9),
    ("Head First Android Development", "Jonathan Simon", "ISBN233", "Mobile Development", 6, 6),
    ("Kotlin Programming", "Dmitry Jemerov", "ISBN234", "Mobile Development", 8, 8),
    ("Flutter in Action", "Eric Windmill", "ISBN235", "Mobile Development", 5, 5),
    ("Beginning Flutter", "Marco L. Napoli", "ISBN236", "Mobile Development", 7, 7),
    ("React Native in Action", "Nader Dabit", "ISBN237", "Mobile Development", 6, 6),
    ("Mobile UI Design", "Michael Firtman", "ISBN238", "Mobile Development", 8, 8),
    ("iOS Programming", "Matt Neuburg", "ISBN239", "Mobile Development", 5, 5),
    ("Cross Platform Development", "Alessandro B.", "ISBN240", "Mobile Development", 7, 7),

    ("Cybersecurity Essentials", "Charles J. Brooks", "ISBN241", "Cyber Security", 8, 8),
    ("Ethical Hacking", "Jon Erickson", "ISBN242", "Cyber Security", 6, 6),
    ("Hacking: The Art of Exploitation", "Jon Erickson", "ISBN243", "Cyber Security", 5, 5),
    ("Network Security", "William Stallings", "ISBN244", "Cyber Security", 9, 9),
    ("Web Application Security", "Andrew Hoffman", "ISBN245", "Cyber Security", 7, 7),
    ("Cryptography and Network Security", "William Stallings", "ISBN246", "Cyber Security", 10, 10),
    ("Digital Forensics", "Bill Nelson", "ISBN247", "Cyber Security", 6, 6),
    ("Cybersecurity Risk Management", "Robert Slade", "ISBN248", "Cyber Security", 5, 5),
    ("Secure Coding", "Robert C. Seacord", "ISBN249", "Cyber Security", 8, 8),
    ("Information Security", "Mark Stamp", "ISBN250", "Cyber Security", 7, 7),

    ("Human Computer Interaction", "Alan Dix", "ISBN251", "Computer Science", 8, 8),
    ("Computer Graphics", "Donald D. Hearn", "ISBN252", "Computer Science", 7, 7),
    ("Compiler Design", "Alfred V. Aho", "ISBN253", "Computer Science", 9, 9),
    ("Theory of Computation", "Michael Sipser", "ISBN254", "Computer Science", 6, 6),
    ("Computer Organization", "Carl Hamacher", "ISBN255", "Computer Science", 10, 10),
    ("Distributed Systems", "Andrew S. Tanenbaum", "ISBN256", "Computer Science", 7, 7),
    ("Parallel Computing", "Michael Quinn", "ISBN257", "Computer Science", 5, 5),
    ("Data Compression", "David Salomon", "ISBN258", "Computer Science", 6, 6),
    ("Information Retrieval", "Christopher D. Manning", "ISBN259", "Computer Science", 8, 8),
    ("Computer Science Fundamentals", "P. K. Sinha", "ISBN260", "Computer Science", 9, 9),

    ("Algorithm Design Manual", "Steven S. Skiena", "ISBN261", "Algorithms", 7, 7),
    ("Algorithms", "Robert Sedgewick", "ISBN262", "Algorithms", 10, 10),
    ("Competitive Programming", "Steven Halim", "ISBN263", "Algorithms", 6, 6),
    ("Introduction to Graph Algorithms", "Thomas Cormen", "ISBN264", "Algorithms", 5, 5),
    ("Dynamic Programming", "Vijay Vazirani", "ISBN265", "Algorithms", 8, 8),
    ("Greedy Algorithms", "Bernard Chazelle", "ISBN266", "Algorithms", 7, 7),
    ("String Algorithms", "Dan Gusfield", "ISBN267", "Algorithms", 6, 6),
    ("Computational Complexity", "Christos Papadimitriou", "ISBN268", "Algorithms", 5, 5),
    ("Algorithmic Thinking", "Daniel Zingaro", "ISBN269", "Algorithms", 9, 9),
    ("Problem Solving with Algorithms", "Brad Miller", "ISBN270", "Algorithms", 8, 8),

    ("Data Mining", "Jiawei Han", "ISBN271", "Data Science", 7, 7),
    ("Data Analytics", "Mahesh Joshi", "ISBN272", "Data Science", 9, 9),
    ("Practical Data Science", "Nina Zumel", "ISBN273", "Data Science", 6, 6),
    ("Data Visualization", "Claus Wilke", "ISBN274", "Data Science", 8, 8),
    ("Python for Data Analysis", "Wes McKinney", "ISBN275", "Data Science", 12, 12),
    ("Statistics in Plain English", "Timothy Urdan", "ISBN276", "Data Science", 7, 7),
    ("Think Stats", "Allen B. Downey", "ISBN277", "Data Science", 5, 5),
    ("Exploratory Data Analysis", "John Tukey", "ISBN278", "Data Science", 6, 6),
    ("Business Intelligence", "Cindi Howson", "ISBN279", "Data Science", 8, 8),
    ("Practical Machine Learning", "Sanjay Patel", "ISBN280", "Data Science", 9, 9),

    ("Information Technology Basics", "Alex Leon", "ISBN281", "Information Technology", 8, 8),
    ("IT Infrastructure", "Michael H. Hugos", "ISBN282", "Information Technology", 6, 6),
    ("IT Service Management", "David Cannon", "ISBN283", "Information Technology", 7, 7),
    ("Enterprise IT Systems", "Ramesh G.", "ISBN284", "Information Technology", 5, 5),
    ("System Administration", "Evi Nemeth", "ISBN285", "Information Technology", 9, 9),
    ("IT Project Management", "Kathy Schwalbe", "ISBN286", "Information Technology", 8, 8),
    ("Digital Transformation", "Thomas M. Siebel", "ISBN287", "Information Technology", 6, 6),
    ("Technology Management", "V. K. Jain", "ISBN288", "Information Technology", 7, 7),
    ("Enterprise Computing", "George Reese", "ISBN289", "Information Technology", 5, 5),
    ("IT Support Essentials", "Mike Meyers", "ISBN290", "Information Technology", 10, 10),

    ("Artificial Neural Networks", "Simon Haykin", "ISBN291", "AI", 6, 6),
    ("Neural Networks from Scratch", "Harrison Kinsley", "ISBN292", "AI", 7, 7),
    ("Deep Neural Networks", "Charu Aggarwal", "ISBN293", "AI", 5, 5),
    ("Convolutional Neural Networks", "F. Chollet", "ISBN294", "AI", 8, 8),
    ("Recurrent Neural Networks", "J. Schmidhuber", "ISBN295", "AI", 6, 6),
    ("Transformers for NLP", "Lewis Tunstall", "ISBN296", "AI", 7, 7),
    ("Practical Deep Learning", "Jeremy Howard", "ISBN297", "AI", 9, 9),
    ("Neural Network Optimization", "Ian Goodfellow", "ISBN298", "AI", 5, 5),
    ("Computer Vision with Python", "Adrian Rosebrock", "ISBN299", "AI", 8, 8),
    ("AI Projects with Python", "Prateek Joshi", "ISBN300", "AI", 7, 7),

])


cursor.execute("""
INSERT OR IGNORE INTO teachers
(name, email, password, department)

VALUES
(
'Rahul Sharma',
'teacher@gmail.com',
'12345',
'Computer Science'
)
""")


# Save changes
conn.commit()



# Close the connection
conn.close()

print("Database and tables created successfully!")