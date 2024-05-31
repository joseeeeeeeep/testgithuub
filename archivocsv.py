import csv
with open('archivocsv.csv','w', newline='') as archivo:
    escritor= csv.writer(archivo)
    escritor.writerow(['Nombre','Edad','Comuna'])
    escritor.writerows([
        ['Esteban',25,'Santiago'],
        ['María',30,'Valparaíso'],
        ['Carlos',17,'Osorno'],
        ['Sigrid',25,'Santiago'],
        ['Daniela',30,'La Cisterna'],
        ['Aylen',10,'La Florida']
        ])
with open('archivocsv.csv','r', newline='') as archivo:
    lector=csv.reader(archivo)
    for fila in lector:
        print(fila)

#OJO  aca chicos
with open('archivocsv.csv','r') as archivo:
    lector=csv.DictReader(archivo)
    for fila in lector:
        nombre=fila['Nombre']
        edad=int(fila['Edad'])
        comuna=fila['Comuna']
        estado_edad= "Mayor de edad "if edad>=18 else "Menor edad"
        print(f"{nombre} tiene {edad} años, es {estado_edad} y vive en {comuna}")