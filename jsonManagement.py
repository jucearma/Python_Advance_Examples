# importar librería json
import json
# ¿Qué es un json?

# creamos un json

jsonPerson= {'name':'jose', 'apellidos':'escribano', 'age':28, 'city':'Madrid'}

#Pass Dictionary into JSON
jsonPersonString= json.dumps(jsonPerson, indent=4)
# Tomamos el String y lo formateamos a un array de bytes
jsonPersonConver= json.loads(jsonPersonString)

print(jsonPersonConver['name'][0:2]+ " "+ jsonPersonConver['apellidos'])