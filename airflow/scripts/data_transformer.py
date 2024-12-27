import psycopg2

def data_transformer(file_path):
    try:
        # Postgres Connection
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="database",
            user="postgres",
            password="secret"
        )
        # Insert Query
        cur = conn.cursor()
        try:
            # Read the SQL file
            with open(file_path, 'r') as file:
                sql_script = file.read()

            # Execute the SQL script
            for statement in sql_script.split(';'):
                statement = statement.strip()
                if statement:  # Ensure non-empty statements
                    cur.execute(statement)
            conn.commit()
            print(f"Successfully executed the SQL script: {file_path}")
        except Exception as e:
            print(f"Failed to execute SQL script: {e}")
        finally:
            cur.close()
            conn.close()
    except Exception as e:
        print(f"connection error:{e}")


