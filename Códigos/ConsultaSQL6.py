import cx_Oracle as orcCon
from cx_Oracle import DatabaseError

conn = orcCon.connect('"david2"/123bdd@localhost')
cursor = conn.cursor()
# Execute query
sql = """select count(mis."var_id_mis") as NUMERO_MISILES, sum(tec."nbr_horas_experiencia") as TOTAL, avg(tec."nbr_horas_experiencia") as PROMEDIO from tb_personal pers
inner join tb_tecnico tec on pers."var_id_per" = tec."var_id_per"
inner join tb_ensamblar ens on pers."var_id_per" = ens."var_id_per"
inner join tb_misil mis on mis."var_id_mis" = ens."var_id_mis"
where mis."var_nombre_mis" like '%A' or mis."var_nombre_mis" like '%C'
"""
cursor.execute(sql)

# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)

cursor.close()
conn.close()