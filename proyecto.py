import csv
import pagina as pg
#import pagina as pag , lo comento por que por ahora no se usa


#toma lista de ciudade y las devuelve en libreria id=ciudad dato= cantidad de apariciones
def mas_apariciones(ciudad, dato_ciudades = None):
    if dato_ciudades is None:
        dato_ciudades = {}
    if ciudad in dato_ciudades:   #aca pregunta si ciudad ya esta en dato_ciudades
        dato_ciudades[ciudad] += 1 #en caso que este agrega uno al dato asignado a "ciudad"
    else:
        dato_ciudades[ciudad] = 1  #en caso de no estar crea la clave con el calor de ciudad y le asigna 1(por que aparecio por primera vez)
    return(dato_ciudades)


#mas_apariciones(lista_excel(VALOR QUE DADO DEL EXCEL))


    


def fun_preguntas():
    with open("global_urban_smog_pm25_hourly_12k.csv") as archivo_csv:
        reader = csv.reader(archivo_csv)
        reader.__next__() # Saltea la primera linea, la de los titulos.
        pregunta1 = {}
        for registro in reader :
            pregunta1= mas_apariciones(registro[1], pregunta1) 
            pregunta2 = None
            #pregunta3
            #pregunta4
            #pregunta5
            #pregunta6
        return((pregunta1,pregunta2))



def main():
     pg.pregunta1(fun_preguntas())              #llama pregunta1 de pagina con el valor que devuelve fun_pregunta de proyecto.py, que devuelve un dic con ciudad:aparicion


if __name__=="__main__":
    main()


    



   

    

