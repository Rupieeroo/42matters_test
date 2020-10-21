import psycopg2

t_host = 'postgresql+psycopg2://user:pass@localhost:5432/apps'
t_port = "5432"
t_dbname = "apps"
t_user = "user"
t_pw = "pass"
db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
db_cursor = db_conn.cursor()

@app.route("/export")
def csv_export():
    s = "'"
    s += "SELECT *"
    s += " FROM "
    s += "apps"
    s += "'"

    # Set up database connection.
    conn = psycopg2.connect...
    db_cursor = conn.cursor()

    # Use the COPY function on the SQL we created above.
    SQL_for_file_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(s)

    # Set up a variable to store our file path and name.
    t_path_n_file = "./data/apps.csv"

    # Trap errors for opening the file
    try:
    WITH Open(t_path_n_file, 'w') as f_output:
        db_cursor.copy_expert(SQL_for_file_output, f_output)
    except psycopg2.Error as e:
        t_message = "Error: " + e + "/n query we ran: " + s + "/n t_path_n_file: " + t_path_n_file
        return render_template("error.html", t_message = t_message)

    # Clean up: Close the database cursor and connection
    db_cursor.close()
    db_conn.close()

    print(f'Successfully packed {t_dbname} table to csv')

    # Not sure about this. Need to look into if this would work
    pd.read_csv("apps.csv",compression='gzip')

if __name__ == "__main__":
    csv_export()
