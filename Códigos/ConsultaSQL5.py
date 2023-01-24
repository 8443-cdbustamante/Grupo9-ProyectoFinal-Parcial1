import cx_Oracle as orcCon
from cx_Oracle import DatabaseError

conn = orcCon.connect('"david2"/123bdd@localhost')
cursor = conn.cursor()
# Execute query
sql = """select ing."var_especialidad_ing"  as ESPECIALIDAD, count(mis."var_id_mis") AS NUMERO from tb_personal pers
inner join tb_ingeniero ing on pers."var_id_per" = ing."var_id_per"
inner join tb_ensamblar ens on pers."var_id_per" = ens."var_id_per"
inner join tb_misil mis on mis."var_id_mis" = ens."var_id_mis"
where mis."var_status_mis" like 'Listo' AND pers."var_genero_per" like 'female'
group by ing."var_especialidad_ing", mis."var_tipo_mis"
"""
cursor.execute(sql)

# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)

cursor.close()
conn.close()