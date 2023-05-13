import psycopg2
from datetime import datetime


def add_gate(type, status):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="gateparking",
            user="postgres",
            password="postgres"
        )
        
        # Create a cursor object
        cur = conn.cursor()
        
        # Execute the SQL query to insert the text into the database
        cur.execute("INSERT INTO gate (gate_type, gate_status) VALUES (%s, %s)", (type, status))
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection objects
        cur.close()
        conn.close()
        
        # Return a success message
        return "Text saved to database successfully"
    
    except (Exception, psycopg2.DatabaseError) as error:
        # If an error occurs, rollback the transaction and return an error message
        conn.rollback()
        return f"Error while saving new gate to database: {error}"

def update_gate_status(id, status):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="gateparking",
            user="postgres",
            password="postgres"
        )
        
        # Create a cursor object
        cur = conn.cursor()
        
        # Execute the SQL query to insert the text into the database
        cur.execute("UPDATE gate SET gate_status = %s WHERE gate_id = %s", (status, id))
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection objects
        cur.close()
        conn.close()
        
        # Return a success message
        return "Text saved to database successfully"
    
    except (Exception, psycopg2.DatabaseError) as error:
        # If an error occurs, rollback the transaction and return an error message
        conn.rollback()
        return f"Error while saving new gate to database: {error}"

# Fungsi untuk etry data mahasiswa masuk ; return id
def add_mhs_masuk(rfid, pelat):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="gateparking",
            user="postgres",
            password="postgres"
        )
        
        # Create a cursor object
        cur = conn.cursor()

        pelat = pelat.replace(" ", "")  # Remove all spaces

        # Execute the SQL query to insert the text into the database
        #cur.execute("INSERT INTO mahasiswa (user_rfid, user_pelat, user_status) VALUES (%s, %s, %s)", (rfid ,pelat, 0))
        
        #new_id = cur.fetchone()[0]
        #print(new_id)

        sql = "INSERT INTO mahasiswa (user_rfid, user_pelat, user_status) VALUES (%s, %s, %s) RETURNING user_id;"

        data = (rfid, pelat, 0)
        cur.execute(sql, data)
        new_id = cur.fetchone()[0]
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection objects
        cur.close()
        conn.close()
        
        
        # Return a success message
        return new_id
    
    except (Exception, psycopg2.DatabaseError) as error:
        # If an error occurs, rollback the transaction and return an error message
        conn.rollback()
        return f"Error while saving new user to database: {error}"

# Fungsi untuk mengubah status mhs setelah keluar (0 = masuk, 1 = keluar, 2 = gagal scan) ; return id
def update_mhs_keluar(rfid, status):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="gateparking",
            user="postgres",
            password="postgres"
        )
        
        # Create a cursor object
        cur = conn.cursor()

        # Execute the SQL query to insert the text into the database
        #cur.execute("INSERT INTO mahasiswa (user_rfid, user_pelat, user_status) VALUES (%s, %s, %s)", (rfid ,pelat, 0))
        
        #new_id = cur.fetchone()[0]
        #print(new_id)
        sql = "UPDATE mahasiswa SET user_status = %s WHERE user_rfid = %s AND user_status = %s RETURNING user_id"
        print(sql)
        data = (status, rfid, 0)
        cur.execute(sql, data)
        userid = cur.fetchone()[0]
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection objects
        cur.close()
        conn.close()
        
        
        # Return a success message
        return userid
    
    except (Exception, psycopg2.DatabaseError) as error:
        # If an error occurs, rollback the transaction and return an error message
        conn.rollback()
        return None

def get_mhs_data_by_rfid(rfid):
    try:
        # establish a connection to the database
        conn = psycopg2.connect(
            host="localhost",
            database="gateparking",
            user="postgres",
            password="postgres"
        )

        # create a cursor object
        cur = conn.cursor()
        
        # execute the SELECT query to retrieve RFID and Plat Nomor data from gateparking table
        cur.execute("SELECT user_id, user_rfid, user_pelat FROM mahasiswa WHERE user_rfid = %s AND user_status = 0", (rfid))
        
        # fetch all the rows from the result set
        rows = cur.fetchall()

        # return the retrieved data
        return rows
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None
        
    finally:
        # close the cursor and connection objects
        cur.close()
        conn.close()

def get_mhs_data_by_id(id):
    try:
        # establish a connection to the database
        conn = psycopg2.connect(
            host="localhost",
            database="gateparking",
            user="postgres",
            password="postgres"
        )

        # create a cursor object
        cur = conn.cursor()
        
        # execute the SELECT query to retrieve RFID and Plat Nomor data from gateparking table
        cur.execute("SELECT user_id, user_rfid, user_pelat FROM mahasiswa WHERE user_id = %s AND user_status = 0", (id))
        
        # fetch all the rows from the result set
        rows = cur.fetchall()

        # return the retrieved data
        return rows
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None
        
    finally:
        # close the cursor and connection objects
        cur.close()
        conn.close()

# Fungsi untuk menambahkan waktu masuk dan bukti masuk
def add_riwayat_masuk(bukti_masuk, id_mhs):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="gateparking",
            user="postgres",
            password="postgres"
        )
        
        # Create a cursor object
        cur = conn.cursor()
        
        now = datetime.now() # Create timestamp

        # Execute the SQL query to insert the text into the database
        cur.execute("INSERT INTO riwayat_parkir (bukti_masuk, waktu_masuk, user_user_id) VALUES (%s, %s, %s)", (bukti_masuk, now, id_mhs))
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection objects
        cur.close()
        conn.close()
        
        # Return a success message
        return "Mhs and Riwayat saved to database successfully"
    
    except (Exception, psycopg2.DatabaseError) as error:
        # If an error occurs, rollback the transaction and return an error message
        conn.rollback()
        return f"Error while saving new riwayat to database: {error}"

# Fungsi untuk menambahkan waktu keluar dan bukti keluar
def update_riwayat_keluar(bukti_keluar, user_id):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="gateparking",
            user="postgres",
            password="postgres"
        )
        
        # Create a cursor object
        cur = conn.cursor()
        
        now = datetime.now() # Create timestamp

        # Execute the SQL query to insert the text into the database
        cur.execute("UPDATE riwayat_parkir SET bukti_keluar = %s, waktu_keluar = %s WHERE user_user_id = %s", (bukti_keluar, now, user_id))
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection objects
        cur.close()
        conn.close()
        
        # Return a success message
        return "Text saved to database successfully"
    
    except (Exception, psycopg2.DatabaseError) as error:
        # If an error occurs, rollback the transaction and return an error message
        conn.rollback()
        return f"Error while saving new riwayat to database: {error}"
        
def get_all_riwayat_parkir():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="gateparking",
            user="postgres",
            password="postgres"
        )
        
        # Create a cursor object
        cur = conn.cursor()

        # Execute the SQL query to insert the text into the database
        cur.execute("SELECT rp.bukti_masuk, rp.waktu_masuk, rp.bukti_keluar, rp.waktu_keluar, m.user_pelat, m.user_rfid, m.user_status FROM riwayat_parkir rp JOIN mahasiswa m ON rp.user_user_id = m.user_id")
        
        # Commit the transaction
        rows = cur.fetchall()
        
        # Close the cursor and connection objects
        cur.close()
        conn.close()
        
        # Return a success message
        return rows
    
    except (Exception, psycopg2.DatabaseError) as error:
        # If an error occurs, rollback the transaction and return an error message
        conn.rollback()
        return f"Error while saving new riwayat to database: {error}"

def get_jml_parkir():
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            database="gateparking",
            user="postgres",
            password="postgres"
        )
        
        # Create a cursor object
        cur = conn.cursor()
        
        now = datetime.now() # Create timestamp

        # Execute the SQL query to insert the text into the database
        cur.execute("SELECT COUNT(*) FROM riwayat_parkir")

        
        result = cur.fetchone()[0]
        
        # Close the cursor and connection objects
        cur.close()
        conn.close()
        
        # Return a success message
        return result
    
    except (Exception, psycopg2.DatabaseError) as error:
        # If an error occurs, rollback the transaction and return an error message
        conn.rollback()
        return f"Error while saving new riwayat to database: {error}"
if __name__ == '__main__':
    #res = add_mhs(12345678901, "D 6280 SAG")]
    #res = update_mhs_keluar("12345678901", 1)
    #res = update_riwayat_keluar("bukti_keluar/1.jpg")
    # rfid = "12345678903"
    # res = get_mhs_data_by_rfid(rfid, "D6280SAG")
    res = get_jml_parkir()
    print(res)