# creates a test SQLite database
export JOBBOSS_TEST=1
python manage.py migrate --run-syncdb
sqlite3 jobboss_test "insert into Auto_Number (Type, System_Generated, Last_Nbr) values ('SalesOrder', 1, 0);"
sqlite3 jobboss_test "insert into Auto_Number (Type, System_Generated, Last_Nbr) values ('Job', 1, 0);"
