UFC ALONG THE YEARS: Un análisis de nacionalidades y desempeño a lo largo del tiempo

INTRODUCCIÓN

Este proyecto analiza cómo han evolucionado las nacionalidades de los peleadores en la UFC desde sus inicios hasta la actualidad. La UFC, como principal promotora mundial de artes marciales mixtas (MMA), ha ido transformando su roster a lo largo de las décadas, incorporando talentos de diversas partes del mundo. El objetivo es entender qué países han tenido mayor representación, cómo ha cambiado esa representación con el tiempo y qué patrones emergen en la actividad y longevidad de los peleadores.

DATOS UTILIZADOS

1.UFC Stats (ufcstats.com)(http://ufcstats.com/statistics/fighters) -Web oficial de estadísticas de UFC. -Se utilizó web scraping para obtener datos de los peleadores: nombre, edad, altura, peso, récord, etc. -Esta fuente no proporciona la nacionalidad, por lo que fue complementada con otras.

2.Kaggle: Pro MMA Fighters Dataset(https://www.kaggle.com/datasets/binduvr/pro-mma-fighters) -Dataset con más de 5.000 peleadores profesionales de MMA. -Se filtraron por nombre aquellos que han participado en UFC y se extrajo su nacionalidad. -Incluye nacionalidad, edad y otros atributos físicos. -Algunas nacionalidades están mal categorizadas o son inconsistentes.

3.Otras herramientas o fuentes -Tapology y Sherdog: Verificación de nacionalidades y fechas de última pelea. -Wikipedia: Fuente secundaria para contraste de tendencias generales. -Chat GPT: Asistencia puntual para automatizar la búsqueda de fechas de última pelea.

PREGUNTAS QUE QUEREMOS RESOLVER

1.¿Cómo ha evolucionado la representación de la nacionalidad en la UFC? -Se contabilizó el número de peleadores por país a lo largo de los años. -CONCLUSIÓN - Aunque Estados Unidos ha sido dominante históricamente, la representación internacional ha crecido de manera sostenida, especialmente desde 2010.

2.¿Qué países tienen actualmente más peleadores activos? -Se consideran activos los peleadores cuya última pelea fue después del 2023 -CONCLUSION - Algunos países muestran crecimiento reciente en número de atletas activos, destacando la expansión internacional de la organización.

3.¿Cuál es la edad media de retiro según la época? -Se estimó a partir de la edad actual de los peleadores cuya última pelea registrada fue hace varios años. -CONCLUSIÓN de la edad media de retiro
-Años 90: 30 años -2000s: 33 años
-2010s: 35 años
-Proyección futura: entre 38 y 40 años, gracias a mejores condiciones físicas, tecnológicas y médicas.

METODOLOGIA

1.Scraping y recopilación de datos: -Extracción de peleadores desde ufcstats.com con sus datos físicos y récords. -Complementación de nacionalidad usando el dataset de Kaggle. 2.Creación de CSV personalizado: -Se generó un archivo con los nombres de los peleadores. -Con ayuda de ChatGPT, se completaron las fechas de última pelea para cada uno. 3.Cálculo de métricas: -Se estimó la edad de retiro basándose en la edad actual y la fecha de última pelea. 4.Clasificación: -Todos los análisis se realizaron por país, no por continentes, para un enfoque más específico. 5.Visualización: -Se utilizaron gráficos de barras Y pie charts para mostrar la evolución y distribución de los datos.

CONCLUSIONES

-La UFC ha diversificado su roster de forma progresiva en las últimas décadas. -La edad de retiro ha ido aumentando, con proyecciones de longevidad deportiva más altas para las generaciones actuales. -Más tradición = más peleadores, no siempre mejor rendimiento. -Ser de un país fuerte en MMA no te asegura el éxito. -Rusia está creciendo en número y consistencia. -Vivir en EE.UU. ofrece más oportunidades: visibilidad, acceso a managers y eventos. -Sacar a EE.UU. del análisis revela patrones ocultos de crecimiento en otros países. -La UFC se expande y el mapa del MMA cambia rápido.

COSAS A MEJORAR/IMPLEMETAR EN EL FUTURO

-Actualizar el dataset incorporando peleadores debutantes después de 2021.
-Análisis por género para incluir representación femenina.
-Incluir el estilo de lucha (wrestling, muay thai, BJJ, etc.).
-Añadir el año del debut para estudiar carreras deportivas completas.
-Incorporar los campeones de cinturón por país para vincular representación con éxito deportivo.

ENLACES UTILES

-UFC Stats (ufcstats.com) (http://ufcstats.com/statistics/fighters)
-Kaggle Dataset: Pro MMA Fighters (https://www.kaggle.com/datasets/binduvr/pro-mma-fighters)
-Prezi del Proyecto (https://prezi.com/view/Rb3SDBNa3pKXSDg231Id/)