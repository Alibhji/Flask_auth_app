# Flask_auth_app

TO Run the code:

You shoudl add the <br>
$ export FLASK_APP=project<br>
$ export FLASK_DEBUG=1<br>
$ export PYTHONPATH="${PYTHONPATH}:/home/pi/" # it should be location of your  package <br>

Then you can run it by following command:
flask run --host="192.168.1.12" # it is the server ip you want to run on it <br>


#Create a database in SQL:<br>



mysql --user=root -p <br>
--> type your password <br>

"Create a database:" <br>
"CREATE DATABASE "mydatabase""<br>
"USE mydatabase"

"Create a tables:" <br>
"CREATE TABLE users (uid INT AUTO_INCREMENT PRIMARY KEY , username VARCHAR(50) , psssword VARCHAR(100) , email VARCHAR(100))"


