import cx_Oracle as orcCon
from cx_Oracle import DatabaseError

conn = orcCon.connect('"david2"/123bdd@localhost')
cursor = conn.cursor()
# Execute query

sql = """select perm."var_entidad_perm" from tb_configurar conf
inner join tb_permiso perm on perm."var_id_perm" = conf."var_id_perm"
inner join tb_rol rl on rl."var_id_rol" = conf."var_id_rol"
where "var_status_rol" = 'Inactivo'
group by perm."var_entidad_perm"
having count(perm."var_entidad_perm")>50
"""
cursor.execute(sql)

# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)

cursor.close()
conn.close()