import cx_Oracle as orcCon
from cx_Oracle import DatabaseError

conn = orcCon.connect('"david2"/123bdd@localhost')
cursor = conn.cursor()
# Execute query
sql = """select mis."var_nombre_mis" as MISIL, prov."var_tipo_pro" as TIPO_PROVEEDOR, count(*) as CANTIDAD from tb_abastecer abas
inner join tb_proveedor prov on prov."var_id_pro" = abas."var_id_pro"
inner join tb_pieza pz on pz."var_id_pieza" = abas."var_id_pieza"
inner join tb_integrar itg on pz."var_id_pieza" = itg."var_id_pieza"
inner join tb_componente comp on comp."var_id_com" = itg."var_id_com"
inner join tb_ensamblar ens on comp."var_id_com" = ens."var_id_com"
inner join tb_misil mis on mis."var_id_mis" = ens."var_id_mis"
group by mis."var_nombre_mis", prov."var_tipo_pro"
"""
cursor.execute(sql)

# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)

cursor.close()
conn.close()