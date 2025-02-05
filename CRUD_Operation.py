import mysql.connector

con = mysql.connector.connect(
    user = 'root',
    host = 'localhost',
    password = 'joy00' 
)

cur = con.cursor()

# cur.execute("Create Database if not exists Practice")

cur.execute("use Practice")

# cur.execute("""
#     CREATE TABLE employee (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     age INT,
#     position VARCHAR(50)
#     );        
# """)

# Insert Data

# emp_id = int(input("Enter Your ID : "))
# emp_name = input("Enter Your Name : ")
# emp_age = int(input("Enter Your Age : "))
# emp_position = input("Enter Your Position : ")

# cur.execute(f"insert into employee(id,name,age,position) values ({emp_id},'{emp_name}',{emp_age},'{emp_position}')")

# con.commit()
# cur.execute("select * from employee")
# print(cur.fetchall())


# Update Data

# cur.execute(f"Update employee set age = 50 where id = 101")
# con.commit()
# print("Update Records Successfully")
# cur.execute("select * from employee")
# print(cur.fetchall())


# Delete Data
# cur.execute("Delete from employee where id = 102")
# cur.execute("select * from employee")
# print(cur.fetchall())
