from lib2to3.pytree import convert
import mysql.connector
import string
import random

mydb = mysql.connector.connect(host="localhost",
user="root",
password="password",
auth_plugin='mysql_native_password',
database="RideShare") 
# print(mydb)

# ----------------------------------------------------------- #

# Create cursor object to iteract with MySQL
mycursor = mydb.cursor()

# ----------------------------------------------------------- #

# Create the db
# mycursor.execute("CREATE SCHEMA RideShare;")

# ----------------------------------------------------------- #

# show the databases that exist in my local mySQL
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#     print(x)

# ----------------------------------------------------------- #

# Create Tables
# mycursor.execute("CREATE TABLE Driver (driverID VARCHAR(22) NOT NULL PRIMARY KEY, name VARCHAR(20), vehicleID VARCHAR(20), driverMode BOOLEAN, rating DOUBLE)")
# mycursor.execute("CREATE TABLE Rider (riderID VARCHAR(22) NOT NULL PRIMARY KEY, name VARCHAR(20), phoneNum VARCHAR(15))")
# mycursor.execute("CREATE TABLE Ride (rideID INT NOT NULL PRIMARY KEY AUTO_INCREMENT, riderID VARCHAR(22), driverID VARCHAR(22), pickUp VARCHAR(50), dropOff VARCHAR(50), rating DOUBLE)")
# mycursor.execute("CREATE TABLE Vehicle (vehicleID VARCHAR(22) NOT NULL UNIQUE PRIMARY KEY, make VARCHAR(20), model VARCHAR(20), color VARCHAR(20), licensePlate VARCHAR(20))")
# mycursor.execute("CREATE TABLE DriverOrRider (driverID VARCHAR(22), riderID VARCHAR(22), name VARCHAR(10))")


# ----------------------------------------------------------- #

# Add Foreign Keys
# mycursor.execute("ALTER TABLE Driver ADD FOREIGN KEY (vehicleID) REFERENCES Vehicle(vehicleID)")
# mycursor.execute("ALTER TABLE Ride ADD FOREIGN KEY (riderID) REFERENCES Rider(riderID)")
# mycursor.execute("ALTER TABLE Ride ADD FOREIGN KEY (driverID) REFERENCES Driver(driverID)")
# mycursor.execute("ALTER TABLE DriverOrRider ADD FOREIGN KEY (driverID) REFERENCES Driver(driverID)")
# mycursor.execute("ALTER TABLE DriverOrRider ADD FOREIGN KEY (riderID) REFERENCES Rider(riderID)")

# ----------------------------------------------------------- #

# Add Data
# sql = "INSERT INTO Vehicle (vehicleID, make, model, color, licensePlate) VALUES (%s, %s, %s, %s, %s)"
# vals = [('xRkOD9td9Zqcqo2', 'Volkswagen', 'Golf', 'Black', '7FY4T01'),
# ('cecGqctlGeCXEZq', 'Volkswagen', 'Golf', 'Black', '7FY4T01'),
# ('3q5NkGqqI5DJrVG', 'Honda', 'Accord', 'Silver', '8KM2WY3'),
# ('y71md24SsEjfA5r', 'Toyota', 'Sienna', 'Red', 'HP7YBBF'),
# ('Qy5PpUSWJ8fTWCg', 'Tesla', 'Model 3', 'White', '24NYRC1'),
# ('8Y7g60B9EEiNy9f', 'Honda', 'Civic', 'Blue', '3EJRKY9'),
# ('sxJD1uQEpwo10iL', 'Toyota', 'Corolla', 'Black', 'SB2OKYH'),
# ('HiL86pTnNmK6WTI', 'Toyota', '4Runner', 'Grey', 'BFNBIUW'),
# ('Iv3MBC1ShNtwO7E', 'Volkswagen', 'Tiguan', 'White', 'M5S21C1'),
# ('QcSnbdqjNFsJgeD', 'Ford', 'Focus', 'Black', 'Z9IE9N7'),
# ('HRwauhkDQWTpL5J', 'Kia', 'Sportage', 'Blue', '2O1YUGC'),
# ('J8vsQB7rMjQoqL5', 'BMW', 'X3', 'Black', 'QL2QCRB'),
# ('PRT0VJiszZYJ1Pa', 'Honda', 'Accord', 'Black', 'D5XS00Q'),
# ('9vKNDK8rxPiocKs', 'Toyota', 'Corolla', 'White', 'TB05BIC'),
# ('C24VZlWq1s8iUoS', 'Volkswagen', 'Jetta', 'Silver', 'GKY0K7P'),]

# mycursor.executemany(sql, vals)
# mydb.commit()
# print(mycursor.rowcount, "rows were inserted")

# sql = "INSERT INTO Driver (driverID, name, vehicleID, driverMode, rating) VALUES (%s, %s, %s, %s, %s)"
# vals = [('ekCKOlExoFvyA5i', 'Wanda Moody', 'xRkOD9td9Zqcqo2', '1', '4.98'), 
# ('InXemtPAPvFX5Z6', 'Kristopher Tucker', 'cecGqctlGeCXEZq', '0', '4.95'), 
# ('IccUCxLJkWEUOuB', 'Frances Alexander', '3q5NkGqqI5DJrVG', '1', '4.99'), 
# ('lkJOuE8uhp5NOXx', 'Debra Snyder', 'y71md24SsEjfA5r', '1', '4.75'), 
# ('S0aL4m9JVv7YxKp', 'Roxanne Harris', 'Qy5PpUSWJ8fTWCg', '1', '4.87'), 
# ('BdT7GREciB3kXGN', 'Harry Andrews', '8Y7g60B9EEiNy9f', '0', '4.98'), 
# ('dSMf9rHTs48t7OQ', 'Lucia Wells', 'sxJD1uQEpwo10iL', '0', '4.99'), 
# ('oBVDrRhpkg6zcgm', 'Malcolm Parker', 'HiL86pTnNmK6WTI', '1', '5.00'), 
# ('VOob7q0tCMWNuBQ', 'Ryan Waters', 'Iv3MBC1ShNtwO7E', '0', '4.92'), 
# ('WyTeYby0BlrLtAy', 'Jerome Bishop', 'QcSnbdqjNFsJgeD', '1', '4.99'), 
# ('vQ8KC1LD8BzE9yq', 'Candice Anderson', 'HRwauhkDQWTpL5J', '1', '4.96'), 
# ('3cQP3m3dceEnieV', 'Jacob Stokes', 'J8vsQB7rMjQoqL5', '1', '4.98'), 
# ('E6NKLqQSaI74CZD', 'Domingo Obrien', 'PRT0VJiszZYJ1Pa', '0', '4.93'), 
# ('wmiFLYKt9rvfUyb', 'Pat Pierce', '9vKNDK8rxPiocKs', '1', '4.97'), 
# ('IZZqGdkBy2eV7b5', 'Henry Fitzgerald', 'C24VZlWq1s8iUoS', '1', '4.98')]

# mycursor.executemany(sql, vals)
# mydb.commit()
# print(mycursor.rowcount, "rows were inserted")

# sql = "INSERT INTO Rider (riderID, name, phoneNum) VALUES (%s, %s, %s)"
# vals = [('CFY0PK5OVTCK0ZF', 'Lewis Tyler', '847-977-8163'),
# ('FT6P76USDAN3EOL', 'Terrance Flowers', '910-949-6413'),
# ('A208SQGLDQRBPQN', 'Tina Howard', '978-670-5079'),
# ('P1C4BEJ4WP1QP2S', 'Jana Clark', '386-219-0878'),
# ('59KBP2NRO9OE9EF', 'Kent Lamb', '410-843-2971'),
# ('T6CGQGIKRUAL7HP', 'Wilfred Underwood', '763-900-8720'),
# ('68EA0TGGHC6I1KW', 'Seth Ryan', '715-325-8632'),
# ('3RO1SGB2FD6VXOJ', 'Eddie Frazier', '254-639-4112'),
# ('M11U36WVX1MSYJ4', 'Dominick Guerrero', '701-699-3769'),
# ('H5GE2QT8ZCG1AL6', 'Rudolph Bowman', '731-642-2727'),
# ('9MDQGD3UD5H2UNK', 'Cynthia Daniel', '662-774-7978'),
# ('6UHNHO8GILJOOR2', 'Penny Newton', '914-713-8470'),
# ('9DB21I7CR34643K', 'Tanya Poole', '806-788-4423'),
# ('RP6A1SE3M1LBO80', 'Lisa Estrada', '262-200-2530'),
# ('B95O7R22F7TEG8M', 'Frances Terry', '405-998-1635'),
# ('VFFTY5IIWNYPWR2', 'Suzanne Fleming', '402-562-1493'),
# ('YLX0UJW4FAP0MHT', 'Phil Gilbert', '386-250-2210'),
# ('Y2ST48IWB43OE3T', 'Sidney Watts', '601-885-2890'),
# ('ZM0BQ9HEU6SELPG', 'Blanche Mann', '716-629-3618'),
# ('T9T3A2DGOHCGB3C', 'Karla Bennett', '818-678-1313'),
# ('YPPWFKOH3DWA6UT', 'Ismael Rice', '219-754-8440'),
# ('J76BR3A2LOAT1O8', 'Genevieve Obrien', '937-564-1769'),
# ('UUM3KAYLF0XIUHK', 'Jeff Hernandez', '847-977-8163'),
# ('RGFT3MJQXG8T2B1', 'Terrance Lloyd', '612-889-2494'),
# ('CUHASHMKWLRDJ7N', 'Isaac Roberson', '801-356-9982'),
# ('IYRQBO4GRKAJ9WJ', 'Vicky Page', '309-498-2035'),
# ('73SGWWQCL2WQUWZ', 'Luis Bryant', '702-593-9262'),
# ('T6IGHRATNJZL5HV', 'Kevin Gomez', '612-304-8710'),
# ('2SSY921BDZE5CIX', 'Lena French', '806-220-1239'),
# ('KSMPQFMHFDWXL5C', 'Rickey Wells', '406-466-7709'),
# ('UZQ50CK5T1DGJKW', 'Maggie Benson', '225-329-5688'),
# ('5DZNVMRKBD6R9RB', 'Caroline Cummings', '630-980-1721'),
# ('GLS5YXLQ550FDFI', 'Loren Roberson', '631-218-7040'),
# ('26SX784DNJ72ZDZ', 'Dawn Mcdonald', '260-748-0759'),
# ('MR9II8YV4OUZGW3', 'Mary Ramos', '912-383-9128'),
# ('HPL71VRLHTULT6G', 'Elias White', '304-385-8389'),
# ('L3R9S8K6MNU08XT', 'Josefina Carpenter', '216-410-6294'),
# ('YP41Q7J1KOCP462', 'Justin Hogan', '858-794-0035'),
# ('3JFSMLBOU9S7KKO', 'Shelly Rivera', '212-500-6148'),
# ('8FV745LYVLX5TXE', 'Joan Wade', '732-416-9606'),
# ('6NAKBP4JZL9JX3Y', 'Monica Herrera', '405-368-7467'),
# ('10Y0Z93OQ1WTRAC', 'Wilfred James', '414-934-2171'),
# ('08UDEYN5QIL2WKT', 'Jim Padilla', '770-590-3001'),
# ('9UXTLUHHIRYKSNR', 'Judith Lewis', '715-466-4810'),
# ('XYND8BQWBN1WGCJ', 'Lance Holland', '240-560-1151'),
# ('71ENJV20KIFHARX', 'Louis Lowe', '414-817-9168'),
# ('ET5ZRE119ZQEGWO', 'Donald Luna', '956-960-7755'),
# ('BD72UODBIEB33OH', 'Hubert Sutton', '937-328-1233'),
# ('SHK43WQV4OM9GS9', 'Lila Benson', '831-239-4057'),
# ('7ULUCNBV89Y9GCK', 'Ben Klein', '336-282-1585'),
# ('N6IP88M0NRP6ZZQ', 'Janie Lindsey', '757-889-4065')]

# mycursor.executemany(sql, vals)
# mydb.commit()
# print(mycursor.rowcount, "rows were inserted")

# sql = "INSERT INTO DriverORRider (driverID, riderID, name) VALUES (%s, %s, %s)"
# vals = [('ekCKOlExoFvyA5i', '','Driver'), 
# ('InXemtPAPvFX5Z6', '', 'Driver'), 
# ('IccUCxLJkWEUOuB', '', 'Driver'), 
# ('lkJOuE8uhp5NOXx', '', 'Driver'), 
# ('S0aL4m9JVv7YxKp', '', 'Driver'), 
# ('BdT7GREciB3kXGN', '', 'Driver'), 
# ('dSMf9rHTs48t7OQ', '', 'Driver'), 
# ('oBVDrRhpkg6zcgm', '', 'Driver'), 
# ('VOob7q0tCMWNuBQ', '', 'Driver'), 
# ('WyTeYby0BlrLtAy', '', 'Driver'), 
# ('vQ8KC1LD8BzE9yq', '', 'Driver'), 
# ('3cQP3m3dceEnieV', '', 'Driver'), 
# ('E6NKLqQSaI74CZD', '', 'Driver'), 
# ('PRT0VJiszZYJ1Pa', '', 'Driver'), 
# ('IZZqGdkBy2eV7b5', '', 'Driver'),
# ('', 'CFY0PK5OVTCK0ZF','Rider'),
# ('', 'FT6P76USDAN3EOL', 'Rider'),
# ('', 'A208SQGLDQRBPQN', 'Rider'),
# ('', 'P1C4BEJ4WP1QP2S', 'Rider'),
# ('', '59KBP2NRO9OE9EF', 'Rider'),
# ('', 'T6CGQGIKRUAL7HP', 'Rider'),
# ('', '68EA0TGGHC6I1KW', 'Rider'),
# ('', '3RO1SGB2FD6VXOJ', 'Rider'),
# ('', 'M11U36WVX1MSYJ4', 'Rider'),
# ('', 'H5GE2QT8ZCG1AL6', 'Rider'),
# ('', '9MDQGD3UD5H2UNK', 'Rider'),
# ('', '6UHNHO8GILJOOR2', 'Rider'),
# ('', '9DB21I7CR34643K', 'Rider'),
# ('', 'RP6A1SE3M1LBO80', 'Rider'),
# ('', 'B95O7R22F7TEG8M', 'Rider'),
# ('', 'VFFTY5IIWNYPWR2', 'Rider'),
# ('', 'YLX0UJW4FAP0MHT', 'Rider'),
# ('', 'Y2ST48IWB43OE3T', 'Rider'),
# ('', 'ZM0BQ9HEU6SELPG', 'Rider'),
# ('', 'T9T3A2DGOHCGB3C', 'Rider'),
# ('', 'YPPWFKOH3DWA6UT', 'Rider'),
# ('', 'J76BR3A2LOAT1O8', 'Rider'),
# ('', 'UUM3KAYLF0XIUHK', 'Rider'),
# ('', 'RGFT3MJQXG8T2B1', 'Rider'),
# ('', 'CUHASHMKWLRDJ7N', 'Rider'),
# ('', 'IYRQBO4GRKAJ9WJ', 'Rider'),
# ('', '73SGWWQCL2WQUWZ', 'Rider'),
# ('', 'T6IGHRATNJZL5HV', 'Rider'),
# ('', '2SSY921BDZE5CIX', 'Rider'),
# ('', 'KSMPQFMHFDWXL5C', 'Rider'),
# ('', 'UZQ50CK5T1DGJKW', 'Rider'),
# ('', '5DZNVMRKBD6R9RB', 'Rider'),
# ('', 'GLS5YXLQ550FDFI', 'Rider'),
# ('', '26SX784DNJ72ZDZ', 'Rider'),
# ('', 'MR9II8YV4OUZGW3', 'Rider'),
# ('', 'HPL71VRLHTULT6G', 'Rider'),
# ('', 'L3R9S8K6MNU08XT', 'Rider'),
# ('', 'YP41Q7J1KOCP462', 'Rider'),
# ('', '3JFSMLBOU9S7KKO', 'Rider'),
# ('', '8FV745LYVLX5TXE', 'Rider'),
# ('', '6NAKBP4JZL9JX3Y', 'Rider'),
# ('', '10Y0Z93OQ1WTRAC', 'Rider'),
# ('', '08UDEYN5QIL2WKT', 'Rider'),
# ('', '9UXTLUHHIRYKSNR', 'Rider'),
# ('', 'XYND8BQWBN1WGCJ', 'Rider'),
# ('', '71ENJV20KIFHARX', 'Rider'),
# ('', 'ET5ZRE119ZQEGWO', 'Rider'),
# ('', 'BD72UODBIEB33OH', 'Rider'),
# ('', 'SHK43WQV4OM9GS9', 'Rider'),
# ('', '7ULUCNBV89Y9GCK', 'Rider'),
# ('', 'N6IP88M0NRP6ZZQ', 'Rider')]

# mycursor.executemany(sql, vals)
# mydb.commit()
# print(mycursor.rowcount, "rows were inserted")

# ----------------------------------------------------------- #

# Test Queries
# mycursor.execute("SELECT * FROM Driver")
# mycursor.execute("SELECT driverMode FROM Driver WHERE name LIKE 'Jacob Stokes'")
# mycursor.execute("SELECT * FROM Rider")
# mycursor.execute("SELECT riderID FROM Rider WHERE name LIKE 'Lewis%'")
# mycursor.execute("SELECT * FROM Vehicle")
# mycursor.execute("SELECT * FROM Vehicle WHERE make LIKE 'Honda'")
# mycursor.execute("SELECT name, driverID FROM Driver")
# mycursor.execute("SELECT d.name, d.driverMode FROM Vehicle v INNER JOIN Driver d ON v.vehicleID = d.vehicleID WHERE v.make = 'Honda' HAVING d.driverMode = '1'")
# mycursor.execute("SELECT d.name FROM DriverOrRider dr INNER JOIN Driver d ON dr.driverID = d.driverID WHERE dr.driverID = '3cQP3m3dceEnieV'")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# ----------------------------------------------------------- #

# Interactive App
# Converts tuple into string
def convert_string_tuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str

# Converts tuple into string
def convert_int_tuple(tup):
    res = ''
    for i in tup:
        res += str(i)
    res = int(res)
    return res

# Converts float to tuple
def convert_float_tuple(tup):
    res = float('.'.join(str(float) for float in tup))
    return res

# Generates random string for rideID
def generate_string():
    res = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
    return res

# Function checks for user input given a list of choices
@staticmethod
def get_choice(lst):
    choice = input("Enter choice number: ")
    while choice.isdigit() == False:
        print("Incorrect option. Try again")
        choice = input("Enter choice number: ")

    while int(choice) not in lst:
        print("Incorrect option. Try again")
        choice = input("Enter choice number: ")
    return int(choice)

# Prints all attributes from Vehicle Table
def get_driver_details(driverID):
    mycursor.execute("SELECT name FROM Driver WHERE driverID = '"+driverID+"'")
    result = mycursor.fetchone()
    name = convert_string_tuple(result)
    mycursor.execute("SELECT vehicleID FROM Driver WHERE driverID = '"+driverID+"'")
    result = mycursor.fetchone()
    vID = convert_string_tuple(result)
    mycursor.execute("SELECT make FROM Vehicle WHERE vehicleID = '"+vID+"'")
    result = mycursor.fetchone()
    make = convert_string_tuple(result)
    mycursor.execute("SELECT model FROM Vehicle WHERE vehicleID = '"+vID+"'")
    result = mycursor.fetchone()
    model = convert_string_tuple(result)
    mycursor.execute("SELECT color FROM Vehicle WHERE vehicleID = '"+vID+"'")
    result = mycursor.fetchone()
    color = convert_string_tuple(result)
    mycursor.execute("SELECT licensePlate FROM Vehicle WHERE vehicleID = '"+vID+"'")
    result = mycursor.fetchone()
    lplate = convert_string_tuple(result)

    str = "[NAME: "+name+"]\n[MAKE :"+make+"]\n[MODEL: "+model+"]\n[COLOR: "+color+"]\n[LICENSE PLATE: "+lplate+"]"
    print("\n*--------------------*")
    print("\n[RIDE DETAILS]")
    print(str)

# Print all options for user and return their choice
def menu_options():
    print("*--------------------*")
    print('''
    [1 LOGIN]\n
    [2 EXIT]
    ''')
    print("*--------------------*")
    return get_choice([1, 2])

# Print all options for driver and return their choice
def driver_options():
    print("*--------------------*")
    print('''
    [1 SWITCH DRIVER MODE]\n
    [2 SEE RATING]\n
    [3 EXIT]
    ''')
    print("*--------------------*")
    return get_choice([1, 2, 3])

# Print all options for rider and return their choice
def rider_options():
    print("*--------------------*")
    print('''
    [1 FIND DRIVER]\n
    [2 RATE RIDE]\n
    [3 EXIT]
    ''')
    print("*--------------------*")
    return get_choice([1, 2, 3])

# Print all options for rating and return their choice
def rating_options():
    print("*--------------------*")
    print('''
    [1 5 STARS]\n
    [2 4.5 STARS]\n
    [3 4 STARS]\n
    [4 3.5 STARS]\n
    [5 3 STARS]\n
    [6 2.5 STARS]\n
    [7 2 STARS]\n
    [8 1.5 STARS]\n
    [9 1 STARS]\n
    [10 0.5 STARS]\n
    [11 EXIT]
    ''')
    print("*--------------------*")
    return get_choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

# Rate interface allows user 
def rate(name):

    print("\n*--------------------*")
    rID = input("Enter your user ID: ")
    print("How was your ride?")

    match rating_options():
        case 1:
            rating = 5.00
        case 2:
            rating = 4.50
        case 3:
            rating = 4.00
        case 4:
            rating = 3.50
        case 5:
            rating = 3.00
        case 6:
            rating = 2.50
        case 7:
            rating = 2.00
        case 8:
            rating = 1.50
        case 9:
            rating = 1.00
        case 10:
            rating = 0.50
        case 11: 
            print("")

    mycursor.execute("SELECT driverID FROM Ride WHERE riderID = '"+rID+"' ORDER BY rideID DESC LIMIT 1")
    myresult = mycursor.fetchone()
    dID = convert_string_tuple(myresult)

    mycursor.execute("UPDATE Ride SET rating = "+str(rating)+" WHERE riderID = '"+rID+"' AND driverID = '"+dID+"' ORDER BY rideID DESC LIMIT 1")
    mydb.commit()

    mycursor.execute("SELECT rating FROM Driver WHERE driverID = '"+dID+"'")
    result = mycursor.fetchone()
    dRating = convert_float_tuple(result)

    dRating = (dRating + rating) / 2

    mycursor.execute("UPDATE Driver SET rating = "+str(dRating)+" WHERE driverID = '"+dID+"'")
    mydb.commit()

# Rider Interface allows rider to get ride and rate driver
def rider(name):
    print("\n*--------------------*")
    print("Welcome, "+name)

    mycursor.execute("SELECT riderID from rider WHERE name = '"+name+"'")
    myresult = mycursor.fetchone()
    rID = convert_string_tuple(myresult)

    match rider_options():
        case 1:
            mycursor.execute("Select driverID FROM Driver WHERE driverMode = 1 ORDER BY RAND() LIMIT 1")
            myresult = mycursor.fetchone()
            dID = convert_string_tuple(myresult)
            pickup = input("\nEnter pick up location: ")
            dropoff = input("\nEnter drop off location: ")
            mycursor.execute("INSERT INTO Ride (riderID, driverID, pickUp, dropOff, rating) VALUES (('"+rID+"'), ('"+dID+"'), ('"+pickup+"'), ('"+dropoff+"'), ('0.00'))")
            mydb.commit()
            mycursor.execute("SELECT rideID FROM Ride WHERE driverID = '"+dID+"' AND riderID = '"+rID+"' ORDER BY rideID DESC LIMIT 1")
            result = mycursor.fetchone()
            rideID = convert_int_tuple(result)
            get_driver_details(dID)
            print("[RIDE ID: "+str(rideID)+"]")
            rider(name)
        case 2:
            rate(name)
            rider(name)
        case 3:
            print("\nThank you for choosing RideShare!\n")

# Driver interface allows for setting driver mode and seeing rating
def driver(name):
    mydb.commit()
    print("\n*--------------------*")
    print("Welcome, "+name)
    mycursor.execute("Select driverMode FROM Driver WHERE name = '"+name+"'")
    myresult = mycursor.fetchone()
    mode = convert_int_tuple(myresult)
    print("[CURRENT MODE: "+str(mode)+"]")

    match driver_options():
        case 1:
            mycursor.execute("UPDATE Driver SET driverMODE = CASE WHEN driverMode = 1 THEN 0 WHEN DriverMode = 0 THEN 1 END WHERE name = '"+name+"'")
            mycursor.execute("Select driverMode FROM Driver WHERE name = '"+name+"'")
            myresult = mycursor.fetchone()
            mode = convert_int_tuple(myresult)
            print("\n[DRIVE MODE SWITCHED]")
            driver(name)
        case 2:
            mycursor.execute("Select rating FROM Driver WHERE name = '"+name+"'")
            myresult = mycursor.fetchone()
            rate = convert_float_tuple(myresult)
            print("\n[RATING: "+str(rate)+"]")
            driver(name)
        case 3:
            print("\nThank you for choosing RideShare!\n")


# Takes in user ID and decides if driver or rider
def choose_role():
    while True:
        try:
            userID = input("\nEnter your user ID: ")
            mycursor.execute("SELECT name FROM DriverOrRider WHERE driverID = '"+userID+"' OR riderID = '"+userID+"'")
            myresult = mycursor.fetchone()
            whichUser = convert_string_tuple(myresult)
            break
        except TypeError:
            print("Invalid input...")

    match whichUser:
        case 'Driver':
            mycursor.execute("SELECT name FROM Driver WHERE driverID = '"+userID+"'")
            result = mycursor.fetchone()
            userName = convert_string_tuple(result)
            driver(userName)
        case 'Rider':
            mycursor.execute("SELECT name FROM Rider WHERE riderID = '"+userID+"'")
            result = mycursor.fetchone()
            userName = convert_string_tuple(result)
            rider(userName)

# Introduce to RideShare
print("*--------------------*")
print("Welcome to RideShare!")

while True:
    match menu_options():
        case 1: 
            choose_role()
            break
        case 2:
            print("\nThank you for choosing RideShare!\n")
            break

# ----------------------------------------------------------- #

# Close Connection
mydb.close()
