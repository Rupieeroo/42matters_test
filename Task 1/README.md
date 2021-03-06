# 42 Matters Test - 1
Here is my solution to task 1 of the 42 Matters test.

1.) Python script which allows us to generate the random source data and push it to a Postgres database.
2.) Python or shell script that allows to dump the data from Postgresql to a gzipped CSV file.
3.) Python script for uploading the gzipped CSV to Amazon S3.

## Structure
The steps are split into the three python files: 

1.) 'data_gen.py' generates a random amount of data and inputs it to a dataframe.
2.) 'table_packaging.py' packages the dataframe into a csv and gzips it.
3.) 's3_upload.py' takes the table and uploads it to an s3 bucket.

A Dockerfile is used to create an isolated environment and run the commands in sequence. The end result of running the Dockerfile will be to upload the gzipped csv file to an Amazon s3 bucket.

### Data generation
'data_gen.py' generates a number of lists with different randomized data. I set the range from 1 to 6 (not quite the 5 million that was requested!) but this can easily be changed. After it generates a list for each column, they are added to a dictionary that can generate into a dataframe and finally a PostgresSQL table.

### Table packing and compressing
'table_packaging.py' sets up a connection to the database and queries it, selecting the rows and pushing them into a csv file before gzipping it.

### Uploading to s3
's3_upload.py' takes environmental variables for the AWS account and uses them to upload the gzipped csv file into an s3 bucket.

## Current Situation
Currently there is a bug in the 'data_gen.py' file:
```
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not connect to server: Connection refused
        Is the server running on host "localhost" (127.0.0.1) and accepting
        TCP/IP connections on port 5432?
could not connect to server: Cannot assign requested address
        Is the server running on host "localhost" (::1) and accepting
        TCP/IP connections on port 5432?
```

From what I gather this is due to an error in the 'create_engine('postgresql+psycopg2://user:pass@localhost:5432/apps')' line.
I havent been able to isolate the issue yet as from what I have read I am using the right syntax. I imagine it is due to how the port mapping works with create_engine as the bug is the same in my local environmetn and the container.

I also believe that the line: 'pd.read_csv("apps.csv",compression='gzip')' possibly is not the correct way of gzipping the file and would like to look into what would wirk with my current set-up.

## Development journey
Unfortunately I didn't have as much time as I had hoped to put into this and so didn't get to fix the bug and move towards pushing to Redshift. All in all I enjoyed designing and working on the data generator and if I had given myself more time and I could have solved the immediate issues. I would have liked to have refactored the different files to make it faster and more streamlined.
