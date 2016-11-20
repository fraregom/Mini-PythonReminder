## Tarea 4 - Lenguajes de programación - Python

  * **Integrantes:** Diego Zamora G.( dzamora 201473076-4) - Francisco Reyes G. (freyes 201473117-5)
    **Aclaraciones:** Utilizamos una pequeña base de datos llamada metadata, en ella se encuentra la informacion importante de cada nota, para ser menos invasivos en el computador nuestras notas poseen el formato .lpy
    **¿Como aplicar estilos en un archivo?:**
        Para ello utilizamos un lenguaje similar a html, a continuación les nombrare los estilos existentes.
        **1.- Colores:** El programa admite los colores, rojo, amarillo, azul, magenta y verde. para aplicar uno realice lo siguiente:
                         primero llamelo de esta manera, < rojo >, escriba su texto y cierre cada bloque de color con </ color >, para mayor
                          información revise el archivo auxiliar.py, donde estaran escritos dichos colores.
        **2.- Especiales:** Para utilizar el subrayado, debe realizarlo de igual forma similiar a los colores, debe llamarlo usando
                            < subrayado > texto </ subrayado>, lo anterior de igual manera puede utilizar las negritas (< negrita >) y cursiva
                            (< cursiva >). 
        (nota: Markdown no permite escribir correctamente html, no existe espacio entre las barras y el color o especial)
  * **Comentarios:**
      * **Create:** Los nombres de los archivos a crear deben estar entre comillas para que se inicie la aplicación, al igual que los tags. eg: create "texto1" "texto2" with tags "tag1" "tag2" [in \home\etc..]
      * **Delete:** Si se desea borrar un solo archivo o con algún detalle en espeficio, debe indicarlo con comillas. 
                    eg: delete all where name contains "texto" [in \home\etc..]
      * **Show:** eg: show all where name contains "text1" [sorted by tags] [in \home\etc...]
      * **Dir:** Aceptara unicamente rutas validas (locales o absolutas), y indicara si se a efectuado un cambio
                   eg: dir \home\etc..
      * **Edit:** Permite editar un texto usando edit, tomamos como supuesto que el usuario no cambiara el nombre la nota, pues ello conllevaria a errores en nuestra base de datos. eg: edit "texto" [in \home\etc..]
      * **Find:**  Las palabras ingresadas deben estar compuestas de unicamente letras (Con mayúsculas incluidas)
                  eg: find some "algo1" "algo2" [in \home\etc..]