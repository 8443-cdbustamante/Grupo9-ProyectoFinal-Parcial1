import cx_Oracle as orcCon
from cx_Oracle import DatabaseError

conn = orcCon.connect('"david2"/123bdd@localhost')
cursor = conn.cursor()
# Execute query
sql = """
select comp."var_id_com", comp."var_nombre_com", pz."var_nombre_pieza", itg."nbr_cantidad_necesaria" from tb_integrar itg
inner join tb_componente comp on comp."var_id_com" = itg."var_id_com"
inner join tb_pieza pz on pz."var_id_pieza" = itg."var_id_pieza"
where pz."var_nombre_pieza" like 'Sensor-C' 
group by comp."var_nombre_com"
"""
cursor.execute(sql)

# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)

cursor.close()
conn.close()