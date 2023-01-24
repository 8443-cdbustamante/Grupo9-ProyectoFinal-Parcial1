import cx_Oracle as orcCon
from cx_Oracle import DatabaseError

conn = orcCon.connect('"david2"/123bdd@localhost')
cursor = conn.cursor()
# Execute query-
sql = """select perm."var_id_perm" as ID_PERMISO, on_date(perm."dt_fecha_caduca_perm") as CADUCA_PERMISO, rl."var_nombre_rol" as NOMBRE_ROL, per."var_nombre_per" as PERSONAL, dp."var_nombre_dept" as DEPARTAMENTO from tb_departamento dp
inner join tb_personal per on dp."var_id_dept" = per."var_id_dept"
inner join tb_ensamblar ens on per."var_id_per" = ens."var_id_per"
inner join tb_rol rl on rl."var_id_rol" = ens."var_id_rol"
inner join tb_configurar conf on rl."var_id_rol" = conf."var_id_rol"
inner join tb_permiso perm on perm."var_id_perm" = conf."var_id_perm"
where rl."var_nombre_rol" like 'Analista'
"""
cursor.execute(sql)

# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)

cursor.close()
conn.close()