# MYSQL Uber Lab

## Idendifying Information
* Name: Marco Mauricio
* StudentID: 2344979
* Email: mauricio@chapman.edu
* Course: CPSC 408
* Assignment: MYSQL Uber Lab

Suppose that a new start-up is trying to create a rideshare app and hires you to design their database. Think about the main information that the app must keep track of and create some deliverables to show your client as you go. You must create (1) an ER diagram (2) a fully filled out schema (3) create the database on MySQL locally (4) add some data to test it (5) create a simple interactive python program.

## Interactive Part ##
* The user should be able to give their ID and you will determine whether they are a driver or a user (cannot be both for simplicity)

* If they are a driver, you should give them the following options:
    * turn drive mode on: updates a flag on their file that they are able to drive

* if they are a rider, you should give them the following options:
    * find a driver: matches them with a driver that has their drive mode on activated
        * the rider will provide the following info:
            * pick up location
            * drop off location
        * and you will provide the rider with a ride ID 
        * then it will go back to main menu
    * rate my driver:
        * the rider will provide their own ID and desired rating
            * You should look up the rider’s last ride and get the driver’s ID Then, calculate the driver’s new rating by taking their current rating + their new rating and dividing by 2.

## Source Files
* uber_lab.py

## Interface Queries
* "SELECT name FROM Driver WHERE driverID = '"+driverID+"'"
* "SELECT vehicleID FROM Driver WHERE driverID = '"+driverID+"'"
* "SELECT make FROM Vehicle WHERE vehicleID = '"+vID+"'"
* "SELECT model FROM Vehicle WHERE vehicleID = '"+vID+"'"
* "SELECT color FROM Vehicle WHERE vehicleID = '"+vID+"'"
* "SELECT licensePlate FROM Vehicle WHERE vehicleID = '"+vID+"'"
* "SELECT driverID FROM Ride WHERE riderID = '"+rID+"' ORDER BY rideID DESC LIMIT 1"
* "UPDATE Ride SET rating = "+str(rating)+" WHERE riderID = '"+rID+"' AND driverID = '"+dID+"' ORDER BY rideID DESC LIMIT 1"
* "SELECT rating FROM Driver WHERE driverID = '"+dID+"'"
* "UPDATE Driver SET rating = "+str(dRating)+" WHERE driverID = '"+dID+"'"
* "SELECT riderID from rider WHERE name = '"+name+"'"
* "Select driverID FROM Driver WHERE driverMode = 1 ORDER BY RAND() LIMIT 1"
* "SELECT rideID FROM Ride WHERE driverID = '"+dID+"' AND riderID = '"+rID+"' ORDER BY rideID DESC LIMIT 1"
* "Select driverMode FROM Driver WHERE name = '"+name+"'"
* "UPDATE Driver SET driverMODE = CASE WHEN driverMode = 1 THEN 0 WHEN DriverMode = 0 THEN 1 END WHERE name = '"+name+"'"
* "Select driverMode FROM Driver WHERE name = '"+name+"'"
* "Select rating FROM Driver WHERE name = '"+name+"'"
* "SELECT name FROM DriverOrRider WHERE driverID = '"+userID+"' OR riderID = '"+userID+"'"
* "SELECT name FROM Driver WHERE driverID = '"+userID+"'"
* "SELECT name FROM Rider WHERE riderID = '"+userID+"'"

## References
* https://www.w3schools.com/sql/func_mysql_case.asp - CASE function
* https://dev.mysql.com/doc/refman/8.0/en/example-auto-increment.html - AUTO INCREMENT field
* https://www.geeksforgeeks.org/python-convert-tuple-to-float-value/ - convert tuple to float
* https://www.geeksforgeeks.org/python-convert-tuple-to-integer/ - convert tuple to int
* https://www.geeksforgeeks.org/python-program-to-convert-a-tuple-to-a-string/ - convert tuple to string
* https://www.mysqltutorial.org/select-random-records-database-table.aspx - RAND() function

## Known Errors
* NA

## Execution Instructions
* TO CREATE DATABASE
    * Uncomment all commented code and run the following command
        * Once all tables are created and data is added, the code can be re-commented
* <code> python3 uber_lab.py </code>