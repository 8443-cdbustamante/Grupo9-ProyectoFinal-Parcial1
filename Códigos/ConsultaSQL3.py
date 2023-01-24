import cx_Oracle as orcCon
from cx_Oracle import DatabaseError

conn = orcCon.connect('"david2"/123bdd@localhost')
cursor = conn.cursor()
# Execute query
sql = """select mis."var_tipo_mis", pr."var_decreto_par", count(pr."var_decreto_par") from tb_cumplir cump
inner join tb_misil mis on mis."var_id_mis" = cump."var_id_mis"
inner join tb_parametro pr on pr."var_id_par" = cump."var_id_par"
where pr."var_status_par" like 'Activo'
group by mis."var_tipo_mis", pr."var_decreto_par"
"""
cursor.execute(sql)

# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)

cursor.close()
conn.close()