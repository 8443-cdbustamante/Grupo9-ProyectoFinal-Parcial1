import pandas as pd
import cx_Oracle as orcCon
from cx_Oracle import DatabaseError

Data = pd.read_csv('dataset_proveedor.csv', sep=",", header=0,index_col=0)

try:
    #orcCon.connect('username/password@localhost')
    conn = orcCon.connect('"david2"/123bdd@localhost')
    if conn:
        print("cx_Oracle version:", orcCon.version)
        print("Database version:", conn.version)
        print("Client version:", orcCon.clientversion())
        cursor = conn.cursor()
        print("You're connected: ")
        print('Inserting data into table....')
        for i,row in Data.iterrows():
            sql = 'INSERT INTO tb_proveedor("var_id_pro","var_nombre_pro","var_tipo_pro","var_email_pro","var_telefono_pro","var_descripcion_pro","var_status_pro") VALUES(:1,:2,:3,:4,:5,:6,:7)'
            cursor.execute(sql, tuple(row))

        # the connection is not autocommitted by default, so we must commit to save our changes
        conn.commit()
        print("Record inserted succesfully")

except DatabaseError as e:
    err, = e.args
    print("Oracle-Error-Code:", err.code)
    print("Oracle-Error-Message:", err.message)

finally:
    cursor.close()
    conn.close()