<div style="page-break-before: always; break-before: page;"></div>

# Capítulo II: Requirements Development and Software Solution Design

En este capítulo se documenta el levantamiento de requerimientos y el diseño de la solución: el análisis de competidores, las entrevistas y los artefactos de needfinding, la especificación de requerimientos y el diseño estratégico y táctico de Guardian+ con Domain-Driven Design.

## 2.1. Competidores

En esta sección se analizan las soluciones que compiten con Guardian+ en el mercado peruano y se definen las estrategias y tácticas con las que el equipo busca diferenciarse.

### 2.1.1. Análisis competitivo

Se identificaron cuatro competidores con dispositivos y servicios orientados al monitoreo de personas: LifeWatch, SaveFamily Senior, SeniorDomo y MovilTecno 866. A continuación se describe cada uno y se comparan con Guardian+ en el Competitive Analysis Landscape.

#### LifeWatch/LifeWatch 2:
Reloj inteligente que monitorea pulso, presión arterial, oxígeno, ejercicio, temperatura corporal y patrones de sueño. Está más orientado al fitness y bienestar general que al cuidado de personas con necesidades específicas, y no cuentan con funciones de emergencia o conectividad familiar especializada. Precio aproximado: S/.140 soles.

#### SaveFamily Senior: 
Smartwatch completo con detector de caídas, frecuencia cardíaca, podómetro, medición de tensión arterial y recordatorio de medicamentos. Su propuesta está orientada al monitoreo integral, pero carece del concepto de "lazo de cuidado" bidireccional y requiere configuración técnica más compleja. Precio aproximado: S/.370 soles.

#### SeniorDomo:
Reloj pulsera con GPS, botón SOS, detección de caídas y llamadas que ofrece protección 24 horas. Está más orientado a la seguridad y emergencias que al acompañamiento cotidiano, y no dispone de la dupla de dispositivos.

#### MovilTecno 866:
Reloj de pulsera diseñado específicamente para personas mayores, ancianos o con principios de Alzheimer, con localización GPS y tecla de socorro. Aunque tiene un enfoque geriátrico, su mercado está limitado a casos avanzados y no contempla el monitoreo preventivo o la conexión familiar cotidiana .

#### Competitive Analysis Landscape

**¿Por qué llevar a cabo este análisis?**
Para nuestra empresa (Guardian+) es esencial identificar fortalezas y debilidades frente a la competencia, entender sus estrategias, tomar decisiones informadas, detectar oportunidades de crecimiento, anticipar movimientos y optimizar recursos para mejorar nuestra posición en el mercado. La Tabla 2.1 compara a Guardian+ con cada competidor en sus principales dimensiones.

<a id="tabla-2-1"></a>**Tabla 2.1.** Competitive Analysis Landscape de Guardian+ frente a sus competidores

|  | Guardian+ | LifeWatch / LifeWatch 2 | SaveFamily Senior | SeniorDomo | MovilTecno866 |
|---|---|---|---|---|---|
| **Logo** | | LIFE WATCH | SaveFamily SENIOR | seniorDOMO | MovilTecno.com |
| **Overview** | Pulsera + suscripción mensual accesible para la app (modelo freemium/premium). | Reloj inteligente orientado al fitness y bienestar: mide pulso, presión, oxígeno, temperatura y sueño. | Smartwatch para adultos mayores: frecuencia cardíaca, detector de caídas, recordatorio de medicamentos, podómetro. | Pulsera con GPS, botón SOS, detección de caídas y llamadas de emergencia 24/7. | Reloj GPS localizador 4G para adultos mayores (Alzheimer, demencia), con detector de caídas, botón SOS y respuesta automática a llamadas entrantes. |
| **Precios y Costos** | Modelo mixto: venta de dispositivo + suscripción (freemium/premium). | S/.140 (aprox.). | S/.370 (aprox.). | S/.470 (aprox.), requiere servicio adicional de geolocalización. | Disponible sin cuotas adicionales, aunque precio no claramente especificado. |
| **Ventaja Competitiva (Valor ofrecido)** | "Lazo de cuidado" bidireccional (persona con necesidades específicas–familiar/cuidador), app intuitiva y accesible, reportes médicos, comunicación directa y enfoque en salud + bienestar emocional. | Económico y multifuncional, accesible como gadget fitness. | Amplia cobertura en salud preventiva, incluye recordatorios de medicación. | Fuerte en seguridad y localización, SOS en tiempo real. | Alta orientación en seguridad y localización en tiempo real con respuesta automática y detector de caídas. |
| **Mercado Objetivo** | Personas que requieren de atención especial, familiares y cuidadores que buscan tranquilidad y monitoreo constante. | Jóvenes y adultos que buscan cuidar su salud y condición física. | Adultos mayores con necesidad de monitoreo de salud integral y rutinas médicas. | Adultos mayores con alto riesgo de caídas o desorientación (Alzheimer, demencia). | Personas mayores con Alzheimer, demencia, desorientación o condiciones similares; enfoque en seguridad. |
| **Estrategias de Marketing** | Enfoque en la tranquilidad familiar, alianzas con instituciones de salud y seguros, comunicación en redes sociales y campañas educativas. | Marketing en tiendas online y marketplaces (ej. MercadoLibre, Linio). | Marketing digital especializado en cuidado de mayores, distribuidores autorizados. | Orientado a familias en Europa, con campañas web y distribuidores de teleasistencia. | Facebook y web informativa; poca inversión en publicidad. |
| **Productos & Servicios** | Pulsera IoT con sensores (FC, SpO2, movimiento, caídas) + app móvil con alertas, reportes, comunicación y soporte. | Wearable fitness (ritmo cardíaco, sueño, oxígeno, presión, podómetro, ejercicio). | Smartwatch senior con caídas, tensión arterial, podómetro y recordatorio de medicación. | Pulsera SOS con GPS, llamadas y caídas, protección permanente. | Reloj con GPS, botón SOS, detección de caídas, llamada automática, sin necesidad de pulsar pantalla. |
| **Canales de Distribución (Web y/o Móvil)** | App móvil, página web, redes sociales, WhatsApp, alianzas con EPS y seguros. | Marketplaces online, tiendas minoristas. | Distribuidores online especializados y página web. | Distribución online y teleasistencia en Europa; importadores en LatAm. | Sitio web oficial MovilTecno, tiendas online (global), marketing web. |
| **Fortalezas** | Solución integral de cuidado físico, emocional y familiar; interfaz simplificada para las personas vulnerables que requieren cuidado. | Precio bajo, multifuncional, fácil acceso. | Orientado específicamente a seniors, con medición integral de salud. | Seguridad y geolocalización permanente, SOS en tiempo real. | Tecnología probada en seguridad, facilidad de uso para situaciones de desorientación (respuesta automática). |
| **Oportunidades** | Integración con servicios de telemedicina, expansión en provincias, modelo escalable con cuidadores y clínicas, integración con seguros. | Ampliar mercado hacia adultos mayores, añadir alertas familiares. | Mejorar accesibilidad y simplicidad de configuración. | Complementar con app de acompañamiento y reportes familiares. | Complementar funcionalidades con monitoreo de salud y comunicación familiar para ofrecer mayor valor añadido. |
| **Debilidades** | En fase de validación y crecimiento, aún sin base de usuarios consolidada. | No enfocado en adultos mayores, sin alertas familiares. | Requiere configuración técnica más compleja, carece de "lazo de cuidado" bidireccional. | Sin acompañamiento emocional, no incluye reportes médicos ni monitoreo integral. | Enfoque limitado a la seguridad física y localización; sin capacidad de monitoreo médico ni reportes de salud. |
| **Amenazas** | Competidores globales con mayor capital y alcance comercial. | Sustitución por otros relojes fitness más económicos. | Aparición de apps con pulseras más intuitivas. | Competencia tecnológica que combine seguridad + monitoreo de salud. | Competidores con plataforma más robusta o integración con servicios de salud podrían desplazarlo. |

### 2.1.2. Estrategias y tácticas frente a competidores

Nuestra solución contará con compatibilidad completa con dispositivos móviles Android e iOS(teóricamente, dado que en el curso no es 100% necesario trabajar con IOS), así como con servicios de geolocalización en tiempo real, lo que permitirá a cuidadores o familiares localizar a las personas que supervisan en cualquier momento, con notificaciones inmediatas ante emergencias o caídas.

La pulsera IoT enviará actualizaciones constantes sobre signos vitales (frecuencia cardíaca, oxígeno, presión arterial), estado de actividad física y posibles caídas, de manera continua antes, durante y después de un evento crítico, generando un historial médico accesible desde la app.

A diferencia de dispositivos genéricos como LifeWatch o SeniorDomo, nuestra propuesta incorpora el concepto de “lazo de cuidado” bidireccional, en el que tanto la persona vulnerable que requiere cuidado como el familiar/cuidador están conectados entre sí. Esto permite comunicación directa, envío de alertas y generación de confianza mutua en tiempo real.

La plataforma contará con un registro digital de incidentes y alertas previas, lo que permitirá a los familiares conocer antecedentes de salud, historial de caídas y cambios en los signos vitales. Esto ofrece mayor capacidad de prevención y facilita la consulta médica posterior.

Hemos identificado una oportunidad clave en las familias que actualmente dependen de dispositivos importados o genéricos, los cuales suelen estar orientados al fitness o a la seguridad básica. Nuestra propuesta integra seguridad, salud y acompañamiento emocional en un solo dispositivo, diferenciándonos por ofrecer un servicio más integral y enfocado en las personas vulnerables que requieren cuidado.

La aplicación contará con pagos seguros e integración con servicios adicionales (como telemedicina, seguros o planes premium), lo que permitirá a los usuarios acceder a un ecosistema completo desde la misma plataforma, generando valor agregado y fidelización.

## 2.2. Entrevistas

En esta sección se presentan las entrevistas realizadas a familiares y cuidadores de personas vulnerables: su diseño, el registro de cada entrevista y el análisis de sus resultados.

### 2.2.1. Diseño de entrevistas

Las entrevistas se diseñaron para conocer cómo familiares y cuidadores acompañan a la persona bajo su cuidado, qué situaciones les generan mayor preocupación y qué herramientas utilizan. A continuación se presentan las preguntas preparadas para cada segmento.

**Preguntas para segmento 1**
**(Familiares de personas vulnerables que requieren cuidado)**

- ¿Qué relación tiene con la persona que cuida o acompaña, y vive usted con ella o de forma independiente?
- ¿Su familiar suele estar solo o con poca compañía en algunos momentos del día? Si es así, ¿qué es lo que más le preocupa a usted en esa situación?
- ¿Cómo maneja usted las situaciones en las que su familiar se siente mal de salud o sufre algún malestar repentino?
- ¿Ha tenido alguna experiencia reciente en la que su familiar necesitó ayuda y no había nadie cerca? ¿Qué ocurrió?
- ¿Qué tipo de ayuda o acompañamiento le gustaría que su familiar tuviera disponible sin depender de que usted esté siempre presente?
- ¿Qué significa para usted que su familiar se sienta seguro en su propia casa?
- En caso de una caída o un problema de salud repentino de su familiar, ¿qué tan rápido cree que podría conseguirse ayuda?
- ¿Su familiar suele tener dificultades para recordar sus horarios de medicamentos o sus citas médicas? Si es así, ¿qué sistemas utilizan actualmente para recordárselos?
- ¿Qué tan cómodo se siente usted usando tecnología (aplicaciones, relojes inteligentes, pulseras) para temas de salud o para comunicarse con el resto de la familia sobre el estado de su familiar?
- ¿A través de qué medios o canales digitales suele mantenerse informado sobre el estado de salud o bienestar de su familiar (WhatsApp, llamadas, apps, redes sociales)?
- Si pudiera contar con un dispositivo que le ayude a monitorear el bienestar de su familiar, ¿qué características serían las más importantes para usted, además de conocer su ubicación?
- ¿Qué tipo de actividades realiza su familiar con más frecuencia (caminar, hacer ejercicio suave, socializar con amigos u otros familiares)?
- ¿Qué cambios ha notado en la salud o en la vida cotidiana de su familiar en los últimos años?
- ¿Qué le daría más tranquilidad: prevenir problemas de salud de su familiar o recibir ayuda inmediata cuando ocurren?
- ¿Qué cosas le resultan fáciles y cuáles difíciles a su familiar al usar aparatos electrónicos?
- Si existiera una pulsera o dispositivo que apoye el cuidado de su familiar, ¿qué es lo primero que le gustaría que hiciera por él/ella?
- ¿Qué funciones o características evitaría en un dispositivo para que no le resulte molesto o incómodo de usar a su familiar?
- ¿Existen marcas de tecnología o salud (relojes, apps, seguros) en las que usted confía especialmente para el cuidado de su familia? ¿Por qué?
- ¿Estaría dispuesto/a a pagar por un servicio de este tipo? ¿Qué precio consideraría razonable?

**Preguntas para segmento 2**
**(Cuidadores responsables del bienestar de personas vulnerables que requieren cuidado)**

- ¿Cómo es un día típico en el cuidado de la persona a su cargo, qué tareas debe hacer normalmente?
- ¿En algún momento ha tenido que dejar a la persona a su cargo sola en casa?
- ¿Qué es lo que más le preocupa cuando la persona a su cargo está sola en casa?
- ¿Cómo le gustaría enterarse si ocurre algo mientras usted no está?
- ¿En qué momentos del día siente mayor necesidad de monitorear a la persona a su cargo?
- ¿Qué aspectos de la salud de la persona a su cargo considera más difíciles de vigilar constantemente?
- ¿Qué tan cómodo cree que sería usar tecnologías (apps, pulseras, dispositivos) para apoyar el cuidado de la persona a su cargo?
- ¿Qué información cree que sería útil que le muestre nuestro servicio sobre el estado de la persona a su cargo, aparte de los signos vitales básicos?
- ¿Piensa usted que la supervisión constante que debe realizar le genera carga? De ser así, ¿de qué manera cree que nuestro servicio le ayudaría a reducir la carga?
- ¿Qué funciones cree que serían más útiles en una aplicación de monitoreo para personas vulnerables que requieren cuidado?
- ¿Cómo le gustaría que se vieran estas funciones en la aplicación o la pulsera, en relación a la facilidad de uso de estas?
- ¿Qué situaciones de emergencia ha tenido que enfrentar con la persona a su cargo y cómo las resolvió?
- ¿Alguna vez ha sentido que la supervisión manual sobre la persona a su cargo fue insuficiente?
- ¿Qué características harían que usted confíe en un sistema de monitoreo para complementar su trabajo?
- ¿Usted compraría el servicio que le ofrecemos si es a un precio razonable?

### 2.2.2. Registro de entrevistas

A continuación se presenta el registro de las entrevistas realizadas a los segmentos de Familiares y Cuidadores, incluyendo la ficha de cada entrevistado y la captura de pantalla correspondiente.

**Enlace a la grabación de las entrevistas:** [Ver grabación en SharePoint](https://upcedupe-my.sharepoint.com/:v:/g/personal/u202421866_upc_edu_pe/IQACcQNLkvZqQpHQRm3if26lAffXgxwl4EZcZ-_CvP5Vc0A?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=xXF12j)

#### Segmento 1: Familiares

**Entrevistado 1**

La Tabla 2.2 resume los datos de la entrevista a Rocío Miranda Alvarado Silva.

<a id="tabla-2-2"></a>**Tabla 2.2.** Datos de la entrevista a Rocío Miranda Alvarado Silva

| Campo | Valor |
|---|---|
| Nombre y apellido | Rocío Miranda Alvarado Silva |
| Edad | 22 |
| Distrito | Jesús María |
| Timing (inicio en la grabación) | 00:04 |
| Duración | 12:35 |

La Figura 2.1 muestra una captura de la entrevista realizada a Rocío Miranda Alvarado Silva.

<a id="figura-2-1"></a>**Figura 2.1.** Captura de la entrevista a Rocío Miranda Alvarado Silva

![Captura Entrevista Familiar 1](../assets/images/chapterII/screenshots-entrevistas/entrevista_familiar_1.png)

**Resumen de la entrevista:** Rocío Alvarado, junto a su madre, es responsable directa del cuidado de su hermano (quien padece esquizofrenia y otros trastornos asociados y convive con ambas). Se turnan para acompañarlo durante el día, aunque existen lapsos de 40 minutos a una hora en los que él queda solo por motivos laborales o académicos, lo que le genera preocupación constante ante el riesgo de brotes psicóticos; relató un episodio en el que, tras ausentarse cerca de dos horas, vecinos les informaron que su hermano se había alterado sin que ellas pudieran enterarse a tiempo, evidenciando la falta de un canal de supervisión inmediata. El control de la medicación depende completamente de ellas mediante registros manuales. Rocío se mostró cómoda con la tecnología (apps, relojes y pulseras de salud) y priorizó el monitoreo del ritmo cardíaco como la funcionalidad más importante de un dispositivo de este tipo, seguido de otros indicadores como la glucosa, prefiriendo la prevención antes que solo reaccionar ante emergencias. Destacó que la facilidad de uso es un requisito indispensable y se mostró dispuesta a pagar hasta S/. 100 mensuales por un servicio que le brinde tranquilidad frente al cuidado de su hermano.

**Entrevistado 2**

La Tabla 2.3 resume los datos de la entrevista a Lucía Infante.

<a id="tabla-2-3"></a>**Tabla 2.3.** Datos de la entrevista a Lucía Infante

| Campo | Valor |
|---|---|
| Nombre y apellido | Lucía Infante |
| Edad | 27 |
| Distrito | Santiago de Surco |
| Timing (inicio en la grabación) | 12:39 |
| Duración | 12:32 |

La Figura 2.2 muestra una captura de la entrevista realizada a Lucía Infante.

<a id="figura-2-2"></a>**Figura 2.2.** Captura de la entrevista a Lucía Infante

![Captura Entrevista Familiar 2](../assets/images/chapterII/screenshots-entrevistas/entrevista_familiar_2.png)

**Resumen de la entrevista:** Lucía Infante vive sola con un adulto mayor bajo su cuidado y comentó que debe dejarlo solo durante sus jornadas laborales, lo que le genera preocupación al tener como único medio de comunicación con él los mensajes o llamadas telefónicas. Consideró que una propuesta como Guardian+ sería de gran alivio, ya que le permitiría saber en todo momento dónde se encuentra su familiar, acceder a información sobre sus signos vitales y recibir alertas ante emergencias. Entre las funcionalidades adicionales que le gustaría encontrar en la aplicación, mencionó opciones para organizar citas médicas y chequeos del adulto mayor, así como recomendaciones o sugerencias sobre su alimentación. Indicó que estaría dispuesta a pagar entre S/. 50 y S/. 100 mensuales por el servicio (aparte del costo del equipo), y sugirió que sería interesante manejar distintos planes según los servicios o necesidades específicas del adulto mayor a su cuidado.

**Entrevistado 3**

La Tabla 2.4 resume los datos de la entrevista a Junio Antenor Ayala.

<a id="tabla-2-4"></a>**Tabla 2.4.** Datos de la entrevista a Junio Antenor Ayala

| Campo | Valor |
|---|---|
| Nombre y apellido | Junio Antenor Ayala |
| Edad | 32 |
| Distrito | San Juan Baustista |
| Timing (inicio en la grabación) | 25:11 |
| Duración | 13:06 |

La Figura 2.3 muestra una captura de la entrevista realizada a Junio Antenor Ayala.

<a id="figura-2-3"></a>**Figura 2.3.** Captura de la entrevista a Junio Antenor Ayala

![Captura Entrevista Familiar 3](../assets/images/chapterII/screenshots-entrevistas/entrevista_familiar_3.png)

**Resumen de la entrevista:** El entrevistado Junior Ayala de 32 años y soldador, vive con su pareja y su hijo y manifiesta preocupación principalmente por la seguridad y el bienestar de su familia cuando no puede estar presente debido al trabajo u otras actividades. Señala que, ante emergencias o problemas de salud, suele experimentar preocupación y desesperación, recurriendo a familiares cercanos o a servicios de emergencia. Considera que una solución tecnológica, como una pulsera o dispositivo inteligente, podría ayudar a monitorear el estado de salud, las actividades y la seguridad de sus familiares, además de recordar medicamentos y citas médicas. Actualmente no utiliza herramientas de monitoreo ni lleva un control preventivo de la salud, ya que normalmente acuden a un centro de salud cuando los síntomas se vuelven graves. Está dispuesto a utilizar tecnología de este tipo, aunque considera importantes factores como el costo, la duración de la batería y la conectividad, especialmente en zonas rurales. Finalmente, estaría dispuesto a pagar por un dispositivo que realmente aporte seguridad y bienestar a su familia, realizando un esfuerzo económico si considera que el producto es útil y de buena calidad.

#### Segmento 2: Cuidadores

**Entrevistado 1**

La Tabla 2.5 resume los datos de la entrevista a Roxana Paola Diana.

<a id="tabla-2-5"></a>**Tabla 2.5.** Datos de la entrevista a Roxana Paola Diana

| Campo | Valor |
|---|---|
| Nombre y apellido | Roxana Paola Diana|
| Edad | 39 |
| Distrito | Surco |
| Timing (inicio en la grabación) | 38:21 |
| Duración | 11:16 |

La Figura 2.4 muestra una captura de la entrevista realizada a Roxana Paola Diana.

<a id="figura-2-4"></a>**Figura 2.4.** Captura de la entrevista a Roxana Paola Diana

![Captura Entrevista Cuidador 1](../assets/images/chapterII/screenshots-entrevistas/entrevista_cuidador_1.png)

**Resumen de la entrevista:** De la entrevista realizada a Roxana Paola Diana Ramírez se pudieron obtener datos que favorecen a la implementación de nuevas features. En primer lugar, el usuario menciona un poco sobre la rutina que debe seguir, en este caso, hace mayor énfasis en el suministro de las pastillas que debe controlar. En segundo lugar, menciona que hay ciertos signos precisos que el usuario debe rastrear los cuales son la presión, saturación y la temperatura. Entre estos, el primero destaca más en el caso particular de este usuario. En tercer lugar, en relación al manejo de situaciones críticas, el usuario generalmente toma medidas generales (llamado a emergencia o sacar citas médicas).
Ante todo lo mencionado, se puede evidenciar que algunas de las features proporcionadas pueden ser aplicables, como los recordatorios de medicación (especialmente en este caso), contacto directo a emergencias o médicos especializados y la medición de signos vitales.


**Entrevistado 2**

La Tabla 2.6 resume los datos de la entrevista a Piero Segura.

<a id="tabla-2-6"></a>**Tabla 2.6.** Datos de la entrevista a Piero Segura

| Campo | Valor |
|---|---|
| Nombre y apellido | Piero Segura|
| Edad | 22 |
| Distrito | Callao |
| Timing (inicio en la grabación) | 49:37 |
| Duración | 5:10 |

La Figura 2.5 muestra una captura de la entrevista realizada a Piero Segura.

<a id="figura-2-5"></a>**Figura 2.5.** Captura de la entrevista a Piero Segura

![Captura Entrevista Cuidador 2](../assets/images/chapterII/screenshots-entrevistas/entrevista_cuidador_2.png)

**Resumen de la entrevista:** Piero Segura Cárdenas, de 22 años, del distrito del Callao y estudiante de psicología, cuenta con experiencia como voluntario en un asilo, donde apoyaba a los adultos mayores en su alimentación, medicamentos, higiene, movilidad y atención ante posibles emergencias. Cuando debía dejar solo a un paciente, su principal preocupación era que pudiera sufrir una caída, descompensarse o necesitar ayuda urgente sin poder comunicarlo. Considera que recibir alertas en su celular con información sobre lo ocurrido sería una solución útil, especialmente cuando se encuentra estudiando, fuera del lugar o durante la noche. Le interesa monitorear aspectos como caídas, presión, ritmo cardíaco, estado de ánimo, sueño, medicación y actividad física. Considera que una aplicación o pulsera sería útil siempre que sea sencilla, cómoda para el paciente y muestre información clara. Además, señala que la supervisión constante le genera carga, por lo que un sistema de monitoreo le permitiría sentirse más tranquilo y organizar mejor su tiempo. Para confiar en el servicio, considera importantes la precisión, rapidez de las alertas, buena duración de la batería y protección de la información del paciente. Finalmente, estaría dispuesto a comprar el servicio si el precio es razonable, ya que considera que facilitaría el cuidado y brindaría mayor seguridad tanto al paciente como al cuidador.

**Entrevistado 3**

La Tabla 2.7 resume los datos de la entrevista a Fernanda Llanos.

<a id="tabla-2-7"></a>**Tabla 2.7.** Datos de la entrevista a Fernanda Llanos

| Campo | Valor |
|---|---|
| Nombre y apellido | Fernanda Llanos |
| Edad | 59 |
| Distrito | San Borja |
| Timing (inicio en la grabación) | 54:47 |
| Duración | 12:19 |

La Figura 2.6 muestra una captura de la entrevista realizada a Fernanda Llanos.

<a id="figura-2-6"></a>**Figura 2.6.** Captura de la entrevista a Fernanda Llanos

![Captura Entrevista Cuidador 3](../assets/images/chapterII/screenshots-entrevistas/entrevista_cuidador_3.png)

**Resumen de la entrevista:** La Sra. Fernanda Llanos trabaja como cuidadora de una señora de 88 años. Comentó que, al no estar siempre presentes los familiares, en varios momentos del día se ve en la necesidad de dejar sola a la señora, lo cual le genera preocupación: teme que se dirija a zonas de la casa que puedan representar un peligro (como escaleras o la cocina) o que sufra algún incidente de salud sin que nadie esté cerca para asistirla a tiempo. Frente a este escenario, considera útil la implementación de una tecnología de supervisión como la que propone Guardian+, ya que le permitiría conocer el estado y la ubicación de la señora incluso en su ausencia, y manifestó que apoyaría y utilizaría una solución de este tipo si estuviera disponible.

**Entrevistado 4**

La Tabla 2.8 resume los datos de la entrevista a Gabriela Cuadros Curihuaman.

<a id="tabla-2-8"></a>**Tabla 2.8.** Datos de la entrevista a Gabriela Cuadros Curihuaman

| Campo | Valor |
|---|---|
| Nombre y apellido | Gabriela Cuadros Curihuaman |
| Edad | 21 |
| Distrito | Santa Anita |
| Timing (inicio en la grabación) | 01:06:58 |
| Duración | 8:53 |

La Figura 2.7 muestra una captura de la entrevista realizada a Gabriela Cuadros Curihuaman.

<a id="figura-2-7"></a>**Figura 2.7.** Captura de la entrevista a Gabriela Cuadros Curihuaman

![Captura Entrevista Cuidador 4](../assets/images/chapterII/screenshots-entrevistas/entrevista_cuidador_4.png)

**Resumen de la entrevista:** Gabriela Cuadro Curihuamán, de 21 años, es enfermera y trabaja en la Casa del Adulto Mayor de Santa Anita, donde se encarga de acompañar y supervisar a pacientes adultos mayores, apoyándolos en su alimentación, higiene, medicamentos y actividades diarias. Su principal preocupación cuando debe dejar solo a un paciente es que pueda sufrir una caída, sentirse mal o tener alguna emergencia sin recibir ayuda inmediata. Considera que un sistema de monitoreo mediante una aplicación y una pulsera sería muy útil para recibir alertas en su celular, conocer la ubicación, actividad, calidad del sueño y detectar caídas o comportamientos fuera de lo normal. También destaca la importancia de contar con recordatorios de medicamentos y un historial del estado del paciente. Señala que la supervisión constante puede ser agotadora y generar preocupación, por lo que la tecnología podría reducir su carga y brindarle mayor tranquilidad. Para confiar en el sistema, considera fundamental que sea preciso, confiable, fácil de usar, con botones grandes, información clara, poco peso, alertas rápidas y una batería que dure todo el día. Finalmente, estaría dispuesta a adquirir el servicio siempre que tenga un precio accesible y cumpla adecuadamente con estas funciones.

### 2.2.3. Análisis de entrevistas

En esta sección se resumen los hallazgos de cada entrevista y, a partir de ellos, se analizan los patrones de cada segmento y las características que sirvieron para construir los arquetipos de usuario.

* En la entrevista con Rocío Alvarado es una familiar cuidadora que vive con su hermano y su madre, quienes se turnan para supervisarlo debido a sus necesidades de atención. Su principal preocupación es que su hermano atraviese una crisis mientras se encuentra solo, ya que en una ocasión reciente ocurrió una situación de este tipo sin que ellas pudieran enterarse hasta regresar a casa. Valora especialmente una solución tecnológica que permita monitorear su estado a distancia, recibir notificaciones y controlar indicadores como el ritmo cardíaco y la actividad física. Se muestra cómoda utilizando tecnología y considera importante que el dispositivo sea sencillo. Su principal motivación es reducir la preocupación y tener mayor tranquilidad, mostrando además una alta disposición de pago, de hasta S/100 mensuales, por un servicio que considere útil.
* La entrevista con Lucía Infante, de 27 años, es diseñadora gráfica y vive con su padre adulto mayor, quien todavía mantiene cierta autonomía. Su principal dificultad aparece cuando se encuentra fuera de casa y no puede saber qué está ocurriendo con él, especialmente cuando no responde sus llamadas. Considera que una aplicación de monitoreo debe ser sencilla, intuitiva y poco recargada, debido a las posibles dificultades de los adultos mayores con la tecnología. Valora la seguridad, la facilidad de uso y la confianza en el manejo de los datos. Está dispuesta a pagar aproximadamente entre S/30 y S/40 mensuales, siempre que el servicio ofrezca beneficios claros y se adapte al nivel de cuidado que requiere cada usuario.
* En la entrevista con Junior Antenor, de 32 años y soldador, vive con su pareja y su hijo, y su principal preocupación es conocer la seguridad y bienestar de su familia cuando se encuentra trabajando o fuera de casa. Ha experimentado situaciones en las que su hijo necesitó la presencia de un adulto debido a accidentes o problemas repentinos, generándole preocupación y la necesidad de recurrir rápidamente a familiares cercanos. Actualmente no utiliza sistemas de monitoreo ni realiza un seguimiento preventivo constante de la salud familiar. Considera atractiva una solución tecnológica que permita monitorear el estado de sus familiares, facilitar la atención ante emergencias y recordar medicamentos o citas. Está dispuesto a realizar un esfuerzo económico por adquirirla, aunque considera importantes el precio, la duración de la batería y la conectividad, especialmente en zonas con poca cobertura.

* La entrevistada Roxana Paola tiene a su cargo el cuidado diario de una adulta mayor y realiza actividades como higiene, alimentación, administración de medicamentos, control de presión y saturación, además de acompañarla durante sus actividades cotidianas. Su principal preocupación está relacionada con el cumplimiento de la medicación, ya que la adulta mayor puede olvidar si tomó sus pastillas, así como con la supervisión durante la noche, cuando existe mayor riesgo de caídas o accidentes al levantarse para ir al baño. Considera que una pulsera vinculada a una aplicación sería útil para automatizar el control de signos vitales como presión, temperatura y saturación, además de generar alertas ante situaciones anormales. Valora especialmente que la solución sea sencilla, funcional y fácil de utilizar, con información precisa y confiable. También reconoce que la tecnología podría reducir la carga que genera la supervisión constante y facilitar el seguimiento del estado de salud de la adulta mayor. Aunque actualmente siempre existe otra persona acompañándola, muestra interés en adquirir el dispositivo si identifica una necesidad concreta y percibe que realmente puede ser útil para el cuidado.
* La entrevista Gabriela Cuadros, de 21 años, es enfermera y trabaja cuidando adultos mayores, por lo que tiene experiencia directa en tareas de alimentación, higiene, medicación y supervisión. Su principal preocupación cuando no puede estar presente es que el paciente pueda sufrir una caída, presentar un problema de salud o tener una emergencia sin recibir ayuda inmediata. Considera que un dispositivo conectado a una aplicación sería una herramienta útil para complementar el cuidado y reducir la carga que genera la supervisión constante. Valora funciones como alertas de emergencia, ubicación, monitoreo de actividad, sueño y medicamentos. Para confiar en el servicio, espera que sea preciso, confiable, sencillo, ligero, con botones grandes, alertas rápidas y batería de larga duración. Además, estaría dispuesta a adquirirlo si el precio es accesible.
* Piero, de 22 años, estudiante de psicología y voluntario en un asilo, cuenta con experiencia apoyando a adultos mayores en su alimentación, higiene, movilidad y medicación. Su principal preocupación son las caídas, descompensaciones y situaciones en las que el paciente pueda necesitar ayuda urgente mientras él se encuentra estudiando o fuera del lugar. Considera útil recibir alertas en el celular y acceder a información sobre signos vitales, medicamentos, sueño, actividad física y posibles comportamientos inusuales. La solución ideal para él debe ser simple, cómoda y fácil de comprender. También considera fundamentales la precisión, rapidez de las alertas, duración de la batería y protección de los datos del paciente. Está dispuesto a comprar el servicio si este facilita el cuidado y proporciona mayor seguridad tanto al paciente como al cuidador.
* En la entrevista con Fernanda Llanos, de 59 años, residente de San Borja y cuidadora de una adulta mayor de 88 años, realiza labores de acompañamiento y supervisión, pero enfrenta dificultades cuando debe dejarla sola debido a la ausencia de los familiares. Su principal preocupación es que la adulta mayor pueda desplazarse hacia lugares peligrosos de la vivienda, como las escaleras o la cocina, o sufrir algún problema de salud sin recibir asistencia inmediata. Esta situación evidencia una necesidad de supervisión a distancia que le permita conocer tanto la ubicación como el estado de la adulta mayor cuando no se encuentra presente. Fernanda muestra una actitud favorable hacia el uso de tecnología para complementar el cuidado y considera que una solución como Guardian+ podría brindarle mayor tranquilidad y seguridad. Su perfil representa a un cuidador con experiencia que busca reducir los riesgos asociados a la ausencia física y contar con información oportuna para actuar ante posibles incidentes.

#### 1. Segmento: familiares de personas que requieren atención 

En este segmento identificamos a **Rocío Alvarado**, **Junior Ayala Miranda**, **Lucia Infante** por lo que la muestra es de **3 entrevistados**. La Tabla 2.9 resume las características identificadas y la proporción de entrevistados que las mencionan.

<a id="tabla-2-9"></a>**Tabla 2.9.** Características identificadas en el segmento de familiares

| Característica identificada                                      | Entrevistados que la mencionan | %    |
| ---------------------------------------------------------------- | ------------------------------ | ---- |
| Preocupación por la seguridad del familiar cuando está solo      | 3/3                            | 100% |
| Necesidad de recibir alertas o información a distancia           | 3/3                            | 100% |
| Interés en monitorear la salud mediante tecnología               | 3/3                            | 100% |
| Preocupación ante emergencias o problemas repentinos             | 3/3                            | 100% |
| Consideran importante una respuesta rápida ante emergencias      | 3/3                            | 100% |
| No utilizan actualmente un sistema tecnológico especializado de monitoreo | 3/3                       | 100% |
| Valoran la facilidad de uso del dispositivo                      | 3/3                            | 100% |
| Consideran importante la conectividad                            | 2/3                            | 67%  |
| Consideran importante una buena duración de batería              | 2/3                            | 67%  |
| Están dispuestos a pagar por una solución útil                   | 3/3                            | 100% |

**Análisis:** Los familiares entrevistados presentan como principal necesidad la seguridad y supervisión de sus seres queridos cuando no pueden estar físicamente presentes. El 100% manifestó preocupación por posibles emergencias, accidentes o problemas de salud durante los períodos en los que el familiar permanece solo. Rocío, por ejemplo, relató una situación en la que su hermano tuvo una crisis mientras ella y su madre se encontraban fuera de casa y no tuvieron conocimiento de lo ocurrido hasta regresar. Por su parte, Junior señaló que cuando se encuentra trabajando o realizando sus actividades diarias le preocupa no saber qué está haciendo su hijo o si se encuentra bien al igual que Lucia. Los entrevistados mostraron interés en una solución tecnológica que permita monitorear el estado del familiar y enviar alertas a distancia, evidenciando una necesidad de mayor tranquilidad y control. Asimismo, el 100% indicó estar dispuesto a utilizar o adquirir una solución de este tipo si resulta útil. Entre las características más valoradas aparecen la facilidad de uso, el monitoreo de indicadores de salud y la posibilidad de recibir asistencia rápida ante una emergencia. Rocío incluso manifestó una disposición de pago de hasta S/100 mensuales, mientras que Junior indicó que realizaría un esfuerzo económico si la tecnología realmente aporta seguridad y salud a su familia.

#### 2. Segmento: cuidadores 

En este segmento podemos considerar a **Roxana Paola**, **Fernanda Llanos**, **Gabriela Curihuamán** y **Piero Segura**, por lo que tenemos una muestra de **4 entrevistados**. La Tabla 2.10 resume las características identificadas y la proporción de entrevistados que las mencionan.

<a id="tabla-2-10"></a>**Tabla 2.10.** Características identificadas en el segmento de cuidadores

| Característica identificada                                      | Entrevistados que la mencionan | %    |
| ---------------------------------------------------------------- | ------------------------------ | ---- |
| Preocupación por caídas o emergencias                            | 4/4                            | 100% |
| Consideran útil recibir alertas en el celular                    | 4/4                            | 100% |
| Interés en monitorear al adulto mayor a distancia                | 4/4                            | 100% |
| Valoran la facilidad de uso                                      | 4/4                            | 100% |
| Consideran importante monitorear medicamentos                    | 2/4                            | 50%  |
| Interés en conocer actividad/sueño del adulto mayor              | 3/4                            | 67%  |
| Consideran que el monitoreo reduce la carga del cuidador         | 3/4                            | 67%  |
| Consideran importantes las alertas rápidas                       | 4/4                            | 67%  |
| Consideran importante una buena duración de batería              | 3/4                            | 67%  |
| Están dispuestos a pagar por el servicio                         | 4/4                            | 100% |

**Analisis:** Los entrevistados de este segmento coinciden principalmente en que el cuidado del adulto mayor requiere una supervisión constante, lo que puede generar preocupación y carga para el cuidador. El 100% identifica las caídas y las emergencias como situaciones críticas y considera útil recibir alertas cuando no se encuentra junto al adulto mayor. Gabriela menciona que la supervisión constante es agotadora y que una aplicación podría ayudarla a sentirse más tranquila, mientras que Piero señala que el monitoreo le permitiría organizar mejor su tiempo cuando debe estudiar o atender otras actividades. Asimismo, existe una alta valoración de funciones relacionadas con la medicación, ubicación, actividad física, sueño y signos vitales. El 100% de los entrevistados considera importante que la solución sea sencilla y fácil de utilizar, especialmente debido a las posibles dificultades que pueden presentar los adultos mayores frente a la tecnología. En cuanto a la disposición de pago, los tres entrevistados estarían dispuestos a adquirir el servicio si el precio resulta razonable; Lucía estima un rango de S/30 a S/40 mensuales, mientras Gabriela y Piero también condicionan su compra a que el precio sea accesible y que el sistema realmente aporte seguridad y utilidad.

#### 3. Características para la construcción de los arquetipos

A partir del análisis, la Tabla 2.11 resume los principales elementos que deberían formar parte de los arquetipos:

<a id="tabla-2-11"></a>**Tabla 2.11.** Elementos para la construcción de los arquetipos de usuario

| Variable                | Familiares                                | Cuidadores de adultos mayores                          |
| ----------------------- | ----------------------------------------- | ------------------------------------------------------ |
| Principal preocupación  | Seguridad y bienestar del familiar        | Caídas, emergencias y estado de salud                  |
| Necesidad principal     | Saber qué ocurre cuando están lejos        | Supervisar sin estar constantemente presentes          |
| Emoción predominante    | Preocupación / desesperación              | Preocupación / agotamiento                             |
| Solución esperada       | Monitoreo y alertas a distancia           | Monitoreo, alertas y seguimiento                       |
| Funciones más valoradas | Salud, seguridad, ubicación y emergencias | Caídas, medicamentos, ubicación, signos vitales, sueño |
| Diseño esperado         | Fácil de utilizar                         | Simple, intuitivo y cómodo                             |
| Problema actual         | Falta de información cuando están ausentes| Supervisión manual constante                           |
| Barreras                | Precio y conectividad                     | Precio, batería y facilidad de uso                     |
| Disposición de pago     | Sí                                        | Sí                                                     |

## 2.3. Needfinding

En esta sección se sintetizan los hallazgos de las entrevistas en los artefactos de needfinding: User Personas, User Task Matrix, User Journey Mapping, Empathy Mapping, Big Picture EventStorming y Ubiquitous Language.

### 2.3.1. User Personas

Las fichas de User Persona presentadas a continuación son el resultado directo del análisis realizado sobre las entrevistas aplicadas a ambos segmentos objetivo: familiares y cuidadores de personas con necesidades especiales. A partir de las respuestas recogidas, se identificaron patrones comunes en preocupaciones, necesidades, emociones y expectativas frente a una solución tecnológica de monitoreo, los cuales fueron sistematizados y traducidos en las características que conforman cada arquetipo. Se elaboró una ficha de User Persona por cada segmento identificado, procurando que cada uno de sus componentes —background, motivations, frustrations, goals, quote, skills y brands and influencers— refleje de manera representativa los hallazgos obtenidos y no las características de un único entrevistado en particular.

Para el segmento de **familiares**, el análisis evidenció que el 100% de los entrevistados manifestó preocupación por la seguridad de su familiar cuando este permanece solo, así como la necesidad de recibir alertas o información a distancia y de monitorear su salud mediante tecnología, incluso sin contar actualmente con un sistema especializado para ello. Estos hallazgos, junto con la alta disposición de pago identificada y la valoración por dispositivos fáciles de usar, dieron forma al User Persona de este segmento, representado en la ficha de María Fernanda Rojas Ibáñez.

Para el segmento de **cuidadores**, el análisis mostró que la totalidad de los entrevistados coincide en la preocupación por caídas y emergencias, la utilidad de recibir alertas en el celular y el interés en monitorear a distancia al adulto mayor, además de una valoración compartida por la facilidad de uso y el seguimiento de medicamentos y signos vitales como funciones clave para reducir la carga que genera la supervisión constante. Estas características quedaron plasmadas en el User Persona de este segmento, representado en la ficha de Roxana Paola Diana Ramírez. Ambas fichas fueron elaboradas en la herramienta UXPressia, siguiendo las mejores prácticas para la especificación de arquetipos de usuario.

#### Primer segmento: Familiares 

La Figura 2.8 presenta el User Persona del segmento de familiares.

<a id="figura-2-8"></a>**Figura 2.8.** User Persona del segmento de familiares

![user-persona-1](../assets/images/chapterII/user-persona-1-fix.png)

#### Segundo segmento: Cuidadores

La Figura 2.9 presenta el User Persona del segmento de cuidadores.

<a id="figura-2-9"></a>**Figura 2.9.** User Persona del segmento de cuidadores

![user-persona-2](../assets/images/chapterII/user-persona-2.png)

### 2.3.2. User Task Matrix

El User Task Matrix que se presenta a continuación concentra las tareas que cada User Persona realiza para cumplir sus objetivos de cuidado y supervisión. Es fundamental distinguir entre **tareas** (actividades realizadas por los usuarios independientemente de la existencia de Guardian+) y **características de software** (funcionalidades que la solución proporciona). Las tareas aquí identificadas representan actividades que los usuarios realizan actualmente mediante métodos manuales, informales o tradicionales para garantizar el bienestar y la seguridad del ciudadano frágil.

Los User Personas analizados son:
- **María Fernanda Llanos Ibáñes**: Representa a familiares que asumen la responsabilidad del cuidado y supervisión a distancia.
- **Roxana Paola Diana Ramírez**: Representa a cuidadores que brindan atención directa y cotidiana.

Para cada User Persona, se evaluaron las tareas considerando dos dimensiones:
- **Frecuencia**: Regularidad con que realiza la tarea (Baja, Media, Alta).
- **Importancia**: Criticidad de la tarea para cumplir objetivos de cuidado (Baja, Media, Alta).

#### Matriz de Tareas de Usuario

La Tabla 2.12 presenta la frecuencia e importancia de cada tarea para ambos User Personas.

<a id="tabla-2-12"></a>**Tabla 2.12.** User Task Matrix de los segmentos de familiares y cuidadores

| Tarea | María Fernanda – Frecuencia | María Fernanda – Importancia | Roxana Paola – Frecuencia | Roxana Paola – Importancia |
|---|---|---|---|---|
| Supervisar toma de medicamentos | Media | Alta | Alta | Alta |
| Monitorear signos vitales | Media | Alta | Alta | Alta |
| Atender alertas de emergencia | Baja | Alta | Baja | Alta |
| Conocer estado general de salud | Media | Alta | Alta | Alta |
| Revisar reportes médicos | Alta | Alta | Media | Media |
| Acompañar en citas médicas | Baja | Media | Alta | Alta |
| Supervisar rutinas diarias | Baja | Alta | Alta | Alta |
| Coordinar acciones de cuidado | Baja | Alta | Media | Alta |
| Registrar cambios en el estado de salud | Media | Alta | Alta | Alta |
| Comunicar información a otros miembros del círculo de cuidado | Media | Alta | Alta | Alta |

#### Análisis de Resultados

**Tareas de Mayor Frecuencia e Importancia:**

- **Roxana Paola (Cuidadora)**: Las tareas con mayor impacto son la supervisión de medicamentos, el monitoreo de signos vitales, el conocimiento del estado general de salud, el acompañamiento en citas médicas, la supervisión de rutinas diarias y el registro de cambios en el estado de salud. Todas estas se realizan con alta frecuencia y son consideradas de alta importancia. Esto refleja que la responsabilidad cotidiana y directa del cuidador requiere una vigilancia continua y sistemática del Fragile Citizen.

- **María Fernanda (Familiar)**: La revisión de reportes médicos es la única tarea que realiza con alta frecuencia; sin embargo, tareas como supervisar medicamentos, monitorear signos vitales, conocer el estado general de salud, registrar cambios y comunicar información con el círculo de cuidado son consideradas de alta importancia aunque se realicen con frecuencia media. Esta combinación refleja que María Fernanda requiere información periódica y resumida que le permita mantener la tranquilidad sin necesidad de supervisión continua.

**Principales Diferencias entre User Personas:**

1. **Proximidad y Naturaleza del Contacto**: Roxana Paola, como cuidadora, está físicamente presente y realiza tareas de supervisión con alta frecuencia. María Fernanda, como familiar a distancia, realiza tareas principalmente a través de información indirecta (reportes, alertas, comunicación con otros cuidadores).

2. **Responsabilidad en Actividades Médicas**: Roxana Paola acompaña frecuentemente al ciudadano frágil en citas médicas (Alta, Alta), siendo una tarea operativa clave. María Fernanda participa ocasionalmente (Baja, Media), coordinando de forma puntual.

3. **Tipo de Información Requerida**: Roxana Paola necesita información operativa detallada para ejecutar el cuidado día a día (medicamentos específicos, horarios, signos vitales actuales). María Fernanda requiere información estratégica y tendencias (reportes periódicos, cambios generales en el estado de salud).

4. **Frecuencia en Monitoreo de Reportes**: María Fernanda revisa reportes médicos con alta frecuencia, lo que constituye su principal fuente de información verificable. Roxana Paola lo hace con frecuencia media, ya que está en contacto directo con cambios que puede observar en tiempo real.

**Principales Coincidencias entre User Personas:**

1. **Importancia Crítica de Alertas de Emergencia**: Ambas personas, a pesar de diferencias en frecuencia (ambas Baja), consideran de alta importancia atender alertas de emergencia. Esta coincidencia refleja una preocupación compartida: estar preparadas para responder rápidamente ante situaciones críticas.

2. **Monitoreo de Salud como Tarea Central**: La supervisión de medicamentos y el monitoreo de signos vitales son tareas de alta importancia para ambas. En Roxana Paola es operativo (Alta frecuencia); en María Fernanda es verificador (Media frecuencia), pero ambas reconocen que estos indicadores son fundamentales.

3. **Necesidad de Comunicación en el Círculo de Cuidado**: Ambas valoran la comunicación con otros miembros del círculo de cuidado como tarea importante. Para Roxana Paola es un deber operativo (Media-Alta); para María Fernanda es un mecanismo de coordinación y control.

4. **Registro y Seguimiento**: Tanto María Fernanda como Roxana Paola reconocen la importancia de registrar cambios en el estado de salud. Para la cuidadora es operativo y diario; para la familiar es analítico y periódico, pero ambas usan esta información para tomar decisiones.

### 2.3.3. User Journey Mapping

En esta sección se presentan los User Journey Maps As-Is elaborados para los User Personas correspondientes a los segmentos objetivo de Guardian+. Estos artefactos permiten representar el recorrido actual que realizan los usuarios para cumplir sus objetivos de cuidado y supervisión, antes de la existencia de la solución Guardian+.

Los journeys se construyen a partir de la información obtenida durante las entrevistas, su análisis y los User Personas previamente definidos. Para cada recorrido se identifican las principales etapas, acciones, puntos de contacto, pensamientos, emociones, dificultades y oportunidades encontradas durante la experiencia.

#### User Journey Map - Familiar

El recorrido del segmento de familiares representa la experiencia de supervisar a distancia el bienestar de una persona vulnerable. El journey inicia con la necesidad de conocer su estado, continúa con la búsqueda de información mediante llamadas, mensajería u otros responsables, y contempla la evaluación de posibles situaciones de riesgo, la coordinación de asistencia y el seguimiento posterior. La Figura 2.10 presenta el User Journey Map del segmento de familiares.

<a id="figura-2-10"></a>**Figura 2.10.** User Journey Map del segmento de familiares

![User Journey Map - Familiares](../assets/images/chapterII/user-journey-mapping/journeyMappFamiliar.png)

#### User Journey Map - Cuidador

El recorrido del segmento de cuidadores representa una jornada habitual de supervisión de una o varias personas bajo su responsabilidad. Comprende la revisión inicial del estado y actividades pendientes, el seguimiento de rutinas, la vigilancia continua, la atención de posibles incidencias y el registro o comunicación de lo ocurrido a familiares u otros responsables. La Figura 2.11 presenta el User Journey Map del segmento de cuidadores.

<a id="figura-2-11"></a>**Figura 2.11.** User Journey Map del segmento de cuidadores

![User Journey Map - Cuidadores](../assets/images/chapterII/user-journey-mapping/journeyMappCuidador.png)

### 2.3.4. Empathy Mapping

En esta sección se presentan los Empathy Maps elaborados para los User Personas de cada segmento objetivo de Guardian+. Estos artefactos permiten profundizar en la perspectiva de los usuarios, identificando lo que necesitan hacer, lo que ven, dicen, hacen, escuchan, piensan y sienten durante su labor de cuidado, así como sus principales dolores (pains) y beneficios esperados (gains).

Los mapas se construyen a partir de la información obtenida en las entrevistas, su análisis, los User Personas y los User Journey Maps previamente definidos, consolidando los hallazgos comunes de cada segmento.

#### Empathy Map - Familiar

El mapa del segmento de familiares refleja la experiencia de una persona que asume la responsabilidad del cuidado de un familiar vulnerable mientras cumple con su jornada laboral. Destaca la preocupación constante por no saber qué ocurre en casa, la dependencia de llamadas y mensajes como único canal de información, y la necesidad de recibir alertas oportunas y datos confiables que le brinden tranquilidad a distancia. La Figura 2.12 presenta el Empathy Map del segmento de familiares.

<a id="figura-2-12"></a>**Figura 2.12.** Empathy Map del segmento de familiares

![Empathy Map - Familiar](../assets/images/chapterII/empathy-mapping/empathyMapFamiliar-fix.png)

#### Empathy Map - Cuidador

El mapa del segmento de cuidadores refleja la experiencia de una persona encargada del cuidado directo y cotidiano de un Fragile Citizen. Destaca la carga que genera la supervisión manual continua, el riesgo de olvidar horarios de medicación o no advertir una caída durante sus ausencias, y la necesidad de contar con recordatorios, alertas automáticas y un historial centralizado que facilite su labor y la comunicación con la familia. La Figura 2.13 presenta el Empathy Map del segmento de cuidadores.

<a id="figura-2-13"></a>**Figura 2.13.** Empathy Map del segmento de cuidadores

![Empathy Map - Cuidador](../assets/images/chapterII/empathy-mapping/empathyMapCuidador.png)

### 2.3.5. Big Picture EventStorming

El Big Picture EventStorming permitió explorar el dominio de Guardian+ desde una perspectiva integral, identificando los principales Domain Events que ocurren a lo largo del ciclo de uso de la solución. Este artefacto fue utilizado para comprender de manera global cómo interactúan los actores principales, los sistemas externos y los eventos relevantes del negocio antes de profundizar en la identificación formal de Bounded Contexts.

A diferencia de un EventStorming detallado orientado al diseño interno de un contexto específico, en esta etapa se priorizó la visualización general del comportamiento del dominio. Por ello, se representaron los actores involucrados, los sistemas externos relevantes y los eventos significativos organizados de manera cronológica aproximada, desde la configuración inicial del ecosistema de cuidado hasta los eventos de monitoreo, prevención y respuesta ante incidentes.

Entre los actores identificados se encuentran el usuario de Guardian+, el suscriptor, el cuidador, el Fragile Citizen y los familiares o cuidadores responsables de responder ante alertas. Asimismo, se consideraron sistemas externos como el wearable y el sistema de tracking de ubicación, ya que forman parte esencial del funcionamiento de la solución. A partir de esta exploración fue posible reconocer eventos importantes como la creación de perfiles, el establecimiento de relaciones de cuidado, la activación de suscripciones, la programación y confirmación de recordatorios, la recepción de ubicaciones, la detección de anomalías biométricas, la emisión de advertencias preventivas, la detección de caídas, la activación de SOS y la atención de alertas críticas.

Este artefacto sirvió como base para construir una visión compartida del dominio, alinear el lenguaje del equipo y preparar el análisis posterior de Strategic Domain-Driven Design, especialmente las actividades de Candidate Context Discovery y Context Mapping. La Figura 2.14 presenta el resultado de la sesión.

<a id="figura-2-14"></a>**Figura 2.14.** Big Picture EventStorming de Guardian+

![Big Picture EventStorming - Guardian+](../assets/images/chapterII/bigPicture/bigPictureStorming.png)



### 2.3.6. Ubiquitous Language

Eric Evans plantea que el Ubiquitous Language se modela dentro de un contexto delimitado, donde se identifican los términos y conceptos del dominio del negocio, y no debe existir ambigüedad¹. A continuación, se presenta el glosario de términos del dominio de negocio de Guardian+, construido a partir del análisis de segmentos, entrevistas y arquetipos elaborados.

- **Fragile Citizen (Ciudadano frágil):** Persona con necesidades especiales —adulto mayor, paciente con movilidad reducida, condición crónica o de salud mental, entre otras— que requiere supervisión y monitoreo constante para garantizar su seguridad y bienestar.

- **Family (Familiar):** Persona con un vínculo familiar directo con el Fragile Citizen, que asume la responsabilidad principal o compartida de su cuidado, aunque no lo haga como labor remunerada.

- **Caregiver (Cuidador):** Persona contratada o designada para brindar atención directa y cotidiana al Fragile Citizen, encargándose de tareas como el suministro de medicación, la vigilancia de signos vitales y el acompañamiento diario.

- **Care Circle (Círculo de cuidado):** Conjunto de personas —familiares y/o cuidadores— vinculadas a un mismo Fragile Citizen, que coordinan y comparten la responsabilidad de su cuidado.

- **Bidirectional Care Bond (Lazo de cuidado bidireccional):** Vínculo de comunicación y monitoreo constante entre el Fragile Citizen y su Care Circle, que permite a ambas partes mantenerse informadas y conectadas en tiempo real.

- **Vital Signs (Signos vitales):** Conjunto de indicadores fisiológicos del Fragile Citizen —como frecuencia cardíaca, saturación de oxígeno, presión arterial y temperatura corporal— utilizados para evaluar su estado de salud.

- **Fall Detection (Detección de caídas):** Identificación automática de una caída sufrida por el Fragile Citizen, a partir de la cual se genera una alerta hacia su Care Circle.

- **Emergency Alert (Alerta de emergencia):** Notificación inmediata enviada al Care Circle o a servicios de emergencia ante una situación crítica en la salud o seguridad del Fragile Citizen, como una caída, un signo vital anormal o un episodio de crisis.

- **Crisis Episode (Episodio de crisis):** Situación en la que el Fragile Citizen presenta una alteración repentina y severa de su condición de salud física o mental, que puede requerir intervención inmediata de su Care Circle o de un centro de salud.

- **Safe Zone (Zona segura):** Área geográfica predefinida dentro de la cual se espera que el Fragile Citizen permanezca, cuyo abandono genera una notificación al Care Circle.

- **Medication Reminder (Recordatorio de medicación):** Aviso relacionado con los horarios en que el Fragile Citizen debe recibir su medicación, orientado a evitar olvidos o retrasos en su administración.

- **Care Routine (Rutina de cuidado):** Conjunto de actividades cotidianas relacionadas con la atención del Fragile Citizen, como la administración de medicamentos, el control de signos vitales y el acompañamiento diario.

- **Wellness Recommendation (Recomendación de bienestar):** Sugerencia orientada a mejorar la calidad de vida del Fragile Citizen, como pautas de alimentación o actividad física adaptadas a su condición.

- **Medical Appointment (Cita médica):** Encuentro programado entre el Fragile Citizen y un profesional de la salud, cuya organización y seguimiento suele estar a cargo de su Care Circle.

- **Health History (Historial de salud):** Registro acumulado de signos vitales, alertas e incidentes del Fragile Citizen, utilizado como referencia para consultas médicas y toma de decisiones de cuidado.

- **Peace of Mind (Tranquilidad):** Estado de confianza y bienestar emocional que experimenta el Care Circle al saber que el Fragile Citizen se encuentra seguro y monitoreado, incluso en su ausencia.

- **Care Plan (Plan de cuidado):** Modalidad de servicio contratada por el Care Circle, que define el nivel de funcionalidades y monitoreo disponibles según las necesidades específicas del Fragile Citizen.

- **Alert (Alerta):** Aviso disparado ante una señal que compromete la seguridad del Fragile Citizen —como una caída, una activación de SOS, una anomalía biométrica, la salida de una Safe Zone o una inactividad prolongada—, registrado con su origen, severidad y estado, y entregado a los Emergency Contacts a través de uno o más canales. Cuando su severidad es crítica, constituye una Emergency Alert.

- **Incident (Incidente):** Registro de la atención de una Alert reconocida por un integrante del Care Circle, desde que se marca en atención hasta su estabilización y cierre. Cada Alert origina como máximo un Incident, que forma parte del Health History del Fragile Citizen.

- **Emergency Contact (Contacto de emergencia):** Integrante del Care Circle designado para recibir las Alerts de un Fragile Citizen, con un orden de prioridad que define quién es el contacto primario y a quién se escala después.

- **Escalation Chain (Cadena de escalamiento):** Secuencia de niveles de notificación —contacto primario, contactos secundarios y difusión a todos los Emergency Contacts— que avanza cuando la Alert no es reconocida dentro del tiempo de espera configurado.

- **Alert Settings (Configuración de alertas):** Preferencias de alertamiento definidas para cada Fragile Citizen: tiempo de espera del reconocimiento del contacto primario, habilitación del escalamiento y estado del Silent Mode. Los canales de notificación se configuran por cada integrante del Care Circle.

- **Severity (Severidad):** Nivel de criticidad de una Alert —crítica, alta o media— que determina la estrategia de notificación: difusión simultánea a todos los Emergency Contacts, escalamiento secuencial mediante la Escalation Chain o aviso únicamente al contacto primario.

- **Acknowledgment (Reconocimiento):** Confirmación explícita de un integrante del Care Circle de haber recibido una Alert, que detiene el escalamiento y abre el Incident en atención.

- **Silent Mode (Modo silencioso):** Configuración de cada Fragile Citizen que hace que sus Alerts no críticas lleguen sin sonido a los celulares del Care Circle; las Alerts de severidad crítica siempre suenan.

## 2.4. Requirements specification

En esta sección se especifican los requerimientos de Guardian+: las User Stories agrupadas en epics, el Impact Mapping que las relaciona con los objetivos de negocio y el Product Backlog priorizado.

### 2.4.1. User Stories

Las User Stories describen las funcionalidades de Guardian+ desde la perspectiva de sus usuarios, cada una con sus criterios de aceptación. Se organizan en las siguientes epics.

#### Epics Identificadas

* **EP01 - Monitoreo de Salud en Tiempo Real:** Supervisión continua y telemetría de signos vitales (ritmo cardíaco, presión arterial, saturación de oxígeno, temperatura y frecuencia respiratoria) para la detección temprana de irregularidades fisiológicas.
* **EP02 - Recordatorios y Rutinas de Bienestar:** Gestión programada de tomas de medicación, hidratación, actividad física, citas médicas y supervisión de patrones de descanso.
* **EP03 - Alertas y Gestión de Emergencias:** Procesamiento, detección local/remota y escalamiento automatizado ante situaciones de riesgo crítico como caídas, anomalías biomédicas o activación manual de SOS.
* **EP04 - Localización y Seguridad en Movilidad:** Rastreo geográfico en tiempo real, delimitación de perímetros seguros (geocercas) y canales de comunicación directa familiar.
* **EP05 - Presencia Web y Adquisición (Landing Page):** Difusión de la propuesta de valor, planes de suscripción, canales de contacto y educación al usuario respecto al ecosistema Guardian+.
* **EP06 - Servicios de Integración y Plataforma Backend:** Capacidades técnicas de ingesta de telemetría, consultas RESTful y persistencia segura de datos clínicos e incidentes.
* **EP07 - Spikes de Investigación Técnica:** Exploración, análisis de compatibilidad y prototipado rápido de dependencias de hardware embebido, protocolos IoT y pasarelas de pago.

---

Las Tablas 2.13 a 2.49 presentan cada User Story, Technical Story y Spike con su identificador, usuario, prioridad, epic, título, descripción y criterios de aceptación.

<a id="tabla-2-13"></a>**Tabla 2.13.** User Story US01: Visualización de ritmo cardíaco en tiempo real

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US01</strong></td>
    <td>Cuidador</td>
    <td>High</td>
    <td>EP01 - Monitoreo de Salud en Tiempo Real</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Visualización de ritmo cardíaco en tiempo real</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo consultar la lectura actual del ritmo cardíaco del Fragile Citizen para monitorear su estabilidad cardiovascular e identificar irregularidades de manera oportuna.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Lectura de ritmo cardíaco en rango normal</strong><br>- <strong>Dado que</strong> el dispositivo wearable transmite lecturas de frecuencia cardíaca entre 60 y 100 lpm.<br>- <strong>Cuando</strong> el cuidador consulta el estado cardiovascular actual del Fragile Citizen.<br>- <strong>Entonces</strong> el sistema presenta el valor biométrico en tiempo real y clasifica el estado cardíaco como normal.<br><br><strong>Escenario 2: Detección de taquicardia o ritmo elevado</strong><br>- <strong>Dado que</strong> el dispositivo wearable transmite una frecuencia cardíaca superior a 100 lpm.<br>- <strong>Cuando</strong> el cuidador consulta el estado cardiovascular del Fragile Citizen.<br>- <strong>Entonces</strong> el sistema clasifica el valor como elevado y genera un indicador de advertencia sobre la lectura.<br><br><strong>Escenario 3: Detección de bradicardia o ritmo bajo</strong><br>- <strong>Dado que</strong> el dispositivo wearable transmite una frecuencia cardíaca inferior a 50 lpm.<br>- <strong>Cuando</strong> el cuidador consulta el estado cardiovascular del Fragile Citizen.<br>- <strong>Entonces</strong> el sistema clasifica el valor como bajo y genera un indicador de advertencia sobre la lectura.<br><br><strong>Escenario 4: Interrupción en la transmisión de telemetría</strong><br>- <strong>Dado que</strong> la transmisión de telemetría desde el dispositivo wearable no responde o pierde sincronización.<br>- <strong>Cuando</strong> el cuidador intenta consultar el ritmo cardíaco actual.<br>- <strong>Entonces</strong> el sistema expone el último valor histórico registrado indicando la ausencia de señal en vivo.</td>
  </tr>
</table>

<br>

<a id="tabla-2-14"></a>**Tabla 2.14.** User Story US02: Visualización de presión arterial estimada

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US02</strong></td>
    <td>Cuidador</td>
    <td>High</td>
    <td>EP01 - Monitoreo de Salud en Tiempo Real</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Visualización de presión arterial estimada</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo consultar los valores estimados de presión arterial sistólica y diastólica del Fragile Citizen para evaluar su condición hemodinámica y prevenir descompensaciones.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Presión arterial dentro del umbral normotenso</strong><br>- <strong>Dado que</strong> el sensor registra valores de presión arterial dentro de 90/60 mmHg y 120/80 mmHg.<br>- <strong>Cuando</strong> el cuidador consulta las mediciones de presión arterial del Fragile Citizen.<br>- <strong>Entonces</strong> el sistema expone los valores sistólicos y diastólicos indicando un estado estable sin generar alertas.<br><br><strong>Escenario 2: Detección de pico hipertensivo</strong><br>- <strong>Dado que</strong> el sensor registra un valor sistólico superior a 140 mmHg o diastólico superior a 90 mmHg.<br>- <strong>Cuando</strong> el cuidador solicita los valores actuales de presión arterial.<br>- <strong>Entonces</strong> el sistema categoriza la lectura como valor fuera de rango y activa una marca de observación clínica.<br><br><strong>Escenario 3: Detección de hipotensión</strong><br>- <strong>Dado que</strong> el sensor registra una presión arterial inferior a 90/60 mmHg.<br>- <strong>Cuando</strong> el cuidador solicita los valores actuales de presión arterial.<br>- <strong>Entonces</strong> el sistema clasifica la condición como presión baja y notifica el valor fuera de umbral de seguridad.<br><br><strong>Escenario 4: Lectura fallida o no concluyente</strong><br>- <strong>Dado que</strong> las señales hemodinámicas obtenidas por el sensor presentan ruido excesivo o artefactos de movimiento.<br>- <strong>Cuando</strong> el cuidador consulta la presión arterial.<br>- <strong>Entonces</strong> el sistema descarta la medición errónea y reporta la lectura como inválida sin alterar los umbrales de alerta.</td>
  </tr>
</table>

<br>

<a id="tabla-2-15"></a>**Tabla 2.15.** User Story US03: Visualización de saturación de oxígeno periférico (SpO₂)

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US03</strong></td>
    <td>Cuidador</td>
    <td>High</td>
    <td>EP01 - Monitoreo de Salud en Tiempo Real</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Visualización de saturación de oxígeno periférico (SpO₂)</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo consultar el porcentaje de saturación de oxígeno en sangre del Fragile Citizen para identificar posibles cuadros de hipoxemia o dificultad respiratoria.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Saturación de oxígeno en nivel óptimo</strong><br>- <strong>Dado que</strong> la pulsera registra una saturación de oxígeno SpO₂ igual o superior al 95%.<br>- <strong>Cuando</strong> el cuidador consulta el nivel de oxígeno del Fragile Citizen.<br>- <strong>Entonces</strong> el sistema confirma el porcentaje en tiempo real catalogándolo en estado normal.<br><br><strong>Escenario 2: Hipoxemia o saturación por debajo de umbral seguro</strong><br>- <strong>Dado que</strong> el sensor de oximetría registra un valor inferior al 90% de SpO₂.<br>- <strong>Cuando</strong> el cuidador consulta el nivel de oxígeno o el sistema procesa la telemetría.<br>- <strong>Entonces</strong> el sistema clasifica inmediatamente el estado como crítico y reporta la anomalía de oxigenación.<br><br><strong>Escenario 3: Artefacto de censado por desconexión</strong><br>- <strong>Dado que</strong> la pulsera pierde contacto cutáneo continuo durante la captura fotopletismográfica.<br>- <strong>Cuando</strong> se procesa la lectura de saturación de oxígeno.<br>- <strong>Entonces</strong> el sistema suspende el cálculo de SpO₂ y registra una condición de lectura incompleta conservando el último registro válido.</td>
  </tr>
</table>

<br>

<a id="tabla-2-16"></a>**Tabla 2.16.** User Story US04: Supervisión de temperatura corporal continua

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US04</strong></td>
    <td>Cuidador</td>
    <td>High</td>
    <td>EP01 - Monitoreo de Salud en Tiempo Real</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Supervisión de temperatura corporal continua</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo supervisar las mediciones de temperatura corporal del Fragile Citizen para alertar de forma oportuna episodios febriles o cuadros de hipotermia.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Registro de normotermia</strong><br>- <strong>Dado que</strong> el sensor infrarrojo reporta una temperatura cutánea normal entre 36.0 °C y 37.2 °C.<br>- <strong>Cuando</strong> el cuidador revisa la telemetría térmica del Fragile Citizen.<br>- <strong>Entonces</strong> el sistema valida el estado térmico como normal y registra la serie temporal.<br><br><strong>Escenario 2: Detección de estado febril</strong><br>- <strong>Dado que</strong> el sensor reporta una temperatura corporal que excede los 37.8 °C de manera sostenida.<br>- <strong>Cuando</strong> el sistema procesa la medición térmica recibida.<br>- <strong>Entonces</strong> el sistema cataloga el evento como fiebre y marca visualmente la anomalía en el perfil del usuario.<br><br><strong>Escenario 3: Detección de hipotermia</strong><br>- <strong>Dado que</strong> el sensor reporta una temperatura corporal inferior a 35.0 °C.<br>- <strong>Cuando</strong> el sistema procesa la medición térmica recibida.<br>- <strong>Entonces</strong> el sistema cataloga el registro como hipotermia y genera un aviso de control inmediato.</td>
  </tr>
</table>

<br>

<a id="tabla-2-17"></a>**Tabla 2.17.** User Story US05: Visualización de frecuencia respiratoria estimada

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US05</strong></td>
    <td>Cuidador</td>
    <td>High</td>
    <td>EP01 - Monitoreo de Salud en Tiempo Real</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Visualización de frecuencia respiratoria estimada</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo examinar la frecuencia respiratoria del Fragile Citizen para monitorear su ritmo ventilatorio e identificar taquipnea o bradipnea.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Frecuencia ventilatoria normal</strong><br>- <strong>Dado que</strong> el algoritmo biomédico procesa entre 12 y 20 respiraciones por minuto (rpm).<br>- <strong>Cuando</strong> el cuidador consulta la frecuencia respiratoria del Fragile Citizen.<br>- <strong>Entonces</strong> el sistema muestra la métrica actual catalogándola dentro de los estándares fisiológicos seguros.<br><br><strong>Escenario 2: Detección de frecuencia respiratoria alterada</strong><br>- <strong>Dado que</strong> el algoritmo estima una frecuencia respiratoria superior a 24 rpm o menor a 10 rpm.<br>- <strong>Cuando</strong> el sistema procesa el flujo continuo de datos respiratorios.<br>- <strong>Entonces</strong> el sistema destaca el valor como anómalo y actualiza la condición de alerta respiratoria del Fragile Citizen.</td>
  </tr>
</table>

<br>

<a id="tabla-2-18"></a>**Tabla 2.18.** User Story US06: Emisión y confirmación de recordatorios de medicación

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US06</strong></td>
    <td>Cuidador</td>
    <td>High</td>
    <td>EP02 - Recordatorios y Rutinas de Bienestar</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Emisión y confirmación de recordatorios de medicación</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo programar las tomas de medicación del Fragile Citizen y que su pulsera emita los avisos hápticos y sonoros en los horarios exactos para asegurar la adherencia al tratamiento prescrito.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Disparo puntual del recordatorio programado</strong><br>- <strong>Dado que</strong> el cuidador ha registrado una toma de medicamento para una hora específica.<br>- <strong>Cuando</strong> el reloj del sistema alcanza la hora programada.<br>- <strong>Entonces</strong> el dispositivo emite señales vibratorias y sonoras, y el sistema marca el recordatorio como emitido.<br><br><strong>Escenario 2: Confirmación manual de ingestión de medicamento</strong><br>- <strong>Dado que</strong> el recordatorio de medicamento está activo en el dispositivo.<br>- <strong>Cuando</strong> el Fragile Citizen ejecuta la confirmación de la toma en el dispositivo.<br>- <strong>Entonces</strong> el sistema registra la dosis como administrada exitosamente y refleja el evento en la aplicación del cuidador.<br><br><strong>Escenario 3: Reintento por omisión de confirmación</strong><br>- <strong>Dado que</strong> un recordatorio ha sido emitido y no se registra la confirmación de la toma dentro de 10 minutos.<br>- <strong>Cuando</strong> expira dicho lapso de tolerancia.<br>- <strong>Entonces</strong> el sistema genera una segunda advertencia local y remite una notificación de dosis pendiente al cuidador.</td>
  </tr>
</table>

<br>

<a id="tabla-2-19"></a>**Tabla 2.19.** User Story US07: Análisis comparativo y tendencias históricas de signos vitales

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US07</strong></td>
    <td>Cuidador</td>
    <td>Medium</td>
    <td>EP01 - Monitoreo de Salud en Tiempo Real</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Análisis comparativo y tendencias históricas de signos vitales</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo revisar gráficas de tendencias históricas de los signos vitales para identificar patrones de deterioro fisiológico y compartir reportes con el médico tratante.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Generación de serie temporal consolidada</strong><br>- <strong>Dado que</strong> existen registros continuos de signos vitales durante los últimos 7 días.<br>- <strong>Cuando</strong> el cuidador solicita el análisis de tendencia para un parámetro específico y rango de fechas.<br>- <strong>Entonces</strong> el sistema consolida los valores históricos y calcula los promedios, valores mínimos y valores máximos.<br><br><strong>Escenario 2: Muestreo insuficiente para conformar tendencia</strong><br>- <strong>Dado que</strong> el período seleccionado posee menos de 12 horas acumuladas de lecturas válidas.<br>- <strong>Cuando</strong> el cuidador intenta generar la gráfica de tendencia histórica.<br>- <strong>Entonces</strong> el sistema notifica que el volumen de datos recolectado es insuficiente para emitir un gráfico representativo.</td>
  </tr>
</table>

<br>

<a id="tabla-2-20"></a>**Tabla 2.20.** User Story US08: Detección automática de caídas y despacho de emergencia

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US08</strong></td>
    <td>Familiar / Cuidador</td>
    <td>Highest</td>
    <td>EP03 - Alertas y Gestión de Emergencias</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Detección automática de caídas y despacho de emergencia</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como familiar o cuidador, deseo recibir una alerta crítica inmediata cuando la pulsera detecte un patrón de caída del Fragile Citizen para gestionar auxilio oportuno.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Identificación cinemática de caída no mitigada</strong><br>- <strong>Dado que</strong> el microcontrolador detecta una aceleración brusca seguida de impacto e inmovilidad relativa.<br>- <strong>Cuando</strong> concluye el ciclo de evaluación cinemática en el firmware.<br>- <strong>Entonces</strong> el sistema despacha una notificación de emergencia de máxima prioridad en un lapso menor a 5 segundos.<br><br><strong>Escenario 2: Cancelación por falsa alarma efectuada por el usuario</strong><br>- <strong>Dado que</strong> el sistema clasifica una caída y activa una ventana de cancelación local de 20 segundos.<br>- <strong>Cuando</strong> el Fragile Citizen activa la opción de confirmación de bienestar antes del vencimiento del temporizador.<br>- <strong>Entonces</strong> el sistema interrumpe el despacho a contactos de emergencia y clasifica el evento como falso positivo resuelto.<br><br><strong>Escenario 3: Escalamiento por falta de respuesta del usuario</strong><br>- <strong>Dado que</strong> se dispara el temporizador de alerta local por caída.<br>- <strong>Cuando</strong> el temporizador de 20 segundos culmina sin interacción del Fragile Citizen.<br>- <strong>Entonces</strong> el sistema confirma la emergencia, envía la telemetría con coordenadas GPS y activa el flujo de auxilio.</td>
  </tr>
</table>

<br>

<a id="tabla-2-21"></a>**Tabla 2.21.** User Story US09: Generación de alertas por transgresión de umbrales biomédicos

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US09</strong></td>
    <td>Familiar / Cuidador</td>
    <td>Highest</td>
    <td>EP03 - Alertas y Gestión de Emergencias</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Generación de alertas por transgresión de umbrales biomédicos</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como familiar o cuidador, deseo que el sistema genere una notificación prioritaria cuando los signos vitales del Fragile Citizen excedan los rangos seguros configurados para intervenir preventivamente.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Superación persistente de umbrales clínicos</strong><br>- <strong>Dado que</strong> una variable biomédica se mantiene fuera de los límites de seguridad durante más de 3 lecturas consecutivas.<br>- <strong>Cuando</strong> el motor de reglas procesa la telemetría entrante.<br>- <strong>Entonces</strong> el sistema genera un evento de alerta crítica con nivel de severidad correspondiente y la distribuye al cuidador.<br><br><strong>Escenario 2: Restablecimiento de valores basales seguros</strong><br>- <strong>Dado que</strong> una alerta por anomalía biomédica se encuentra activa.<br>- <strong>Cuando</strong> las lecturas biométricas retornan a valores dentro de los márgenes seguros por 5 minutos continuos.<br>- <strong>Entonces</strong> el sistema actualiza el estado del incidente a estabilizado y notifica el cierre de la anomalía al cuidador.</td>
  </tr>
</table>

<br>

<a id="tabla-2-22"></a>**Tabla 2.22.** User Story US10: Confirmación manual de estado de bienestar tras incidente

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US10</strong></td>
    <td>Familiar / Cuidador</td>
    <td>High</td>
    <td>EP03 - Alertas y Gestión de Emergencias</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Confirmación manual de estado de bienestar tras incidente</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como familiar o cuidador, deseo que el Fragile Citizen pueda descartar desde su pulsera una advertencia preventiva cuando se encuentra a salvo para evitar movilizaciones innecesarias del Care Circle ante falsas alarmas.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Notificación de resolución rápida por parte del Fragile Citizen</strong><br>- <strong>Dado que</strong> se ha emitido una advertencia preventiva en el ecosistema Guardian+.<br>- <strong>Cuando</strong> el Fragile Citizen confirma la opción de estado seguro dentro de una ventana de 30 segundos.<br>- <strong>Entonces</strong> el sistema notifica al cuidador que el evento ha sido atendido y descartado desde la pulsera por el Fragile Citizen.<br><br><strong>Escenario 2: Vencimiento de ventana de confirmación manual</strong><br>- <strong>Dado que</strong> la advertencia preventiva se encuentra activa en el dispositivo.<br>- <strong>Cuando</strong> transcurren 30 segundos continuos sin registro de interacción manual.<br>- <strong>Entonces</strong> el sistema promueve la advertencia a categoría de alerta de confirmación requerida y la despacha al cuidador.</td>
  </tr>
</table>

<br>

<a id="tabla-2-23"></a>**Tabla 2.23.** User Story US11: Escalamiento automatizado de alertas críticas no atendidas

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US11</strong></td>
    <td>Familiar / Cuidador</td>
    <td>Highest</td>
    <td>EP03 - Alertas y Gestión de Emergencias</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Escalamiento automatizado de alertas críticas no atendidas</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como familiar o cuidador, deseo que las alertas críticas no reconocidas se transmitan a contactos secundarios o entidades de apoyo para asegurar que el Fragile Citizen reciba atención de emergencia.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Reenvío a lista jerárquica de contactos de respaldo</strong><br>- <strong>Dado que</strong> se emite una alerta crítica de emergencia dirigida al cuidador primario.<br>- <strong>Cuando</strong> el cuidador primario no confirma la recepción del evento dentro de los 60 segundos posteriores.<br>- <strong>Entonces</strong> el sistema despacha la alerta de auxilio de forma simultánea a los contactos secundarios definidos.<br><br><strong>Escenario 2: Neutralización del protocolo de escalamiento</strong><br>- <strong>Dado que</strong> la alerta crítica ha sido escalada hacia contactos secundarios.<br>- <strong>Cuando</strong> cualquiera de los contactos autorizados registra el reconocimiento de la emergencia.<br>- <strong>Entonces</strong> el sistema detiene los envíos sucesivos de escalamiento y actualiza el estado a incidente en atención.</td>
  </tr>
</table>

<br>

<a id="tabla-2-24"></a>**Tabla 2.24.** User Story US12: Configuración y parametrización de niveles de alerta

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US12</strong></td>
    <td>Familiar / Cuidador</td>
    <td>Medium</td>
    <td>EP03 - Alertas y Gestión de Emergencias</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Configuración y parametrización de niveles de alerta</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como familiar o cuidador, deseo personalizar los canales y umbrales de severidad de las notificaciones para adaptar el comportamiento del sistema a los requerimientos clínicos específicos del Fragile Citizen.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Modificación de canales de notificación por severidad</strong><br>- <strong>Dado que</strong> el cuidador dispone de permisos de administración sobre el perfil del Fragile Citizen.<br>- <strong>Cuando</strong> el cuidador asigna canales específicos (vibración, notificación prioritaria, SMS) a un tipo de alerta.<br>- <strong>Entonces</strong> el sistema persiste la configuración y la aplica de forma inmediata a los eventos generados a partir de ese momento.<br><br><strong>Escenario 2: Restablecimiento de umbrales clínicos predeterminados</strong><br>- <strong>Dado que</strong> existen parámetros de alerta modificados respecto a la configuración original.<br>- <strong>Cuando</strong> el cuidador opta por restablecer los valores de fábrica.<br>- <strong>Entonces</strong> el sistema reasigna los rangos estándar definidos por las guías clínicas preconfiguradas.</td>
  </tr>
</table>

<br>

<a id="tabla-2-25"></a>**Tabla 2.25.** User Story US13: Programación y notificación de consultas médicas

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US13</strong></td>
    <td>Cuidador</td>
    <td>Medium</td>
    <td>EP02 - Recordatorios y Rutinas de Bienestar</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Programación y notificación de consultas médicas</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo agendar los controles y citas médicas del Fragile Citizen para recibir avisos preventivos y evitar inasistencias a los centros de salud.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Generación de recordatorio previo a la cita</strong><br>- <strong>Dado que</strong> existe una cita médica registrada en el calendario del Fragile Citizen.<br>- <strong>Cuando</strong> el tiempo restante coincide con la antelación configurada por el cuidador (por ejemplo, 1 hora antes).<br>- <strong>Entonces</strong> el sistema genera una notificación preventiva tanto en el dispositivo del Fragile Citizen como en el del cuidador.<br><br><strong>Escenario 2: Cancelación de evento programado</strong><br>- <strong>Dado que</strong> una cita médica agendada es anulada por el cuidador en el sistema.<br>- <strong>Cuando</strong> se confirma la cancelación de la cita.<br>- <strong>Entonces</strong> el sistema desactiva los temporizadores asociados y purga los recordatorios pendientes correspondientes.</td>
  </tr>
</table>

<br>

<a id="tabla-2-26"></a>**Tabla 2.26.** User Story US14: Recordatorios programados para actividad física ligera

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US14</strong></td>
    <td>Cuidador</td>
    <td>Low</td>
    <td>EP02 - Recordatorios y Rutinas de Bienestar</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Recordatorios programados para actividad física ligera</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo programar recordatorios de pausas activas y ejercicios de movilidad suave en la pulsera del Fragile Citizen para contribuir a la conservación de su autonomía funcional.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Disparo de rutina de ejercicio planificada</strong><br>- <strong>Dado que</strong> el cuidador ha configurado un plan de actividad física para un horario definido.<br>- <strong>Cuando</strong> el reloj del sistema coincide con dicho horario.<br>- <strong>Entonces</strong> la pulsera emite una señal háptica indicando el inicio del bloque de actividad física.<br><br><strong>Escenario 2: Registro de cumplimiento de actividad</strong><br>- <strong>Dado que</strong> el recordatorio de actividad física ha sido presentado al Fragile Citizen.<br>- <strong>Cuando</strong> el Fragile Citizen confirma la finalización del ejercicio en el dispositivo.<br>- <strong>Entonces</strong> el sistema incrementa el contador de adherencia a rutinas de movilidad en el registro diario consultable por el cuidador.</td>
  </tr>
</table>

<br>

<a id="tabla-2-27"></a>**Tabla 2.27.** User Story US15: Activación de auxilio mediante botón SOS en pulsera

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US15</strong></td>
    <td>Familiar / Cuidador</td>
    <td>Highest</td>
    <td>EP03 - Alertas y Gestión de Emergencias</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Activación de auxilio mediante botón SOS en pulsera</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como familiar o cuidador, deseo recibir un aviso de auxilio de máxima prioridad cuando el Fragile Citizen presione el botón SOS físico de la pulsera para acudir de inmediato sin que él dependa del teléfono móvil.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Disparo efectivo por pulsación sostenida</strong><br>- <strong>Dado que</strong> la pulsera se encuentra encendida y con enlace de datos disponible.<br>- <strong>Cuando</strong> el Fragile Citizen presiona el botón físico de SOS por al menos 3 segundos continuos.<br>- <strong>Entonces</strong> el sistema despacha de forma inmediata un evento de auxilio de máxima severidad a los contactos de emergencia registrados, incluyendo la ubicación actual.<br><br><strong>Escenario 2: Aborto preventivo por pulsación involuntaria</strong><br>- <strong>Dado que</strong> el Fragile Citizen presiona el botón de SOS por un lapso inferior a 3 segundos.<br>- <strong>Cuando</strong> se libera la presión del botón sin alcanzar el umbral requerido.<br>- <strong>Entonces</strong> el dispositivo descarta la acción y evita el despacho de cualquier evento de alarma.</td>
  </tr>
</table>

<br>

<a id="tabla-2-28"></a>**Tabla 2.28.** User Story US16: Administración de agenda de contactos de auxilio

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US16</strong></td>
    <td>Cuidador</td>
    <td>High</td>
    <td>EP03 - Alertas y Gestión de Emergencias</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Administración de agenda de contactos de auxilio</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo registrar y ordenar los contactos prioritarios de emergencia para garantizar que las notificaciones críticas se canalicen a las personas correctas.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Incorporación de nuevo contacto de auxilio válido</strong><br>- <strong>Dado que</strong> el cuidador ingresa nombre completo, parentesco y número telefónico con código internacional válido.<br>- <strong>Cuando</strong> se solicita el guardado del nuevo contacto.<br>- <strong>Entonces</strong> el sistema valida la integridad de los datos, almacena el registro y lo asocia a la cadena de alertas.<br><br><strong>Escenario 2: Retiro de contacto de emergencia obsoleto</strong><br>- <strong>Dado que</strong> un contacto de emergencia existe en el directorio del Fragile Citizen.<br>- <strong>Cuando</strong> el cuidador elimina dicho contacto y la lista mantiene al menos un contacto primario.<br>- <strong>Entonces</strong> el sistema actualiza la lista de distribución excluyendo al contacto removido de futuros eventos.</td>
  </tr>
</table>

<br>

<a id="tabla-2-29"></a>**Tabla 2.29.** User Story US17: Estimación y registro de fases de sueño

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US17</strong></td>
    <td>Cuidador</td>
    <td>Low</td>
    <td>EP02 - Recordatorios y Rutinas de Bienestar</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Estimación y registro de fases de sueño</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo acceder al registro de descanso nocturno del Fragile Citizen para evaluar la calidad del sueño e identificar patrones de insomnio o agitación.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Procesamiento consolidado de descanso nocturno</strong><br>- <strong>Dado que</strong> la pulsera recopila datos de micromovimientos y frecuencia cardíaca durante la ventana nocturna.<br>- <strong>Cuando</strong> el sistema procesa el intervalo al inicio de la mañana.<br>- <strong>Entonces</strong> el sistema computa el total de horas de sueño, la continuidad del descanso y el número de despertares.<br><br><strong>Escenario 2: Identificación de descanso interrumpido atípico</strong><br>- <strong>Dado que</strong> el análisis de telemetría detecta más de 4 interrupciones prolongadas en una sola noche.<br>- <strong>Cuando</strong> se consolida el reporte matutino.<br>- <strong>Entonces</strong> el sistema cataloga la sesión de descanso como sueño fragmentado y lo registra en el historial del Fragile Citizen.</td>
  </tr>
</table>

<br>

<a id="tabla-2-30"></a>**Tabla 2.30.** User Story US18: Telemetría de geolocalización en tiempo real

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US18</strong></td>
    <td>Cuidador</td>
    <td>Highest</td>
    <td>EP04 - Localización y Seguridad en Movilidad</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Telemetría de geolocalización en tiempo real</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo consultar las coordenadas de ubicación en tiempo real del Fragile Citizen para verificar su paradero y actuar rápidamente si sufre una desorientación.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Transmisión de coordenadas en condiciones normales</strong><br>- <strong>Dado que</strong> el receptor GNSS de la pulsera dispone de cobertura satelital activa.<br>- <strong>Cuando</strong> el cuidador solicita la posición actual del Fragile Citizen.<br>- <strong>Entonces</strong> el sistema entrega las coordenadas de latitud y longitud con una marca de tiempo actualizada dentro de los últimos 30 segundos.<br><br><strong>Escenario 2: Degradación de señal satelital en interiores</strong><br>- <strong>Dado que</strong> la pulsera entra en una zona subterránea o sin cobertura GNSS.<br>- <strong>Cuando</strong> se solicita la localización geográfica del Fragile Citizen.<br>- <strong>Entonces</strong> el sistema expone el último punto geográfico válido conocido indicando explícitamente la pérdida momentánea de fijación satelital.</td>
  </tr>
</table>

<br>

<a id="tabla-2-31"></a>**Tabla 2.31.** User Story US19: Exportación de reporte cronológico de telemetría médica

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US19</strong></td>
    <td>Cuidador</td>
    <td>Medium</td>
    <td>EP01 - Monitoreo de Salud en Tiempo Real</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Exportación de reporte cronológico de telemetría médica</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo generar y exportar el historial de signos vitales en formato estandarizado para respaldar las consultas médicas presenciales.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Exportación exitosa de expediente de telemetría</strong><br>- <strong>Dado que</strong> el Fragile Citizen cuenta con mediciones registradas durante un intervalo de 30 días.<br>- <strong>Cuando</strong> el cuidador selecciona el rango y solicita la exportación documental.<br>- <strong>Entonces</strong> el sistema compila un reporte estructurado en formato PDF conteniendo tablas y resúmenes de las anomalías detectadas.<br><br><strong>Escenario 2: Solicitud de exportación en rango vacío</strong><br>- <strong>Dado que</strong> no existen lecturas de signos vitales dentro del período seleccionado.<br>- <strong>Cuando</strong> el cuidador intenta ejecutar la exportación documental.<br>- <strong>Entonces</strong> el sistema bloquea la generación del archivo y notifica que no existen registros en el rango indicado.</td>
  </tr>
</table>

<br>

<a id="tabla-2-32"></a>**Tabla 2.32.** User Story US20: Notificación de nivel crítico de batería en wearable

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US20</strong></td>
    <td>Cuidador</td>
    <td>High</td>
    <td>EP03 - Alertas y Gestión de Emergencias</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Notificación de nivel crítico de batería en wearable</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo recibir una advertencia oportuna cuando la batería de la pulsera del Fragile Citizen descienda del 20% para coordinar su recarga y evitar la suspensión del monitoreo.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Advertencia preventiva por descarga progresiva</strong><br>- <strong>Dado que</strong> el circuito de carga de la pulsera mide un remanente igual o menor al 20% de energía.<br>- <strong>Cuando</strong> se procesa la lectura periódica del estado de la batería.<br>- <strong>Entonces</strong> el dispositivo activa un aviso de recarga necesaria y envía una notificación preventiva a la aplicación del cuidador.<br><br><strong>Escenario 2: Umbral de apagado inminente</strong><br>- <strong>Dado que</strong> el nivel de batería alcanza un 5% de capacidad residual.<br>- <strong>Cuando</strong> el dispositivo evalúa su reserva energética crítica.<br>- <strong>Entonces</strong> el sistema emite una última telemetría con prioridad crítica avisando del cese temporal inminente de la supervisión.</td>
  </tr>
</table>

<br>

<a id="tabla-2-33"></a>**Tabla 2.33.** User Story US21: Sincronización y persistencia resiliente de telemetría (Offline Sync)

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US21</strong></td>
    <td>Cuidador</td>
    <td>High</td>
    <td>EP01 - Monitoreo de Salud en Tiempo Real</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Sincronización y persistencia resiliente de telemetría (Offline Sync)</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo que los datos recopilados por la pulsera durante pérdidas de red se almacenen localmente y se sincronicen al recuperar conexión para garantizar la integridad histórica.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Buffer local por indisponibilidad de conexión</strong><br>- <strong>Dado que</strong> el dispositivo wearable pierde conexión a la red de datos durante su operación.<br>- <strong>Cuando</strong> se efectúan nuevas lecturas biométricas o de incidentes.<br>- <strong>Entonces</strong> el microcontrolador persiste las tramas localmente en su memoria no volátil manteniendo el orden cronológico.<br><br><strong>Escenario 2: Vaciado automático de buffer tras reconexión</strong><br>- <strong>Dado que</strong> existen tramas biométricas retenidas en la memoria local del dispositivo.<br>- <strong>Cuando</strong> se restablece el enlace inalámbrico con el backend.<br>- <strong>Entonces</strong> el dispositivo transmite en bloque la telemetría pendiente y el servidor las persiste eliminando registros duplicados.</td>
  </tr>
</table>

<br>

<a id="tabla-2-34"></a>**Tabla 2.34.** User Story US22: Silenciamiento de alertas no críticas en el Care Circle

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US22</strong></td>
    <td>Cuidador</td>
    <td>Low</td>
    <td>EP03 - Alertas y Gestión de Emergencias</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Silenciamiento de alertas no críticas en el Care Circle</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo silenciar las alertas no críticas del Fragile Citizen en los celulares del Care Circle para no ser interrumpido por avisos menores, por ejemplo durante la noche, sin dejar de enterarme de una emergencia.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Activación del modo silencioso</strong><br>- <strong>Dado que</strong> el modo silencioso del Fragile Citizen está desactivado.<br>- <strong>Cuando</strong> el cuidador lo activa desde Configuración de alertas y se genera una alerta de severidad alta o media.<br>- <strong>Entonces</strong> el sistema la notifica sin sonido a los integrantes del Care Circle y la mantiene visible en la aplicación.<br><br><strong>Escenario 2: Excepción para alertas críticas</strong><br>- <strong>Dado que</strong> el modo silencioso del Fragile Citizen está activo.<br>- <strong>Cuando</strong> se genera una alerta de severidad crítica, como una caída o un SOS.<br>- <strong>Entonces</strong> el sistema la notifica con sonido a todos sus destinatarios.</td>
  </tr>
</table>

<br>

<a id="tabla-2-35"></a>**Tabla 2.35.** User Story US23: Establecimiento de canal de comunicación directa

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US23</strong></td>
    <td>Familiar</td>
    <td>Medium</td>
    <td>EP04 - Localización y Seguridad en Movilidad</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Establecimiento de canal de comunicación directa</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como familiar, deseo iniciar un canal de comunicación rápida con el Fragile Citizen, mediante videollamada o llamada de voz según la capacidad del modelo de pulsera vinculado, para verificar su condición ante cualquier sospecha o inquietud cotidiana.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Videollamada en pulsera con cámara y pantalla</strong><br>- <strong>Dado que</strong> la pulsera vinculada al Fragile Citizen corresponde a un modelo con cámara y pantalla, y ambos dispositivos mantienen conexión de datos activa.<br>- <strong>Cuando</strong> el familiar solicita la apertura de una videollamada desde la aplicación.<br>- <strong>Entonces</strong> el sistema establece la sesión de vídeo en la pulsera y confirma la conexión entre ambas partes.<br><br><strong>Escenario 2: Degradación a llamada de voz por limitación del modelo</strong><br>- <strong>Dado que</strong> la pulsera vinculada admite audio bidireccional pero no dispone de cámara.<br>- <strong>Cuando</strong> el familiar solicita una videollamada.<br>- <strong>Entonces</strong> el sistema informa que el modelo no admite vídeo y establece la sesión como llamada de voz, sin requerir una nueva solicitud.<br><br><strong>Escenario 3: Modelo sin capacidad de comunicación bidireccional</strong><br>- <strong>Dado que</strong> la pulsera vinculada solo admite telemetría, avisos hápticos y la activación del botón SOS.<br>- <strong>Cuando</strong> el familiar intenta abrir un canal de comunicación con el Fragile Citizen.<br>- <strong>Entonces</strong> el sistema indica que el modelo vinculado no admite llamadas y ofrece la marcación telefónica al número registrado de la persona bajo cuidado o de su acompañante.<br><br><strong>Escenario 4: Llamada no contestada</strong><br>- <strong>Dado que</strong> se emite la señal de comunicación hacia el dispositivo receptor.<br>- <strong>Cuando</strong> transcurren 30 segundos sin que el receptor atienda la solicitud.<br>- <strong>Entonces</strong> el sistema cierra el intento de conexión y genera un registro de llamada no atendida en el historial del cuidador.</td>
  </tr>
</table>

<br>

<a id="tabla-2-36"></a>**Tabla 2.36.** User Story US24: Consolidación y despacho de reporte semanal de salud

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US24</strong></td>
    <td>Cuidador</td>
    <td>Medium</td>
    <td>EP01 - Monitoreo de Salud en Tiempo Real</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Consolidación y despacho de reporte semanal de salud</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo recibir una síntesis semanal automatizada del estado de salud del Fragile Citizen para evaluar su evolución global sin revisar telemetría segundo a segundo.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Compilación automática al cierre de ciclo semanal</strong><br>- <strong>Dado que</strong> culmina el ciclo operativo de 7 días del Fragile Citizen.<br>- <strong>Cuando</strong> el servicio de reportes ejecuta su tarea programada de cierre.<br>- <strong>Entonces</strong> el sistema genera una síntesis agregando estabilidad de signos vitales, alertas disparadas y porcentaje de adherencia a medicación.<br><br><strong>Escenario 2: Resaltado de incidentes recurrentes</strong><br>- <strong>Dado que</strong> el Fragile Citizen experimentó más de 3 anomalías del mismo tipo a lo largo de la semana.<br>- <strong>Cuando</strong> se genera la síntesis semanal.<br>- <strong>Entonces</strong> el sistema marca el parámetro como recurrente e incluye una recomendación de revisión médica preventiva.</td>
  </tr>
</table>

<br>

<a id="tabla-2-37"></a>**Tabla 2.37.** User Story US25: Despacho simultáneo a múltiples contactos de auxilio

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US25</strong></td>
    <td>Familiar</td>
    <td>High</td>
    <td>EP03 - Alertas y Gestión de Emergencias</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Despacho simultáneo a múltiples contactos de auxilio</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como familiar, deseo que las alertas de máxima criticidad se remitan simultáneamente a todo el Care Circle registrado para maximizar la velocidad de respuesta.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Difusión simultánea ante evento crítico</strong><br>- <strong>Dado que</strong> se confirma una emergencia crítica (como caída o SOS manual).<br>- <strong>Cuando</strong> el motor de despacho procesa el incidente.<br>- <strong>Entonces</strong> el sistema emite notificaciones simultáneas a todos los contactos registrados en el Care Circle activo.<br><br><strong>Escenario 2: Notificación colaborativa de atención confirmada</strong><br>- <strong>Dado que</strong> múltiples familiares recibieron la notificación de emergencia en paralelo.<br>- <strong>Cuando</strong> el primer familiar pulsa la opción de acudir al auxilio.<br>- <strong>Entonces</strong> el sistema distribuye una actualización al resto de los contactos informando que dicho integrante ya asumió la respuesta.</td>
  </tr>
</table>

<br>

<a id="tabla-2-38"></a>**Tabla 2.38.** User Story US26: Recordatorios periódicos de hidratación y pausas activas

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US26</strong></td>
    <td>Cuidador</td>
    <td>Low</td>
    <td>EP02 - Recordatorios y Rutinas de Bienestar</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Recordatorios periódicos de hidratación y pausas activas</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo que la pulsera del Fragile Citizen le recuerde periódicamente tomar agua o levantarse para prevenir la deshidratación y la rigidez articular.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Notificación de intervalo de hidratación</strong><br>- <strong>Dado que</strong> transcurren 120 minutos consecutivos sin registro de confirmación de ingesta hídrica.<br>- <strong>Cuando</strong> se cumple la ventana de tiempo establecida.<br>- <strong>Entonces</strong> el dispositivo emite un patrón de vibración indicando el recordatorio de hidratación.<br><br><strong>Escenario 2: Supresión durante horas de descanso</strong><br>- <strong>Dado que</strong> el sistema identifica que el Fragile Citizen se encuentra dentro del rango horario de sueño nocturno.<br>- <strong>Cuando</strong> vence el ciclo de hidratación periódica.<br>- <strong>Entonces</strong> el sistema inhibe la emisión del recordatorio para resguardar el descanso del Fragile Citizen.</td>
  </tr>
</table>

<br>

<a id="tabla-2-39"></a>**Tabla 2.39.** User Story US27: Detección de inactividad física prolongada

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US27</strong></td>
    <td>Cuidador</td>
    <td>Medium</td>
    <td>EP02 - Recordatorios y Rutinas de Bienestar</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Detección de inactividad física prolongada</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo ser alertado si el Fragile Citizen permanece inmóvil por un período anómalo durante el día para descartar episodios de desvanecimiento o auxilio retenido.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Superación de umbral de inmovilidad en horas diurnas</strong><br>- <strong>Dado que</strong> el Fragile Citizen no presenta movimiento articular durante más de 60 minutos en su jornada activa.<br>- <strong>Cuando</strong> se evalúa el contador de inactividad física.<br>- <strong>Entonces</strong> el sistema despacha un aviso preventivo de inactividad prolongada al cuidador.<br><br><strong>Escenario 2: Restablecimiento de conteo por detección motriz</strong><br>- <strong>Dado que</strong> el contador de inactividad acumula 45 minutos continuos.<br>- <strong>Cuando</strong> los acelerómetros del dispositivo detectan patrones de marcha o desplazamiento físico.<br>- <strong>Entonces</strong> el sistema reinicia el contador a cero sin generar ningún tipo de alarma.</td>
  </tr>
</table>

<br>

<a id="tabla-2-40"></a>**Tabla 2.40.** User Story US28: Delimitación y monitoreo perimetral mediante geocercas múltiples

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US28</strong></td>
    <td>Cuidador</td>
    <td>High</td>
    <td>EP04 - Localización y Seguridad en Movilidad</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Delimitación y monitoreo perimetral mediante geocercas múltiples</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como cuidador, deseo delimitar zonas geográficas seguras (hogar, parque, club) para ser alertado oportunamente si el Fragile Citizen cruza los perímetros autorizados.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Detección de salida de zona segura autorizada</strong><br>- <strong>Dado que</strong> el Fragile Citizen dispone de una o más geocercas activas configuradas con coordenadas y radio métrico.<br>- <strong>Cuando</strong> las coordenadas del receptor GPS se posicionan de forma sostenida fuera de todas las zonas seguras activas.<br>- <strong>Entonces</strong> el sistema genera una alerta de egreso de perímetro seguro y la remite de inmediato al cuidador.<br><br><strong>Escenario 2: Reingreso automático al perímetro seguro</strong><br>- <strong>Dado que</strong> el Fragile Citizen se encuentra registrada fuera del perímetro seguro.<br>- <strong>Cuando</strong> las coordenadas actualizadas confirman su retorno al interior del área delimitada.<br>- <strong>Entonces</strong> el sistema notifica el reingreso a la zona de seguridad y restablece la condición de vigilancia regular.</td>
  </tr>
</table>

<br>

<a id="tabla-2-41"></a>**Tabla 2.41.** User Story US29: Previsión de agotamiento de stock y pedidos de medicinas

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US29</strong></td>
    <td>Familiar</td>
    <td>Low</td>
    <td>EP02 - Recordatorios y Rutinas de Bienestar</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Previsión de agotamiento de stock y pedidos de medicinas</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como familiar, deseo recibir avisos de reabastecimiento cuando las dosis prescritas estén por terminarse para coordinar oportunamente la compra de medicamentos.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Generación de advertencia por saldo bajo de medicamentos</strong><br>- <strong>Dado que</strong> el conteo de dosis registradas en el tratamiento indica una disponibilidad remanente para 3 días o menos.<br>- <strong>Cuando</strong> el sistema computa el balance de consumo diario.<br>- <strong>Entonces</strong> se emite un recordatorio de reposición al familiar sugiriendo la reposición del medicamento prescrito.<br><br><strong>Escenario 2: Actualización de stock farmacéutico tras adquisición</strong><br>- <strong>Dado que</strong> el familiar confirma la adquisición de un nuevo envase de medicamento en la plataforma.<br>- <strong>Cuando</strong> se ingresa la cantidad de unidades adicionadas.<br>- <strong>Entonces</strong> el sistema recalcula el balance total y actualiza la fecha estimada del próximo requerimiento de compra.</td>
  </tr>
</table>

<br>

<a id="tabla-2-42"></a>**Tabla 2.42.** User Story US30: Navegación entre secciones informativas de la Landing Page

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US30</strong></td>
    <td>Visitante</td>
    <td>Medium</td>
    <td>EP05 - Presencia Web y Adquisición (Landing Page)</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Navegación entre secciones informativas de la Landing Page</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como visitante, deseo navegar de forma fluida entre las diferentes secciones del portal web para conocer rápidamente la propuesta de valor, funciones y testimonios de Guardian+.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Transición dirigida mediante elementos de navegación</strong><br>- <strong>Dado que</strong> el visitante se encuentra explorando cualquier bloque de la Landing Page.<br>- <strong>Cuando</strong> el visitante selecciona un enlace del menú principal de navegación.<br>- <strong>Entonces</strong> el navegador efectúa un desplazamiento animado hacia el bloque seleccionado y actualiza el estado activo de la opción.<br><br><strong>Escenario 2: Fijación contextual de la barra de navegación</strong><br>- <strong>Dado que</strong> el visitante realiza desplazamiento vertical superando el área superior de bienvenida.<br>- <strong>Cuando</strong> la posición de scroll sobrepasa el umbral inicial de la página.<br>- <strong>Entonces</strong> la barra de navegación permanece anclada en la parte superior manteniendo accesibles los accesos a todas las secciones.</td>
  </tr>
</table>

<br>

<a id="tabla-2-43"></a>**Tabla 2.43.** User Story US31: Presentación de características y beneficios clave del sistema

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US31</strong></td>
    <td>Visitante</td>
    <td>Medium</td>
    <td>EP05 - Presencia Web y Adquisición (Landing Page)</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Presentación de características y beneficios clave del sistema</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como visitante, deseo examinar las ventajas comparativas y capacidades de Guardian+ en la Landing Page para evaluar si satisface los requerimientos de cuidado de mi familia.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Despliegue de capacidades y arquitectura de valor</strong><br>- <strong>Dado que</strong> el visitante accede al portal desde un navegador web compatible.<br>- <strong>Cuando</strong> se presenta la sección de características del producto.<br>- <strong>Entonces</strong> el sistema expone los pilares de la solución (sensores biomédicos, detección de caídas, geolocalización y lazo familiar) de forma ordenada y legible.<br><br><strong>Escenario 2: Interacción con componentes informativos de producto</strong><br>- <strong>Dado que</strong> los bloques explicativos de beneficios se encuentran renderizados en la página.<br>- <strong>Cuando</strong> el visitante interactúa sobre cada beneficio presentado.<br>- <strong>Entonces</strong> el sistema expone información complementaria detallando el impacto funcional de cada capacidad.</td>
  </tr>
</table>

<br>

<a id="tabla-2-44"></a>**Tabla 2.44.** User Story US32: Captura y procesamiento de solicitudes de contacto institucional

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US32</strong></td>
    <td>Visitante</td>
    <td>Medium</td>
    <td>EP05 - Presencia Web y Adquisición (Landing Page)</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Captura y procesamiento de solicitudes de contacto institucional</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como visitante, deseo enviar mis dudas o consultas comerciales a través de un formulario de contacto web para recibir orientación directa del equipo de Guardian+.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Envío de solicitud con datos íntegros</strong><br>- <strong>Dado que</strong> el visitante ingresa nombre completo, correo con sintaxis válida y mensaje explicativo.<br>- <strong>Cuando</strong> el visitante confirma el envío del formulario de contacto.<br>- <strong>Entonces</strong> el sistema persiste la consulta, emite acuse de recibo en pantalla y despacha un correo de confirmación al remitente.<br><br><strong>Escenario 2: Rechazo por omisión o formato inválido de datos</strong><br>- <strong>Dado que</strong> el visitante intenta remitir el formulario omitiendo campos mandatorios o con un formato de correo erróneo.<br>- <strong>When</strong> el visitante ejecuta la acción de envío.<br>- <strong>Then</strong> el sistema interrumpe el procesamiento, marca los campos en error y mantiene los datos previamente ingresados.</td>
  </tr>
</table>

<br>

<a id="tabla-2-45"></a>**Tabla 2.45.** User Story US33: Visualización comparativa de planes de suscripción Guardian+

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>US33</strong></td>
    <td>Visitante</td>
    <td>Medium</td>
    <td>EP05 - Presencia Web y Adquisición (Landing Page)</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Visualización comparativa de planes de suscripción Guardian+</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como visitante interesado, deseo comparar los planes de suscripción y sus beneficios asociados para elegir el esquema comercial más adecuado a mis necesidades.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Comparativa de tarifas y coberturas disponibles</strong><br>- <strong>Dado que</strong> existen planes comerciales parametrizados en la plataforma (básico, familiar, premium).<br>- <strong>Cuando</strong> el visitante consulta la sección de tarifas y suscripciones.<br>- <strong>Entonces</strong> el sistema expone los costos periódicos, las inclusiones de servicio y los métodos de pago aceptados.<br><br><strong>Escenario 2: Selección y redirección hacia flujo de adquisición</strong><br>- <strong>Dado que</strong> el visitante examina la tabla comparativa de planes comerciales.<br>- <strong>Cuando</strong> el visitante selecciona la opción de contratación en un plan seleccionado.<br>- <strong>Entonces</strong> el sistema canaliza la sesión hacia el flujo de registro y procesamiento de pago correspondiente al plan elegido.</td>
  </tr>
</table>

<br>

<a id="tabla-2-46"></a>**Tabla 2.46.** Technical Story TS01: Endpoint RESTful para consulta y filtrado de incidentes y alertas

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>TS01</strong></td>
    <td>Developer</td>
    <td>High</td>
    <td>EP06 - Servicios de Integración y Plataforma Backend</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Endpoint RESTful para consulta y filtrado de incidentes y alertas</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, deseo disponer de un endpoint RESTful `/api/v1/incidents` para consultar, paginar y filtrar incidentes registrados por rango de fechas, tipo de evento y severidad clínica.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Consulta de incidentes autorizada y exitosa</strong><br>- <strong>Dado que</strong> la base de datos de telemetría está operativa y el cliente HTTP remite un token JWT de autorización válido.<br>- <strong>Cuando</strong> el Developer envía una petición <code>GET /api/v1/incidents?patientId={id}&page=1&size=20</code>.<br>- <strong>Entonces</strong> la API retorna el código de estado HTTP 200 OK junto con una carga JSON paginada con los incidentes requeridos.<br><br><strong>Escenario 2: Petición sin cabecera de autenticación válida</strong><br>- <strong>Dado que</strong> la solicitud HTTP no incluye un token de autorización o este ha expirado.<br>- <strong>Cuando</strong> el cliente realiza un requerimiento <code>GET /api/v1/incidents</code>.<br>- <strong>Entonces</strong> la API intercepta la petición y responde con el código de estado HTTP 401 Unauthorized y un cuerpo de error descriptivo.<br><br><strong>Escenario 3: Filtro por severidad crítica sin resultados asociados</strong><br>- <strong>Dado que</strong> una persona monitoreada no posee registros clasificados bajo el nivel de criticidad solicitado.<br>- <strong>Cuando</strong> el Developer envía una petición <code>GET /api/v1/incidents?patientId={id}&severity=CRITICAL</code>.<br>- <strong>Entonces</strong> la API devuelve el código HTTP 200 OK conteniendo un arreglo JSON vacío y metadatos de paginación en cero.</td>
  </tr>
</table>

<br>

<a id="tabla-2-47"></a>**Tabla 2.47.** Technical Story TS02: Endpoint RESTful para ingesta de telemetría biomédica por lotes

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>TS02</strong></td>
    <td>Developer</td>
    <td>High</td>
    <td>EP06 - Servicios de Integración y Plataforma Backend</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Endpoint RESTful para ingesta de telemetría biomédica por lotes</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como Developer, deseo implementar un endpoint `POST /api/v1/telemetry/batches` que procese y valide cargas útiles por lotes provenientes del wearable o gateway móvil.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Ingesta de lote biométrico estructurado correctamente</strong><br>- <strong>Dado que</strong> el lote enviado contiene lecturas con marcas de tiempo ISO-8601, identificador de pulsera y mediciones fisiológicas válidas.<br>- <strong>Cuando</strong> se efectúa una petición <code>POST /api/v1/telemetry/batches</code> con autenticación válida de dispositivo.<br>- <strong>Entonces</strong> la API persiste las mediciones en la base de datos de series temporales y retorna el código de estado HTTP 202 Accepted.<br><br><strong>Escenario 2: Ingesta rechazada por malformación de esquema</strong><br>- <strong>Dado que</strong> la carga útil contiene campos numéricos fuera de los rangos admisibles o carece de identificador de dispositivo.<br>- <strong>Cuando</strong> se efectúa una petición <code>POST /api/v1/telemetry/batches</code>.<br>- <strong>Entonces</strong> la API rechaza el procesamiento retornando el código HTTP 422 Unprocessable Entity detallando los campos inválidos.</td>
  </tr>
</table>

<br>

<a id="tabla-2-48"></a>**Tabla 2.48.** Spike SP01: Investigación de protocolos de transporte ligero y telemetría MQTT sobre ESP32-S3

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>SP01</strong></td>
    <td>Developer</td>
    <td>High</td>
    <td>EP07 - Spikes de Investigación Técnica</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Investigación de protocolos de transporte ligero y telemetría MQTT sobre ESP32-S3</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como equipo de desarrollo, deseamos investigar, comparar y prototipar la transmisión de telemetría biométrica mediante MQTT y WebSockets sobre el microcontrolador ESP32-S3 para determinar el balance óptimo entre latencia de alerta (menor a 5 segundos) y consumo de batería.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Evaluación y prueba de rendimiento de latencia y sobrecarga de red</strong><br>- <strong>Dado que</strong> se despliega un broker de mensajería de prueba (EMQX/HiveMQ) y un entorno de prototipado con firmware en ESP-IDF.<br>- <strong>Cuando</strong> el desarrollador mide los tiempos de entrega de mensajes de alerta simulados bajo MQTT con QoS 1 frente a WebSockets bajo condiciones de cobertura 4G/WiFi variables.<br>- <strong>Entonces</strong> el desarrollador elabora un reporte comparativo documentando los tiempos de latencia observados y la sobrecarga de bytes por trama transmitida.<br><br><strong>Escenario 2: Prototipo funcional de reconexión y almacenamiento en buffer local</strong><br>- <strong>Dado que</strong> se simula una caída forzada del enlace inalámbrico durante la ejecución del firmware del ESP32-S3.<br>- <strong>Cuando</strong> el microcontrolador retiene lecturas simuladas en memoria flash y detecta la reanudación del canal de comunicación.<br>- <strong>Entonces</strong> el prototipo ejecuta la retransmisión completa sin pérdidas de tramas y el proceso queda evidenciado en un repositorio y reporte técnico.<br><br><strong>Definition of Done (DoD):</strong><br>- Código fuente del firmware prototipo disponible en una rama del repositorio de GitHub.<br>- Reporte técnico comparativo documentado con conclusiones sobre consumo de energía y latencia.<br>- Refinamiento de historias técnicas de backend y firmware basadas en el protocolo seleccionado.<br>- Límite de tiempo (Timebox): 16 horas de desarrollo e investigación.</td>
  </tr>
</table>

<br>

<a id="tabla-2-49"></a>**Tabla 2.49.** Spike SP02: Investigación de pasarela de pagos y cobro recurrente de suscripciones con Stripe

<table>
  <tr>
    <th style="width: 20%;">Story ID</th>
    <th style="width: 25%;">User</th>
    <th style="width: 20%;">Priority</th>
    <th style="width: 35%;">Epic</th>
  </tr>
  <tr>
    <td><strong>SP02</strong></td>
    <td>Developer</td>
    <td>Medium</td>
    <td>EP07 - Spikes de Investigación Técnica</td>
  </tr>
  <tr>
    <th>Title</th>
    <td colspan="3"><strong>Investigación de pasarela de pagos y cobro recurrente de suscripciones con Stripe</strong></td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Description</th>
  </tr>
  <tr>
    <td colspan="4">Como equipo de desarrollo, deseamos investigar e implementar una prueba de concepto mínima con la API de Stripe para validar la integración de cobros recurrentes de suscripciones tanto en la aplicación web como en los clientes móviles.</td>
  </tr>
  <tr>
    <th colspan="4" style="text-align: center;">Acceptance Criteria</th>
  </tr>
  <tr>
    <td colspan="4"><strong>Escenario 1: Análisis de compatibilidad de flujos Checkout y Payment Intents</strong><br>- <strong>Dado que</strong> el equipo requiere determinar la arquitectura más segura y costo-eficiente para gestionar planes de suscripción mensual.<br>- <strong>Cuando</strong> el desarrollador analiza la integración de Stripe Billing mediante webhooks y componentes móviles.<br>- <strong>Entonces</strong> el desarrollador documenta el flujo de autenticación, cumplimiento PCI-DSS y gestión de estados de pago en un reporte técnico compartido.<br><br><strong>Escenario 2: Prueba de concepto funcional en entorno Sandbox</strong><br>- <strong>Dado que</strong> se dispone de credenciales de prueba de la API de Stripe y un endpoint webhook en el backend.<br>- <strong>Cuando</strong> se ejecuta una transacción simulada de suscripción mensual con tarjetas de prueba.<br>- <strong>Entonces</strong> el backend procesa el evento <code>invoice.paid</code>, actualiza el estado de la suscripción y registra el ciclo de facturación exitosamente.<br><br><strong>Definition of Done (DoD):</strong><br>- Prueba de concepto (PoC) operativa en rama de desarrollo probada en entorno Sandbox.<br>- Diagrama de secuencia de integración y reporte de comisiones y consideraciones legales documentado.<br>- Historias de usuario para el módulo de facturación refinadas y estimadas en el Product Backlog.<br>- Límite de tiempo (Timebox): 12 horas de investigación y prototipado.</td>
  </tr>
</table>

### 2.4.2. Impact Mapping

El Impact Mapping de Guardian+ permite relacionar los objetivos de negocio de la solución con los actores que participan en el ecosistema, los cambios de comportamiento esperados en cada uno de ellos y los entregables que permitirán generar dichos impactos.

Para este análisis se consideran tres actores principales: los familiares, los cuidadores y las personas bajo cuidado, conformadas principalmente por adultos mayores, personas con discapacidad o personas en situación de dependencia. El mapa permite mantener trazabilidad entre las necesidades del negocio, el comportamiento esperado de los usuarios, las funcionalidades planteadas y las User Stories definidas previamente.

El objetivo de negocio planteado busca mejorar de manera integral la efectividad del cuidado remoto y favorecer la adopción de Guardian+. Durante los primeros seis meses del piloto se espera alcanzar un uso recurrente de la plataforma por parte de al menos el 70% de los familiares y cuidadores activos, lograr que al menos el 80% de las alertas críticas sean reconocidas dentro de los primeros 60 segundos y alcanzar una conversión mínima del 15% de usuarios del plan gratuito hacia un plan de pago.

Los impactos identificados se concentran en reducir la dependencia de la supervisión presencial, mejorar la capacidad de respuesta frente a emergencias, facilitar el monitoreo continuo de la salud, apoyar el cumplimiento de rutinas de bienestar y brindar mayor autonomía y seguridad a las personas bajo cuidado. A partir de estos impactos se identifican entregables relacionados con monitoreo remoto, gestión de emergencias, reportes de salud, recordatorios de cuidado, localización segura y planes de suscripción. La Figura 2.15 presenta el Impact Mapping resultante.

<a id="figura-2-15"></a>**Figura 2.15.** Impact Mapping de Guardian+

![Impact Mapping - Guardian+](../assets/images/chapterII/impactMapping/impactMapping.png)

El Impact Map evidencia que las funcionalidades principales de Guardian+ no se plantean de manera aislada, sino como mecanismos orientados a generar cambios concretos en el comportamiento de los actores. Los familiares buscan reducir la incertidumbre y reaccionar con mayor rapidez; los cuidadores requieren centralizar la supervisión y mejorar la toma de decisiones; mientras que las personas bajo cuidado necesitan mayor autonomía para cumplir sus rutinas y solicitar ayuda ante situaciones de riesgo.

Asimismo, el artefacto permite mantener trazabilidad con las User Stories del Product Backlog. Entre las historias relacionadas se encuentran la detección automática de caídas y despacho de emergencia (US08), la generación y escalamiento de alertas críticas (US09 y US11), el monitoreo de signos vitales (US01-US05), los reportes históricos de salud (US07, US19 y US24), los recordatorios de bienestar (US06, US14 y US26), el botón SOS (US15), la localización y geocercas (US18 y US28), y la visualización comparativa de planes de suscripción (US33).

### 2.4.3. Product Backlog

El Product Backlog se construyó a partir de las 33 User Stories definidas en la sección 2.4.1, ordenadas según el valor que cada una aporta al negocio. Bajo ese criterio, las historias con mayor valor de negocio son las de detección y respuesta ante emergencias (EP03) y localización (EP04), pues constituyen la propuesta de valor central de Guardian+ ("lazo de cuidado" bidireccional ante situaciones críticas); les siguen el monitoreo de salud en tiempo real (EP01) y, después, recordatorios, reportes y comunicación (EP02). Las historias del sitio web estático o Landing Page (EP05) se incorporan desde el primer sprint, en un frente de trabajo paralelo al del aplicativo móvil, ya que son necesarias tempranamente para la difusión de la propuesta de valor y la adquisición de usuarios.

La estimación de esfuerzo se realizó con Story Points en escala de Fibonacci, en función de la complejidad técnica y del número de escenarios de aceptación de cada historia, utilizando ClickUp como herramienta de gestión del Product Backlog. La Tabla 2.50 presenta el Product Backlog priorizado.


<a id="tabla-2-50"></a>**Tabla 2.50.** Product Backlog de Guardian+

| # Orden | User Story Id | Título | Story Points (1 / 2 / 3 / 5 / 8) | Sprint |
|---|---|---|---|---|
| 1 | US15 | Activación de auxilio mediante botón SOS en pulsera | 5 | Sprint 1 |
| 2 | US08 | Detección automática de caídas y despacho de emergencia | 8 | Sprint 1 |
| 3 | US09 | Generación de alertas por transgresión de umbrales biomédicos | 5 | Sprint 1 |
| 4 | US11 | Escalamiento automatizado de alertas críticas no atendidas | 5 | Sprint 1 |
| 5 | US16 | Administración de agenda de contactos de auxilio | 2 | Sprint 1 |
| 6 | US18 | Telemetría de geolocalización en tiempo real | 5 | Sprint 1 |
| 7 | US30 | Navegación entre secciones informativas de la Landing Page | 1 | Sprint 1 |
| 8 | US31 | Presentación de características y beneficios clave del sistema | 2 | Sprint 1 |
| 9 | US32 | Captura y procesamiento de solicitudes de contacto institucional | 3 | Sprint 1 |
| 10 | US33 | Visualización comparativa de planes de suscripción Guardian+ | 3 | Sprint 1 |
| 11 | US01 | Visualización de ritmo cardíaco en tiempo real | 3 | Sprint 2 |
| 12 | US02 | Visualización de presión arterial estimada | 3 | Sprint 2 |
| 13 | US03 | Visualización de saturación de oxígeno periférico (SpO₂) | 3 | Sprint 2 |
| 14 | US04 | Supervisión de temperatura corporal continua | 3 | Sprint 2 |
| 15 | US05 | Visualización de frecuencia respiratoria estimada | 3 | Sprint 2 |
| 16 | US10 | Confirmación manual de estado de bienestar tras incidente | 3 | Sprint 2 |
| 17 | US20 | Notificación de nivel crítico de batería en wearable | 2 | Sprint 2 |
| 18 | US25 | Despacho simultáneo a múltiples contactos de auxilio | 3 | Sprint 2 |
| 19 | US21 | Sincronización y persistencia resiliente de telemetría (Offline Sync) | 8 | Sprint 2 |
| 20 | US06 | Emisión y confirmación de recordatorios de medicación | 5 | Sprint 3 |
| 21 | US07 | Análisis comparativo y tendencias históricas de signos vitales | 5 | Sprint 3 |
| 22 | US12 | Configuración y parametrización de niveles de alerta | 3 | Sprint 3 |
| 23 | US13 | Programación y notificación de consultas médicas | 3 | Sprint 3 |
| 24 | US19 | Exportación de reporte cronológico de telemetría médica | 3 | Sprint 3 |
| 25 | US23 | Establecimiento de canal de comunicación directa | 5 | Sprint 3 |
| 26 | US24 | Consolidación y despacho de reporte semanal de salud | 3 | Sprint 3 |
| 27 | US28 | Delimitación y monitoreo perimetral mediante geocercas múltiples | 5 | Sprint 3 |
| 28 | US14 | Recordatorios programados para actividad física ligera | 2 | Sprint 4 |
| 29 | US17 | Estimación y registro de fases de sueño | 5 | Sprint 4 |
| 30 | US22 | Silenciamiento de alertas no críticas en el Care Circle | 2 | Sprint 4 |
| 31 | US26 | Recordatorios periódicos de hidratación y pausas activas | 2 | Sprint 4 |
| 32 | US27 | Detección de inactividad física prolongada | 5 | Sprint 4 |
| 33 | US29 | Previsión de agotamiento de stock y pedidos de medicinas | 5 | Sprint 4 |

## 2.5. Strategic-Level Domain-Driven Design

En esta sección se presenta el diseño estratégico de Guardian+ con Domain-Driven Design: el EventStorming con el que se descubrieron los Bounded Contexts, el Context Mapping que define sus relaciones y la arquitectura de software representada con el C4 Model.

### 2.5.1. EventStorming

El equipo aplicó EventStorming para explorar el dominio de Guardian+ a partir de sus eventos, comandos, actores y políticas. Con ese análisis se identificaron los Bounded Contexts candidatos, se modelaron los flujos de mensajes del contexto principal y se elaboraron los Bounded Context Canvases.

#### 2.5.1.1. Candidate Context Discovery

Una vez detallados los flujos mediante Design-Level EventStorming, se procedió con la actividad de Candidate Context Discovery. Esta etapa representa la transición entre el análisis del comportamiento del dominio y la definición de su arquitectura estratégica. El objetivo fue identificar agrupaciones de funcionalidades que comparten un mismo Lenguaje Ubicuo, reglas de negocio relacionadas y responsabilidades cohesivas.

A partir del análisis de los eventos, comandos, actores, políticas, agregados y sistemas externos identificados durante el EventStorming, fue posible reconocer límites naturales dentro del dominio de Guardian+. Estas agrupaciones permitieron proponer contextos candidatos que posteriormente servirán como base para la descomposición del sistema en módulos independientes y con responsabilidades claramente diferenciadas.

Como resultado del análisis se identificaron siete Bounded Contexts candidatos, clasificados de acuerdo con su relevancia estratégica dentro del dominio de Guardian+: dos pertenecientes al Core Domain, dos al Supporting Domain y tres al Generic Domain. A continuación, se presentan los resultados de EventStorming utilizados para sustentar el descubrimiento de cada contexto.



##### Emergency & Alerting Bounded Context (Core Domain)

La Figura 2.16 presenta el EventStorming del Bounded Context Emergency & Alerting.

<a id="figura-2-16"></a>**Figura 2.16.** EventStorming del Bounded Context Emergency & Alerting

![Emergency & Alerting EventStorming](../assets/images/chapterII/EventStorming/Emergency.jpg)

Este contexto candidato agrupa los comportamientos relacionados con la detección y gestión de situaciones de emergencia, la generación y escalamiento de alertas, el reconocimiento de incidentes y la coordinación de la respuesta por parte de familiares y cuidadores.

Su Lenguaje Ubicuo se encuentra asociado a conceptos como detección de caídas, SOS, alerta crítica, reconocimiento de alerta, escalamiento, contacto de emergencia y estabilización de incidentes.

Se clasificó como parte del **Core Domain** debido a que representa una de las capacidades de mayor valor diferencial de Guardian+: permitir que familiares y cuidadores reaccionen oportunamente ante eventos que puedan comprometer el bienestar de una persona vulnerable.



##### Health Monitoring Bounded Context (Core Domain)

La Figura 2.17 presenta el EventStorming del Bounded Context Health Monitoring.

<a id="figura-2-17"></a>**Figura 2.17.** EventStorming del Bounded Context Health Monitoring

![alt text](../assets/images/chapterII/EventStorming/health-monitoring-bc.png)

Este contexto candidato concentra las capacidades relacionadas con el monitoreo de bioseñales, la evaluación de umbrales biométricos, la visualización de información de salud y la generación de reportes y resúmenes periódicos.

Dentro de su Lenguaje Ubicuo se encuentran conceptos como bioseñales, telemetría, umbral biométrico, indicadores de salud, métricas en tiempo real, reportes de salud y resúmenes semanales.

Se clasificó como parte del **Core Domain** porque el monitoreo continuo del estado de la persona bajo cuidado constituye una de las funcionalidades centrales de Guardian+ y proporciona información fundamental para detectar posibles anomalías y alimentar posteriormente los procesos de prevención y emergencia.



##### Care Routines & Wellness Bounded Context (Supporting Domain)

La Figura 2.18 presenta el EventStorming del Bounded Context Care Routines & Wellness.

<a id="figura-2-18"></a>**Figura 2.18.** EventStorming del Bounded Context Care Routines & Wellness

![Care Routines & Wellness EventStorming](../assets/images/chapterII/EventStorming/careRoutine.png)

Este contexto candidato agrupa las capacidades destinadas a apoyar las actividades cotidianas de cuidado y bienestar. Entre ellas se encuentran la programación, emisión, confirmación, reemisión y cancelación de recordatorios, así como el seguimiento del stock de medicamentos, ciclos de sueño, periodos prolongados de inactividad y reanudación de actividad.

Su Lenguaje Ubicuo incluye conceptos como recordatorio, rutina, medicación, stock, sueño, actividad, inactividad y bienestar.

Fue clasificado como **Supporting Domain**, ya que complementa las capacidades principales de monitoreo y atención de emergencias, mejorando la continuidad del cuidado diario, pero sin constituir por sí mismo el principal diferenciador estratégico de Guardian+.



##### Mobility & Geofencing Bounded Context (Supporting Domain)

La Figura 2.19 presenta el EventStorming del Bounded Context Mobility & Geofencing.

<a id="figura-2-19"></a>**Figura 2.19.** EventStorming del Bounded Context Mobility & Geofencing

![Mobility & Geofencing EventStorming](../assets/images/chapterII/EventStorming/MOBILITY.png)

Este contexto candidato reúne las funcionalidades relacionadas con el seguimiento de ubicación y la definición de zonas seguras para la persona bajo cuidado. Incluye la creación y actualización de geocercas, la recepción de ubicaciones y la evaluación de si la persona permanece dentro o fuera de los límites configurados.

Su Lenguaje Ubicuo se encuentra compuesto por conceptos como geocerca, zona segura, ubicación, seguimiento, estado de ubicación y violación de zona segura.

Se clasificó como **Supporting Domain**, debido a que aporta información contextual importante para la seguridad de la persona bajo cuidado y puede originar situaciones que requieran atención, aunque su funcionamiento complementa a los contextos principales de monitoreo y alertamiento.



##### IAM Bounded Context (Generic Domain)

La Figura 2.20 presenta el EventStorming del Bounded Context IAM.

<a id="figura-2-20"></a>**Figura 2.20.** EventStorming del Bounded Context IAM

![IAM EventStorming](../assets/images/chapterII/EventStorming/IAM.png)

Este contexto candidato agrupa los procesos relacionados con la gestión de identidad y acceso a Guardian+. Incluye el registro de credenciales, verificación de correo electrónico, autenticación, uso de códigos OTP y recuperación de contraseña.

Su Lenguaje Ubicuo comprende conceptos como credenciales, autenticación, verificación, OTP, contraseña, inicio de sesión y usuario autenticado.

Se clasificó como **Generic Domain** porque representa una capacidad necesaria para garantizar el acceso seguro a la plataforma, pero corresponde a una problemática común en numerosos sistemas de software y no constituye un elemento diferenciador propio del negocio de Guardian+.


##### Profile Bounded Context (Generic Domain)

La Figura 2.21 presenta el EventStorming del Bounded Context Profile.

<a id="figura-2-21"></a>**Figura 2.21.** EventStorming del Bounded Context Profile

![Profile EventStorming](../assets/images/chapterII/EventStorming/PROFILE.png)

Este contexto candidato gestiona la información asociada a los perfiles de los usuarios y de las personas bajo cuidado, así como las relaciones existentes entre familiares, cuidadores y Care Recipients. También contempla la gestión de información de contacto y preferencias de uso de la aplicación.

Su Lenguaje Ubicuo incluye conceptos como perfil de usuario, perfil de persona bajo cuidado, relación de cuidado, información de contacto, preferencias de aplicación, idioma y accesibilidad.

Se clasificó como **Generic Domain** debido a que proporciona información fundamental para que otros contextos puedan operar correctamente, pero sus capacidades corresponden principalmente a gestión de perfiles y relaciones, y no constituyen el núcleo diferenciador de Guardian+.



##### Subscriptions Bounded Context (Generic Domain)

Las Figuras 2.22 y 2.23 presentan el EventStorming del Bounded Context Subscriptions, dividido en dos partes por su extensión.

<a id="figura-2-22"></a>**Figura 2.22.** EventStorming del Bounded Context Subscriptions (parte 1)

![Subscriptions EventStorming - Parte 1](../assets/images/chapterII/EventStorming/subscription1.png)

<a id="figura-2-23"></a>**Figura 2.23.** EventStorming del Bounded Context Subscriptions (parte 2)

![Subscriptions EventStorming - Parte 2](../assets/images/chapterII/EventStorming/Subscription2.png)

Este contexto candidato concentra las reglas relacionadas con el ciclo de vida comercial de las suscripciones de Guardian+. Incluye la solicitud y activación de suscripciones, cambios de plan, renovación, cancelación, expiración y administración de los beneficios asociados a cada plan.

Su Lenguaje Ubicuo se encuentra relacionado con conceptos como suscripción, plan, pago, renovación, cancelación, expiración y entitlement.

Se clasificó como **Generic Domain** porque permite implementar el modelo comercial y controlar los beneficios disponibles para los usuarios, pero no representa la principal fuente de innovación o diferenciación de Guardian+.



Como resultado del Candidate Context Discovery, el equipo estableció una primera descomposición estratégica del dominio de Guardian+. Los contextos **Emergency & Alerting** y **Health Monitoring** fueron reconocidos como parte del Core Domain debido a su relación directa con la propuesta de valor principal de la solución. **Care Routines & Wellness** y **Mobility & Geofencing** fueron clasificados como Supporting Domains debido a que complementan y fortalecen las capacidades centrales de cuidado. Finalmente, **IAM**, **Profile** y **Subscriptions** fueron identificados como Generic Domains al representar capacidades necesarias para el funcionamiento de la plataforma, pero comunes a otros tipos de sistemas.

Esta descomposición servirá como base para las siguientes actividades de Strategic-Level Domain-Driven Design, donde se analizarán los mensajes intercambiados entre contextos, sus responsabilidades y las relaciones de integración mediante Domain Message Flows, Bounded Context Canvases y Context Mapping.

#### 2.5.1.2. Domain Message Flows Modeling

En esta sección se documentan los principales flujos de mensajes (comandos, eventos y policies) del Bounded Context **Emergency & Alerting**, modelados como diagramas de secuencia a partir del Design-Level EventStorming. Se seleccionaron los tres flujos de mayor valor de negocio, que recorren los dos agregados centrales del contexto (ALERT e INCIDENT) y las policies de despacho y escalamiento que los conectan.

##### Bounded Context: Emergency & Alerting

**Flujo 1 — Caída confirmada**

La Figura 2.24 presenta el diagrama de secuencia del flujo de caída confirmada y la Figura 2.25, su domain storytelling.

El flujo inicia cuando el Wearable Device detecta una caída y envía el comando Trigger Alert (FALL_DETECTED) al agregado ALERT, que registra el evento Alert Triggered en estado PENDING_CONFIRMATION. La policy Fall Confirmation Timeout otorga 20 segundos al Fragile Citizen para descartar la caída; al no recibir respuesta, la alerta se confirma (Confirm Alert y Alert Confirmed). Como la severidad es CRITICAL, el Dispatch Strategy Selector ordena difundir la alerta a todos los contactos (Broadcast Alert), lo que se registra como Alert Broadcasted por PUSH y SMS. Cuando un Family Member reconoce la alerta (Acknowledge Alert y Alert Acknowledged), la policy Escalation Stopper detiene el escalamiento y se abre un INCIDENT, que queda en estado IN_ATTENTION.

<a id="figura-2-24"></a>**Figura 2.24.** Domain message flow del flujo de caída confirmada

![Domain Message Flow - Caída confirmada](../assets/images/chapterII/domain-message-flows/emergency-alerting-flow1-fall-confirmed.png)

El domain storytelling describe el mismo escenario desde la perspectiva de los actores. El Wearable Device detecta un patrón de caída y lo envía a Emergency & Alerting, que (1) espera la confirmación de bienestar del Fragile Citizen. Como (2) el Fragile Citizen no confirma que se encuentra bien, el sistema (3) envía una notificación que llega al cuidador o familiar.

<a id="figura-2-25"></a>**Figura 2.25.** Domain storytelling del flujo de caída confirmada

![alt text](../assets/images/chapterII/domain-message-flows/fall-storytelling.png)

**Flujo 2 — SOS manual**

La Figura 2.26 presenta el diagrama de secuencia del flujo de SOS manual.

En este flujo el Fragile Citizen presiona el botón SOS y envía el comando Trigger Alert (SOS_TRIGGERED) al agregado ALERT, que registra Alert Triggered. A diferencia de la caída, el SOS no requiere ventana de confirmación, por lo que la alerta pasa de inmediato a Alert Confirmed. La severidad siempre es CRITICAL, de modo que el Dispatch Strategy Selector ordena el Broadcast Alert y se registra Alert Broadcasted. A partir de ese punto, el reconocimiento por parte del contacto y la apertura del incidente continúan igual que en el Flujo 1.

<a id="figura-2-26"></a>**Figura 2.26.** Domain message flow del flujo de SOS manual

![Domain Message Flow - SOS manual](../assets/images/chapterII/domain-message-flows/emergency-alerting-flow2-sos-triggered.png)

**Flujo 3 — Anomalía biométrica escalada**

La Figura 2.27 presenta el diagrama de secuencia del flujo de anomalía biométrica escalada y la Figura 2.28, su domain storytelling.

El flujo inicia con el evento VitalSignAnomalyDetected, publicado por el Bounded Context externo Health Monitoring y recibido a través de una Anti-Corruption Layer (ACL). La policy Biometric Alert Raiser lo traduce en el comando Trigger Alert (VITAL_SIGN_ANOMALY), y el agregado ALERT registra Alert Triggered y Alert Confirmed. Con severidad HIGH, el Dispatch Strategy Selector despacha la alerta solo al contacto primario (Alert Dispatched, PRIMARY). El diagrama muestra dos alternativas: si el Caregiver responde a tiempo, reconoce la alerta y se abre un INCIDENT en estado IN_ATTENTION; si vence el Ack Timeout de 60 segundos, la policy Ack Timeout Escalation escala la alerta al contacto secundario (Alert Escalated, SECONDARY). Si nuevamente nadie la reconoce, la policy Critical Broadcast Fallback la difunde por SMS a todos los contactos (Alert Broadcasted).

<a id="figura-2-27"></a>**Figura 2.27.** Domain message flow del flujo de anomalía biométrica escalada

![Domain Message Flow - Anomalía biométrica escalada](../assets/images/chapterII/domain-message-flows/emergency-alerting-flow3-biometric-anomaly-escalated.png)

El domain storytelling muestra la colaboración entre Bounded Contexts. El Wearable Device envía lecturas de signos vitales que son evaluadas por Health Monitoring, el cual (4) detecta tres violaciones consecutivas del umbral y publica un evento de anomalía. Emergency & Alerting (5) escucha ese evento, (6) genera una alerta y (7) envía una notificación que llega al cuidador o familiar.

<a id="figura-2-28"></a>**Figura 2.28.** Domain storytelling del flujo de anomalía biométrica escalada

![alt text](../assets/images/chapterII/domain-message-flows/vitalsign-anomaly-storytelling.png)

**Flujo 4 - Reminder sent**

La Figura 2.29 presenta el domain storytelling del flujo de recordatorio enviado.

El domain storytelling representa el seguimiento de los recordatorios de medicación. Care Routines & Wellness (8) emite un recordatorio que llega al Fragile Citizen; cuando este (9) no confirma la toma, el contexto (10) reemite el recordatorio mediante un evento de reemisión. Emergency & Alerting (11) escucha ese evento y (12) envía una notificación que llega al cuidador o familiar, para que pueda verificar que la medicación se cumpla.

<a id="figura-2-29"></a>**Figura 2.29.** Domain storytelling del flujo de recordatorio enviado

![alt text](../assets/images/chapterII/domain-message-flows/reminder-storytelling.png)


**Flujo 5 - Inactivity**

La Figura 2.30 presenta el domain storytelling del flujo de inactividad prolongada.

El domain storytelling describe la detección de inactividad prolongada. El Wearable Device envía telemetría de inactividad que es recibida por Care Routines & Wellness, el cual (13) detecta que se superó el umbral de 60 minutos y publica el evento de inactividad prolongada. Emergency & Alerting (14) escucha ese evento, (15) genera una alerta y (16) envía una notificación que llega al cuidador o familiar.

<a id="figura-2-30"></a>**Figura 2.30.** Domain storytelling del flujo de inactividad prolongada

![alt text](../assets/images/chapterII/domain-message-flows/inactivity-storytelling.png)


#### 2.5.1.3. Bounded Context Canvases
En esta sección se detallan los diseños de los Bounded Contexts candidatos identificados, priorizando aquellos clasificados como Core Domain por su impacto estratégico en Guardian+. El diseño aplica rigurosamente la estructura visual del **Bounded Context Design Canvas V1 (Nick Tune)**, utilizando el formato estándar de tablas Markdown para asegurar compatibilidad absoluta con cualquier procesador de texto (GitHub, Notion, Word, PDF). Se define la interfaz pública mediante Actions y Queries, aislando el Ubiquitous Language y las Policies.

##### Bounded Context: Emergency & Alerting (Core Domain)

<!-- CANVAS: EMERGENCY & ALERTING (NICK TUNE V1 TEMPLATE) -->

La Figura 2.31 presenta el Bounded Context Canvas de Emergency & Alerting.

<a id="figura-2-31"></a>**Figura 2.31.** Bounded Context Canvas de Emergency & Alerting

<table class="canvas" table border="1" width="100%" cellpadding="10" cellspacing="0" style="border-collapse: collapse; font-family: Arial, sans-serif;">
<tr>
<td width="42%" valign="top" style="border-right: 2px solid #333; border-bottom: none; padding: 15px;">
<div style="font-size: 0.9em; font-weight: bold; color: #222;">Name</div>
<div style="color: #c62828; font-size: 1.3em; font-weight: bold; margin-top: 4px; margin-bottom: 12px;">Emergency &amp; Alerting</div>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Strategic Classification</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 4px;">core/supportive/generic/other</div>
<div style="color: #c62828; font-size: 1em; margin-bottom: 12px;">
<strong>Core - </strong> Principal diferenciador de Guardian+: garantiza una respuesta humana oportuna ante eventos que comprometen la seguridad del Fragile Citizen.
</div>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Description</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 4px;">Summary of purpose and responsibilities - not implementation</div>
<div style="color: #c62828; font-size: 0.95em; line-height: 1.4; margin-bottom: 15px;">
Dispara las Alerts ante señales que comprometen la seguridad del Fragile Citizen, las despacha a sus Emergency Contacts según la severidad, gobierna el escalamiento progresivo hasta obtener un reconocimiento efectivo y registra la atención del Incident hasta su cierre.
</div>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Business Policies</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 8px;">Key business rules and policies</div>
<table width="100%" border="0" cellpadding="0" cellspacing="4" style="text-align: center;">
<tr>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">Dispatch Strategy Selector (escalamiento por niveles; difusión inmediata de CRITICAL configurable)</td>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">Ventana de Confirmación de Caída (20 s)</td>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">Ack Timeout del contacto primario (60 s por defecto)</td>
</tr>
<tr>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">Escalation Stopper (el reconocimiento abre el Incident)</td>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">Critical Broadcast Fallback ante cadena agotada</td>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">Override de Silent Mode solo en severidad CRITICAL</td>
</tr>
</table>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Ubiquitous Language</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 6px;">Key domain terminology</div>
<table width="100%" border="0" cellpadding="0" cellspacing="0" style="color: #c62828; font-weight: bold; font-size: 0.85em;">
<tr>
<td width="50%" valign="top">
• Alert<br>
• Incident<br>
• Emergency Contact<br>
• Escalation Chain<br>
• Alert Settings
</td>
<td width="50%" valign="top">
• Severity<br>
• Acknowledgment<br>
• Emergency Contact<br>
• Silent Mode
</td>
</tr>
</table>
</td>

<td width="58%" valign="top" style="padding: 0;">
<div style="padding: 12px; border-bottom: 2px solid #333;">
<div align="center">
<strong style="font-size: 1em;">Capabilities &amp; Responsibilities</strong><br>
<span style="font-size: 0.75em; color: #777;">Services provided to consumers</span>
</div>
<table width="100%" border="0" cellpadding="8" cellspacing="0" style="margin-top: 8px;">
<tr>
<td width="50%" valign="top" align="center" style="border-right: 1px solid #ddd; padding-right: 10px;">
<strong style="font-size: 0.85em;">Informational</strong><br>
<span style="font-size: 0.7em; color: #777;">Queries, reports, etc.</span><br><br>
<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">Get Active Alerts</td></tr>
</table>
<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">Get Alert History</td></tr>
</table>
<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">Get Pending Alerts</td></tr>
</table>
<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">Get Alert Settings</td></tr>
</table>
</td>
<td width="50%" valign="top" align="center" style="padding-left: 10px;">
<strong style="font-size: 0.85em;">Actions</strong><br>
<span style="font-size: 0.7em; color: #777;">Invokable commands, scheduled tasks, etc.</span><br><br>

<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Trigger Alert</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Confirm / Dismiss Alert</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Dispatch / Broadcast Alert</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Escalate Alert</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Acknowledge Alert / Close Incident</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Manage Settings &amp; Emergency Contacts</td></tr>
</table>
</td>
</tr>
</table>
</div>

<div style="padding: 12px;">
<div align="center" style="margin-bottom: 8px;">
<strong style="font-size: 1em;">Dependencies</strong><br>
<span style="font-size: 0.75em; color: #777;">Interactions with other bounded contexts and services</span>
</div>
<table width="100%" border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; font-size: 0.8em; text-align: left;">
<tr bgcolor="#f5f5f5">
<th>Name</th>
<th>Reason</th>
<th>System</th>
<th>Relationship</th>
</tr>
<tr>
<td>Health Monitoring</td>
<td>Consume anomalías biométricas confirmadas</td>
<td>Internal</td>
<td>In (Customer/Supplier)</td>
</tr>
<tr>
<td>Mobility &amp; Geofencing</td>
<td>Consume violaciones de zona segura y consulta la última ubicación para la notificación</td>
<td>Internal</td>
<td>In (Customer/Supplier)</td>
</tr>
<tr>
<td>Care Routines &amp; Wellness</td>
<td>Consume inactividad prolongada, recordatorios reemitidos y sugerencias de reabastecimiento</td>
<td>Internal</td>
<td>In (Customer/Supplier)</td>
</tr>
<tr>
<td>Profile</td>
<td>Sincroniza los Emergency Contacts con las relaciones de cuidado</td>
<td>Internal</td>
<td>In (ECST)</td>
</tr>
<tr>
<td>IAM</td>
<td>Valida identidad y autorización de cada comando</td>
<td>Internal</td>
<td>In (OHS)</td>
</tr>
<tr>
<td>Notification Providers</td>
<td>Despacha las notificaciones push y SMS al Care Circle</td>
<td>External</td>
<td>Out (ACL)</td>
</tr>
</table>
</div>
</td>
</tr>
</table>

##### Bounded Context: Health Monitoring (Core Domain)

<!-- CANVAS: HEALTH MONITORING (NICK TUNE V1 TEMPLATE) -->

La Figura 2.32 presenta el Bounded Context Canvas de Health Monitoring.

<a id="figura-2-32"></a>**Figura 2.32.** Bounded Context Canvas de Health Monitoring

<table class="canvas" table border="1" width="100%" cellpadding="10" cellspacing="0" style="border-collapse: collapse; font-family: Arial, sans-serif;">
<tr>
<td width="42%" valign="top" style="border-right: 2px solid #333; border-bottom: none; padding: 15px;">
<div style="font-size: 0.9em; font-weight: bold; color: #222;">Name</div>
<div style="color: #c62828; font-size: 1.3em; font-weight: bold; margin-top: 4px; margin-bottom: 12px;">Health Monitoring</div>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Strategic Classification</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 4px;">core/supportive/generic/other</div>
<div style="color: #c62828; font-size: 1em; margin-bottom: 12px;">
<strong>Core - </strong> Esencial para habilitar el monitoreo clínico continuo y la prevención de crisis.
</div>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Description</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 4px;">Summary of purpose and responsibilities - not implementation</div>
<div style="color: #c62828; font-size: 0.95em; line-height: 1.4; margin-bottom: 15px;">
Administra los Wearable Devices asignados a un Care Recipient, ingesta y emite en vivo cada Vital Sign detectado, lo evalúa contra un Vital Sign Threshold configurable por paciente y tipo, y consolida Health Reports preventivos.
</div>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Business Policies</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 8px;">Key business rules and policies</div>
<table width="100%" border="0" cellpadding="0" cellspacing="4" style="text-align: center;">
<tr>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">Validación de Integridad de Vital Signs</td>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">Regla de Tolerancia (3 lecturas consecutivas)</td>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">Política de Compilación Semanal</td>
</tr>
</table>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Ubiquitous Language</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 6px;">Key domain terminology</div>
<table width="100%" border="0" cellpadding="0" cellspacing="0" style="color: #c62828; font-weight: bold; font-size: 0.85em;">
<tr>
<td width="50%" valign="top">
• Vital Sign<br>
• Vital Sign Type<br>
• Vital Sign Threshold
</td>
<td width="50%" valign="top">
• Wearable Device<br>
• Care Recipient<br>
• Health Report
</td>
</tr>
</table>
</td>

<td width="58%" valign="top" style="padding: 0;">
<div style="padding: 12px; border-bottom: 2px solid #333;">
<div align="center">
<strong style="font-size: 1em;">Capabilities & Responsibilities</strong><br>
<span style="font-size: 0.75em; color: #777;">Services provided to consumers</span>
</div>
<table width="100%" border="0" cellpadding="8" cellspacing="0" style="margin-top: 8px;">
<tr>
<td width="50%" valign="top" align="center" style="border-right: 1px solid #ddd; padding-right: 10px;">
<strong style="font-size: 0.85em;">Informational</strong><br>
<span style="font-size: 0.7em; color: #777;">Queries, reports, etc.</span><br><br>
<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">Get Live Vital Signs</td></tr>
</table>
<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">Get Vital Sign Thresholds</td></tr>
</table>
<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">Get Historical Health Report</td></tr>
</table>
</td>
<td width="50%" valign="top" align="center" style="padding-left: 10px;">
<strong style="font-size: 0.85em;">Actions</strong><br>
<span style="font-size: 0.7em; color: #777;">Invokable commands, scheduled tasks, etc.</span><br><br>

<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Detect / Emit Vital Signs</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Evaluate Vital Signs Thresholds</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Assign Wearable Device</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Define Vital Sign Threshold</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Compile Weekly Summary</td></tr>
</table>
</td>
</tr>
</table>
</div>

<div style="padding: 12px;">
<div align="center" style="margin-bottom: 8px;">
<strong style="font-size: 1em;">Dependencies</strong><br>
<span style="font-size: 0.75em; color: #777;">Interactions with other bounded contexts and services</span>
</div>
<table width="100%" border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; font-size: 0.8em; text-align: left;">
<tr bgcolor="#f5f5f5">
<th>Name</th>
<th>Reason</th>
<th>System</th>
<th>Relationship</th>
</tr>
<tr>
<td>Wearable Hardware</td>
<td>Dispositivo físico externo que provee los datos biométricos crudos ingeridos como Vital Sign (distinto del registro interno WearableDevice, que solo administra la asignación del dispositivo al Care Recipient)</td>
<td>External</td>
<td>In (ACL)</td>
</tr>
<tr>
<td>Emergency & Alerting</td>
<td>Consume anomalías de signos vitales (eventos)</td>
<td>Internal</td>
<td>Out (Supplier)</td>
</tr>
<tr>
<td>Profile / IAM</td>
<td>Resuelve el Care Recipient Profile y el usuario autenticado que solicita un Health Report</td>
<td>Internal</td>
<td>In (OHS)</td>
</tr>
</table>
</div>
</td>
</tr>
</table>

##### Bounded Context: Care Routines & Wellness (Supporting Domain)

<!-- CANVAS: CARE ROUTINES & WELLNESS (NICK TUNE V1 TEMPLATE) -->

La Figura 2.33 presenta el Bounded Context Canvas de Care Routines & Wellness.

<a id="figura-2-33"></a>**Figura 2.33.** Bounded Context Canvas de Care Routines & Wellness

<table class="canvas" table border="1" width="100%" cellpadding="10" cellspacing="0" style="border-collapse: collapse; font-family: Arial, sans-serif;">
<tr>
<td width="42%" valign="top" style="border-right: 2px solid #333; border-bottom: none; padding: 15px;">
<div style="font-size: 0.9em; font-weight: bold; color: #222;">Name</div>
<div style="color: #c62828; font-size: 1.3em; font-weight: bold; margin-top: 4px; margin-bottom: 12px;">Care Routines &amp; Wellness</div>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Strategic Classification</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 4px;">core/supportive/generic/other</div>
<div style="color: #c62828; font-size: 1em; margin-bottom: 12px;">
<strong>Supporting - </strong> Da soporte al valor central de Guardian+ asegurando que las rutinas de bienestar del Fragile Citizen se cumplan.
</div>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Description</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 4px;">Summary of purpose and responsibilities - not implementation</div>
<div style="color: #c62828; font-size: 0.95em; line-height: 1.4; margin-bottom: 15px;">
Gestiona el ciclo de vida de los Reminders de rutina (medicación, citas, actividad física e hidratación), registra y clasifica los Sleep Cycles, detecta Prolonged Inactivity mediante el Activity Monitor, y controla el Medication Stock sugiriendo su reabastecimiento.
</div>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Business Policies</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 8px;">Key business rules and policies</div>
<table width="100%" border="0" cellpadding="0" cellspacing="4" style="text-align: center;">
<tr>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">Reminder Issuance Policy (Sleep Window)</td>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">Reminder Reissue Policy (10 min)</td>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">Medication Stock Policy (umbral 3 días)</td>
</tr>
</table>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Ubiquitous Language</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 6px;">Key domain terminology</div>
<table width="100%" border="0" cellpadding="0" cellspacing="0" style="color: #c62828; font-weight: bold; font-size: 0.85em;">
<tr>
<td width="50%" valign="top">
- Reminder<br>
- Sleep Cycle
</td>
<td width="50%" valign="top">
- Activity Monitor<br>
- Medication Stock
</td>
</tr>
</table>
</td>

<td width="58%" valign="top" style="padding: 0;">
<div style="padding: 12px; border-bottom: 2px solid #333;">
<div align="center">
<strong style="font-size: 1em;">Capabilities &amp; Responsibilities</strong><br>
<span style="font-size: 0.75em; color: #777;">Services provided to consumers</span>
</div>
<table width="100%" border="0" cellpadding="8" cellspacing="0" style="margin-top: 8px;">
<tr>
<td width="50%" valign="top" align="center" style="border-right: 1px solid #ddd; padding-right: 10px;">
<strong style="font-size: 0.85em;">Informational</strong><br>
<span style="font-size: 0.7em; color: #777;">Queries, reports, etc.</span><br><br>
<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">Get Reminder Status</td></tr>
</table>
<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">Get Medication Stock Status</td></tr>
</table>
</td>
<td width="50%" valign="top" align="center" style="padding-left: 10px;">
<strong style="font-size: 0.85em;">Actions</strong><br>
<span style="font-size: 0.7em; color: #777;">Invokable commands, scheduled tasks, etc.</span><br><br>

<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Schedule / Issue / Reissue Reminder</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Confirm / Cancel Reminder</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Record Activity &amp; Sleep Telemetry</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Confirm Medication Acquisition</td></tr>
</table>
</td>
</tr>
</table>
</div>

<div style="padding: 12px;">
<div align="center" style="margin-bottom: 8px;">
<strong style="font-size: 1em;">Dependencies</strong><br>
<span style="font-size: 0.75em; color: #777;">Interactions with other bounded contexts and services</span>
</div>
<table width="100%" border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; font-size: 0.8em; text-align: left;">
<tr bgcolor="#f5f5f5">
<th>Name</th>
<th>Reason</th>
<th>System</th>
<th>Relationship</th>
</tr>
<tr>
<td>Wearable Device</td>
<td>Provee telemetría de actividad, inactividad y sueño</td>
<td>External</td>
<td>In (ACL)</td>
</tr>
<tr>
<td>Profile / IAM</td>
<td>Resuelve identidad y perfil de la persona bajo cuidado</td>
<td>Internal</td>
<td>In (OHS)</td>
</tr>
<tr>
<td>Emergency &amp; Alerting</td>
<td>Consume inactividad prolongada, reemisión y reabastecimiento</td>
<td>Internal</td>
<td>Out (Supplier)</td>
</tr>
</table>
</div>
</td>
</tr>
</table>

##### Bounded Context: Subscriptions (Generic Domain)

<!-- CANVAS: SUBSCRIPTIONS (NICK TUNE V1 TEMPLATE) -->

La Figura 2.34 presenta el Bounded Context Canvas de Subscriptions.

<a id="figura-2-34"></a>**Figura 2.34.** Bounded Context Canvas de Subscriptions

<table class="canvas" table border="1" width="100%" cellpadding="10" cellspacing="0" style="border-collapse: collapse; font-family: Arial, sans-serif;">
<tr>
<td width="42%" valign="top" style="border-right: 2px solid #333; border-bottom: none; padding: 15px;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Name</div>
<div style="color: #c62828; font-size: 1.3em; font-weight: bold; margin-top: 4px; margin-bottom: 12px;">
Subscriptions
</div>

<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Strategic Classification</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 4px;">
core/supportive/generic/other
</div>
<div style="color: #c62828; font-size: 1em; margin-bottom: 12px;">
<strong>Generic - </strong>
Gestiona el modelo comercial de Guardian+, controlando el ciclo de vida de las suscripciones, planes y beneficios disponibles para cada usuario.
</div>

<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Description</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 4px;">
Summary of purpose and responsibilities - not implementation
</div>
<div style="color: #c62828; font-size: 0.95em; line-height: 1.4; margin-bottom: 15px;">
Gestiona el ciclo de vida de una Subscription desde su solicitud y activación hasta su renovación, cambio de Plan, cancelación y expiración. Coordina los pagos requeridos con el Payment Provider y mantiene sincronizados los Entitlements que determinan las capacidades disponibles para el Subscriber.
</div>

<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Business Policies</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 8px;">
Key business rules and policies
</div>

<table width="100%" border="0" cellpadding="0" cellspacing="4" style="text-align: center;">
<tr>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Payment Verification Policy
</td>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Renewal Scheduler Policy
</td>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Entitlement Synchronization Policy
</td>
</tr>
<tr>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Subscription Activation Requirements
</td>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Cancellation Effective Date Policy
</td>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Plan Change Conditions Policy
</td>
</tr>
</table>

<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Ubiquitous Language</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 6px;">
Key domain terminology
</div>

<table width="100%" border="0" cellpadding="0" cellspacing="0"
       style="color: #c62828; font-weight: bold; font-size: 0.85em;">
<tr>
<td width="50%" valign="top">
• Subscription<br>
• Plan<br>
• Subscriber<br>
• Renewal
</td>
<td width="50%" valign="top">
• Entitlement<br>
• Payment Attempt<br>
• Cancellation<br>
• Expiration
</td>
</tr>
</table>

</td>

<td width="58%" valign="top" style="padding: 0;">

<div style="padding: 12px; border-bottom: 2px solid #333;">

<div align="center">
<strong style="font-size: 1em;">Capabilities &amp; Responsibilities</strong><br>
<span style="font-size: 0.75em; color: #777;">Services provided to consumers</span>
</div>

<table width="100%" border="0" cellpadding="8" cellspacing="0" style="margin-top: 8px;">
<tr>

<td width="50%" valign="top" align="center"
    style="border-right: 1px solid #ddd; padding-right: 10px;">

<strong style="font-size: 0.85em;">Informational</strong><br>
<span style="font-size: 0.7em; color: #777;">Queries, reports, etc.</span><br><br>

<table width="90%" border="0" cellpadding="8" cellspacing="0"
       bgcolor="#e8f5e9"
       style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">
<tr>
<td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">
Get Subscription Status
</td>
</tr>
</table>

<table width="90%" border="0" cellpadding="8" cellspacing="0"
       bgcolor="#e8f5e9"
       style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">
<tr>
<td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">
Get Current Plan
</td>
</tr>
</table>

<table width="90%" border="0" cellpadding="8" cellspacing="0"
       bgcolor="#e8f5e9"
       style="border: 1px solid #2e7d32; text-align: center;">
<tr>
<td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">
Check Available Entitlements
</td>
</tr>
</table>

</td>

<td width="50%" valign="top" align="center" style="padding-left: 10px;">

<strong style="font-size: 0.85em;">Actions</strong><br>
<span style="font-size: 0.7em; color: #777;">Invokable commands, scheduled tasks, etc.</span><br><br>

<table width="90%" border="0" cellpadding="6" cellspacing="0"
       bgcolor="#e3f2fd"
       style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Request / Activate Subscription
</td></tr>
</table>

<table width="90%" border="0" cellpadding="6" cellspacing="0"
       bgcolor="#e3f2fd"
       style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Renew Subscription
</td></tr>
</table>

<table width="90%" border="0" cellpadding="6" cellspacing="0"
       bgcolor="#e3f2fd"
       style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Request / Apply Plan Change
</td></tr>
</table>

<table width="90%" border="0" cellpadding="6" cellspacing="0"
       bgcolor="#e3f2fd"
       style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Request / Execute Cancellation
</td></tr>
</table>

<table width="90%" border="0" cellpadding="6" cellspacing="0"
       bgcolor="#e3f2fd"
       style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Process Payment Result
</td></tr>
</table>

<table width="90%" border="0" cellpadding="6" cellspacing="0"
       bgcolor="#e3f2fd"
       style="border: 1px solid #1565c0; text-align: center;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Update Entitlements
</td></tr>
</table>

</td>
</tr>
</table>
</div>

<div style="padding: 12px;">

<div align="center" style="margin-bottom: 8px;">
<strong style="font-size: 1em;">Dependencies</strong><br>
<span style="font-size: 0.75em; color: #777;">
Interactions with other bounded contexts and services
</span>
</div>

<table width="100%" border="1" cellpadding="6" cellspacing="0"
       style="border-collapse: collapse; font-size: 0.8em; text-align: left;">

<tr bgcolor="#f5f5f5">
<th>Name</th>
<th>Reason</th>
<th>System</th>
<th>Relationship</th>
</tr>

<tr>
<td>IAM</td>
<td>Provee la identidad autenticada y el UserId del Subscriber</td>
<td>Internal</td>
<td>In (OHS / PL)</td>
</tr>

<tr>
<td>Stripe</td>
<td>Procesa pagos de activación y renovación y devuelve confirmaciones o fallos mediante webhooks</td>
<td>External</td>
<td>In / Out (ACL)</td>
</tr>

<tr>
<td>Guardian+ Feature Contexts</td>
<td>Consumen el estado de los Entitlements para habilitar capacidades asociadas al plan activo</td>
<td>Internal</td>
<td>Out (OHS / PL)</td>
</tr>

</table>
</div>

</td>
</tr>
</table>

##### Bounded Context: Profile (Generic Domain)

<!-- CANVAS: PROFILE (NICK TUNE V1 TEMPLATE) -->

La Figura 2.35 presenta el Bounded Context Canvas de Profile.

<a id="figura-2-35"></a>**Figura 2.35.** Bounded Context Canvas de Profile

<table class="canvas" table border="1" width="100%" cellpadding="10" cellspacing="0" style="border-collapse: collapse; font-family: Arial, sans-serif;">
<tr>

<td width="42%" valign="top"
    style="border-right: 2px solid #333; border-bottom: none; padding: 15px;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Name</div>
<div style="color: #c62828; font-size: 1.3em; font-weight: bold; margin-top: 4px; margin-bottom: 12px;">
Profile
</div>

<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Strategic Classification</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 4px;">
core/supportive/generic/other
</div>

<div style="color: #c62828; font-size: 1em; margin-bottom: 12px;">
<strong>Generic - </strong>
Proporciona la identidad descriptiva, las relaciones de cuidado y las preferencias necesarias para que los demás contextos de Guardian+ operen sobre usuarios y personas bajo cuidado.
</div>

<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Description</div>

<div style="font-size: 0.75em; color: #777; margin-bottom: 4px;">
Summary of purpose and responsibilities - not implementation
</div>

<div style="color: #c62828; font-size: 0.95em; line-height: 1.4; margin-bottom: 15px;">
Gestiona los User Profiles y Care Recipient Profiles de Guardian+, mantiene la información personal y de contacto, establece y finaliza Care Relationships entre usuarios y personas bajo cuidado, y administra las preferencias de idioma, accesibilidad y experiencia de uso.
</div>

<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Business Policies</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 8px;">
Key business rules and policies
</div>

<table width="100%" border="0" cellpadding="0" cellspacing="4" style="text-align: center;">

<tr>
<td width="32%" bgcolor="#e8eaf6"
    style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Profile Completeness Policy
</td>

<td width="32%" bgcolor="#e8eaf6"
    style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Care Relationship Lifecycle Policy
</td>

<td width="32%" bgcolor="#e8eaf6"
    style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
IAM Identity Ownership Boundary
</td>
</tr>

<tr>
<td width="32%" bgcolor="#e8eaf6"
    style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Profile Completeness Policy
</td>

<td width="32%" bgcolor="#e8eaf6"
    style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Care Recipient Linking Policy
</td>

<td width="32%" bgcolor="#e8eaf6"
    style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Preference Validation Policy
</td>
</tr>

</table>

<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Ubiquitous Language</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 6px;">
Key domain terminology
</div>

<table width="100%" border="0" cellpadding="0" cellspacing="0"
       style="color: #c62828; font-weight: bold; font-size: 0.85em;">

<tr>
<td width="50%" valign="top">
• User Profile<br>
• Care Recipient Profile<br>
• Care Relationship<br>
• Profile Completeness
</td>

<td width="50%" valign="top">
• User Preferences<br>
• Contact Information<br>
• Language Preference<br>
• Accessibility Preference
</td>
</tr>

</table>

</td>

<td width="58%" valign="top" style="padding: 0;">

<div style="padding: 12px; border-bottom: 2px solid #333;">

<div align="center">
<strong style="font-size: 1em;">Capabilities &amp; Responsibilities</strong><br>
<span style="font-size: 0.75em; color: #777;">Services provided to consumers</span>
</div>

<table width="100%" border="0" cellpadding="8" cellspacing="0" style="margin-top: 8px;">

<tr>

<td width="50%" valign="top" align="center"
    style="border-right: 1px solid #ddd; padding-right: 10px;">

<strong style="font-size: 0.85em;">Informational</strong><br>
<span style="font-size: 0.7em; color: #777;">Queries, reports, etc.</span><br><br>

<table width="90%" border="0" cellpadding="8" cellspacing="0"
       bgcolor="#e8f5e9"
       style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">
Get User Profile
</td></tr>
</table>

<table width="90%" border="0" cellpadding="8" cellspacing="0"
       bgcolor="#e8f5e9"
       style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">
Get Care Recipient Profile
</td></tr>
</table>

<table width="90%" border="0" cellpadding="8" cellspacing="0"
       bgcolor="#e8f5e9"
       style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">
Get Care Relationships
</td></tr>
</table>

<table width="90%" border="0" cellpadding="8" cellspacing="0"
       bgcolor="#e8f5e9"
       style="border: 1px solid #2e7d32; text-align: center;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">
Get User Preferences
</td></tr>
</table>

</td>

<td width="50%" valign="top" align="center" style="padding-left: 10px;">

<strong style="font-size: 0.85em;">Actions</strong><br>
<span style="font-size: 0.7em; color: #777;">Invokable commands, scheduled tasks, etc.</span><br><br>

<table width="90%" border="0" cellpadding="6" cellspacing="0"
       bgcolor="#e3f2fd"
       style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Create / Update Profile
</td></tr>
</table>

<table width="90%" border="0" cellpadding="6" cellspacing="0"
       bgcolor="#e3f2fd"
       style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Update Contact Information
</td></tr>
</table>

<table width="90%" border="0" cellpadding="6" cellspacing="0"
       bgcolor="#e3f2fd"
       style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Create Care Recipient Profile
</td></tr>
</table>

<table width="90%" border="0" cellpadding="6" cellspacing="0"
       bgcolor="#e3f2fd"
       style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Establish / End Care Relationship
</td></tr>
</table>

<table width="90%" border="0" cellpadding="6" cellspacing="0"
       bgcolor="#e3f2fd"
       style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Update Language &amp; Accessibility
</td></tr>
</table>

<table width="90%" border="0" cellpadding="6" cellspacing="0"
       bgcolor="#e3f2fd"
       style="border: 1px solid #1565c0; text-align: center;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Update Application Preferences
</td></tr>
</table>

</td>
</tr>
</table>

</div>

<div style="padding: 12px;">

<div align="center" style="margin-bottom: 8px;">
<strong style="font-size: 1em;">Dependencies</strong><br>
<span style="font-size: 0.75em; color: #777;">
Interactions with other bounded contexts and services
</span>
</div>

<table width="100%" border="1" cellpadding="6" cellspacing="0"
       style="border-collapse: collapse; font-size: 0.8em; text-align: left;">

<tr bgcolor="#f5f5f5">
<th>Name</th>
<th>Reason</th>
<th>System</th>
<th>Relationship</th>
</tr>

<tr>
<td>IAM</td>
<td>Provee la identidad autenticada y el UserId asociado al Profile sin transferir la propiedad de credenciales</td>
<td>Internal</td>
<td>In (OHS / PL)</td>
</tr>

<tr>
<td>Emergency &amp; Alerting</td>
<td>Consume cambios en Care Relationships y contactos para mantener una proyección local del Care Circle</td>
<td>Internal</td>
<td>Out (Customer / Supplier + ECST)</td>
</tr>

<tr>
<td>Health Monitoring</td>
<td>Consume la identidad del Care Recipient necesaria para asociar información de monitoreo</td>
<td>Internal</td>
<td>Out (Supplier)</td>
</tr>

<tr>
<td>Care Routines &amp; Wellness</td>
<td>Consume la identidad del Care Recipient y sus relaciones de cuidado para asignar rutinas</td>
<td>Internal</td>
<td>Out (Supplier)</td>
</tr>

<tr>
<td>Mobility &amp; Geofencing</td>
<td>Consume la identidad de la persona bajo cuidado para asociar zonas seguras y seguimiento</td>
<td>Internal</td>
<td>Out (Supplier)</td>
</tr>

</table>

</div>

</td>
</tr>
</table>

##### Bounded Context: Mobility & Geofencing (Supporting Domain)
<!-- CANVAS: MOBILITY & GEOFENCING (NICK TUNE V1 TEMPLATE) -->

La Figura 2.36 presenta el Bounded Context Canvas de Mobility & Geofencing.

<a id="figura-2-36"></a>**Figura 2.36.** Bounded Context Canvas de Mobility & Geofencing

<table class="canvas" table class="canvas" table border="1" width="100%" cellpadding="10" cellspacing="0" style="border-collapse: collapse; font-family: Arial, sans-serif;">
<tr>

<td width="42%" valign="top" style="border-right: 2px solid #333; border-bottom: none; padding: 15px;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Name</div>
<div style="color: #c62828; font-size: 1.3em; font-weight: bold; margin-top: 4px; margin-bottom: 12px;">
Mobility &amp; Geofencing
</div>

<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Strategic Classification</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 4px;">
core/supportive/generic/other
</div>

<div style="color: #c62828; font-size: 1em; margin-bottom: 12px;">
<strong>Supporting - </strong>
Proporciona capacidades de seguimiento de ubicación y control de zonas seguras que complementan las funciones principales de monitoreo y respuesta ante emergencias de Guardian+.
</div>

<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Description</div>

<div style="font-size: 0.75em; color: #777; margin-bottom: 4px;">
Summary of purpose and responsibilities - not implementation
</div>

<div style="color: #c62828; font-size: 0.95em; line-height: 1.4; margin-bottom: 15px;">
Gestiona el seguimiento de ubicación de la persona bajo cuidado, administra las Safe Zones configuradas y evalúa las ubicaciones recibidas para determinar si la persona permanece dentro de una zona segura o si se ha producido una violación de dicha zona.
</div>

<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Business Policies</div>

<div style="font-size: 0.75em; color: #777; margin-bottom: 8px;">
Key business rules and policies
</div>

<table width="100%" border="0" cellpadding="0" cellspacing="4" style="text-align: center;">

<tr>

<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Safe Zone Boundary Policy
</td>

<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Location Validation Policy
</td>

<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Zone Violation Detection Policy
</td>

</tr>

<tr>

<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
La ubicación se evalúa respecto a la zona segura activa configurada.
</td>

<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Solo se procesan ubicaciones que contengan coordenadas válidas y una marca temporal válida.
</td>

<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">
Una salida de la zona segura genera un evento de violación para iniciar el flujo de atención correspondiente.
</td>

</tr>

</table>

<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">
Ubiquitous Language
</div>

<div style="font-size: 0.75em; color: #777; margin-bottom: 6px;">
Key domain terminology
</div>

<table width="100%" border="0" cellpadding="0" cellspacing="0" style="color: #c62828; font-weight: bold; font-size: 0.85em;">

<tr>

<td width="50%" valign="top">
• Geofence<br>
• Safe Zone<br>
• Location<br>
• Location Tracking
</td>

<td width="50%" valign="top">
• Location Status<br>
• Zone Violation<br>
• Coordinates<br>
• Safe Zone Boundary
</td>

</tr>

</table>

</td>


<td width="58%" valign="top" style="padding: 0;">

<div style="padding: 12px; border-bottom: 2px solid #333;">

<div align="center">
<strong style="font-size: 1em;">
Capabilities &amp; Responsibilities
</strong>
<br>
<span style="font-size: 0.75em; color: #777;">
Services provided to consumers
</span>
</div>

<table width="100%" border="0" cellpadding="8" cellspacing="0" style="margin-top: 8px;">

<tr>

<td width="50%" valign="top" align="center" style="border-right: 1px solid #ddd; padding-right: 10px;">

<strong style="font-size: 0.85em;">
Informational
</strong>

<br>

<span style="font-size: 0.7em; color: #777;">
Queries, reports, etc.
</span>

<br><br>


<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">

<tr>
<td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">
Get Current Location
</td>
</tr>

</table>


<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">

<tr>
<td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">
Get Location History
</td>
</tr>

</table>


<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">

<tr>
<td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">
Get Active Safe Zone
</td>
</tr>

</table>


<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center;">

<tr>
<td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">
Get Location Status
</td>
</tr>

</table>

</td>


<td width="50%" valign="top" align="center" style="padding-left: 10px;">

<strong style="font-size: 0.85em;">
Actions
</strong>

<br>

<span style="font-size: 0.7em; color: #777;">
Invokable commands, scheduled tasks, etc.
</span>

<br><br>


<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">

<tr>
<td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Create Safe Zone
</td>
</tr>

</table>


<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">

<tr>
<td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Update Safe Zone
</td>
</tr>

</table>


<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">

<tr>
<td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Receive Location
</td>
</tr>

</table>


<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">

<tr>
<td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Evaluate Location
</td>
</tr>

</table>


<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">

<tr>
<td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Record Location Status
</td>
</tr>

</table>


<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center;">

<tr>
<td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">
Record Safe Zone Violation
</td>
</tr>

</table>

</td>

</tr>

</table>

</div>

<div style="padding: 12px;">
<div align="center" style="margin-bottom: 8px;">
<strong style="font-size: 1em;">Dependencies</strong><br>
<span style="font-size: 0.75em; color: #777;">
Interactions with other bounded contexts and services
</span>
</div>

<table width="100%" border="1" cellpadding="6" cellspacing="0"
style="border-collapse: collapse; font-size: 0.8em; text-align: left;">

<tr bgcolor="#f5f5f5">
<th>Name</th>
<th>Reason</th>
<th>System</th>
<th>Relationship</th>
</tr>

<tr>
<td>Wearable Device / Location Provider</td>
<td>
Proporciona las coordenadas de ubicación utilizadas
para evaluar la posición del adulto mayor respecto
a las zonas seguras configuradas.
</td>
<td>External</td>
<td>In (ACL)</td>
</tr>

<tr>
<td>Profile</td>
<td>
Permite asociar las geocercas con el adulto mayor
y resolver la información contextual necesaria
para su configuración.
</td>
<td>Internal</td>
<td>In (Customer/Supplier)</td>
</tr>

<tr>
<td>IAM</td>
<td>
Valida la autenticación y autorización de las
operaciones de creación, actualización y gestión
de geocercas.
</td>
<td>Internal</td>
<td>In (OHS)</td>
</tr>

<tr>
<td>Emergency &amp; Alerting</td>
<td>
Consume el evento SafeZoneBreached generado cuando
la ubicación del adulto mayor se encuentra fuera
de los límites de una zona segura.
</td>
<td>Internal</td>
<td>Out (Published Language)</td>
</tr>

</table>
</div>
</td>

</tr>

</table>

##### Bounded Context: IAM (Generic Domain)

<!-- CANVAS: IAM (NICK TUNE V1 TEMPLATE) -->

La Figura 2.37 presenta el Bounded Context Canvas de IAM.

<a id="figura-2-37"></a>**Figura 2.37.** Bounded Context Canvas de IAM

<table class="canvas" table border="1" width="100%" cellpadding="10" cellspacing="0" style="border-collapse: collapse; font-family: Arial, sans-serif;">
<tr>
<td width="42%" valign="top" style="border-right: 2px solid #333; border-bottom: none; padding: 15px;">
<div style="font-size: 0.9em; font-weight: bold; color: #222;">Name</div>
<div style="color: #c62828; font-size: 1.3em; font-weight: bold; margin-top: 4px; margin-bottom: 12px;">IAM</div>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Strategic Classification</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 4px;">core/supportive/generic/other</div>
<div style="color: #c62828; font-size: 1em; margin-bottom: 12px;">
<strong>Generic - </strong> Provee acceso seguro a la plataforma mediante un problema común a cualquier sistema de software (identidad y autenticación), sin constituir un diferenciador propio de Guardian+.
</div>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Description</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 4px;">Summary of purpose and responsibilities - not implementation</div>
<div style="color: #c62828; font-size: 0.95em; line-height: 1.4; margin-bottom: 15px;">
Gestiona el ciclo de vida completo de la identidad digital de cuidadores y familiares registrados en Guardian+: registro y verificación de credenciales, autenticación reforzada mediante un segundo factor (OTP) y recuperación segura de contraseña. Actúa como el Open Host Service que emite y valida la identidad autenticada consumida por el resto de los Bounded Contexts.
</div>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Business Policies</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 8px;">Key business rules and policies</div>
<table width="100%" border="0" cellpadding="0" cellspacing="4" style="text-align: center;">
<tr>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">Email Uniqueness Policy</td>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">Mandatory Email Verification Policy</td>
<td width="32%" bgcolor="#e8eaf6" style="border: 1px solid #3f51b5; padding: 8px; font-size: 0.8em;">Two-Factor OTP Authentication Policy</td>
</tr>
</table>
<hr style="border: 0; border-top: 1px solid #ddd; margin: 10px 0;">

<div style="font-size: 0.9em; font-weight: bold; color: #222;">Ubiquitous Language</div>
<div style="font-size: 0.75em; color: #777; margin-bottom: 6px;">Key domain terminology</div>
<table width="100%" border="0" cellpadding="0" cellspacing="0" style="color: #c62828; font-weight: bold; font-size: 0.85em;">
<tr>
<td width="50%" valign="top">
• UserAccount<br>
• Credentials<br>
• Email Verification<br>
• One-Time Password (OTP)<br>
• Password Reset Token
</td>
<td width="50%" valign="top">
• Password Reset Token<br>
• Authenticated User<br>
• Login Session<br>
• Two-Factor Authentication (2FA)
</td>
</tr>
</table>
</td>

<td width="58%" valign="top" style="padding: 0;">
<div style="padding: 12px; border-bottom: 2px solid #333;">
<div align="center">
<strong style="font-size: 1em;">Capabilities &amp; Responsibilities</strong><br>
<span style="font-size: 0.75em; color: #777;">Services provided to consumers</span>
</div>
<table width="100%" border="0" cellpadding="8" cellspacing="0" style="margin-top: 8px;">
<tr>
<td width="50%" valign="top" align="center" style="border-right: 1px solid #ddd; padding-right: 10px;">
<strong style="font-size: 0.85em;">Informational</strong><br>
<span style="font-size: 0.7em; color: #777;">Queries, reports, etc.</span><br><br>
<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">Get User Account By Id</td></tr>
</table>
<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center; margin-bottom: 8px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">Get User Account By Email</td></tr>
</table>
<table width="90%" border="0" cellpadding="8" cellspacing="0" bgcolor="#e8f5e9" style="border: 1px solid #2e7d32; text-align: center;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #1b5e20;">Check Email Availability</td></tr>
</table>
</td>
<td width="50%" valign="top" align="center" style="padding-left: 10px;">
<strong style="font-size: 0.85em;">Actions</strong><br>
<span style="font-size: 0.7em; color: #777;">Invokable commands, scheduled tasks, etc.</span><br><br>

<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Register User Credentials</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Issue Email Verification Code</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Verify Email</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Login (Validate Credentials)</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Trigger / Verify OTP (2FA)</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center; margin-bottom: 6px;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Request Password Reset</td></tr>
</table>
<table width="90%" border="0" cellpadding="6" cellspacing="0" bgcolor="#e3f2fd" style="border: 1px solid #1565c0; text-align: center;">
<tr><td style="font-size: 0.8em; font-weight: bold; color: #0d47a1;">Reset Password</td></tr>
</table>
</td>
</tr>
</table>
</div>

<div style="padding: 12px;">
<div align="center" style="margin-bottom: 8px;">
<strong style="font-size: 1em;">Dependencies</strong><br>
<span style="font-size: 0.75em; color: #777;">Interactions with other bounded contexts and services</span>
</div>
<table width="100%" border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; font-size: 0.8em; text-align: left;">
<tr bgcolor="#f5f5f5">
<th>Name</th>
<th>Reason</th>
<th>System</th>
<th>Relationship</th>
</tr>
<tr>
<td>Email Provider</td>
<td>Envía los correos de verificación de cuenta, códigos OTP y enlaces de recuperación de contraseña</td>
<td>External</td>
<td>Out (ACL)</td>
</tr>
<tr>
<td>Profile</td>
<td>Provee identidad autenticada (UserId) para que Profile asocie la información descriptiva del usuario</td>
<td>Internal</td>
<td>Out (OHS/PL)</td>
</tr>
<tr>
<td>Subscriptions</td>
<td>Provee identidad autenticada (UserId) para resolver el titular de la suscripción</td>
<td>Internal</td>
<td>Out (OHS/PL)</td>
</tr>
<tr>
<td>Health Monitoring</td>
<td>Provee identidad autenticada (UserId) para autorizar el acceso a la telemetría del Fragile Citizen</td>
<td>Internal</td>
<td>Out (OHS/PL)</td>
</tr>
<tr>
<td>Emergency &amp; Alerting</td>
<td>Valida identidad y autorización de cada comando de incidentes, alertas y escalamiento</td>
<td>Internal</td>
<td>Out (OHS/PL)</td>
</tr>
<tr>
<td>Mobility &amp; Geofencing</td>
<td>Valida la autenticación y autorización de las operaciones de creación y gestión de geocercas</td>
<td>Internal</td>
<td>Out (OHS/PL)</td>
</tr>
</table>
</div>
</td>
</tr>
</table>

### 2.5.2. Context Mapping

En esta sección se definen las relaciones entre los siete Bounded Contexts de Guardian+ y los sistemas externos. Se evalúan alternativas mediante preguntas heurísticas, se comparan las topologías posibles y se presentan el Context Map global, dos mapas enfocados y el catálogo de patrones de integración.

#### 2.5.2.1. Heurísticas de Diseño y Exploración de Alternativas (What-If Analysis Global)

El equipo sometió la totalidad de los siete Bounded Contexts candidatos al proceso de cuestionamiento heurístico recomendado por Domain-Driven Design (DDD Crew y Nick Tune) para validar la ubicación de cada capability y evitar dependencias cíclicas o acoplamiento innecesario:

*   **¿Qué pasaría si movemos el capability de evaluación de umbrales clínicos (`EvaluateVitalSignsThresholds`) de *Health Monitoring* a *Emergency & Alerting*?**
    *   *Evaluación:* Si la evaluación clínica se traslada a Emergencias, *Health Monitoring* se degradaría a un almacén pasivo de telemetría (CRUD). Además, obligaría a *Emergency & Alerting* a conocer la semántica médica de rangos basales, tolerancias fisiológicas y filtros de ruido. Se descarta: la evaluación médica permanece en *Health Monitoring*, y este solo notifica a emergencias cuando una anomalía clínica ha sido confirmada.
*   **¿Qué pasaría si descomponemos el capability de alertas en *Emergency & Alerting* y movemos el despacho de recordatorios de medicación desde *Care Routines & Wellness* hacia este?**
    *   *Evaluación:* Aunque ambos implican notificar al usuario, sus invariantes y acuerdos de nivel de servicio (SLA) son divergentes. Una alerta de emergencia exige despacho de máxima prioridad en menos de 5 segundos con escalamiento jerárquico no bloqueante, mientras que un recordatorio de medicación es un aviso programado con tolerancia a reintentos lentos. Mezclarlos en el mismo contexto generaría contención y riesgo de saturación en el bus de emergencias críticas. Se mantiene la separación.
*   **¿Qué pasaría si tomamos el capability de despacho de notificaciones (Push/SMS) de *Emergency & Alerting*, *Care Routines & Wellness* y *Health Monitoring* para formar un nuevo Bounded Context (*Notification Service*)?**
    *   *Evaluación:* Crear un contexto de dominio para enviar notificaciones introduce una sobrecarga transaccional y de red innecesaria para una función que es netamente técnica y de infraestructura. En su lugar, cada contexto interactúa de manera aislada con pasarelas de mensajería externas a través de puertos y adaptadores (`Infrastructure Layer`).
*   **¿Qué pasaría si duplicamos la información de relaciones de cuidado (`CareCircle`) en *Emergency & Alerting* para romper la dependencia en tiempo real con *Profile*?**
    *   *Evaluación:* Durante un incidente crítico (como una caída con pérdida de conocimiento), una falla de red o una consulta lenta hacia *Profile* bloquearía el auxilio al paciente. Se decidió que *Emergency & Alerting* almacene su propia agenda y jerarquía de contactos del *Care Circle* y consulte a *Profile* solo mediante una Anti-Corruption Layer al registrar un contacto. Los eventos de integración emitidos por *Profile* (`CareRelationshipEstablished`, `CareRelationshipEnded`) son el contrato previsto para mantener esa agenda sincronizada.
*   **¿Qué pasaría si unificamos *IAM*, *Profile* y *Subscriptions* en un único gran Bounded Context genérico?**
    *   *Evaluación:* Aunque los tres pertenecen al Generic Domain, operan con ciclos de vida y razones de cambio dispares. *IAM* maneja autenticación, credenciales efímeras y seguridad criptográfica; *Profile* gestiona la semántica de lazos familiares y preferencias de accesibilidad; y *Subscriptions* gobierna la facturación recurrente, planes comerciales y pasarelas de pago. Mantenerlos como tres contextos genéricos separados protege la pureza de sus modelos y minimiza el radio de impacto ante auditorías de seguridad o cambios en proveedores comerciales.
*   **¿Qué pasaría si aislamos el cálculo de transgresión de zonas seguras en *Mobility & Geofencing* y emitimos solo eventos de brecha a *Emergency & Alerting*?**
    *   *Evaluación:* Es la decisión óptima. *Mobility & Geofencing* ingesta la señal de posicionamiento GPS y calcula polígonos/radios geográficos de manera continua. *Emergency & Alerting* no necesita conocer latitud ni longitud en cada segundo, únicamente consume el evento de negocio `SafeZoneViolation` cuando la persona abandona su perímetro seguro autorizado.

---

#### 2.5.2.2. Discusión de Alternativas de Context Mapping Global

La Tabla 2.51 compara las alternativas de Context Mapping evaluadas por el equipo, con sus ventajas, desventajas y el veredicto sobre cada una.

<a id="tabla-2-51"></a>**Tabla 2.51.** Alternativas de Context Mapping evaluadas

| Alternativa | Topología y Patrones Evaluados | Ventajas | Desventajas | Veredicto |
| :--- | :--- | :--- | :--- | :--- |
| **Alternativa 1:** Modelo Monolítico con *Shared Kernel* | Todos los contextos de negocio comparten un núcleo común de librerías (`Shared Kernel`) que contiene los modelos de `User`, `Patient` y `Biometrics`. | Reduce el código duplicado y  evita la necesidad de mappers entre módulos en etapas tempranas. | Fuerte acoplamiento bidireccional; cualquier cambio en el modelo del paciente obliga a recompilar y desplegar todos los módulos. Alto riesgo de corrupción conceptual. | **Rechazada:** Destruye la autonomía de los Bounded Contexts y viola los principios del diseño táctico de DDD. |
| **Alternativa 2:** Orquestación Centralizada y *Conformist* | *Emergency & Alerting* actúa como orquestador síncrono mediante llamadas directas REST, conformándose con los esquemas de *Health Monitoring*, *Mobility* y *Profile*. | Trazabilidad directa y centralizada de flujos de control en un único punto. | Efecto dominó: si *Health Monitoring* se congestiona por ráfagas de telemetría IoT, bloquea el hilo de ejecución de *Emergency & Alerting*. Viola los SLAs de tiempo real. | **Rechazada:** Compromete la seguridad física del Fragile Citizen ante contingencias de infraestructura. |
| **Alternativa 3:** Desacoplamiento Basado en Eventos con OHS/PL y ACL | Core Domains consumen eventos de dominio asíncronos vía *Customer/Supplier*; Generic Domains ofrecen contratos abiertos (*Open Host Service*); se usan *Anti-Corruption Layers* para hardware IoT y pasarelas externas. | Aislamiento frente a fallos, procesamiento no bloqueante de telemetría en tiempo real, independencia evolutiva de esquemas y resiliencia ante cortes de servicios externos. | Requiere diseñar y versionar contratos de eventos de integración (*Published Language*) y adaptadores de traducción para cada contexto. | **Aprobada:** Proporciona la resiliencia y el aislamiento de dominio requeridos por la plataforma Guardian+. |

---

#### 2.5.2.3. Context Map Global de Guardian+

Siguiendo las recomendaciones de DDD Crew, el Context Map se presenta en un mapa global y en dos mapas enfocados en preguntas concretas. Los diagramas se generan con Context Mapper a partir de archivos CML: cada relación marca el extremo upstream (U) y downstream (D), y junto a cada contexto se indica el patrón que aplica.

La Tabla 2.52 presenta la leyenda de los patrones usados en los diagramas.

<a id="tabla-2-52"></a>**Tabla 2.52.** Leyenda de patrones del Context Map

| Notación | Patrón | Significado en Guardian+ |
| :--- | :--- | :--- |
| **U / D** | Upstream / Downstream | Los cambios del contexto upstream afectan al downstream, pero no a la inversa. |
| **Customer/Supplier** | Customer / Supplier | El downstream (customer) consume los eventos del upstream (supplier), y sus necesidades se consideran en la planificación del upstream. |
| **OHS** | Open Host Service | El upstream expone un protocolo abierto que cualquier contexto puede usar sin integraciones a medida. |
| **PL** | Published Language | El upstream publica un contrato documentado (eventos de integración o tokens) independiente de su modelo interno. |
| **ACL** | Anticorruption Layer | El downstream traduce el modelo del upstream a su propio Ubiquitous Language para que no contamine su dominio. |
| Borde punteado | Sistema externo | Sistema fuera de Guardian+ con el que se integra un Bounded Context. |

La Figura 2.38 presenta el Context Map global con todas las relaciones entre los Bounded Contexts y los sistemas externos.

<a id="figura-2-38"></a>**Figura 2.38.** Context Map global de Guardian+

![global-context-map](../assets/images/chapterII/context-mapping/global-context-map.png)

La Figura 2.39 responde qué señales disparan alertas en Emergency & Alerting.

<a id="figura-2-39"></a>**Figura 2.39.** Context Map de las señales que disparan alertas

![alerting-context-map](../assets/images/chapterII/context-mapping/alerting-context-map.png)

La Figura 2.40 muestra cómo se integran con Guardian+ la identidad provista por IAM y los sistemas externos.

<a id="figura-2-40"></a>**Figura 2.40.** Context Map de identidad y sistemas externos

![identity-external-context-map](../assets/images/chapterII/context-mapping/identity-external-context-map.png)

#### 2.5.2.4. Catálogo de Relaciones y Patrones de Integración Global

La Tabla 2.53 detalla cada relación del Context Map, con sus extremos, el patrón de integración aplicado y la justificación de su elección.

<a id="tabla-2-53"></a>**Tabla 2.53.** Catálogo de relaciones del Context Map

| Relación | Upstream | Downstream | Patrón | Justificación |
| :--- | :--- | :--- | :--- | :--- |
| Wearable Device → Health Monitoring | Wearable Device (sistema externo) | Health Monitoring | **ACL** | El wearable físico emite tramas crudas serializadas y optimizadas para las restricciones energéticas del microcontrolador (ESP32-S3). Aunque el canal de transporte es un bus Pub/Sub (MQTT), Health Monitoring implementa una Anti-Corruption Layer en su capa de infraestructura (`VitalSignTelemetryMqttSubscriber` y `VitalSignTelemetryMessageHandler`) que valida cada trama y la traduce a los comandos y Value Objects del dominio (`DetectVitalSignsCommand`, `VitalSignValue`), de modo que las particularidades del firmware no acoplen el modelo clínico. |
| Wearable Device → Mobility & Geofencing | Wearable Device (sistema externo) | Mobility & Geofencing | **ACL** | El wearable emite la posición como coordenadas crudas (latitud, longitud y precisión). La ACL (`WearableLocationConsumer` y `WearableLocationTransformer`) transforma cada mensaje en el Value Object `Coordinates` y en el comando `ReceiveLocationCommand`. |
| Wearable Device → Care Routines & Wellness | Wearable Device (sistema externo) | Care Routines & Wellness | **ACL** | `WearableTelemetryBrokerAdapter` recibe la telemetría de actividad, inactividad y sueño, la deserializa en registros propios del contexto y la entrega a `ActivityTelemetryConsumer` y `SleepTelemetryConsumer`, de modo que el formato del dispositivo no alcance al modelo de rutinas. |
| Health Monitoring → Emergency & Alerting | Health Monitoring (supplier) | Emergency & Alerting (customer) | **Customer/Supplier** con **PL** | Health Monitoring actúa como proveedor notificando desviaciones clínicas. Para evitar acoplamiento, expone el evento de integración `VitalSignAnomalyDetected` con el payload necesario (Care Recipient, tipo de signo vital, umbral transgredido, valor y clasificación), de modo que Emergency & Alerting opere como cliente sin conocer cómo se calcularon los umbrales basales. |
| Mobility & Geofencing → Emergency & Alerting | Mobility & Geofencing (supplier) | Emergency & Alerting (customer) | **Customer/Supplier** con **PL**; **ACL** en Emergency & Alerting | Cuando una ubicación del Fragile Citizen queda fuera de su zona segura activa, Mobility & Geofencing emite de forma asíncrona el evento `SafeZoneViolation`, que Emergency & Alerting consume para disparar una alerta de severidad alta y activar el despacho a los contactos de emergencia. Para incluir la ubicación en la notificación, Emergency & Alerting consulta la última ubicación conocida mediante su ACL `MobilityContextAcl`, sin persistirla. |
| Care Routines & Wellness → Emergency & Alerting | Care Routines & Wellness (supplier) | Emergency & Alerting (customer) | **Customer/Supplier** con **PL** | El contexto de rutinas monitorea la actividad diaria del paciente. Si se registra una inactividad prolongada no justificada en horas diurnas (US27), emite el evento `ProlongedInactivityDetected`, consumido por Emergency & Alerting para ejecutar la verificación de bienestar. Del mismo modo, `ReminderReissued` y `MedicationRestockSuggested` se consumen como alertas de severidad media dirigidas al contacto primario. |
| Profile → Emergency & Alerting | Profile (supplier) | Emergency & Alerting (customer) | **Customer/Supplier**; **ACL** en Emergency & Alerting | Emergency & Alerting requiere conocer qué integrantes del Care Circle pueden recibir alertas para el escalamiento a 60 segundos. Para no depender de Profile durante el despacho, mantiene su propia tabla `emergency_contacts` y consulta a Profile solo mediante su ACL `ProfileContextAcl`: al registrar un contacto verifica que exista una relación de cuidado activa y, al componer la notificación, obtiene el nombre del Fragile Citizen. Los eventos `CareRelationshipEstablished` y `CareRelationshipEnded` de Profile son el contrato previsto para activar o desactivar los contactos (sección 2.6.4). |
| Profile → Mobility & Geofencing | Profile | Mobility & Geofencing | **ACL** en Mobility & Geofencing | Mobility & Geofencing verifica los datos del Fragile Citizen mediante su componente Profile ACL, el adaptador anticorrupción que consume la información de identidad del contexto Profile (Figura 2.60). La columna `fragile_citizen_id` de sus tablas referencia los perfiles gobernados por Profile. |
| IAM → Emergency & Alerting, Health Monitoring, Care Routines & Wellness, Mobility & Geofencing, Profile, Subscriptions | IAM | Los seis Bounded Contexts de negocio | **OHS** con **PL** | IAM provee autenticación y autorización mediante tokens de acceso estándar (JSON Web Tokens firmados) con un Published Language documentado. Los contextos descendentes validan la firma de los tokens y extraen el `UserId` y los roles sin consultar la base de datos de identidad en cada petición. |
| Stripe → Subscriptions | Stripe (sistema externo) | Subscriptions | **ACL** | La gestión de pagos depende de las librerías oficiales del proveedor externo. Subscriptions implementa adaptadores (`PaymentWebhookController` y `PaymentProviderAdapter`) que traducen los eventos de facturación de Stripe (`invoice.paid`, `customer.subscription.deleted`) a las transiciones de estado del agregado `Subscription` (`ACTIVE`, `CANCELLED`, `EXPIRED`). |
| Notification Providers → Emergency & Alerting | Notification Providers (sistema externo) | Emergency & Alerting | **ACL** | Emergency & Alerting despacha las notificaciones mediante adaptadores por canal (`PushNotificationProviderAdapter` y `SmsProviderAdapter`) y recibe el resultado de cada entrega en `NotificationDeliveryWebhookController`, de modo que los formatos de los proveedores de push y SMS no alcancen al modelo de alertas. |
| Email Provider → IAM | Email Provider (sistema externo) | IAM | **ACL** | IAM envía los correos de verificación de cuenta, los códigos OTP y los enlaces de recuperación de contraseña mediante `EmailProviderAdapter`, ubicado en el paquete `infrastructure/notifications/adapters` (Figura 2.63), de modo que el proveedor de correo no alcance al modelo de identidad. |

### 2.5.3. Software Architecture

En esta sección se presenta la arquitectura de software de Guardian+ con el C4 Model en sus vistas de contexto, contenedores, componentes y despliegue.

#### 2.5.3.1. Software Architecture Context Level Diagrams

En esta sección se presenta la vista de contexto de Guardian+ aplicando el C4 Model, elaborada con Structurizr. Este diagrama posiciona a Guardian+ como un único sistema de software en el centro, y muestra alrededor a los actores que lo utilizan y a los sistemas externos con los que se integra, sin entrar todavía en detalles internos de implementación.

Guardian+ es utilizado por tres tipos de actores: el Familiar, quien supervisa remotamente el bienestar de la persona bajo cuidado sin estar presente de forma permanente; el Cuidador, encargado del cuidado frecuente o permanente de dicha persona, ya sea de forma particular o institucional; y la Persona bajo cuidado (adulto mayor, persona con discapacidad o en situación de dependencia), quien interactúa con el sistema físicamente a través de la pulsera IoT.

El sistema se integra con cuatro servicios externos, cada uno resolviendo una necesidad específica que Guardian+ no implementa por sí mismo: Stripe, para el procesamiento de pagos y suscripciones; un servicio de notificaciones push/SMS, para el despacho de alertas y recordatorios; un servicio de videollamada, que habilita la comunicación directa en tiempo real entre familiar/cuidador y la persona bajo cuidado; y Google Maps, utilizado tanto para la geocodificación y el cálculo de geocercas en el backend como para la visualización del mapa y la ubicación en tiempo real dentro de la aplicación móvil. La Figura 2.41 presenta el diagrama de contexto.

<a id="figura-2-41"></a>**Figura 2.41.** Diagrama de contexto de Guardian+

![context-diagram](../assets/images/chapterII/c4-diagrams/system-context.png)

#### 2.5.3.2. Software Architecture Container Level Diagrams

Esta sección descompone a Guardian+ en sus contenedores de alto nivel — las unidades desplegables independientes que conforman la solución — y muestra cómo se distribuyen las responsabilidades entre ellos, las decisiones tecnológicas adoptadas y los protocolos de comunicación entre contenedores.

La plataforma está compuesta por cinco contenedores. La Guardian+ Landing Page (React, HTML, CSS, JavaScript) es el sitio público de marketing donde familiares y cuidadores conocen la propuesta de valor, los planes de suscripción y los canales de contacto de Guardian+; funciona como página informativa independiente, sin comunicación directa con el backend. La Guardian+ Mobile Application (Android nativo, Kotlin) es la interfaz que usan diariamente familiares y cuidadores para todo el monitoreo, gestión de rutinas, alertas y localización — es el único cliente que consume la API. El Guardian+ Wearable Firmware (embebido en C/C++ sobre ESP32-S3) es el software que corre dentro de la pulsera IoT, responsable de capturar signos vitales, detectar caídas, obtener ubicación GPS y permitir la activación del botón SOS. La pulsera IoT se proporciona al suscriptor como parte de la afiliación a Guardian+, de modo que la plataforma opera sobre un dispositivo de características conocidas y el usuario aprovecha la totalidad de las funciones de la aplicación. Las capacidades de telemetría, detección de caídas, geolocalización, avisos hápticos y botón SOS están presentes en todos los modelos contemplados; en cambio, la comunicación bidireccional depende del modelo entregado: los modelos con cámara y pantalla admiten videollamada, los modelos con audio bidireccional se limitan a la llamada de voz y los modelos básicos no ofrecen este canal, caso en el que la aplicación recurre a la marcación telefónica convencional (US23).

Ambos clientes activos (Mobile Application y Wearable Firmware) se comunican con la Guardian+ REST API (Java y Spring Boot), que centraliza toda la lógica de negocio del sistema y persiste su información en la Guardian+ Database (PostgreSQL Server) vía JDBC. La comunicación del wearable con el backend utiliza MQTT sobre HTTPS — un protocolo liviano, adecuado para telemetría IoT de bajo consumo — mientras que la aplicación móvil consume la API mediante peticiones RESTful en JSON sobre HTTPS. Adicionalmente, el backend se comunica directamente con Stripe, el servicio de notificaciones y Google Maps para resolver pagos, alertas y geolocalización respectivamente, mientras que la videollamada se establece directamente entre la aplicación móvil y el servicio externo correspondiente, una vez que el backend orquesta el inicio de la sesión. La Figura 2.42 presenta el diagrama de contenedores.


<a id="figura-2-42"></a>**Figura 2.42.** Diagrama de contenedores de Guardian+

![containers-diagram](../assets/images/chapterII/c4-diagrams/containers.png)

#### 2.5.3.3. Software Architecture Components Level Diagrams

Esta sección presenta la vista de componentes de la Guardian+ REST API, ilustrando los módulos funcionales internos del backend y cómo interactúan entre sí para resolver las distintas capacidades del sistema, con la API como elemento centralizado y sus componentes circundantes.

El backend se organiza en siete componentes, correspondientes uno a uno con los Bounded Contexts definidos en el diseño estratégico de Domain-Driven Design del equipo: Emergency & Alerting y Health Monitoring como Core Domains, encargados respectivamente de la detección/escalamiento de emergencias y del monitoreo de signos vitales — los diferenciadores centrales de la propuesta de valor de Guardian+; Care Routines & Wellness y Mobility & Geofencing como Supporting Domains, que dan soporte a la gestión de rutinas de bienestar y a la localización/geocercas; y IAM, Profile y Subscriptions como Generic Domains, que resuelven capacidades transversales reutilizables (identidad y autorización, gestión de perfiles, y planes de suscripción).

Todos los componentes de negocio dependen de IAM para validar identidad y autorización mediante una capa anticorrupción (ACL), asegurando que cada comando solo pueda ser ejecutado por el actor correspondiente (por ejemplo, solo el Cuidador puede cancelar un recordatorio, o solo la persona bajo cuidado puede confirmarlo). Asimismo, Emergency & Alerting escucha eventos de integración emitidos por Health Monitoring, Care Routines & Wellness y Mobility & Geofencing — anomalías en signos vitales, inactividad prolongada y salida de zona segura respectivamente — reaccionando automáticamente para generar y escalar alertas; esta relación es la traducción directa de las políticas ya definidas en el Event Storming del equipo. Finalmente, Emergency & Alerting es también responsable de despachar las notificaciones push/SMS y de orquestar las sesiones de videollamada hacia los servicios externos correspondientes, mientras que Subscriptions se comunica con Stripe para el procesamiento de pagos. La Figura 2.43 presenta el diagrama de componentes.

<a id="figura-2-43"></a>**Figura 2.43.** Diagrama de componentes de la Guardian+ REST API

![components-diagram](../assets/images/chapterII/c4-diagrams/components.png)

#### 2.5.3.4. Software Architecture Deployment Diagrams

En esta sección se presenta la vista de despliegue de Guardian+ aplicando el C4 Model, elaborada con Structurizr. El diagrama muestra la distribución física de la solución en el entorno de producción: los nodos de infraestructura y plataformas en la nube que alojan cada contenedor, los dispositivos sobre los que se ejecutan los clientes y los servicios externos con los que se integra el backend.

La Guardian+ Landing Page se publica en Cloudflare Pages, que la distribuye a través de la red global de entrega de contenido de Cloudflare. La Guardian+ REST API se ejecuta como un contenedor Docker con JRE 26 dentro de una máquina virtual de Microsoft Azure con Ubuntu 24.04, detrás del proxy inverso Caddy, que la publica por HTTPS, y persiste su información en la Guardian+ Database, alojada en el servicio gestionado Azure Database for PostgreSQL. Ambos servicios se ubican en la región Chile Central para reducir la latencia entre el backend y la base de datos.

La Guardian+ Mobile Application se ejecuta en los smartphones Android de familiares y cuidadores, desde Android 7.0 (API 24), y sus versiones de prueba se distribuyen mediante Firebase App Distribution. El Guardian+ Wearable Firmware se ejecuta en la pulsera basada en ESP32-S3; durante el desarrollo, este nodo es reemplazado por el IoT Simulator, que genera la telemetría y los eventos del dispositivo y los envía directamente a la REST API. Finalmente, el backend se integra con los servicios externos de notificaciones (Firebase), pagos (Stripe en modo de prueba), mapas y geolocalización (Google Maps Platform) y videollamadas. La Figura 2.44 presenta el diagrama de despliegue.

<a id="figura-2-44"></a>**Figura 2.44.** Diagrama de despliegue de Guardian+

![deployment-diagram](../assets/images/chapterII/c4-diagrams/deployment.png)

## 2.6. Tactical-Level Domain-Driven Design

En esta sección se detalla el diseño táctico de cada Bounded Context de Guardian+. Para cada uno se describen sus capas Domain, Interface, Application e Infrastructure y se presentan sus diagramas de componentes, de clases y de base de datos. Al final se incluye el esquema físico consolidado de la base de datos.

### 2.6.1. Bounded Context: Emergency & Alerting

El Bounded Context **Emergency & Alerting** pertenece al Core Domain de Guardian+ y es el contexto central de la solución. Su responsabilidad consiste en disparar las alertas ante señales que comprometen la seguridad de un Fragile Citizen (caídas, activaciones de SOS, anomalías biométricas, violaciones de zona segura, inactividad prolongada y avisos de rutina), despacharlas hacia sus contactos de emergencia según la severidad, gobernar el escalamiento hasta obtener un reconocimiento efectivo y registrar la atención del incidente hasta su cierre.

A diferencia de los contextos que producen señales (Health Monitoring, Mobility & Geofencing y Care Routines & Wellness), este contexto no observa telemetría: consume eventos de integración ya interpretados y concentra las reglas de reacción, temporización y escalamiento que traducen una señal en una respuesta humana oportuna. El Fragile Citizen se referencia mediante `CareRecipientProfileId` y los integrantes del Care Circle mediante `UserId`, ambos gobernados por otros contextos.

La arquitectura táctica se implementa sobre Java y Spring Boot con una estructura de paquetes dividida en cuatro capas: domain, interfaces, application e infrastructure. Su código se organiza en el paquete `com.healthify.guardian.platform.emergencyalerting` del repositorio `guardian-plus-platform`, con la siguiente estructura:

```
com.healthify.guardian.platform.emergencyalerting/
├── domain/
│   ├── model/
│   │   ├── aggregates/
│   │   ├── commands/
│   │   ├── entities/
│   │   ├── events/
│   │   ├── queries/
│   │   └── valueobjects/
│   ├── repositories/
│   └── services/
├── interfaces/
│   ├── acl/
│   ├── events/
│   └── rest/
│       ├── resources/
│       └── transform/
├── application/
│   ├── acl/
│   ├── commandservices/
│   ├── internal/
│   │   ├── commandservices/
│   │   ├── eventhandlers/
│   │   ├── outboundservices/
│   │   └── queryservices/
│   ├── outboundservices/
│   └── queryservices/
└── infrastructure/
    ├── acl/
    ├── configuration/
    ├── notifications/
    │   └── adapters/
    ├── persistence/
    │   └── jpa/
    │       ├── adapters/
    │       ├── assemblers/
    │       ├── converters/
    │       ├── embeddables/
    │       ├── entities/
    │       └── repositories/
    └── scheduling/
```

#### 2.6.1.1. Domain Layer

Encapsula las reglas de reacción ante emergencias, las invariantes del ciclo de vida de alertas e incidentes y las políticas de despacho y escalamiento. La decisión de modelado central del contexto es la separación entre `Alert` e `Incident`: `Alert` es el agregado raíz que nace de una señal, se entrega a los contactos de emergencia (`AlertDelivery`) y recoge sus respuestas (`AlertResponse`); `Incident` solo existe cuando un integrante del Care Circle reconoce la alerta y asume la atención, registrando su estabilización y cierre. Por ello, una alerta origina como máximo un incidente, mientras que las alertas descartadas como falso positivo nunca llegan a generar uno.

El escalamiento no se modela como un agregado independiente: se expresa mediante el nivel de destinatario (`RecipientLevel`) de cada entrega, el orden de prioridad de los `EmergencyContact` y el tiempo de espera configurado en `AlertSettings`. Toda operación sujeta a tiempo recibe el instante actual como parámetro (`Instant`) en lugar de leer el reloj, de modo que las ventanas de 20 s y 60 s se verifican de forma determinista.

##### Aggregates

*   **Alert**
    *   Agregado raíz que representa la alerta disparada por una señal de riesgo sobre un Fragile Citizen, junto con sus entregas a los contactos de emergencia y las respuestas del Care Circle.
    *   Hereda de `AbstractDomainAggregateRoot<Alert>` para registrar y publicar eventos de dominio.
    *   Gobierna de forma autónoma su ciclo de vida (`PENDING_CONFIRMATION → TRIGGERED → ESCALATED → ACKNOWLEDGED → RESOLVED`, con `DISMISSED` como salida de un falso positivo), rechazando transiciones inválidas sin depender de servicios externos. La severidad se deriva del tipo de origen (`AlertSourceType.defaultSeverity()`), nunca del emisor de la señal.
    *   *Atributos:*
        *   `id: AlertId`
        *   `careRecipientProfileId: CareRecipientProfileId`
        *   `source: AlertSource`
        *   `severity: Severity`
        *   `status: AlertStatus`
        *   `deliveries: List<AlertDelivery>`
        *   `responses: List<AlertResponse>`
        *   `triggeredAt: Instant`
        *   `confirmedAt: Instant`: inicio de la medición de la latencia de despacho (US08).
        *   `lastDispatchedAt: Instant`: base del cálculo del `AckTimeout` de cada nivel.
        *   `acknowledgedAt: Instant`
        *   `acknowledgedByUserId: UserId`
        *   `resolvedAt: Instant`
        *   `version: Long`: marca de bloqueo optimista restaurada desde persistencia.
    *   *Métodos:*
        *   `Alert(TriggerAlertCommand command)`
        *   `confirm(Instant confirmedAt): void`
        *   `dismissAsFalsePositive(Instant now): void`
        *   `dispatch(RecipientLevel level, List<DeliveryTarget> targets, Instant now): List<AlertDelivery>`
        *   `escalate(List<DeliveryTarget> targets, Instant now): List<AlertDelivery>`
        *   `broadcast(List<DeliveryTarget> targets, Instant now): List<AlertDelivery>`
        *   `registerDeliveryResult(AlertDeliveryId deliveryId, DeliveryStatus status, Instant occurredAt): void`: ignora callbacks repetidos o tardíos del proveedor.
        *   `acknowledge(UserId userId, Instant now): void`: solo un destinatario notificado puede reconocer.
        *   `claimResponse(UserId responderUserId, Instant now): AlertResponse`: solo una respuesta en curso a la vez; si la alerta no estaba reconocida, también la reconoce para detener el escalamiento.
        *   `completeResponse(AlertResponseId responseId, String notes, Instant now): void`
        *   `resolve(Instant now): void`
        *   `currentRecipientLevel(): RecipientLevel`
        *   `isAwaitingAcknowledgement(): boolean`
        *   `isAckTimeoutExpired(AckTimeout ackTimeout, Instant now): boolean`
        *   `isConfirmationWindowExpired(Instant now): boolean`

*   **Incident**
    *   Agregado raíz que representa la atención humana de una alerta reconocida. Referencia a su alerta por identidad (`AlertId`), con una relación de uno a cero o uno.
    *   Ciclo de vida: `IN_ATTENTION → STABILIZED → CLOSED`. Puede cerrarse directamente desde `IN_ATTENTION` cuando no hubo nada que estabilizar; las notas de cada etapa se acumulan.
    *   *Atributos:*
        *   `id: IncidentId`
        *   `alertId: AlertId`
        *   `status: IncidentStatus`
        *   `markedInAttentionAt: Instant`
        *   `stabilizedAt: Instant`
        *   `closedAt: Instant`
        *   `notes: String`
    *   *Métodos:*
        *   `Incident(OpenIncidentCommand command)`
        *   `stabilize(String notes, Instant now): void`
        *   `close(String notes, Instant now): void`
        *   `isClosed(): boolean`

*   **AlertSettings**
    *   Agregado raíz que concentra la configuración de alertamiento por Fragile Citizen: tiempo de espera del reconocimiento, habilitación del escalamiento, difusión inmediata de alertas críticas y modo silencioso. Existe como máximo una configuración por `CareRecipientProfileId`; mientras no se modifique, se aplican los valores por defecto sin persistirlos.
    *   *Atributos:*
        *   `id: AlertSettingsId`
        *   `careRecipientProfileId: CareRecipientProfileId`
        *   `primaryAckTimeout: AckTimeout`
        *   `escalationEnabled: boolean`
        *   `silentModeEnabled: boolean`
        *   `broadcastCriticalImmediately: boolean`
    *   *Métodos:*
        *   `AlertSettings(CareRecipientProfileId careRecipientProfileId)`: crea la configuración con valores por defecto (60 s, escalamiento habilitado, alertas críticas escalan como las demás, modo silencioso desactivado).
        *   `update(AckTimeout primaryAckTimeout, Boolean escalationEnabled, Boolean broadcastCriticalImmediately): void`
        *   `activateSilentMode(): void`
        *   `deactivateSilentMode(): void`
        *   `allowsAudibleNotificationFor(Severity severity): boolean`

*   **EmergencyContact**
    *   Agregado raíz que registra a un integrante del Care Circle como contacto de auxilio de un Fragile Citizen, con su prioridad dentro del escalamiento. Conserva una copia local de los datos del contacto (Event-Carried State Transfer desde Profile) para que un Profile lento o no disponible nunca bloquee un despacho. El contacto activo con `priorityOrder = 1` es el contacto primario.
    *   *Atributos:*
        *   `id: EmergencyContactId`
        *   `careRecipientProfileId: CareRecipientProfileId`
        *   `userId: UserId`
        *   `displayName: String`
        *   `relationship: String`
        *   `phoneNumber: PhoneNumber`
        *   `priorityOrder: PriorityOrder`
        *   `active: boolean`
    *   *Métodos:*
        *   `EmergencyContact(AddEmergencyContactCommand command)`
        *   `updateContactDetails(String displayName, String relationship, PhoneNumber phoneNumber): void`
        *   `changePriority(PriorityOrder priorityOrder): void`
        *   `activate(): void`
        *   `deactivate(): void`
        *   `isPrimary(): boolean`

*   **AlertChannelSetting**
    *   Agregado raíz que registra si un canal de notificación está habilitado para un integrante del Care Circle y, para `PUSH`, el token del dispositivo. Existe un registro por combinación de `UserId` y `NotificationChannel`.
    *   *Atributos:*
        *   `id: AlertChannelSettingId`
        *   `userId: UserId`
        *   `channel: NotificationChannel`
        *   `enabled: boolean`
        *   `deviceToken: String`
    *   *Métodos:*
        *   `AlertChannelSetting(ConfigureAlertChannelCommand command)`
        *   `enable(): void`
        *   `disable(): void`
        *   `registerDeviceToken(String deviceToken): void`

##### Entities

*   **AlertDelivery**
    *   Entidad interna de `Alert` que representa la entrega de la alerta a un destinatario concreto, por un canal y en un nivel de escalamiento determinado.
    *   *Atributos:*
        *   `id: AlertDeliveryId`
        *   `recipientUserId: UserId`
        *   `recipientLevel: RecipientLevel`
        *   `channel: NotificationChannel`
        *   `deliveryStatus: DeliveryStatus`
        *   `sentAt: Instant`
        *   `deliveredAt: Instant`
    *   *Métodos:* `markAsSent(Instant sentAt)`, `markAsDelivered(Instant deliveredAt)`, `markAsFailed()`.
*   **AlertResponse**
    *   Entidad interna de `Alert` que registra que un integrante del Care Circle asumió la respuesta a la alerta y el resultado de su intervención.
    *   *Atributos:*
        *   `id: AlertResponseId`
        *   `responderUserId: UserId`
        *   `responseStatus: ResponseStatus`
        *   `claimedAt: Instant`
        *   `completedAt: Instant`
        *   `notes: String`
    *   *Métodos:* `complete(String notes, Instant completedAt)`, `cancel()`, `isActive()`.

##### Value Objects

*   **AlertSource:** Origen de la alerta (`sourceType: AlertSourceType`, `sourceReferenceId: UUID`). `sourceReferenceId` identifica el registro del contexto proveedor que originó la señal (lectura biométrica, zona segura, monitor de actividad, recordatorio, stock de medicación o dispositivo wearable). Método: `requiresConfirmationWindow()`, verdadero únicamente para `FALL_DETECTED`.
*   **AlertSourceType:** Enum (`FALL_DETECTED`, `SOS_TRIGGERED`, `VITAL_SIGN_ANOMALY`, `SAFE_ZONE_VIOLATION`, `PROLONGED_INACTIVITY`, `REMINDER_REISSUED`, `MEDICATION_RESTOCK_SUGGESTED`). Métodos: `defaultSeverity()` (caída y SOS: `CRITICAL`; anomalía biométrica, zona segura e inactividad: `HIGH`; recordatorio y reabastecimiento: `MEDIUM`) e `isWearableReported()`.
*   **Severity:** Enum (`CRITICAL`, `HIGH`, `MEDIUM`) que gobierna la estrategia de despacho. Métodos: `allowsImmediateBroadcast()`, `allowsEscalation()`, `overridesSilentMode()` y `requiresSmsBackup()`.
*   **AlertStatus:** Enum (`PENDING_CONFIRMATION`, `TRIGGERED`, `ESCALATED`, `ACKNOWLEDGED`, `DISMISSED`, `RESOLVED`). Métodos: `canTransitionTo(AlertStatus target)`, `isTerminal()` e `isAwaitingAcknowledgement()`.
*   **IncidentStatus:** Enum (`IN_ATTENTION`, `STABILIZED`, `CLOSED`).
*   **RecipientLevel:** Enum (`PRIMARY`, `SECONDARY`, `BROADCAST`) que indica en qué nivel del escalamiento se entregó la alerta. Método: `next()`.
*   **NotificationChannel:** Enum (`PUSH`, `SMS`, `IN_APP`).
*   **DeliveryStatus:** Enum (`PENDING`, `SENT`, `DELIVERED`, `FAILED`). Método: `isFinal()`.
*   **ResponseStatus:** Enum (`CLAIMED`, `COMPLETED`, `CANCELLED`).
*   **EmergencyContactChange:** Enum (`ADDED`, `DETAILS_UPDATED`, `REPRIORITIZED`, `ACTIVATED`, `DEACTIVATED`) transportado por `EmergencyContactsChangedEvent`.
*   **AckTimeout:** Encapsula el tiempo de espera del reconocimiento antes de escalar (`seconds: Integer`). Invariante: valor entre $15$ y $300\text{ s}$; valor por defecto $60\text{ s}$. Método: `hasExpired(Instant since, Instant now)`.
*   **FallConfirmationWindow:** Ventana de cancelación local del Fragile Citizen ante una caída detectada. Valor fijo de política de $20\text{ s}$, no persistido. Métodos: `hasExpired(Instant triggeredAt, Instant now)` y `expiredIfTriggeredBefore(Instant now)`.
*   **PriorityOrder:** Posición del contacto dentro del escalamiento (`value: Integer`). Invariante: valor mayor o igual a 1. Método: `isPrimary()`.
*   **PhoneNumber:** Teléfono del contacto para el canal `SMS` (`value: String`). Invariante: formato internacional E.164 (p. ej. `+51987654321`).
*   **DeliveryTarget:** Destinatario y canal resueltos por `EscalationPolicy` (`recipientUserId: UserId`, `channel: NotificationChannel`).
*   **DateRange:** Periodo opcional para filtrar el historial (`from`, `to`). Invariante: `from` no posterior a `to`.
*   **AlertId / AlertDeliveryId / AlertResponseId / IncidentId / AlertSettingsId / EmergencyContactId / AlertChannelSettingId:** Identificadores inmutables tipo UUID, generados por el propio agregado o entidad.
*   **CareRecipientProfileId:** Identificador de referencia inmutable al Fragile Citizen, gobernado por el Bounded Context Profile.
*   **UserId:** Identificador de referencia inmutable a un integrante del Care Circle, gobernado por el Bounded Context IAM.

##### Domain Services

*   **DispatchStrategyPolicy:** Determina el nivel inicial de despacho de una alerta confirmada a partir de su `Severity` y de `AlertSettings`. Por defecto toda alerta comienza en el contacto primario (`PRIMARY`) y escala por niveles, que es el comportamiento comprometido en US08 y US11. `CRITICAL` difunde de inmediato a todos los contactos activos (`BROADCAST`, US25) cuando la configuración del Fragile Citizen lo solicita (`broadcastCriticalImmediately`). `CRITICAL` y `HIGH` también difunden de inmediato si el escalamiento está deshabilitado. `MEDIUM` notifica únicamente al contacto primario. Método: `resolveInitialLevel(Severity severity, AlertSettings settings): RecipientLevel`.
*   **EscalationPolicy:** Resuelve los destinatarios de cada nivel a partir de los `EmergencyContact` activos ordenados por prioridad (`PRIMARY`: primer contacto activo; `SECONDARY`: los siguientes; `BROADCAST`: todos), de modo que los huecos dejados por contactos desactivados no afectan. Los canales salen de `AlertChannelSetting`, con `IN_APP` como respaldo si el contacto no tiene ninguno habilitado, y se añade `SMS` en severidad `CRITICAL` y en el nivel `BROADCAST`. También decide el siguiente nivel cuando vence el `AckTimeout`: `PRIMARY → SECONDARY` (o `BROADCAST` si no hay contactos secundarios o el escalamiento está deshabilitado) y `SECONDARY → BROADCAST`; las alertas `MEDIUM` nunca escalan. Métodos: `resolveRecipients(RecipientLevel level, Severity severity, List<EmergencyContact> contacts, List<AlertChannelSetting> channelSettings): List<DeliveryTarget>` y `resolveNextLevel(Alert alert, AlertSettings settings, List<EmergencyContact> activeContacts): Optional<RecipientLevel>`.

##### Commands & Queries (Domain Model)

*   `TriggerAlertCommand(UUID careRecipientProfileId, AlertSourceType sourceType, UUID sourceReferenceId, Instant triggeredAt)`
*   `ConfirmAlertCommand(UUID alertId)`
*   `DismissAlertCommand(UUID alertId)`
*   `DispatchAlertCommand(UUID alertId)`
*   `EscalateAlertCommand(UUID alertId)`
*   `BroadcastAlertCommand(UUID alertId)`
*   `RegisterDeliveryResultCommand(UUID alertId, UUID deliveryId, DeliveryStatus deliveryStatus, Instant occurredAt)`
*   `AcknowledgeAlertCommand(UUID alertId, UUID userId)`
*   `ClaimAlertResponseCommand(UUID alertId, UUID responderUserId)`
*   `CompleteAlertResponseCommand(UUID alertId, UUID responseId, String notes)`
*   `ResolveAlertCommand(UUID alertId)`
*   `OpenIncidentCommand(UUID alertId, Instant markedInAttentionAt)`
*   `StabilizeIncidentCommand(UUID incidentId, String notes)`
*   `CloseIncidentCommand(UUID incidentId, String notes)`
*   `UpdateAlertSettingsCommand(UUID careRecipientProfileId, Integer primaryAckTimeoutSec, Boolean escalationEnabled, Boolean broadcastCriticalImmediately)`
*   `ActivateSilentModeCommand(UUID careRecipientProfileId)`
*   `DeactivateSilentModeCommand(UUID careRecipientProfileId)`
*   `AddEmergencyContactCommand(UUID careRecipientProfileId, UUID userId, String displayName, String relationship, String phoneNumber, Integer priorityOrder)`
*   `ReorderEmergencyContactsCommand(UUID careRecipientProfileId, List<UUID> orderedEmergencyContactIds)`
*   `DeactivateEmergencyContactCommand(UUID emergencyContactId)`
*   `ConfigureAlertChannelCommand(UUID userId, NotificationChannel channel, Boolean enabled, String deviceToken)`
*   `GetAlertByIdQuery(AlertId alertId)`
*   `GetActiveAlertsByCareRecipientProfileIdQuery(CareRecipientProfileId careRecipientProfileId)`
*   `GetAlertHistoryByCareRecipientProfileIdQuery(CareRecipientProfileId careRecipientProfileId, DateRange dateRange, Severity severityFilter, int page, int size)`
*   `GetPendingAlertsByRecipientUserIdQuery(UserId recipientUserId)`
*   `GetIncidentByIdQuery(IncidentId incidentId)`
*   `GetIncidentByAlertIdQuery(AlertId alertId)`
*   `GetAlertSettingsByCareRecipientProfileIdQuery(CareRecipientProfileId careRecipientProfileId)`
*   `GetEmergencyContactsByCareRecipientProfileIdQuery(CareRecipientProfileId careRecipientProfileId)`
*   `GetAlertChannelSettingsByUserIdQuery(UserId userId)`

##### Domain Events

*   `AlertTriggeredEvent`: Emitido al disparar una alerta, portando su origen, severidad y estado inicial.
*   `AlertConfirmedEvent`: Emitido cuando vence la `FallConfirmationWindow` sin cancelación del Fragile Citizen, o de inmediato cuando el origen no requiere confirmación.
*   `AlertDismissedEvent`: Emitido cuando el Fragile Citizen cancela dentro de la ventana, clasificando la alerta como falso positivo.
*   `AlertDispatchedEvent`: Emitido al generar las entregas de un nivel (`PRIMARY`, `SECONDARY` o `BROADCAST`), con los identificadores de las entregas a enviar.
*   `AlertEscalatedEvent`: Emitido al avanzar al nivel `SECONDARY` por vencimiento del `AckTimeout`.
*   `AlertBroadcastedEvent`: Emitido al difundir la alerta a todos los contactos activos, ya sea de inmediato o como último recurso.
*   `AlertDeliveryFailedEvent`: Emitido cuando el proveedor informa que una entrega no pudo completarse.
*   `AlertAcknowledgedEvent`: Emitido cuando un destinatario reconoce la alerta, deteniendo el escalamiento.
*   `AlertResponseClaimedEvent`: Emitido cuando un destinatario declara que asumirá la respuesta, habilitando la notificación al resto del Care Circle.
*   `AlertResponseCompletedEvent`: Emitido cuando el responsable registra el resultado de su intervención.
*   `AlertResolvedEvent`: Emitido al cerrar definitivamente la alerta tras el cierre de su incidente.
*   `IncidentOpenedEvent`: Emitido al registrar la atención de una alerta reconocida (`IN_ATTENTION`).
*   `IncidentStabilizedEvent`: Emitido cuando el responsable declara estabilizada la situación del Fragile Citizen.
*   `IncidentClosedEvent`: Emitido al cierre definitivo del incidente.
*   `AlertSettingsUpdatedEvent`: Emitido ante cualquier modificación del tiempo de espera, del escalamiento, de la difusión crítica o del modo silencioso.
*   `EmergencyContactsChangedEvent`: Emitido al añadir, actualizar, reordenar, activar o desactivar un contacto de emergencia, indicando el tipo de cambio (`EmergencyContactChange`).
*   `AlertChannelSettingChangedEvent`: Emitido al habilitar o deshabilitar un canal de notificación.

##### Repositories (Domain Interfaces)

*   **AlertRepository:**
    *   `save(Alert alert): Alert`
    *   `findById(AlertId id): Optional<Alert>`
    *   `findActiveBySource(CareRecipientProfileId careRecipientProfileId, AlertSource source): Optional<Alert>`: evita disparar dos veces la misma señal reintentada.
    *   `findActiveByCareRecipientProfileId(CareRecipientProfileId careRecipientProfileId): List<Alert>`
    *   `findHistory(CareRecipientProfileId careRecipientProfileId, DateRange period, Severity severity, Pageable pageable): Page<Alert>`
    *   `findPendingByRecipientUserId(UserId recipientUserId): List<Alert>`
    *   `findPendingConfirmationTriggeredBefore(Instant threshold): List<Alert>`
    *   `findAwaitingAcknowledgement(): List<Alert>`
*   **IncidentRepository:**
    *   `save(Incident incident): Incident`
    *   `findById(IncidentId id): Optional<Incident>`
    *   `findByAlertId(AlertId alertId): Optional<Incident>`
    *   `existsByAlertId(AlertId alertId): boolean`
*   **AlertSettingsRepository:**
    *   `save(AlertSettings settings): AlertSettings`
    *   `findByCareRecipientProfileId(CareRecipientProfileId careRecipientProfileId): Optional<AlertSettings>`
*   **EmergencyContactRepository:**
    *   `save(EmergencyContact contact): EmergencyContact`
    *   `saveAll(List<EmergencyContact> contacts): List<EmergencyContact>`
    *   `findById(EmergencyContactId id): Optional<EmergencyContact>`
    *   `findActiveByCareRecipientProfileIdOrderByPriority(CareRecipientProfileId careRecipientProfileId): List<EmergencyContact>`
    *   `findByCareRecipientProfileIdAndUserId(CareRecipientProfileId careRecipientProfileId, UserId userId): Optional<EmergencyContact>`
*   **AlertChannelSettingRepository:**
    *   `save(AlertChannelSetting setting): AlertChannelSetting`
    *   `findByUserId(UserId userId): List<AlertChannelSetting>`
    *   `findByUserIdIn(Collection<UserId> userIds): List<AlertChannelSetting>`
    *   `findByUserIdAndChannel(UserId userId, NotificationChannel channel): Optional<AlertChannelSetting>`

#### 2.6.1.2. Interface Layer

Traduce estímulos externos hacia comandos y consultas de aplicación, expone contratos HTTP RESTful para la app móvil y canaliza los eventos de integración provenientes de los contextos proveedores de señales. Los errores se devuelven con el formato común de la plataforma: `400` (validación), `404`, `409` (conflicto) y `422` (regla de negocio).

##### REST Controllers

*   **AlertsController** (`/api/v1/alerts`):
    *   `POST /`: Dispara una alerta reportada por el gateway del dispositivo wearable. Fuera del perfil de desarrollo solo acepta `FALL_DETECTED` y `SOS_TRIGGERED`; la hora de disparo la asigna el servidor y reintentar la misma señal devuelve la alerta activa existente.
    *   `GET /`: Historial paginado y filtrable por `careRecipientProfileId`, `severity`, `from`, `to`, `page` y `size`.
    *   `GET /active/care-recipient/{careRecipientProfileId}`: Lista las alertas activas de un Fragile Citizen.
    *   `GET /pending/recipient/{userId}`: Lista las alertas pendientes de reconocimiento de un destinatario; la app móvil la consulta para mostrar las alertas del canal `IN_APP`.
    *   `GET /{alertId}`: Recupera el detalle de una alerta con sus entregas (en orden de despacho) y respuestas.
    *   `POST /{alertId}/dismiss`: Cancela la alerta dentro de la ventana de confirmación (falso positivo).
    *   `POST /{alertId}/acknowledge`: Registra el reconocimiento de la alerta por parte del destinatario.
    *   `POST /{alertId}/responses`: Declara que el destinatario asumirá la respuesta.
    *   `POST /{alertId}/responses/{responseId}/complete`: Registra el resultado de la intervención.
*   **IncidentsController** (`/api/v1/incidents`):
    *   `GET /{incidentId}`: Recupera el detalle de un incidente.
    *   `GET /alert/{alertId}`: Recupera el incidente asociado a una alerta.
    *   `POST /{incidentId}/stabilize`: Declara estabilizada la situación.
    *   `POST /{incidentId}/close`: Cierra definitivamente el incidente.
*   **AlertSettingsController** (`/api/v1/alert-settings`):
    *   `GET /care-recipient/{careRecipientProfileId}`: Recupera la configuración vigente, o los valores por defecto.
    *   `PUT /care-recipient/{careRecipientProfileId}`: Actualiza el tiempo de espera, el escalamiento y la difusión inmediata de alertas críticas.
    *   `POST /care-recipient/{careRecipientProfileId}/silent-mode`: Activa el modo silencioso.
    *   `DELETE /care-recipient/{careRecipientProfileId}/silent-mode`: Desactiva el modo silencioso.
*   **EmergencyContactsController** (`/api/v1/emergency-contacts`):
    *   `GET /care-recipient/{careRecipientProfileId}`: Lista los contactos de emergencia activos ordenados por prioridad.
    *   `POST /`: Incorpora un contacto en la prioridad indicada (o al final), desplazando a los siguientes; reactiva un contacto dado de baja.
    *   `PUT /care-recipient/{careRecipientProfileId}/order`: Reordena la prioridad de los contactos.
    *   `DELETE /{emergencyContactId}`: Desactiva un contacto, validando que permanezca al menos un contacto activo.
*   **AlertChannelSettingsController** (`/api/v1/alert-channel-settings`):
    *   `GET /user/{userId}`: Lista los canales de notificación de un integrante del Care Circle (sin exponer el token del dispositivo).
    *   `PUT /user/{userId}/channels/{channel}`: Habilita o deshabilita un canal y, para `PUSH`, registra el token del dispositivo.
*   **NotificationDeliveryWebhookController** (`/api/v1/webhooks/notification-deliveries`):
    *   `POST /`: Recibe la confirmación de entrega o fallo informada por el proveedor de notificaciones y responde `204`.

##### Resources & Assemblers

*   *Resources (DTOs):* `TriggerAlertResource`, `AlertResource`, `AlertSummaryResource`, `AlertDeliveryResource`, `AlertResponseResource`, `AcknowledgeAlertResource`, `ClaimAlertResponseResource`, `CompleteAlertResponseResource`, `IncidentResource`, `StabilizeIncidentResource`, `CloseIncidentResource`, `AlertSettingsResource`, `UpdateAlertSettingsResource`, `EmergencyContactResource`, `AddEmergencyContactResource`, `ReorderEmergencyContactsResource`, `AlertChannelSettingResource`, `ConfigureAlertChannelResource`, `DeliveryStatusCallbackResource` y `PageResource` (compartido).
*   *Assemblers (Mappers):* `TriggerAlertCommandFromResourceAssembler`, `AlertResourceFromEntityAssembler`, `AcknowledgeAlertCommandFromResourceAssembler`, `IncidentResourceFromEntityAssembler`, `AlertSettingsResourceFromEntityAssembler`, `UpdateAlertSettingsCommandFromResourceAssembler`, `EmergencyContactResourceFromEntityAssembler`, `AddEmergencyContactCommandFromResourceAssembler`, `AlertChannelSettingResourceFromEntityAssembler`, `ConfigureAlertChannelCommandFromResourceAssembler` y `RegisterDeliveryResultCommandFromResourceAssembler`.

##### Integration Events & ACL Facade

*   *Eventos consumidos (inbound):*
    *   `ProlongedInactivityDetectedIntegrationEvent`: Proveniente de `Care Routines & Wellness`; dispara una alerta `PROLONGED_INACTIVITY` con severidad `HIGH`. Mientras el evento no incluya el monitor de actividad, la referencia de origen es el propio Fragile Citizen, por lo que existe como máximo una alerta de inactividad activa por persona.
    *   `ReminderReissuedIntegrationEvent`: Proveniente de `Care Routines & Wellness`; dispara una alerta `REMINDER_REISSUED` con severidad `MEDIUM` dirigida al contacto primario.
    *   `MedicationRestockSuggestedIntegrationEvent`: Proveniente de `Care Routines & Wellness`; dispara una alerta `MEDICATION_RESTOCK_SUGGESTED` con severidad `MEDIUM` dirigida al contacto primario.
    *   `VitalSignAnomalyDetectedIntegrationEvent` (`Health Monitoring`), `SafeZoneViolationIntegrationEvent` (`Mobility & Geofencing`) y `CareRelationshipEstablishedIntegrationEvent` / `CareRelationshipEndedIntegrationEvent` (`Profile`): contratos acordados que se incorporarán cuando esos contextos los publiquen. Mientras tanto, en el perfil de desarrollo las alertas biométricas y de zona segura pueden dispararse mediante `POST /api/v1/alerts`, y los contactos se registran con `POST /api/v1/emergency-contacts`.
*   *Eventos publicados (outbound):*
    *   `EmergencyDispatchedIntegrationEvent(alertId, careRecipientProfileId, sourceType, severity, dispatchedAt)`: Notifica que una alerta confirmada de severidad `CRITICAL` o `HIGH` entró en despacho.
    *   `IncidentClosedIntegrationEvent(incidentId, alertId, careRecipientProfileId, sourceType, notes, closedAt)`: Notifica el cierre de un incidente para su incorporación al historial de salud.
*   `EmergencyAlertingContextFacade`: Interfaz expuesta para consultas sincrónicas de lectura segura entre contextos (`hasActiveAlerts(UUID careRecipientProfileId)`).

#### 2.6.1.3. Application Layer

Orquesta los flujos de casos de uso delegando las reglas de negocio en los agregados y servicios de dominio. Los Event Handlers y Schedulers son la materialización directa de las policies identificadas en el Design-Level EventStorming. Los servicios devuelven `Result<T, ApplicationError>` y obtienen la hora de un `Clock` inyectable.

##### Command Services

*   **AlertCommandService & AlertCommandServiceImpl:** Resuelve `TriggerAlertCommand` (o devuelve la alerta activa de la misma señal), `ConfirmAlertCommand`, `DismissAlertCommand`, `DispatchAlertCommand` (aplica `DispatchStrategyPolicy` y `EscalationPolicy`), `EscalateAlertCommand`, `BroadcastAlertCommand`, `RegisterDeliveryResultCommand`, `AcknowledgeAlertCommand`, `ClaimAlertResponseCommand`, `CompleteAlertResponseCommand` y `ResolveAlertCommand`. Cuando una operación pierde una carrera de concurrencia sobre la misma alerta (p. ej. un reconocimiento mientras se registra el resultado de una entrega o se escala), recarga la alerta y reevalúa la transición sobre el estado actualizado, de modo que deciden las reglas de negocio y no el orden de llegada. Tras guardar, devuelve el estado más reciente, ya que los handlers síncronos pueden haber avanzado la alerta (un SOS queda confirmado y despachado antes de responder).
*   **IncidentCommandService & IncidentCommandServiceImpl:** `OpenIncidentCommand` (valida que la alerta esté reconocida y no tenga ya un incidente), `StabilizeIncidentCommand` y `CloseIncidentCommand`.
*   **AlertSettingsCommandService & AlertSettingsCommandServiceImpl:** `UpdateAlertSettingsCommand`, `ActivateSilentModeCommand` y `DeactivateSilentModeCommand`; la configuración se crea con sus valores por defecto la primera vez que se modifica.
*   **EmergencyContactCommandService & EmergencyContactCommandServiceImpl:** `AddEmergencyContactCommand` (valida la relación de cuidado mediante `ProfileContextAcl` e inserta en la prioridad solicitada), `ReorderEmergencyContactsCommand` y `DeactivateEmergencyContactCommand` (rechaza dejar al Fragile Citizen sin contactos activos). Todas mantienen prioridades consecutivas desde 1.
*   **AlertChannelSettingCommandService & AlertChannelSettingCommandServiceImpl:** `ConfigureAlertChannelCommand`, que rechaza dejar al usuario sin canales habilitados.

##### Query Services

*   **AlertQueryService & AlertQueryServiceImpl:** Resuelve `GetAlertByIdQuery`, `GetActiveAlertsByCareRecipientProfileIdQuery`, `GetAlertHistoryByCareRecipientProfileIdQuery` y `GetPendingAlertsByRecipientUserIdQuery`.
*   **IncidentQueryService & IncidentQueryServiceImpl:** Resuelve `GetIncidentByIdQuery` y `GetIncidentByAlertIdQuery`.
*   **AlertSettingsQueryService & AlertSettingsQueryServiceImpl:** Resuelve `GetAlertSettingsByCareRecipientProfileIdQuery`, devolviendo los valores por defecto si no existe configuración.
*   **EmergencyContactQueryService & EmergencyContactQueryServiceImpl:** Resuelve `GetEmergencyContactsByCareRecipientProfileIdQuery`.
*   **AlertChannelSettingQueryService & AlertChannelSettingQueryServiceImpl:** Resuelve `GetAlertChannelSettingsByUserIdQuery`.

##### Event Handlers

*   `AlertTriggeredEventHandler`: Si la alerta no requiere ventana de confirmación, despacha `ConfirmAlertCommand` de inmediato; en caso de caída, delega la espera en `FallConfirmationTimeoutScheduler`.
*   `AlertConfirmedEventHandler`: Implementa la policy **Dispatch Strategy Selector** despachando `DispatchAlertCommand`.
*   `AlertDispatchedEventHandler`: Envía las entregas de cada nivel mediante `AlertNotificationSender` y publica `EmergencyDispatchedIntegrationEvent` en el primer despacho de una alerta `CRITICAL` o `HIGH`.
*   `AlertAcknowledgedEventHandler`: Implementa la policy **Escalation Stopper**: la alerta reconocida deja de ser candidata al escalamiento y se despacha `OpenIncidentCommand`.
*   `AlertResponseClaimedEventHandler`: Notifica al resto de destinatarios que un integrante del Care Circle ya asumió la respuesta (US25).
*   `IncidentClosedEventHandler`: Despacha `ResolveAlertCommand` y publica `IncidentClosedIntegrationEvent`.
*   `ProlongedInactivityDetectedEventHandler`, `ReminderReissuedEventHandler` y `MedicationRestockSuggestedEventHandler`: Traducen los eventos de integración de `Care Routines & Wellness` en alertas del tipo y severidad correspondientes.
*   Ningún handler propaga errores hacia quien publicó el evento: los fallos se registran y la alerta permanece activa y visible.
*   No se implementa un handler de reintento por fallo de entrega: toda entrega `CRITICAL` ya incluye `SMS` como respaldo, por lo que un reintento la duplicaría. El fallo queda registrado en la entrega (`FAILED`).

##### Outbound Services

*   `NotificationDispatcher`: Puerto de salida para el envío efectivo de las notificaciones, independiente del proveedor.
*   `AlertNotificationSender`: Envía de forma asíncrona (executor dedicado) las entregas pendientes de un nivel, componiendo cada notificación con el canal, la dirección (teléfono o token), si puede ser audible según el modo silencioso y, en alertas `CRITICAL` y `SAFE_ZONE_VIOLATION`, la última ubicación conocida. Registra el resultado de cada entrega con `RegisterDeliveryResultCommand`.

##### Application ACL Implementation

*   `EmergencyAlertingContextFacadeImpl`: Implementa la fachada de acceso público del contexto.
*   `ProfileContextAcl`: Verifica que un `UserId` mantenga una relación de cuidado activa con un `CareRecipientProfileId` y obtiene el nombre del Fragile Citizen para el contenido de la notificación.
*   `MobilityContextAcl`: Consulta la última ubicación conocida del Fragile Citizen para incluirla en el contenido de la notificación; la ubicación no se persiste en este contexto.
*   Mientras Profile y Mobility & Geofencing no estén implementados, ambos puertos se resuelven con implementaciones provisionales en infraestructura (`ProfileContextAclStub`, `MobilityContextAclStub`).

#### 2.6.1.4. Infrastructure Layer

Implementa la persistencia técnica en PostgreSQL, la integración con los proveedores de notificación y los componentes de programación temporal que sostienen las políticas de temporización del contexto.

##### Persistence JPA Entities

*   `AlertPersistenceEntity`: Mapea la tabla `alerts`. Columnas: `id`, `care_recipient_profile_id`, `source_type`, `source_reference_id`, `severity`, `status`, `triggered_at`, `confirmed_at`, `last_dispatched_at`, `acknowledged_at`, `acknowledged_by_user_id`, `resolved_at`, `version`, `created_at`, `updated_at`. `version` aplica bloqueo optimista. Mantiene relaciones `@OneToMany` hacia entregas y respuestas, cargadas junto con la alerta y ordenadas por su posición.
*   `AlertDeliveryPersistenceEntity`: Mapea la tabla `alert_deliveries`. Columnas: `id`, `alert_id`, `dispatch_order`, `recipient_user_id`, `recipient_level`, `channel`, `delivery_status`, `sent_at`, `delivered_at`. `dispatch_order` se escribe una sola vez al insertar.
*   `AlertResponsePersistenceEntity`: Mapea la tabla `alert_responses`. Columnas: `id`, `alert_id`, `claim_order`, `responder_user_id`, `response_status`, `claimed_at`, `completed_at`, `notes`.
*   `IncidentPersistenceEntity`: Mapea la tabla `incidents`. Columnas: `id`, `alert_id` (única), `status`, `marked_in_attention_at`, `stabilized_at`, `closed_at`, `notes`, `created_at`, `updated_at`.
*   `AlertSettingsPersistenceEntity`: Mapea la tabla `alert_settings`. Columnas: `id`, `care_recipient_profile_id` (única), `primary_ack_timeout_sec`, `escalation_enabled`, `silent_mode_enabled`, `broadcast_critical_immediately`, `created_at`, `updated_at`.
*   `EmergencyContactPersistenceEntity`: Mapea la tabla `emergency_contacts`. Columnas: `id`, `care_recipient_profile_id`, `user_id`, `display_name`, `relationship`, `phone_number`, `priority_order`, `active`, `created_at`, `updated_at`. Restricción única sobre (`care_recipient_profile_id`, `user_id`).
*   `AlertChannelSettingPersistenceEntity`: Mapea la tabla `alert_channel_settings`. Columnas: `id`, `user_id`, `channel`, `enabled`, `device_token`, `created_at`, `updated_at`. Restricción única sobre (`user_id`, `channel`).
*   `AlertSourceEmbeddable`: Agrupa `source_type` y `source_reference_id` dentro de `AlertPersistenceEntity`.
*   *Converters:* `CareRecipientProfileIdPersistenceConverter` y `UserIdPersistenceConverter` traducen los identificadores de referencia hacia columnas `UUID`; los enums de dominio se almacenan como texto (`@Enumerated(EnumType.STRING)`), siguiendo la convención de la plataforma.

##### Spring Data Repositories & Adapters

*   `AlertPersistenceRepository` (con `JpaSpecificationExecutor` para combinar los filtros opcionales del historial), `IncidentPersistenceRepository`, `AlertSettingsPersistenceRepository`, `EmergencyContactPersistenceRepository` y `AlertChannelSettingPersistenceRepository`: Extienden `JpaRepository<..., UUID>`.
*   `AlertRepositoryImpl`, `IncidentRepositoryImpl`, `AlertSettingsRepositoryImpl`, `EmergencyContactRepositoryImpl` y `AlertChannelSettingRepositoryImpl`: Implementan las interfaces de dominio usando los assemblers de persistencia y publican los eventos de dominio una vez persistido el agregado.

##### Persistence Assemblers

*   `AlertPersistenceAssembler`: Traduce `AlertPersistenceEntity` y sus entregas y respuestas hacia los Value Objects (`AlertSource`, `Severity`, `AlertStatus`, `RecipientLevel`) y recompone el agregado `Alert`, conservando su versión y el orden de sus entregas.
*   `IncidentPersistenceAssembler`, `AlertSettingsPersistenceAssembler`, `EmergencyContactPersistenceAssembler` y `AlertChannelSettingPersistenceAssembler`: Traducen entre sus respectivas entidades JPA y agregados de dominio.

##### Notification Adapters

*   `RoutingNotificationDispatcher`: Implementa `NotificationDispatcher` delegando cada notificación en el adaptador de su canal (`ChannelNotificationAdapter`).
*   `InAppNotificationAdapter`: Marca como enviadas las entregas del canal `IN_APP`, que la app móvil recupera mediante la consulta de alertas pendientes.
*   `PushNotificationProviderAdapter`: Canal `PUSH`. Simulado hasta integrar Firebase Cloud Messaging; falla, igual que el proveedor real, si el usuario no registró un token.
*   `SmsProviderAdapter`: Canal `SMS`, respaldo obligatorio en severidad `CRITICAL` y en el nivel `BROADCAST`. Simulado hasta integrar un proveedor SMS; falla si el contacto no tiene teléfono.

##### Configuration

*   `EmergencyAlertingConfiguration`: Expone el `Clock` del contexto y el executor dedicado al envío de notificaciones (`emergency-alerting.notifications.executor.pool-size`).

##### Scheduling

*   `FallConfirmationTimeoutScheduler`: Cada segundo recupera las alertas en `PENDING_CONFIRMATION` cuya `FallConfirmationWindow` venció y despacha `ConfirmAlertCommand`, de modo que una caída confirmada llega al contacto primario dentro del presupuesto de 5 s de US08.
*   `AckTimeoutEscalationScheduler`: Cada cinco segundos recupera las alertas en `TRIGGERED` o `ESCALATED` cuyo `primaryAckTimeout` venció desde el último despacho y aplica `EscalationPolicy.resolveNextLevel`: despacha `EscalateAlertCommand` hacia el nivel `SECONDARY` o `BroadcastAlertCommand` como último recurso (**Critical Broadcast Fallback**).

#### 2.6.1.5. Bounded Context Software Architecture Component Level Diagrams

La Figura 2.45 presenta los componentes del Bounded Context **Emergency & Alerting** organizados por capa: los controladores REST, el consumidor de eventos de integración y el webhook de entrega en la Interface Layer; los servicios, event handlers y schedulers en la Application Layer; los agregados y servicios de dominio en la Domain Layer; y los adaptadores de persistencia y notificación en la Infrastructure Layer.

<a id="figura-2-45"></a>**Figura 2.45.** Diagrama de componentes del Bounded Context Emergency & Alerting

![Emergency & Alerting Component Diagram](../assets/images/chapterII/c4-diagrams/EmergencyAlerting_Layers_Component.png)

#### 2.6.1.6. Bounded Context Software Architecture Code Level Diagrams

En esta sección se presenta la estructura interna del Bounded Context **Emergency & Alerting** a nivel de código, mediante el diagrama de clases de su Domain Layer y el diseño de su base de datos.

##### 2.6.1.6.1. Bounded Context Domain Layer Class Diagrams

El diagrama UML de la Figura 2.46 presenta la Domain Layer de **Emergency & Alerting**, organizada alrededor de los agregados `Alert`, `Incident`, `AlertSettings`, `EmergencyContact` y `AlertChannelSetting`, junto con sus entidades, Value Objects, servicios de dominio y repositorios.

<a id="figura-2-46"></a>**Figura 2.46.** Diagrama de clases de la Domain Layer de Emergency & Alerting

![Emergency & Alerting Domain Class Diagram](../assets/images/chapterII/classDiagrams/EmergencyAlertingDomainClassDiagram.png)

##### 2.6.1.6.2. Bounded Context Database Design Diagram

La Figura 2.47 presenta el diseño de persistencia de **Emergency & Alerting**. La tabla `alerts` concentra el ciclo de vida de cada alerta y se relaciona con `alert_deliveries`, `alert_responses` e `incidents`, mientras que `alert_settings`, `emergency_contacts` y `alert_channel_settings` guardan la configuración del Care Circle. Las tablas `user_accounts` y `care_recipient_profiles` se muestran como referencias externas.

<a id="figura-2-47"></a>**Figura 2.47.** Diagrama de base de datos de Emergency & Alerting

![Emergency & Alerting Database Design Diagram](../assets/images/chapterII/databaseDiagrams/emergency-alerting-db-diagram.png)


### 2.6.2. Bounded Context: Health Monitoring

El Bounded Context **Health Monitoring** pertenece al Core Domain de Guardian+. Su responsabilidad consiste en administrar los dispositivos wearables (`WearableDevice`) asignados a un Care Recipient, capturar cada signo vital (`VitalSign`) contra un catálogo de tipos soportados (`VitalSignType`: frecuencia cardíaca, presión arterial, saturación de oxígeno, temperatura y frecuencia respiratoria), evaluarlo frente a un umbral clínico configurable por paciente y tipo (`VitalSignThreshold`) y compilar Health Reports periódicos.

Este contexto recibe la telemetría del wearable por MQTT y la traduce al lenguaje del dominio mediante una Anti-Corruption Layer, de modo que el formato del firmware no afecte al modelo clínico. Cuando un signo vital supera su umbral, publica el evento de integración `VitalSignAnomalyDetected`, que Emergency & Alerting consume para generar la alerta correspondiente. Health Monitoring no despacha alertas ni gestiona su escalamiento.

La arquitectura táctica se implementa sobre Java y Spring Boot con una estructura de paquetes dividida en cuatro capas: domain, interfaces, application e infrastructure. Su código se organiza en el paquete `com.healthify.guardian.platform.healthmonitoring` del repositorio `guardian-plus-platform`, con la siguiente estructura:

```
com.healthify.guardian.platform.healthmonitoring/
├── domain/
│   ├── model/
│   │   ├── aggregates/
│   │   ├── commands/
│   │   ├── entities/
│   │   ├── events/
│   │   ├── queries/
│   │   └── valueobjects/
│   └── repositories/
├── interfaces/
│   ├── acl/
│   ├── events/
│   └── rest/
│       ├── resources/
│       └── transform/
├── application/
│   ├── acl/
│   ├── commandservices/
│   ├── internal/
│   │   ├── commandservices/
│   │   ├── eventhandlers/
│   │   └── queryservices/
│   └── queryservices/
└── infrastructure/
    ├── messaging/
    │   └── mqtt/
    ├── persistence/
    │   └── jpa/
    │       ├── adapters/
    │       ├── assemblers/
    │       ├── converters/
    │       ├── entities/
    │       └── repositories/
    └── scheduling/
```

#### 2.6.2.1. Domain Layer

Encapsula la lógica pura del dominio médico, las invariantes fisiológicas y las reglas de evaluación clínica embebidas en los propios agregados y Value Objects. Se distinguen cinco agregados en lugar de dos: el Design-Level EventStorming separa explícitamente tres comandos sobre el mismo sticky de agregado (`Detect Vital Signs`, `Emit Vital Signs`, `Evaluate Vital Signs Thresholds`, todos etiquetados **VitalSign**), y el Database Design Diagram revela tres tablas propias del contexto (`wearable_devices`, `vital_sign_types`, `vital_sign_thresholds`) sin ningún agregado equivalente en el modelo original.

##### Aggregates

*   **VitalSign**
    *   Agregado raíz que representa la captura de un único tipo de signo vital de un Care Recipient en un instante dado (una fila = una métrica, no un conjunto fijo de cinco).
    *   Hereda de `AbstractDomainAggregateRoot<VitalSign>` para registrar y publicar eventos de dominio.
    *   *Atributos:*
        *   `id: VitalSignId`
        *   `wearableDeviceId: WearableDeviceId`
        *   `careRecipientProfileId: CareRecipientProfileId`
        *   `vitalSignTypeId: VitalSignTypeId`
        *   `value: VitalSignValue`
        *   `measuredAt: Instant`
        *   `receivedAt: Instant`
        *   `emittedAt: Instant`
    *   *Métodos:*
        *   `VitalSign(DetectVitalSignsCommand command)`
        *   `emit(): void`
        *   `evaluateThresholds(VitalSignThreshold threshold): boolean`
        *   `isEmitted(): boolean`

*   **VitalSignThreshold**
    *   Agregado raíz que configura, por Care Recipient y tipo de signo vital, el rango clínico válido y la cantidad de lecturas consecutivas requeridas para confirmar una anomalía. Reemplaza los invariantes fijos que antes vivían embebidos en Value Objects específicos (p. ej. "20-300 BPM" hardcodeado) por un umbral configurable por paciente.
    *   *Atributos:*
        *   `id: VitalSignThresholdId`
        *   `careRecipientProfileId: CareRecipientProfileId`
        *   `vitalSignTypeId: VitalSignTypeId`
        *   `minimumValue: BigDecimal`
        *   `maximumValue: BigDecimal`
        *   `requiredConsecutiveHits: Integer`
        *   `active: Boolean`
        *   `createdAt: Instant`
        *   `updatedAt: Instant`
    *   *Métodos:*
        *   `VitalSignThreshold(DefineVitalSignThresholdCommand command)`
        *   `isExceededBy(VitalSignValue value): boolean`
        *   `activate(): void`
        *   `deactivate(): void`

*   **WearableDevice**
    *   Agregado raíz que registra el dispositivo físico asignado a un Care Recipient y gobierna su ciclo de vida de asignación.
    *   *Atributos:*
        *   `id: WearableDeviceId`
        *   `careRecipientProfileId: CareRecipientProfileId`
        *   `serialNumber: SerialNumber`
        *   `deviceType: DeviceType`
        *   `status: DeviceStatus`
        *   `assignedAt: Instant`
        *   `createdAt: Instant`
        *   `updatedAt: Instant`
    *   *Métodos:*
        *   `WearableDevice(AssignWearableDeviceCommand command)`
        *   `deactivate(): void`

*   **VitalSignType**
    *   Agregado raíz que actúa como catálogo de los tipos de signo vital soportados por la plataforma (frecuencia cardíaca, presión sistólica/diastólica, saturación de oxígeno, temperatura, frecuencia respiratoria), cada uno con su código único y unidad de medida.
    *   *Atributos:*
        *   `id: VitalSignTypeId`
        *   `code: VitalSignTypeCode`
        *   `name: String`
        *   `unit: String`
    *   *Métodos:*
        *   `VitalSignType(RegisterVitalSignTypeCommand command)`

*   **HealthReport**
    *   Agregado raíz que consolida y sintetiza series temporales de `VitalSign` dentro de un rango temporal.
    *   *Atributos:*
        *   `id: HealthReportId`
        *   `careRecipientProfileId: CareRecipientProfileId`
        *   `generatedByUserId: UserId`
        *   `reportType: HealthReportType`
        *   `period: DateRange`
        *   `summaries: List<VitalSignSummary>`
        *   `recurrentAnomaliesCount: Integer`
        *   `generatedAt: Instant`
    *   *Métodos:*
        *   `HealthReport(GenerateHealthReportCommand command, List<VitalSign> vitalSigns)`
        *   `isClinicallyStable(): boolean`

##### Entities

*   **VitalSignSummary**
    *   Entidad interna que compone el reporte médico agregado (`HealthReport`). No tiene columna propia en `health_reports`: se serializa hacia el campo `summary` (TEXT) al persistir, junto con `recurrentAnomaliesCount`.
    *   *Atributos:*
        *   `id: Long`
        *   `metricType: String`
        *   `averageValue: Double`
        *   `minValue: Double`
        *   `maxValue: Double`
        *   `stabilityIndex: String`

##### Value Objects

*   **VitalSignValue:** Encapsula el valor numérico crudo de una lectura (`value: BigDecimal`), sin acoplarse a una unidad o rango fijo; su interpretación clínica depende del `VitalSignType` y del `VitalSignThreshold` vigente.
*   **VitalSignTypeCode:** Código único del catálogo (`value: String`, p. ej. `HR`, `BP_SYS`, `BP_DIA`, `SPO2`, `TEMP`, `RESP_RATE`).
*   **SerialNumber:** Identificador de fábrica único del dispositivo (`value: String`).
*   **DeviceType:** Enum (`SMARTWATCH`, `WRISTBAND`, `PATCH`).
*   **DeviceStatus:** Enum (`ASSIGNED`, `INACTIVE`, `DECOMMISSIONED`).
*   **HealthReportType:** Enum (`ON_DEMAND`, `WEEKLY_AUTOMATIC`).
*   **DateRange:** Intervalo temporal inmutable (`startDate: LocalDate`, `endDate: LocalDate`). Método: `contains(LocalDate date)`.
*   **VitalSignId / VitalSignThresholdId / WearableDeviceId / VitalSignTypeId / HealthReportId:** Identificadores inmutables tipo UUID.
*   **CareRecipientProfileId:** Identificador de referencia inmutable al paciente monitoreado, gobernado por el Bounded Context Profile.
*   **UserId:** Identificador de referencia inmutable al usuario autenticado (IAM) que solicitó un `HealthReport`.

##### Commands & Queries (Domain Model)

*   `DetectVitalSignsCommand(UUID wearableDeviceId, UUID careRecipientProfileId, UUID vitalSignTypeId, BigDecimal value, Instant measuredAt, Instant receivedAt)`
*   `EmitVitalSignsCommand(UUID vitalSignId)`
*   `EvaluateVitalSignsThresholdsCommand(UUID vitalSignId)`
*   `DefineVitalSignThresholdCommand(UUID careRecipientProfileId, UUID vitalSignTypeId, BigDecimal minimumValue, BigDecimal maximumValue, Integer requiredConsecutiveHits)`
*   `AssignWearableDeviceCommand(UUID careRecipientProfileId, String serialNumber, String deviceType)`
*   `RegisterVitalSignTypeCommand(String code, String name, String unit)`
*   `GenerateHealthReportCommand(UUID careRecipientProfileId, UUID generatedByUserId, String reportType, LocalDate periodStart, LocalDate periodEnd)`
*   `CompileWeeklySummaryCommand(UUID careRecipientProfileId)`
*   `GetLiveVitalSignsByCareRecipientProfileIdQuery(CareRecipientProfileId careRecipientProfileId)`
*   `GetVitalSignsByCareRecipientProfileIdAndPeriodQuery(CareRecipientProfileId careRecipientProfileId, DateRange dateRange)`
*   `GetHealthReportByIdQuery(HealthReportId healthReportId)`
*   `GetAllHealthReportsByCareRecipientProfileIdQuery(CareRecipientProfileId careRecipientProfileId)`

##### Domain Events

*   `VitalSignsDetectedEvent`: Emitido tras validar e instanciar la captura de un signo vital (`Detect Vital Signs`).
*   `VitalSignsEmittedEvent`: Emitido al publicar el signo vital para su consumo en vivo (`Emit Vital Signs`), habilitando la vista `Live Vital Signs View`.
*   `VitalSignsThresholdsEvaluatedEvent`: Emitido al concluir la evaluación contra el `VitalSignThreshold` vigente (`Evaluate Vital Signs Thresholds`), portando el estado de desviación (`hasDeviation: boolean`).
*   `HealthReportGeneratedEvent`: Emitido tras la compilación de un reporte longitudinal.
*   `WeeklySummaryCompiledEvent`: Emitido por la tarea programada dominical.

##### Repositories (Domain Interfaces)

*   **VitalSignRepository:**
    *   `save(VitalSign vitalSign): VitalSign`
    *   `saveAll(List<VitalSign> vitalSigns): List<VitalSign>`
    *   `findLatestByCareRecipientProfileIdAndVitalSignTypeId(CareRecipientProfileId careRecipientProfileId, VitalSignTypeId vitalSignTypeId): Optional<VitalSign>`
    *   `findRecentByCareRecipientProfileIdAndVitalSignTypeId(CareRecipientProfileId careRecipientProfileId, VitalSignTypeId vitalSignTypeId, int count): List<VitalSign>`
    *   `findByCareRecipientProfileIdAndPeriod(CareRecipientProfileId careRecipientProfileId, DateRange period): List<VitalSign>`
*   **VitalSignThresholdRepository:**
    *   `save(VitalSignThreshold threshold): VitalSignThreshold`
    *   `findByCareRecipientProfileIdAndVitalSignTypeId(CareRecipientProfileId careRecipientProfileId, VitalSignTypeId vitalSignTypeId): Optional<VitalSignThreshold>`
    *   `findAllActiveByCareRecipientProfileId(CareRecipientProfileId careRecipientProfileId): List<VitalSignThreshold>`
*   **WearableDeviceRepository:**
    *   `save(WearableDevice device): WearableDevice`
    *   `findById(WearableDeviceId id): Optional<WearableDevice>`
    *   `findByCareRecipientProfileId(CareRecipientProfileId careRecipientProfileId): List<WearableDevice>`
    *   `findBySerialNumber(SerialNumber serialNumber): Optional<WearableDevice>`
*   **VitalSignTypeRepository:**
    *   `save(VitalSignType vitalSignType): VitalSignType`
    *   `findById(VitalSignTypeId id): Optional<VitalSignType>`
    *   `findByCode(VitalSignTypeCode code): Optional<VitalSignType>`
*   **HealthReportRepository:**
    *   `save(HealthReport report): HealthReport`
    *   `findById(HealthReportId id): Optional<HealthReport>`
    *   `findByCareRecipientProfileId(CareRecipientProfileId careRecipientProfileId): List<HealthReport>`

#### 2.6.2.2. Interface Layer

Traduce estímulos externos hacia comandos y consultas de aplicación, expone contratos HTTP RESTful y canaliza eventos de integración.

##### REST Controllers

*   **VitalSignsController** (`/api/v1/vital-signs`):
    *   `POST /`: Registra la detección de un signo vital (`DetectVitalSignsCommand`).
    *   `POST /batches`: Ingesta por lotes para sincronización offline.
    *   `POST /{vitalSignId}/emit`: Publica el signo vital detectado para su visualización en vivo.
    *   `GET /live/{careRecipientProfileId}`: Consulta el último estado biométrico emitido por tipo de signo vital.
    *   `GET /history/{careRecipientProfileId}`: Retorna lecturas históricas filtradas por rango temporal.
*   **VitalSignThresholdsController** (`/api/v1/vital-sign-thresholds`):
    *   `GET /care-recipient/{careRecipientProfileId}`: Lista los umbrales activos configurados.
    *   `PUT /`: Define o actualiza un umbral (mínimo, máximo, lecturas consecutivas requeridas).
    *   `POST /{thresholdId}/activate` / `DELETE /{thresholdId}`: Activa o desactiva un umbral.
*   **WearableDevicesController** (`/api/v1/wearable-devices`):
    *   `POST /`: Asigna un nuevo dispositivo a un Care Recipient.
    *   `GET /care-recipient/{careRecipientProfileId}`: Lista los dispositivos asignados.
    *   `DELETE /{deviceId}`: Desactiva un dispositivo.
*   **VitalSignTypesController** (`/api/v1/vital-sign-types`):
    *   `GET /`: Lista el catálogo de tipos de signo vital soportados.
    *   `POST /`: Registra un nuevo tipo (uso administrativo).
*   **HealthReportsController** (`/api/v1/health-reports`):
    *   `POST /`: Dispara la generación bajo demanda de un reporte de salud.
    *   `GET /{reportId}`: Recupera un reporte específico compilado.
    *   `GET /care-recipient/{careRecipientProfileId}`: Lista los reportes emitidos de un Care Recipient.

##### Resources & Assemblers

*   *Resources (DTOs):* `DetectVitalSignsResource`, `VitalSignResource`, `LiveVitalSignsResource`, `DefineVitalSignThresholdResource`, `AssignWearableDeviceResource`, `WearableDeviceResource`, `VitalSignTypeResource`, `GenerateHealthReportResource`, `HealthReportResource`.
*   *Assemblers (Mappers):* `DetectVitalSignsCommandFromResourceAssembler`, `VitalSignResourceFromEntityAssembler`, `LiveVitalSignsResourceFromEntityAssembler`, `DefineVitalSignThresholdCommandFromResourceAssembler`, `WearableDeviceResourceFromEntityAssembler`, `GenerateHealthReportCommandFromResourceAssembler`, `HealthReportResourceFromEntityAssembler`.

##### Integration Events & ACL Facade

*   `VitalSignAnomalyDetectedIntegrationEvent`: Evento publicado hacia el bus de mensajería cuando se confirman `requiredConsecutiveHits` transgresiones consecutivas del umbral vigente, consumido por `Emergency & Alerting`.
*   `HealthReportCompiledIntegrationEvent`: Notifica a contextos de soporte la disponibilidad de un nuevo reporte estructurado.
*   `HealthMonitoringContextFacade`: Interfaz expuesta para consultas sincrónicas de lectura segura entre contextos.

#### 2.6.2.3. Application Layer

Orquesta los flujos de casos de uso delegando las reglas clínicas en los agregados correspondientes. Los Event Handlers materializan el encadenamiento Detect → Emit → Evaluate distinguido en el Design-Level EventStorming.

##### Command Services

*   **VitalSignCommandService & VitalSignCommandServiceImpl:**
    *   `handle(DetectVitalSignsCommand command): Optional<VitalSign>`: Construye y persiste `VitalSign`.
    *   `handle(EmitVitalSignsCommand command): void`: Marca el signo vital como emitido, habilitando su lectura en vivo.
    *   `handle(EvaluateVitalSignsThresholdsCommand command): void`: Recupera el `VitalSignThreshold` activo para el Care Recipient y tipo correspondientes, y evalúa el signo vital contra él.
*   **VitalSignThresholdCommandService & VitalSignThresholdCommandServiceImpl:**
    *   `handle(DefineVitalSignThresholdCommand command): Optional<VitalSignThreshold>`
*   **WearableDeviceCommandService & WearableDeviceCommandServiceImpl:**
    *   `handle(AssignWearableDeviceCommand command): Optional<WearableDevice>`
*   **VitalSignTypeCommandService & VitalSignTypeCommandServiceImpl:**
    *   `handle(RegisterVitalSignTypeCommand command): Optional<VitalSignType>`
*   **HealthReportCommandService & HealthReportCommandServiceImpl:**
    *   `handle(GenerateHealthReportCommand command): Optional<HealthReport>`: Extrae los `VitalSign` del período y construye y persiste el aggregate `HealthReport`.
    *   `handle(CompileWeeklySummaryCommand command): void`: Orquesta la síntesis semanal programada.

##### Query Services

*   **VitalSignQueryService & VitalSignQueryServiceImpl:** Resuelve `GetLiveVitalSignsByCareRecipientProfileIdQuery` y `GetVitalSignsByCareRecipientProfileIdAndPeriodQuery`.
*   **HealthReportQueryService & HealthReportQueryServiceImpl:** Resuelve `GetHealthReportByIdQuery` y `GetAllHealthReportsByCareRecipientProfileIdQuery`.

##### Event Handlers

*   `VitalSignsDetectedEventHandler`: Reacciona a `VitalSignsDetectedEvent` y despacha `EmitVitalSignsCommand`.
*   `VitalSignsEmittedEventHandler`: Reacciona a `VitalSignsEmittedEvent` y despacha `EvaluateVitalSignsThresholdsCommand`.
*   `VitalSignsThresholdsEvaluatedEventHandler`: Implementa la policy **Regla de Tolerancia**. Si hubo desviación, consulta las `requiredConsecutiveHits - 1` lecturas inmediatamente anteriores del mismo Care Recipient y tipo en `VitalSignRepository`; si todas violan el umbral, despacha `VitalSignAnomalyDetectedIntegrationEvent`.
*   `WeeklySummaryCompiledEventHandler`: Gestiona la indexación y caché de los resúmenes médicos compilados.

##### Application ACL Implementation

*   `HealthMonitoringContextFacadeImpl`: Implementa la fachada de acceso público del contexto.

#### 2.6.2.4. Infrastructure Layer

Implementa la persistencia técnica en PostgreSQL, la comunicación con el broker MQTT y los componentes de programación temporal.

##### Persistence JPA Entities

*   `VitalSignPersistenceEntity`: Mapea la tabla `vital_sign_readings`. Columnas: `id`, `wearable_device_id`, `care_recipient_profile_id`, `vital_sign_type_id`, `value`, `measured_at`, `received_at`.
*   `VitalSignThresholdPersistenceEntity`: Mapea la tabla `vital_sign_thresholds`. Columnas: `id`, `care_recipient_profile_id`, `vital_sign_type_id`, `minimum_value`, `maximum_value`, `required_consecutive_hits`, `active`, `created_at`, `updated_at`.
*   `WearableDevicePersistenceEntity`: Mapea la tabla `wearable_devices`. Columnas: `id`, `care_recipient_profile_id`, `serial_number`, `device_type`, `status`, `assigned_at`, `created_at`, `updated_at`.
*   `VitalSignTypePersistenceEntity`: Mapea la tabla `vital_sign_types`. Columnas: `id`, `code`, `name`, `unit`.
*   `HealthReportPersistenceEntity`: Mapea la tabla `health_reports`. Columnas: `id`, `care_recipient_profile_id`, `generated_by_user_id`, `report_type`, `period_start`, `period_end`, `summary`, `generated_at`. El campo `summary` (TEXT) persiste la serialización de `summaries` y `recurrentAnomaliesCount`; no existe una tabla `report_summaries` separada.

##### Spring Data Repositories & Adapters

*   `VitalSignPersistenceRepository`, `VitalSignThresholdPersistenceRepository`, `WearableDevicePersistenceRepository`, `VitalSignTypePersistenceRepository` y `HealthReportPersistenceRepository`: Extienden `JpaRepository<..., UUID>`.
*   `VitalSignRepositoryImpl`, `VitalSignThresholdRepositoryImpl`, `WearableDeviceRepositoryImpl`, `VitalSignTypeRepositoryImpl` y `HealthReportRepositoryImpl`: Implementan las interfaces de dominio usando los assemblers de persistencia para traducir bidireccionalmente entre entidades JPA y agregados.

##### Persistence Assemblers

*   `VitalSignPersistenceAssembler`: Traduce los tipos primitivos de `VitalSignPersistenceEntity` hacia los Value Objects (`VitalSignValue`, `WearableDeviceId`, `VitalSignTypeId`) y recompone el agregado `VitalSign`.
*   `VitalSignThresholdPersistenceAssembler`, `WearableDevicePersistenceAssembler`, `VitalSignTypePersistenceAssembler` y `HealthReportPersistenceAssembler`: Traducen entre sus respectivas entidades JPA y agregados de dominio; `HealthReportPersistenceAssembler` serializa/deserializa `summaries` y `recurrentAnomaliesCount` hacia y desde el campo `summary`.

##### Scheduling

*   `WeeklyHealthSummaryScheduler`: Tarea periódica anotada con `@Scheduled(cron = "0 0 0 * * SUN")` que invoca `CompileWeeklySummaryCommand` para los pacientes activos.

#### 2.6.2.5. Bounded Context Software Architecture Component Level Diagrams

La Figura 2.48 presenta las cuatro capas del Bounded Context **Health Monitoring**, su comunicación con la aplicación móvil y con el broker MQTT que entrega la telemetría del wearable, y la publicación de eventos de integración hacia Emergency & Alerting.

<a id="figura-2-48"></a>**Figura 2.48.** Diagrama de componentes del Bounded Context Health Monitoring

![Health Monitoring Component Diagram](../assets/images/chapterII/c4-diagrams/HealthMonitoring_Layers_Component.png)

#### 2.6.2.6. Bounded Context Software Architecture Code Level Diagrams

En esta sección se presenta la estructura interna del Bounded Context **Health Monitoring** a nivel de código, mediante el diagrama de clases de su Domain Layer y el diseño de su base de datos.

##### 2.6.2.6.1. Bounded Context Domain Layer Class Diagrams

El diagrama UML de la Figura 2.49 presenta la Domain Layer de **Health Monitoring**, con los agregados `VitalSignType`, `VitalSignThreshold`, `VitalSign`, `WearableDevice` y `HealthReport`, sus Value Objects y las interfaces de repositorio que los gestionan.

<a id="figura-2-49"></a>**Figura 2.49.** Diagrama de clases de la Domain Layer de Health Monitoring

![Health Monitoring Domain Class Diagram](../assets/images/chapterII/classDiagrams/health-monitoring-classDiagram.png)


##### 2.6.2.6.2. Bounded Context Database Design Diagram

La Figura 2.50 presenta el diseño de persistencia de **Health Monitoring**: `wearable_devices` registra los dispositivos asignados a cada persona bajo cuidado, `vital_sign_types` y `vital_sign_thresholds` definen el catálogo de signos vitales y sus umbrales, `vital_sign_readings` almacena cada lectura recibida y `health_reports` guarda los reportes generados.

<a id="figura-2-50"></a>**Figura 2.50.** Diagrama de base de datos de Health Monitoring

![Health Monitoring Database Design Diagram](../assets/images/chapterII/databaseDiagrams/health-monitoring-new-db.png)

### 2.6.3. Bounded Context: Subscriptions

El Bounded Context **Subscriptions** pertenece al Generic Domain de Guardian+. Su responsabilidad consiste en gestionar el ciclo de vida comercial de las suscripciones de la plataforma: la solicitud y activación de una suscripción, los cambios de plan, la renovación, la cancelación, la expiración y la determinación de los beneficios (entitlements) asociados al plan vigente.

Este contexto mantiene aisladas las reglas comerciales de Guardian+ respecto de la identidad, los perfiles, el monitoreo de salud y la gestión de emergencias. La integración con Stripe se realiza mediante adaptadores que traducen sus notificaciones de pago a las transiciones de estado del agregado `Subscription`, y la evaluación periódica de renovaciones y expiraciones se delega a un mecanismo de programación temporal, de modo que ninguna de estas dependencias forme parte del modelo de dominio.

La arquitectura táctica se diseñó sobre Java y Spring Boot con la misma estructura de paquetes de cuatro capas que el resto de Bounded Contexts: domain, interfaces, application e infrastructure. Su código se organizará en el paquete `com.healthify.guardian.platform.subscriptions` del repositorio `guardian-plus-platform`, con la siguiente estructura:

```
com.healthify.guardian.platform.subscriptions/
├── domain/
│   ├── model/
│   │   ├── aggregates/
│   │   ├── commands/
│   │   ├── entities/
│   │   ├── events/
│   │   ├── queries/
│   │   └── valueobjects/
│   ├── repositories/
│   └── services/
├── interfaces/
│   ├── events/
│   └── rest/
│       ├── resources/
│       └── transform/
├── application/
│   ├── commandservices/
│   ├── internal/
│   │   ├── commandservices/
│   │   ├── eventhandlers/
│   │   └── queryservices/
│   └── queryservices/
└── infrastructure/
    ├── payments/
    │   └── adapters/
    ├── persistence/
    │   └── jpa/
    │       ├── adapters/
    │       ├── assemblers/
    │       ├── entities/
    │       └── repositories/
    └── scheduling/
```

#### 2.6.3.1. Domain Layer

La Domain Layer concentra las reglas de negocio relacionadas con el ciclo de vida de las suscripciones, la definición de planes comerciales, el procesamiento de pagos y la determinación de los entitlements habilitados para cada suscripción. Esta capa se mantiene independiente de proveedores de pago, tecnologías de persistencia y mecanismos externos de programación.

##### Aggregates

**`Subscription`**

Representa una suscripción de Guardian+ y constituye el Aggregate Root principal del ciclo de vida comercial. Controla su activación, renovación, cambio de plan, cancelación y expiración.

**Atributos principales:**

- `id: SubscriptionId`
- `subscriberUserId: UserId`
- `planId: PlanId`
- `status: SubscriptionStatus`
- `currentPeriod: Period`
- `cancelAtPeriodEnd: Boolean`
- `cancelledAt: Instant`
- `createdAt: Instant`
- `updatedAt: Instant`

**Métodos principales:**

- `activate(): void`
- `renew(period: Period): void`
- `changePlan(planId: PlanId): void`
- `requestCancellation(): void`
- `cancel(): void`
- `expire(): void`
- `isActive(): Boolean`

**Relaciones principales:**

- Una `Subscription` se encuentra asociada a un `Plan`.
- Una `Subscription` puede registrar múltiples `PaymentAttempt`.
- Una `Subscription` puede disponer de un `EntitlementSet` con los beneficios efectivos habilitados.

**`Plan`**

Representa una alternativa comercial disponible en Guardian+. Mantiene la configuración utilizada para determinar el precio, ciclo de facturación y beneficios asociados a una suscripción.

**Atributos principales:**

- `id: PlanId`
- `name: String`
- `description: String`
- `price: Money`
- `billingCycle: BillingCycle`
- `active: Boolean`
- `createdAt: Instant`
- `updatedAt: Instant`

**Métodos principales:**

- `activate(): void`
- `deactivate(): void`
- `changePrice(price: Money): void`

**Relaciones principales:**

- Un `Plan` puede estar asociado a múltiples suscripciones.
- Un `Plan` puede habilitar múltiples `Entitlement`.
- Un mismo `Entitlement` puede formar parte de distintos planes.

**`EntitlementSet`**

Representa el conjunto efectivo de beneficios habilitados para una suscripción. Permite mantener sincronizados los entitlements que corresponden según el plan contratado y el estado vigente de la suscripción. Cada beneficio efectivo se representa mediante un `SubscriptionEntitlement`, que conserva su estado y su periodo de vigencia en lugar de una simple pertenencia al conjunto.

**Atributos principales:**

- `subscriptionId: SubscriptionId`
- `items: List<SubscriptionEntitlement>`
- `updatedAt: Instant`

**Métodos principales:**

- `replaceWith(entitlementIds: Set<EntitlementId>, effectiveFrom: Instant): void`
- `revoke(entitlementId: EntitlementId, effectiveTo: Instant): void`
- `revokeAll(effectiveTo: Instant): void`
- `contains(entitlementId: EntitlementId): Boolean`
- `activeItems(): List<SubscriptionEntitlement>`

**Relaciones principales:**

- Un `EntitlementSet` pertenece a una suscripción.
- Un `EntitlementSet` puede contener múltiples `SubscriptionEntitlement`.
- Cada `SubscriptionEntitlement` referencia por identidad a un `Entitlement` del catálogo.

**`Entitlement`**

Representa un beneficio o capacidad comercial del catálogo de Guardian+, que puede estar habilitado por uno o más planes de suscripción. Constituye un Aggregate Root propio porque es un catálogo compartido entre planes y suscripciones, con identidad y ciclo de vida independientes de ambos.

**Atributos principales:**

- `id: EntitlementId`
- `code: String`
- `name: String`
- `description: String`

**Métodos principales:**

- `matches(code: String): Boolean`

**Relaciones principales:**

- Un `Entitlement` puede formar parte de múltiples `Plan`, mediante la relación `plan_entitlements`.
- Un `Entitlement` puede encontrarse habilitado dentro de distintos `EntitlementSet`, mediante `SubscriptionEntitlement`.

##### Entities

**`PaymentAttempt`**

Representa un intento de pago asociado a una suscripción, ya sea para su activación inicial o para una renovación.

**Atributos principales:**

- `id: UUID`
- `subscriptionId: SubscriptionId`
- `paymentType: PaymentType`
- `amount: Money`
- `provider: String`
- `status: PaymentStatus`
- `providerReference: String`
- `createdAt: Instant`
- `paidAt: Instant`

**Métodos principales:**

- `markConfirmed(reference: String): void`
- `markFailed(): void`
- `isSuccessful(): Boolean`

**Relaciones principales:**

- Cada `PaymentAttempt` se encuentra asociado a una `Subscription`.

**`SubscriptionEntitlement`**

Representa un beneficio efectivo habilitado para una suscripción durante un periodo determinado. Es la entidad interna de `EntitlementSet` y conserva el estado y la vigencia que no pueden expresarse mediante la simple pertenencia a un conjunto.

**Atributos principales:**

- `id: UUID`
- `entitlementId: EntitlementId`
- `status: SubscriptionEntitlementStatus`
- `effectivePeriod: Period`

**Métodos principales:**

- `revoke(effectiveTo: Instant): void`
- `isEffectiveAt(date: Instant): Boolean`

**Relaciones principales:**

- Cada `SubscriptionEntitlement` pertenece a un `EntitlementSet`.
- Cada `SubscriptionEntitlement` referencia un `Entitlement` del catálogo mediante `EntitlementId`.

##### Value Objects

**`SubscriptionId`**

Identificador inmutable utilizado para distinguir una suscripción.

**Atributos:**

- `value: UUID`

**`PlanId`**

Identificador inmutable utilizado para distinguir un plan comercial.

**Atributos:**

- `value: UUID`

**`UserId`**

Identificador externo utilizado para referenciar al usuario propietario de una suscripción sin incorporar el modelo interno del Bounded Context IAM.

**Atributos:**

- `value: UUID`

**`EntitlementId`**

Identificador inmutable utilizado para distinguir un entitlement.

**Atributos:**

- `value: UUID`

**`Money`**

Representa un monto monetario junto con su moneda.

**Atributos:**

- `amount: Decimal`
- `currency: String`

**Métodos principales:**

- `isPositive(): Boolean`

**`Period`**

Representa el intervalo temporal vigente de una suscripción.

**Atributos:**

- `start: Instant`
- `end: Instant`

**Métodos principales:**

- `contains(date: Instant): Boolean`
- `durationInDays(): Long`

##### Enumerations

**`SubscriptionStatus`**

Representa el estado vigente de una suscripción.

- `PENDING`
- `ACTIVE`
- `CANCELLED`
- `EXPIRED`

**`PaymentStatus`**

Representa el resultado o estado de un intento de pago.

- `PENDING`
- `CONFIRMED`
- `FAILED`

**`PaymentType`**

Permite distinguir el propósito de una operación de pago.

- `INITIAL`
- `RENEWAL`

**`BillingCycle`**

Representa la periodicidad comercial configurada para un plan.

- `MONTHLY`
- `YEARLY`

**`SubscriptionEntitlementStatus`**

Representa el estado de un beneficio efectivo dentro de una suscripción.

- `ACTIVE`
- `REVOKED`

##### Domain Policies

**`SubscriptionActivationPolicy`**

Evalúa las condiciones necesarias para iniciar y activar una suscripción de acuerdo con el plan seleccionado.

**Operaciones principales:**

- `requiresPayment(plan: Plan): Boolean`
- `canActivate(plan: Plan): Boolean`

**`SubscriptionLifecyclePolicy`**

Agrupa las reglas de negocio relacionadas con los cambios de plan, cancelación, renovación y expiración de una suscripción.

**Operaciones principales:**

- `canChangePlan(subscription: Subscription, newPlan: Plan): Boolean`
- `determineCancellationEffectiveDate(subscription: Subscription): Instant`
- `canRenew(subscription: Subscription, plan: Plan): Boolean`
- `canExpire(subscription: Subscription): Boolean`

**`EntitlementPolicy`**

Determina los beneficios efectivos que deben mantenerse habilitados como consecuencia de los cambios producidos durante el ciclo de vida de una suscripción.

**Operaciones principales:**

- `afterActivation(subscription: Subscription, plan: Plan): Set<EntitlementId>`
- `afterPlanChange(subscription: Subscription, plan: Plan): Set<EntitlementId>`
- `afterCancellation(subscription: Subscription): Set<EntitlementId>`
- `afterExpiration(subscription: Subscription): Set<EntitlementId>`

##### Commands & Queries (Domain Model)

- `RequestSubscriptionCommand(UUID subscriberUserId, UUID planId)`
- `ActivateSubscriptionCommand(UUID subscriptionId)`
- `InitiateSubscriptionPaymentCommand(UUID subscriptionId)`
- `RequestPlanChangeCommand(UUID subscriptionId, UUID newPlanId)`
- `ApplyPlanChangeCommand(UUID subscriptionId, UUID newPlanId)`
- `RequestSubscriptionCancellationCommand(UUID subscriptionId)`
- `CancelSubscriptionCommand(UUID subscriptionId)`
- `EvaluateSubscriptionRenewalCommand(UUID subscriptionId)`
- `InitiateRenewalPaymentCommand(UUID subscriptionId)`
- `RenewSubscriptionCommand(UUID subscriptionId, Period newPeriod)`
- `EvaluateSubscriptionExpirationCommand(UUID subscriptionId)`
- `ExpireSubscriptionCommand(UUID subscriptionId)`
- `UpdateEntitlementsCommand(UUID subscriptionId)`
- `GetSubscriptionStatusQuery(SubscriptionId subscriptionId)`
- `GetCurrentPlanQuery(SubscriptionId subscriptionId)`
- `GetAvailableEntitlementsQuery(SubscriptionId subscriptionId)`

##### Domain Events

- `SubscriptionActivated`: Emitido cuando una suscripción cumple las condiciones de activación definidas por `SubscriptionActivationPolicy`.
- `SubscriptionPlanChanged`: Emitido al aplicarse efectivamente un cambio de plan sobre una suscripción vigente.
- `SubscriptionCancelled`: Emitido cuando la cancelación se hace efectiva según la fecha determinada por `SubscriptionLifecyclePolicy`.
- `SubscriptionRenewed`: Emitido al establecerse el nuevo periodo de vigencia de una suscripción renovada.
- `SubscriptionExpired`: Emitido cuando una suscripción finaliza su vigencia sin renovación.
- `PaymentConfirmed`: Emitido al confirmarse el pago inicial requerido para la activación.
- `PaymentFailed`: Emitido cuando el pago inicial no pudo completarse, sin activar la suscripción.
- `RenewalPaymentConfirmed`: Emitido al confirmarse el pago de una renovación.
- `RenewalPaymentFailed`: Emitido cuando el pago de renovación falla, sin extender el periodo vigente.
- `EntitlementsUpdated`: Emitido cuando `EntitlementPolicy` determina un nuevo conjunto de beneficios efectivos y el `EntitlementSet` se sincroniza.

##### Repositories (Domain Interfaces)

**`SubscriptionRepository`**

Abstracción utilizada para recuperar y persistir el Aggregate Root `Subscription`.

**Operaciones principales:**

- `findById(id: SubscriptionId): Optional<Subscription>`
- `findActiveBySubscriberUserId(userId: UserId): Optional<Subscription>`
- `save(subscription: Subscription): Subscription`

**`PlanRepository`**

Abstracción utilizada para consultar y persistir los planes comerciales administrados por Subscriptions.

**Operaciones principales:**

- `findById(id: PlanId): Optional<Plan>`
- `findActivePlans(): List<Plan>`

**`EntitlementRepository`**

Abstracción utilizada para consultar el catálogo de beneficios comerciales de Guardian+.

**Operaciones principales:**

- `findById(id: EntitlementId): Optional<Entitlement>`
- `findByCode(code: String): Optional<Entitlement>`
- `findAll(): List<Entitlement>`
- `findByPlanId(planId: PlanId): List<Entitlement>`

**`EntitlementSetRepository`**

Abstracción utilizada para recuperar y persistir los beneficios efectivos asociados a una suscripción.

**Operaciones principales:**

- `findBySubscriptionId(subscriptionId: SubscriptionId): Optional<EntitlementSet>`
- `save(entitlementSet: EntitlementSet): EntitlementSet`

El modelo de persistencia no replica de manera uno a uno todos los objetos del dominio. Los Value Objects se almacenan como parte de las entidades correspondientes, mientras que las asociaciones entre planes y entitlements y los beneficios efectivos de una suscripción se representan mediante las relaciones definidas en el modelo de base de datos.

#### 2.6.3.2. Interface Layer

La Interface Layer expone las capacidades del Bounded Context **Subscriptions** hacia los clientes de Guardian+ y recibe mensajes provenientes de integraciones externas. Su responsabilidad es transformar solicitudes HTTP, notificaciones externas y señales temporales en comandos o consultas que serán procesados por la Application Layer, sin incorporar reglas de negocio ni acceder directamente a la persistencia.

##### REST Controllers

**`SubscriptionController`**

Expone las operaciones relacionadas con el ciclo de vida y consulta de las suscripciones.

**Operaciones principales:**

- `requestSubscription()`
- `requestPlanChange()`
- `requestCancellation()`
- `getSubscriptionStatus()`
- `getAvailableEntitlements()`

**Relaciones principales:**

- recibe solicitudes de los clientes de Guardian+;
- delega comandos y consultas a los handlers correspondientes de la Application Layer;
- no accede directamente a los repositories ni a la base de datos.

**`PaymentWebhookController`**

Recibe las notificaciones enviadas por el proveedor externo de pagos y las transforma en acciones de aplicación relacionadas con la confirmación o fallo de pagos de activación y renovación.

**Operaciones principales:**

- `handlePaymentConfirmed()`
- `handlePaymentFailed()`

**Relaciones principales:**

- recibe notificaciones del Payment Provider;
- delega el procesamiento de los resultados de pago a la Application Layer;
- no modifica directamente el estado de `Subscription` ni de `PaymentAttempt`.

##### Message Consumers

**`BillingSchedulerConsumer`**

Recibe las señales temporales utilizadas para iniciar la evaluación de renovaciones y expiraciones de suscripciones.

**Operaciones principales:**

- `handleRenewalEvaluation()`
- `handleExpirationEvaluation()`

**Relaciones principales:**

- recibe señales generadas por el mecanismo de scheduling;
- delega las evaluaciones correspondientes a la Application Layer;
- no contiene reglas para decidir si una suscripción debe renovarse o expirar.

#### 2.6.3.3. Application Layer

La Application Layer coordina los casos de uso del Bounded Context **Subscriptions** utilizando los Aggregate Roots, Domain Policies y Repository Interfaces definidos en la Domain Layer. Esta capa organiza el flujo de cada operación, pero delega las reglas de negocio al modelo de dominio.

Los handlers no mantienen estado de negocio propio. Sus principales dependencias corresponden a los repositories y políticas necesarias para recuperar los aggregates, ejecutar las reglas del dominio y persistir los cambios resultantes.

##### Command Handlers

La Tabla 2.54 describe los command handlers del contexto y la operación principal de cada uno.

<a id="tabla-2-54"></a>**Tabla 2.54.** Command Handlers de Subscriptions

| Class | Purpose | Main Operation |
|---|---|---|
| `RequestSubscriptionHandler` | Procesa una nueva solicitud de suscripción y determina las condiciones iniciales según el plan seleccionado. | `handle(RequestSubscriptionCommand)` |
| `ActivateSubscriptionHandler` | Activa una suscripción cuando se cumplen las condiciones definidas por el dominio. | `handle(ActivateSubscriptionCommand)` |
| `InitiateSubscriptionPaymentHandler` | Coordina el inicio del pago requerido para activar una suscripción de pago. | `handle(InitiateSubscriptionPaymentCommand)` |
| `RequestPlanChangeHandler` | Recibe la solicitud de cambio de plan y evalúa si el cambio puede realizarse. | `handle(RequestPlanChangeCommand)` |
| `ApplyPlanChangeHandler` | Aplica el nuevo plan sobre una suscripción luego de cumplir las condiciones correspondientes. | `handle(ApplyPlanChangeCommand)` |
| `RequestSubscriptionCancellationHandler` | Procesa una solicitud de cancelación y determina cuándo debe hacerse efectiva. | `handle(RequestSubscriptionCancellationCommand)` |
| `CancelSubscriptionHandler` | Ejecuta la cancelación efectiva de una suscripción. | `handle(CancelSubscriptionCommand)` |
| `EvaluateSubscriptionRenewalHandler` | Evalúa una suscripción próxima al final de su periodo para determinar si corresponde iniciar su renovación. | `handle(EvaluateSubscriptionRenewalCommand)` |
| `InitiateRenewalPaymentHandler` | Coordina el pago requerido para renovar una suscripción de pago. | `handle(InitiateRenewalPaymentCommand)` |
| `RenewSubscriptionHandler` | Renueva una suscripción y establece su nuevo periodo de vigencia. | `handle(RenewSubscriptionCommand)` |
| `EvaluateSubscriptionExpirationHandler` | Evalúa si una suscripción debe finalizar su vigencia. | `handle(EvaluateSubscriptionExpirationCommand)` |
| `ExpireSubscriptionHandler` | Cambia una suscripción al estado expirado cuando se cumplen las condiciones del dominio. | `handle(ExpireSubscriptionCommand)` |
| `UpdateEntitlementsHandler` | Actualiza los beneficios efectivos de una suscripción después de cambios relevantes en su ciclo de vida. | `handle(UpdateEntitlementsCommand)` |

##### Query Handlers

La Tabla 2.55 describe los query handlers del contexto.

<a id="tabla-2-55"></a>**Tabla 2.55.** Query Handlers de Subscriptions

| Class | Purpose | Main Operation |
|---|---|---|
| `GetSubscriptionStatusHandler` | Recupera el estado vigente de una suscripción. | `handle(GetSubscriptionStatusQuery)` |
| `GetCurrentPlanHandler` | Recupera el plan actualmente asociado a una suscripción. | `handle(GetCurrentPlanQuery)` |
| `GetAvailableEntitlementsHandler` | Recupera los entitlements efectivos habilitados para una suscripción. | `handle(GetAvailableEntitlementsQuery)` |

##### Event Handlers

La Tabla 2.56 describe los event handlers del contexto y el evento al que reacciona cada uno.

<a id="tabla-2-56"></a>**Tabla 2.56.** Event Handlers de Subscriptions

| Class | Purpose | Main Operation |
|---|---|---|
| `SubscriptionActivatedHandler` | Reacciona a la activación de una suscripción para sincronizar sus entitlements. | `handle(SubscriptionActivated)` |
| `SubscriptionPlanChangedHandler` | Recalcula los entitlements luego de un cambio de plan. | `handle(SubscriptionPlanChanged)` |
| `SubscriptionCancelledHandler` | Actualiza los beneficios efectivos cuando una suscripción es cancelada. | `handle(SubscriptionCancelled)` |
| `SubscriptionExpiredHandler` | Revoca o actualiza los entitlements cuando una suscripción expira. | `handle(SubscriptionExpired)` |
| `PaymentConfirmedHandler` | Procesa la confirmación del pago inicial y permite continuar con la activación de la suscripción. | `handle(PaymentConfirmed)` |
| `PaymentFailedHandler` | Procesa el fallo del pago inicial sin activar la suscripción. | `handle(PaymentFailed)` |
| `RenewalPaymentConfirmedHandler` | Procesa la confirmación de un pago de renovación y permite continuar con la renovación de la suscripción. | `handle(RenewalPaymentConfirmed)` |
| `RenewalPaymentFailedHandler` | Procesa el fallo de un pago de renovación sin extender el periodo de la suscripción. | `handle(RenewalPaymentFailed)` |


#### 2.6.3.4. Infrastructure Layer

La Infrastructure Layer contiene las implementaciones técnicas necesarias para persistir el estado del Bounded Context **Subscriptions** y comunicarse con servicios externos. Esta capa implementa las abstracciones utilizadas por las capas internas sin incorporar reglas propias del dominio.

##### Persistence JPA Entities

*   `SubscriptionPersistenceEntity`: Mapea la tabla `subscriptions`. Columnas: `id`, `subscriber_user_id`, `plan_id`, `status`, `current_period_start`, `current_period_end`, `cancel_at_period_end`, `cancelled_at`, `created_at`, `updated_at`. Mantiene una relación `@OneToMany` hacia `PaymentPersistenceEntity`.
*   `PaymentPersistenceEntity`: Mapea la tabla `payments`. Columnas: `id`, `subscription_id`, `payment_type`, `amount`, `currency`, `provider`, `provider_reference`, `status`, `paid_at`, `created_at`. Las columnas `amount` y `currency` componen el Value Object `Money`.
*   `SubscriptionPlanPersistenceEntity`: Mapea la tabla `subscription_plans`. Columnas: `id`, `name`, `description`, `price`, `currency`, `billing_cycle`, `active`, `created_at`, `updated_at`.
*   `EntitlementPersistenceEntity`: Mapea la tabla `entitlements`. Columnas: `id`, `code`, `name`, `description`.
*   `PlanEntitlementPersistenceEntity`: Mapea la tabla de relación `plan_entitlements`. Columnas: `id`, `plan_id`, `entitlement_id`. Resuelve la asociación muchos a muchos entre planes y beneficios del catálogo.
*   `SubscriptionEntitlementPersistenceEntity`: Mapea la tabla `subscription_entitlements`. Columnas: `id`, `subscription_id`, `entitlement_id`, `status`, `effective_from`, `effective_to`. Las columnas `effective_from` y `effective_to` componen el Value Object `Period`.
*   *Converters:* `SubscriptionStatusConverter`, `PaymentStatusConverter`, `PaymentTypeConverter`, `BillingCycleConverter` y `SubscriptionEntitlementStatusConverter` traducen los enums de dominio hacia columnas `VARCHAR(30)`.

##### Repository Implementations

**`SubscriptionRepositoryImpl`**

Implementa `SubscriptionRepository` y gestiona la persistencia del Aggregate Root `Subscription`.

**Responsabilidades principales:**

- recuperar una suscripción por su identificador;
- recuperar la suscripción activa asociada a un usuario;
- persistir los cambios de estado, periodo, plan y cancelación de una suscripción;
- persistir los `PaymentAttempt` asociados al ciclo de vida de la suscripción.

**Relaciones principales:**

- implementa `SubscriptionRepository`;
- persiste información mediante las tablas `subscriptions` y `payments`.

**`PlanRepositoryImpl`**

Implementa `PlanRepository` y permite consultar la configuración comercial de los planes disponibles.

**Responsabilidades principales:**

- recuperar un plan mediante su identificador;
- recuperar los planes activos disponibles.

**Relaciones principales:**

- implementa `PlanRepository`;
- utiliza la información almacenada en `subscription_plans` y su asociación con `plan_entitlements`.

**`EntitlementSetRepositoryImpl`**

Implementa `EntitlementSetRepository` y gestiona la persistencia de los beneficios efectivos asociados a cada suscripción.

**Responsabilidades principales:**

- recuperar el `EntitlementSet` asociado a una suscripción, con el estado y la vigencia de cada `SubscriptionEntitlement`;
- persistir los beneficios efectivos habilitados para una suscripción, registrando su revocación sin eliminar el historial.

**Relaciones principales:**

- implementa `EntitlementSetRepository` y `EntitlementRepository`;
- utiliza `entitlements` como catálogo y `subscription_entitlements` para reconstruir y persistir el conjunto efectivo de beneficios.

##### External Service Adapters

**`PaymentProviderAdapter`**

Encapsula la comunicación con el proveedor externo encargado de procesar los pagos requeridos para activaciones y renovaciones.

**Operaciones principales:**

- `initiatePayment()`
- `validatePaymentNotification()`

**Relaciones principales:**

- es utilizado por la Application Layer para iniciar operaciones de pago;
- traduce las respuestas del proveedor externo al modelo utilizado por Guardian+;
- trabaja junto con `PaymentWebhookController` para procesar confirmaciones y fallos de pago.

La selección del proveedor permanece desacoplada del dominio. Stripe se mantiene como candidato de implementación mientras no se haya definido de manera definitiva el proveedor externo.

**`BillingSchedulerAdapter`**

Implementa el mecanismo técnico utilizado para generar las señales temporales necesarias para evaluar renovaciones y expiraciones.

**Operaciones principales:**

- `scheduleRenewalEvaluation()`
- `scheduleExpirationEvaluation()`

**Relaciones principales:**

- genera las señales consumidas por `BillingSchedulerConsumer`;
- no contiene las reglas que determinan si una suscripción debe renovarse o expirar.

##### Event Publishing

**`EventPublisher`**

Publica los eventos producidos por el ciclo de vida de las suscripciones para que puedan ser consumidos por otros Bounded Contexts de Guardian+.

**Operaciones principales:**

- `publish(event)`

**Relaciones principales:**

- recibe desde la Application Layer los eventos que deben comunicarse externamente;
- publica cambios relevantes como activación, cambio de plan, cancelación, expiración y actualización de entitlements;
- no modifica directamente el estado de los aggregates.

#### 2.6.3.5. Bounded Context Software Architecture Component Level Diagrams

La Figura 2.51 presenta la arquitectura a nivel de componentes del Bounded Context **Subscriptions**. La vista descompone el backend de Guardian+ en los componentes responsables de exponer las operaciones de suscripción, orquestar los casos de uso, aplicar las reglas del dominio y resolver las dependencias técnicas relacionadas con persistencia, publicación de eventos e integración con el proveedor de pagos.

La **Interface Layer** se encuentra representada por los controladores REST de suscripciones y el controlador de webhooks de pagos. La **Application Layer** coordina los casos de uso mediante `Subscription Application Service` y `Payment Application Service`. La lógica central del dominio se concentra en los aggregates `Subscription` y `Entitlement Set`, junto con las políticas de suscripción. Finalmente, la **Infrastructure Layer** implementa los adaptadores de repositorio, publicación de eventos e integración con Stripe.

<a id="figura-2-51"></a>**Figura 2.51.** Diagrama de componentes del Bounded Context Subscriptions

![Subscriptions Component Level Diagram](../assets/images/chapterII/Subscriptions/SubscriptionComponents.png)

El componente `Subscriptions REST Controllers` recibe las solicitudes relacionadas con activación, renovación, cambio de plan, cancelación y consulta del estado de la suscripción, delegando su procesamiento a la capa de aplicación.

`Subscription Application Service` coordina las operaciones sobre el ciclo de vida de las suscripciones y utiliza los aggregates y políticas del dominio para mantener las reglas de negocio. Asimismo, utiliza los adaptadores de persistencia y el publicador de eventos para almacenar los cambios producidos y comunicar eventos relevantes hacia otros bounded contexts.

Para las operaciones que requieren pagos, `Payment Application Service` utiliza `Stripe Adapter`, que encapsula la comunicación con el proveedor externo Stripe. Las confirmaciones o fallos de pago regresan hacia Guardian+ mediante el `Payment Webhook Controller`.

#### 2.6.3.6. Bounded Context Software Architecture Code Level Diagrams

En esta sección se presenta la estructura interna del Bounded Context **Subscriptions** a nivel de código. Se incluyen el modelo de clases correspondiente a la Domain Layer y el diseño de persistencia utilizado como referencia para la implementación del contexto.

##### 2.6.3.6.1. Bounded Context Domain Layer Class Diagrams

El diagrama UML de la Figura 2.52 representa los principales elementos que conforman la Domain Layer de **Subscriptions**. El modelo se organiza alrededor del Aggregate Root `Subscription`, encargado de controlar el ciclo de vida de una suscripción, y del Aggregate Root `EntitlementSet`, responsable de administrar los beneficios disponibles de acuerdo con el plan vigente.

<a id="figura-2-52"></a>**Figura 2.52.** Diagrama de clases de la Domain Layer de Subscriptions

![Subscriptions Domain Layer Class Diagram](../assets/images/chapterII/Subscriptions/SubscriptionsCodeLevelDiagram.png)

`Subscription` mantiene las reglas relacionadas con activación, renovación, cambio de plan, cancelación y expiración, y contiene la entidad `PaymentAttempt`, que registra cada intento de pago de su ciclo de vida. `Plan` y `Entitlement` son Aggregate Roots propios: el primero concentra la configuración comercial y el segundo actúa como catálogo de beneficios compartido entre planes y suscripciones.

`EntitlementSet` administra los `SubscriptionEntitlement` habilitados para una suscripción, cada uno con su estado y su periodo de vigencia. El dominio utiliza Value Objects como `SubscriptionId`, `PlanId`, `EntitlementId`, `Money` y `Period` para representar conceptos con semántica propia y evitar el uso de valores primitivos sin significado de negocio.

Los estados principales de las suscripciones, los pagos y los beneficios efectivos se representan mediante las enumeraciones `SubscriptionStatus`, `PaymentStatus` y `SubscriptionEntitlementStatus`, permitiendo controlar explícitamente las transiciones válidas dentro del dominio.

##### 2.6.3.6.2. Bounded Context Database Design Diagram

La Figura 2.53 presenta el diseño de persistencia correspondiente al Bounded Context **Subscriptions**. Las tablas reflejan las entidades y aggregates que requieren almacenamiento persistente en el backend, manteniendo las relaciones necesarias para administrar planes, suscripciones, pagos y entitlements.

<a id="figura-2-53"></a>**Figura 2.53.** Diagrama de base de datos de Subscriptions

![Subscriptions Database Design Diagram](../assets/images/chapterII/Subscriptions/SubscriptionsDatabaseDesigDiagram.png)

La tabla `subscriptions` constituye el elemento central del modelo de persistencia y relaciona al usuario suscriptor con el plan contratado. `subscription_plans` almacena la configuración comercial de los planes disponibles, mientras que `payments` registra las operaciones de pago asociadas al ciclo de vida de cada suscripción.

Los beneficios disponibles se representan mediante `entitlements`. La relación entre planes y beneficios se mantiene mediante `plan_entitlements`, mientras que `subscription_entitlements` permite registrar los beneficios efectivos asociados a una suscripción durante un determinado periodo.

### 2.6.4. Bounded Context: Profile

El Bounded Context **Profile** pertenece al Generic Domain de Guardian+. Su responsabilidad consiste en gestionar la información descriptiva de los usuarios, los perfiles de las personas bajo cuidado, las relaciones de cuidado entre familiares o cuidadores y la persona a su cargo, y las preferencias de idioma, accesibilidad y notificaciones de la aplicación.

Este contexto separa la información personal de la identidad y la autenticación: utiliza `UserId` únicamente como referencia externa al Bounded Context IAM y no almacena contraseñas, tokens ni credenciales. Al establecer o finalizar una relación de cuidado publica los eventos `CareRelationshipEstablished` y `CareRelationshipEnded`, que Emergency & Alerting utiliza para mantener actualizados los contactos de emergencia. La integración directa con IAM queda pendiente hasta que dicho contexto se implemente en el backend.

La arquitectura táctica se implementa sobre Java y Spring Boot con una estructura de paquetes dividida en cuatro capas: domain, interfaces, application e infrastructure. Su código se organiza en el paquete `com.healthify.guardian.platform.profile` del repositorio `guardian-plus-platform`, con la siguiente estructura:

```
com.healthify.guardian.platform.profile/
├── domain/
│   ├── model/
│   │   ├── aggregates/
│   │   ├── commands/
│   │   ├── events/
│   │   ├── queries/
│   │   └── valueobjects/
│   ├── repositories/
│   └── services/
├── interfaces/
│   └── rest/
│       ├── resources/
│       └── transform/
├── application/
│   ├── commandservices/
│   ├── internal/
│   │   ├── commandservices/
│   │   └── queryservices/
│   └── queryservices/
└── infrastructure/
    ├── configuration/
    └── persistence/
        └── jpa/
            ├── adapters/
            ├── assemblers/
            ├── converters/
            ├── entities/
            └── repositories/
```

#### 2.6.4.1. Domain Layer

La Domain Layer concentra las reglas de negocio relacionadas con la gestión de perfiles de usuario, personas bajo cuidado, relaciones de cuidado y preferencias de aplicación. Esta capa mantiene las invariantes del contexto Profile y permanece independiente de los mecanismos de persistencia y de autenticación externos.

##### Aggregates

**`UserProfile`**

Representa la información descriptiva asociada a un usuario de Guardian+. El aggregate mantiene los datos personales, información de contacto e imagen de perfil utilizados por la aplicación.

**Atributos principales:**

- `id: UserProfileId`
- `userId: UserId`
- `firstName: String`
- `lastName: String`
- `phoneNumber: String`
- `profileImageUrl: String`
- `createdAt: Instant`
- `updatedAt: Instant`

**Métodos principales:**

- `updatePersonalInformation(firstName: String, lastName: String, updatedAt: Instant): void`
- `updateContactInformation(phoneNumber: String, updatedAt: Instant): void`
- `updateProfileImage(profileImageUrl: String, updatedAt: Instant): void`

El aggregate garantiza que cada perfil permanezca asociado a un identificador de usuario mediante `UserId`, sin asumir responsabilidades relacionadas con autenticación.

**`CareRecipientProfile`**

Representa el perfil de una persona bajo cuidado dentro de Guardian+. Mantiene la información descriptiva necesaria para identificar y administrar a la persona vinculada con familiares o cuidadores.

**Atributos principales:**

- `id: CareRecipientProfileId`
- `createdByUserId: UserId`
- `firstName: String`
- `lastName: String`
- `birthDate: LocalDate`
- `profileImageUrl: String`
- `createdAt: Instant`
- `updatedAt: Instant`

**Métodos principales:**

- `updatePersonalInformation(firstName: String, lastName: String, birthDate: LocalDate, updatedAt: Instant): void`
- `updateProfileImage(profileImageUrl: String, updatedAt: Instant): void`

El aggregate permite actualizar tanto la información personal como la imagen de la persona bajo cuidado, conservando el usuario que creó originalmente el perfil mediante `createdByUserId`.

**`CareRelationship`**

Representa la relación de responsabilidad entre un usuario de Guardian+ y una persona bajo cuidado. Permite distinguir si el usuario participa como familiar o cuidador y controlar el ciclo de vida de dicha relación.

**Atributos principales:**

- `id: CareRelationshipId`
- `userId: UserId`
- `careRecipientProfileId: CareRecipientProfileId`
- `relationshipType: RelationshipType`
- `status: CareRelationshipStatus`
- `startedAt: Instant`
- `endedAt: Instant`

**Métodos principales:**

- `establish(startedAt: Instant): void`
- `end(endedAt: Instant): void`
- `isActive(): Boolean`

La relación inicia con estado `ACTIVE` y puede finalizar pasando a estado `ENDED`. Una relación finalizada deja de considerarse activa, manteniéndose su información para conservar el historial de cuidado.

**`UserPreferences`**

Representa las preferencias de aplicación, idioma y accesibilidad configuradas por un usuario de Guardian+.

**Atributos principales:**

- `userId: UserId`
- `language: Language`
- `notificationsEnabled: Boolean`
- `highContrastEnabled: Boolean`
- `reduceMotionEnabled: Boolean`
- `fontScale: FontScale`
- `updatedAt: Instant`

Las preferencias visuales iniciales utilizan español de Latinoamérica (`es-419`), tamaño de fuente predeterminado, alto contraste desactivado y reducción de movimiento desactivada. El estado inicial de las notificaciones es proporcionado por la solicitud del usuario.

**Métodos principales:**

- `updateApplicationPreferences(notificationsEnabled: Boolean, updatedAt: Instant): void`
- `updateLanguageAndAccessibilityPreferences(language: Language, highContrastEnabled: Boolean, reduceMotionEnabled: Boolean, fontScale: FontScale, updatedAt: Instant): void`

La actualización de idioma y accesibilidad se realiza como una única operación de dominio para mantener de forma consistente las preferencias asociadas a la experiencia de uso.

##### Value Objects

**`UserProfileId`**

Identificador inmutable utilizado para distinguir un perfil de usuario dentro del Bounded Context Profile.

**Atributos:**

- `value: UUID`

El identificador es generado por el propio dominio al crear un nuevo `UserProfile`.

**`CareRecipientProfileId`**

Identificador inmutable utilizado para distinguir el perfil de una persona bajo cuidado.

**Atributos:**

- `value: UUID`

El identificador es generado por el dominio al registrar un nuevo `CareRecipientProfile`.

**`CareRelationshipId`**

Identificador inmutable utilizado para distinguir una relación de cuidado.

**Atributos:**

- `value: UUID`

El identificador es generado por el dominio cuando se establece una nueva relación de cuidado.

**`UserId`**

Referencia inmutable al identificador de un usuario externo al Bounded Context Profile.

**Atributos:**

- `value: UUID`

A diferencia de los identificadores pertenecientes al propio contexto, `UserId` no es generado por Profile. Se utiliza únicamente como referencia externa hacia el usuario que posteriormente será administrado por el Bounded Context IAM.

`UserPreferences` no posee un Value Object `UserPreferencesId`; su identidad dentro del dominio se encuentra asociada directamente a `UserId`.

##### Enumerations

**`RelationshipType`**

Representa el tipo de responsabilidad existente entre un usuario y una persona bajo cuidado.

- `FAMILY`
- `CAREGIVER`

**`CareRelationshipStatus`**

Representa el estado actual del ciclo de vida de una relación de cuidado.

- `ACTIVE`
- `ENDED`

Una relación se crea inicialmente con estado `ACTIVE` y cambia a `ENDED` cuando finaliza.

**`Language`**

Representa los idiomas soportados actualmente por Guardian+.

- `SPANISH_LATIN_AMERICA` — código `es-419`
- `ENGLISH_UNITED_STATES` — código `en-US`

**`FontScale`**

Representa las opciones de tamaño de texto disponibles en las preferencias de accesibilidad.

- `SMALL`
- `DEFAULT`
- `LARGE`

El tamaño de fuente se maneja como una enumeración de opciones soportadas y no como un valor decimal arbitrario.

##### Domain Policies

**`CareRelationshipPolicy`**

Evalúa las condiciones necesarias para establecer una nueva relación de cuidado entre un usuario y una persona bajo cuidado.

La policy utiliza `CareRelationshipRepository` para comprobar que no exista previamente una relación activa entre el mismo usuario y el mismo `CareRecipientProfile`.

**Operaciones principales:**

- `canEstablishRelationship(userId: UserId, careRecipientProfileId: CareRecipientProfileId): Boolean`
- `validateRelationshipType(type: RelationshipType): void`

`canEstablishRelationship(...)` retorna `false` cuando alguno de los identificadores es inválido o cuando ya existe una relación activa entre ambos participantes.

`validateRelationshipType(...)` garantiza que el tipo de relación proporcionado sea válido dentro del dominio.

##### Commands & Queries (Domain Model)

Los comandos representan intenciones de modificación del estado del dominio, mientras que las queries permiten recuperar información sin modificar los Aggregate Roots.

**Commands:**

- `CreateUserProfileCommand(UUID userId, String firstName, String lastName, String phoneNumber, String profileImageUrl)`

- `UpdateUserProfileCommand(UUID userProfileId, String firstName, String lastName)`

- `UpdateContactInformationCommand(UUID userProfileId, String phoneNumber)`

- `UpdateUserProfileImageCommand(UUID userProfileId, String profileImageUrl)`

- `CreateCareRecipientProfileCommand(UUID createdByUserId, String firstName, String lastName, LocalDate birthDate, String profileImageUrl)`

- `UpdateCareRecipientProfileCommand(UUID careRecipientProfileId, String firstName, String lastName, LocalDate birthDate)`

- `UpdateCareRecipientProfileImageCommand(UUID careRecipientProfileId, String profileImageUrl)`

- `EstablishCareRelationshipCommand(UUID userId, UUID careRecipientProfileId, RelationshipType relationshipType)`

- `EndCareRelationshipCommand(UUID careRelationshipId)`

- `UpdateApplicationPreferencesCommand(UUID userId, boolean notificationsEnabled)`

- `UpdateLanguageAndAccessibilityPreferencesCommand(UUID userId, Language language, boolean highContrastEnabled, boolean reduceMotionEnabled, FontScale fontScale)`

**Queries:**

- `GetUserProfileByUserIdQuery(UserId userId)`

- `GetCareRecipientProfileQuery(CareRecipientProfileId careRecipientProfileId)`

- `GetCareRecipientProfilesByCreatedByUserIdQuery(UserId createdByUserId)`

- `GetCareRelationshipsByUserIdQuery(UserId userId)`

- `GetCareRelationshipsByCareRecipientProfileIdQuery(CareRecipientProfileId careRecipientProfileId)`

- `GetUserPreferencesQuery(UserId userId)`

La separación entre commands y queries permite que la Application Layer coordine las operaciones del contexto manteniendo las reglas de negocio dentro de los Aggregate Roots y Domain Services.

##### Domain Events

El Bounded Context Profile registra eventos de dominio cuando ocurren cambios relevantes sobre sus aggregates.

- `ProfileCreatedEvent`: registrado cuando se crea el perfil descriptivo asociado a un usuario.

- `ProfileUpdatedEvent`: registrado cuando se actualiza la información personal de un perfil de usuario.

- `ContactInformationUpdatedEvent`: registrado cuando cambia la información de contacto de un usuario.

- `CareRecipientProfileCreatedEvent`: registrado cuando se crea el perfil de una nueva persona bajo cuidado.

- `CareRelationshipEstablishedEvent`: registrado cuando se establece una nueva relación de cuidado.

- `CareRelationshipEndedEvent`: registrado cuando una relación activa pasa al estado `ENDED`.

- `ApplicationPreferencesUpdatedEvent`: registrado cuando se crean o modifican las preferencias generales de aplicación, como el estado de las notificaciones.

- `LanguageAndAccessibilityPreferencesUpdatedEvent`: registrado cuando cambian el idioma, alto contraste, reducción de movimiento o tamaño de fuente.

Los repositorios JPA recuperan los eventos registrados por los Aggregate Roots después de persistir su estado y utilizan el mecanismo de publicación de eventos de Spring para comunicarlos dentro de la aplicación.

La implementación actual no define Event Handler classes específicas dentro del Bounded Context Profile; la publicación de los eventos queda preparada para futuras integraciones con otros contextos.

##### Repositories (Domain Interfaces)

**`UserProfileRepository`**

Abstracción utilizada para recuperar y persistir perfiles de usuario.

**Operaciones principales:**

- `save(profile: UserProfile): UserProfile`

- `findById(id: UserProfileId): Optional<UserProfile>`

- `findByUserId(userId: UserId): Optional<UserProfile>`

**`CareRecipientProfileRepository`**

Abstracción utilizada para recuperar y persistir perfiles de personas bajo cuidado.

**Operaciones principales:**

- `save(profile: CareRecipientProfile): CareRecipientProfile`

- `findById(id: CareRecipientProfileId): Optional<CareRecipientProfile>`

- `findByCreatedByUserId(userId: UserId): List<CareRecipientProfile>`

**`CareRelationshipRepository`**

Abstracción utilizada para recuperar y persistir las relaciones de cuidado.

**Operaciones principales:**

- `save(relationship: CareRelationship): CareRelationship`

- `findById(id: CareRelationshipId): Optional<CareRelationship>`

- `findActiveByUserId(userId: UserId): List<CareRelationship>`

- `findActiveByCareRecipientId(careRecipientProfileId: CareRecipientProfileId): List<CareRelationship>`

**`UserPreferencesRepository`**

Abstracción utilizada para recuperar y persistir las preferencias asociadas a cada usuario.

**Operaciones principales:**

- `save(preferences: UserPreferences): UserPreferences`

- `findByUserId(userId: UserId): Optional<UserPreferences>`

El modelo de dominio utiliza identificadores tipados para los elementos que pertenecen a Profile y mantiene `UserId` como referencia externa. En la implementación actual no existe `UserPreferencesId`, ya que las preferencias se encuentran asociadas directamente al usuario.

#### 2.6.4.2. Interface Layer

La Interface Layer expone las capacidades del Bounded Context **Profile** mediante una API REST. Esta capa recibe las solicitudes HTTP, valida los recursos de entrada y los transforma en comandos o consultas que son delegados a la Application Layer.

Los controllers no contienen reglas de negocio ni acceden directamente a la persistencia. Su responsabilidad consiste en actuar como punto de entrada hacia los casos de uso del contexto.

##### REST Controllers

**`UserProfilesController`**

Expone las operaciones relacionadas con la creación, consulta y actualización del perfil descriptivo de un usuario.

**Operaciones principales:**

- `POST /api/v1/user-profiles`

Crea un nuevo perfil de usuario utilizando la información personal, de contacto e imagen proporcionada.

- `GET /api/v1/user-profiles/user/{userId}`

Obtiene el perfil asociado a un determinado `UserId`.

- `PUT /api/v1/user-profiles/{userProfileId}`

Actualiza el nombre y apellido de un perfil existente.

- `PUT /api/v1/user-profiles/{userProfileId}/contact-information`

Actualiza la información de contacto asociada al perfil.

- `PUT /api/v1/user-profiles/{userProfileId}/profile-image`

Actualiza la imagen de perfil del usuario.

**Relaciones principales:**

- recibe recursos HTTP desde los clientes de Guardian+;

- transforma las solicitudes en commands y queries del Bounded Context Profile;

- delega las operaciones a `UserProfileCommandService` y `UserProfileQueryService`;

- utiliza `UserId` como referencia externa sin administrar credenciales ni mecanismos de autenticación;

- transforma los resultados del dominio en recursos REST antes de devolver la respuesta al cliente.


**`CareRecipientProfilesController`**

Expone las operaciones relacionadas con las personas bajo cuidado registradas dentro de Guardian+.

**Operaciones principales:**

- `POST /api/v1/care-recipient-profiles`

Registra un nuevo perfil de persona bajo cuidado.

- `GET /api/v1/care-recipient-profiles/{careRecipientProfileId}`

Obtiene un `CareRecipientProfile` mediante su identificador.

- `GET /api/v1/care-recipient-profiles/created-by/{userId}`

Obtiene la lista de perfiles de personas bajo cuidado registrados por un determinado usuario.

- `PUT /api/v1/care-recipient-profiles/{careRecipientProfileId}`

Actualiza la información personal de una persona bajo cuidado, incluyendo nombres y fecha de nacimiento.

- `PUT /api/v1/care-recipient-profiles/{careRecipientProfileId}/profile-image`

Actualiza la imagen de perfil de una persona bajo cuidado.

**Relaciones principales:**

- delega las operaciones de modificación a `CareRecipientProfileCommandService`;

- utiliza `CareRecipientProfileQueryService` para recuperar uno o varios perfiles;

- utiliza `CareRecipientProfileId` como identificador propio del contexto;

- mantiene `createdByUserId` como referencia al usuario que registró originalmente a la persona bajo cuidado;

- no accede directamente a la tabla `care_recipient_profiles`.


**`CareRelationshipsController`**

Expone las operaciones utilizadas para administrar las relaciones de cuidado existentes entre usuarios y personas bajo cuidado.

**Operaciones principales:**

- `POST /api/v1/care-relationships`

Establece una nueva relación de cuidado entre un usuario y un `CareRecipientProfile`.

- `GET /api/v1/care-relationships/user/{userId}`

Obtiene las relaciones activas asociadas a un determinado usuario.

- `GET /api/v1/care-relationships/care-recipient/{careRecipientProfileId}`

Obtiene las relaciones activas asociadas a una determinada persona bajo cuidado.

- `DELETE /api/v1/care-relationships/{careRelationshipId}`

Finaliza una relación de cuidado existente.

La operación de finalización no elimina físicamente la relación. El Aggregate Root cambia su estado de `ACTIVE` a `ENDED`, permitiendo conservar el historial de la relación.

**Relaciones principales:**

- delega el establecimiento y finalización de relaciones a `CareRelationshipCommandService`;

- utiliza `CareRelationshipQueryService` para consultar las relaciones activas;

- las reglas necesarias para evitar relaciones activas duplicadas son evaluadas por la Domain Layer;

- no modifica directamente la tabla `care_relationships`.


**`UserPreferencesController`**

Expone las operaciones necesarias para consultar y modificar las preferencias de aplicación, idioma y accesibilidad de cada usuario.

**Operaciones principales:**

- `GET /api/v1/user-preferences/user/{userId}`

Obtiene las preferencias configuradas para un determinado usuario.

- `PUT /api/v1/user-preferences/user/{userId}/application`

Actualiza las preferencias generales de aplicación, actualmente representadas por el estado de las notificaciones.

- `PUT /api/v1/user-preferences/user/{userId}/language-accessibility`

Actualiza conjuntamente el idioma y las preferencias de accesibilidad: alto contraste, reducción de movimiento y tamaño de fuente.

**Relaciones principales:**

- delega las operaciones de modificación a `UserPreferencesCommandService`;

- utiliza `UserPreferencesQueryService` para recuperar las preferencias existentes;

- mantiene las preferencias asociadas directamente a `UserId`;

- no modifica directamente la tabla `user_preferences`.


##### Resources & Assemblers

La Interface Layer utiliza recursos REST para representar la información recibida y enviada por la API.

Entre los principales recursos de entrada se encuentran:

- `CreateUserProfileResource`
- `UpdateUserProfileResource`
- `UpdateContactInformationResource`
- `UpdateProfileImageResource`
- `CreateCareRecipientProfileResource`
- `UpdateCareRecipientProfileResource`
- `EstablishCareRelationshipResource`
- `UpdateApplicationPreferencesResource`
- `UpdateLanguageAndAccessibilityPreferencesResource`

Los recursos de salida principales son:

- `UserProfileResource`
- `CareRecipientProfileResource`
- `CareRelationshipResource`
- `UserPreferencesResource`

Los Transform Assemblers convierten estos recursos en los Commands correspondientes y transforman los Aggregate Roots recuperados por la Application Layer en los recursos devueltos por la API.

Esta separación evita que las clases propias del dominio sean expuestas directamente a través de la interfaz HTTP.

#### 2.6.4.3. Application Layer

La Application Layer coordina los casos de uso del Bounded Context **Profile** y actúa como intermediaria entre la Interface Layer y el modelo de dominio.

Esta capa recibe Commands y Queries provenientes de los controllers, recupera los Aggregate Roots requeridos mediante Repository Interfaces y delega las reglas de negocio a los propios aggregates y Domain Services.

La implementación se organiza mediante Command Services para operaciones que modifican el estado del dominio y Query Services para operaciones de consulta.

##### Command Services

**`UserProfileCommandService`**

Define las operaciones de aplicación relacionadas con la creación y modificación de perfiles de usuario.

Su implementación concreta, `UserProfileCommandServiceImpl`, coordina los siguientes casos de uso:

- creación de un nuevo `UserProfile`;

- actualización de información personal;

- actualización de información de contacto;

- actualización de la imagen de perfil.

Durante la creación, el servicio verifica que no exista previamente un perfil asociado al mismo `UserId`.

Las validaciones propias del perfil permanecen dentro del Aggregate Root `UserProfile`, mientras que el servicio coordina la búsqueda y persistencia mediante `UserProfileRepository`.


**`CareRecipientProfileCommandService`**

Define las operaciones relacionadas con la creación y actualización de perfiles de personas bajo cuidado.

Su implementación `CareRecipientProfileCommandServiceImpl` coordina:

- creación de un nuevo `CareRecipientProfile`;

- actualización de nombres y fecha de nacimiento;

- actualización de la imagen del perfil.

El servicio recupera el Aggregate Root correspondiente mediante `CareRecipientProfileRepository`, ejecuta la operación de dominio requerida y persiste posteriormente su nuevo estado.


**`CareRelationshipCommandService`**

Coordina los casos de uso relacionados con el ciclo de vida de una relación de cuidado.

Su implementación `CareRelationshipCommandServiceImpl` permite:

- establecer una nueva relación entre un usuario y una persona bajo cuidado;

- finalizar una relación de cuidado existente.

Antes de establecer una nueva relación utiliza `CareRelationshipPolicy` para comprobar que no exista ya una relación activa entre el mismo usuario y el mismo `CareRecipientProfile`.

La finalización de una relación no elimina el aggregate. Se ejecuta la operación `end(...)`, que modifica su estado de `ACTIVE` a `ENDED`.


**`UserPreferencesCommandService`**

Coordina las operaciones de modificación de las preferencias asociadas a un usuario.

Su implementación `UserPreferencesCommandServiceImpl` permite:

- crear o actualizar las preferencias generales de aplicación mediante `UpdateApplicationPreferencesCommand`;

- actualizar conjuntamente idioma y accesibilidad mediante `UpdateLanguageAndAccessibilityPreferencesCommand`.

Cuando todavía no existen preferencias para un usuario, la actualización de preferencias generales puede originar la creación inicial del Aggregate Root `UserPreferences`.

La operación de idioma y accesibilidad actúa sobre preferencias previamente existentes.


##### Query Services

Los Query Services recuperan información del dominio sin modificar el estado de los Aggregate Roots.

**`UserProfileQueryService`**

Su implementación `UserProfileQueryServiceImpl` recupera el perfil asociado a un usuario mediante `UserId`.

Utiliza `UserProfileRepository` como abstracción de persistencia.


**`CareRecipientProfileQueryService`**

Su implementación `CareRecipientProfileQueryServiceImpl` permite:

- recuperar un `CareRecipientProfile` mediante su identificador;

- recuperar la colección de perfiles registrados por un determinado usuario mediante `createdByUserId`.


**`CareRelationshipQueryService`**

Su implementación `CareRelationshipQueryServiceImpl` permite consultar:

- las relaciones activas asociadas a un usuario;

- las relaciones activas asociadas a una persona bajo cuidado.

Estas operaciones utilizan `CareRelationshipRepository` para recuperar las relaciones que permanecen en estado `ACTIVE`.


**`UserPreferencesQueryService`**

Su implementación `UserPreferencesQueryServiceImpl` recupera las preferencias asociadas a un determinado `UserId`.

La consulta se realiza mediante `UserPreferencesRepository`.


##### Application Error Handling

Los Command Services utilizan la abstracción compartida `Result` para representar el resultado de las operaciones de aplicación.

Cuando una operación finaliza correctamente se devuelve un resultado exitoso. En situaciones de error se utilizan objetos `ApplicationError`, permitiendo representar de forma consistente casos como:

- errores de validación;

- recursos no encontrados;

- conflictos de negocio;

- violaciones de reglas del dominio.

Los mensajes de error son resueltos mediante `MessageResolver`, permitiendo mantener soporte de internacionalización para los mensajes definidos por Profile.


##### Domain Events in the Application Flow

Los Aggregate Roots de Profile registran Domain Events cuando ocurre un cambio relevante en su estado.

Después de persistir un aggregate, las implementaciones de los repositorios pueden recuperar los eventos registrados y publicarlos utilizando el mecanismo de eventos de Spring.

En el estado actual del backend no existen clases específicas de tipo `EventHandler` dentro del Bounded Context Profile. Por ello, dichos handlers no se presentan como componentes implementados en esta capa.

La publicación de eventos queda disponible para permitir futuras integraciones con otros Bounded Contexts conforme avance la implementación del backend.


#### 2.6.4.4. Infrastructure Layer

La Infrastructure Layer contiene las implementaciones técnicas necesarias para persistir y recuperar la información administrada por el Bounded Context **Profile**.

Esta capa implementa las Repository Interfaces definidas por el dominio utilizando Spring Data JPA, entidades de persistencia, assemblers y converters. También contiene la configuración necesaria para proporcionar dependencias técnicas utilizadas por la Application y Domain Layer.

La implementación mantiene separados los Aggregate Roots del modelo de dominio de las entidades utilizadas para representar la información en la base de datos.

##### Persistence JPA Entities

La persistencia del contexto se organiza alrededor de cuatro entidades principales, correspondientes a los cuatro Aggregate Roots implementados.

**`UserProfilePersistenceEntity`**

Representa la persistencia de `UserProfile` en la tabla `user_profiles`.

Entre sus principales datos se encuentran:

- `id`

- `user_id`

- `first_name`

- `last_name`

- `phone_number`

- `profile_image_url`

- `created_at`

- `updated_at`

La entidad almacena únicamente información descriptiva del usuario y utiliza `user_id` como referencia externa.


**`CareRecipientProfilePersistenceEntity`**

Representa la persistencia de `CareRecipientProfile` en la tabla `care_recipient_profiles`.

Entre sus principales datos se encuentran:

- `id`

- `created_by_user_id`

- `first_name`

- `last_name`

- `birth_date`

- `profile_image_url`

- `created_at`

- `updated_at`

`created_by_user_id` permite conservar la referencia hacia el usuario que registró originalmente a la persona bajo cuidado.


**`CareRelationshipPersistenceEntity`**

Representa las relaciones de cuidado almacenadas en la tabla `care_relationships`.

Entre sus principales datos se encuentran:

- `id`

- `user_id`

- `care_recipient_profile_id`

- `relationship_type`

- `status`

- `started_at`

- `ended_at`

Los valores de `relationship_type` representan los tipos `FAMILY` y `CAREGIVER`, mientras que `status` representa los estados `ACTIVE` y `ENDED`.

La finalización de una relación actualiza su estado y `ended_at` en lugar de eliminar físicamente el registro.


**`UserPreferencesPersistenceEntity`**

Representa las preferencias de un usuario mediante la tabla `user_preferences`.

La identidad persistente de estas preferencias corresponde al mismo UUID del `UserId`, por lo que no se utiliza un `UserPreferencesId` independiente.

Entre los datos persistidos se encuentran:

- `user_id`

- `language`

- `notifications_enabled`

- `high_contrast_enabled`

- `reduce_motion_enabled`

- `font_scale`

- `updated_at`

La propiedad `reduce_motion_enabled` corresponde a la preferencia de accesibilidad utilizada actualmente por Guardian+, reemplazando la referencia anterior a `voice_assistance_enabled`.

Los valores de `language` y `font_scale` se corresponden con las enumeraciones definidas por el dominio.


##### Persistence Converters

La implementación actual utiliza converters específicos cuando es necesario traducir Value Objects del dominio hacia representaciones compatibles con JPA.

Los converters implementados son:

- `UserIdPersistenceConverter`

Convierte entre `UserId` y su representación `UUID` utilizada por la persistencia.

- `CareRecipientProfileIdPersistenceConverter`

Convierte entre `CareRecipientProfileId` y su representación `UUID`.

Las enumeraciones como `RelationshipType`, `CareRelationshipStatus`, `Language` y `FontScale` no poseen clases converter independientes dentro de la implementación actual.


##### Persistence Assemblers

Los Persistence Assemblers mantienen separadas las estructuras del dominio y las estructuras utilizadas por JPA.

Se implementan los siguientes assemblers:

- `UserProfilePersistenceAssembler`

- `CareRecipientProfilePersistenceAssembler`

- `CareRelationshipPersistenceAssembler`

- `UserPreferencesPersistenceAssembler`

Cada assembler proporciona las transformaciones necesarias entre el Aggregate Root correspondiente y su Persistence Entity.

De esta manera, las clases del dominio no dependen directamente de las anotaciones ni de las entidades utilizadas por JPA.


##### Repository Implementations

**`UserProfileRepositoryImpl`**

Implementa `UserProfileRepository` y administra la persistencia de `UserProfile`.

**Responsabilidades principales:**

- persistir perfiles de usuario;

- recuperar perfiles mediante `UserProfileId`;

- recuperar el perfil asociado a un determinado `UserId`;

- transformar entre dominio y persistencia mediante `UserProfilePersistenceAssembler`.


**`CareRecipientProfileRepositoryImpl`**

Implementa `CareRecipientProfileRepository` y administra la persistencia de perfiles de personas bajo cuidado.

**Responsabilidades principales:**

- persistir la creación y actualización de un `CareRecipientProfile`;

- recuperar un perfil mediante `CareRecipientProfileId`;

- recuperar los perfiles registrados por un determinado `UserId`;

- utilizar `CareRecipientProfilePersistenceAssembler` para mantener separados dominio y persistencia.


**`CareRelationshipRepositoryImpl`**

Implementa `CareRelationshipRepository` y administra la persistencia del ciclo de vida de las relaciones de cuidado.

**Responsabilidades principales:**

- persistir nuevas relaciones;

- persistir el cambio de estado de `ACTIVE` a `ENDED`;

- recuperar relaciones mediante `CareRelationshipId`;

- recuperar relaciones activas asociadas a un usuario;

- recuperar relaciones activas asociadas a una persona bajo cuidado;

- transformar los modelos mediante `CareRelationshipPersistenceAssembler`.


**`UserPreferencesRepositoryImpl`**

Implementa `UserPreferencesRepository` y administra las preferencias asociadas a cada usuario.

**Responsabilidades principales:**

- persistir la creación o modificación de preferencias;

- recuperar preferencias mediante `UserId`;

- persistir idioma, notificaciones, alto contraste, reducción de movimiento y tamaño de fuente;

- transformar entre `UserPreferences` y `UserPreferencesPersistenceEntity` mediante `UserPreferencesPersistenceAssembler`.


##### Spring Data JPA Repositories

Las Repository Implementations utilizan interfaces de Spring Data JPA para realizar las operaciones sobre la base de datos.

Se encuentran implementadas:

- `UserProfilePersistenceRepository`

- `CareRecipientProfilePersistenceRepository`

- `CareRelationshipPersistenceRepository`

- `UserPreferencesPersistenceRepository`

Estas interfaces contienen las consultas necesarias para localizar los registros utilizados por las Repository Implementations sin exponer directamente detalles de persistencia hacia la Domain Layer.


##### Domain Event Publishing

Los Aggregate Roots registran Domain Events cuando ocurre una modificación relevante de su estado.

Al persistir un aggregate, las implementaciones de repositorio recuperan los eventos registrados antes de limpiarlos del Aggregate Root y utilizan el mecanismo de publicación de eventos proporcionado por Spring para publicarlos dentro de la aplicación.

Este mecanismo permite mantener desacoplada la generación de eventos del modelo de dominio respecto de su publicación técnica.

Actualmente no existe una clase independiente denominada `ProfileEventPublisher`; la publicación se realiza desde las implementaciones de los repositorios mediante la infraestructura de eventos de Spring.


##### Profile Configuration

`ProfileConfiguration` centraliza la configuración técnica necesaria para algunos componentes del Bounded Context.

Entre sus responsabilidades se encuentran:

- proporcionar un `Clock` mediante `Clock.systemUTC()` para que los servicios de aplicación puedan trabajar con timestamps de manera consistente;

- registrar `CareRelationshipPolicy` proporcionando su dependencia `CareRelationshipRepository`.

Esto permite utilizar dichas dependencias mediante inyección sin introducir componentes de infraestructura directamente dentro del modelo de dominio.


##### Integration with IAM

Profile mantiene `UserId` como referencia externa hacia la identidad del usuario, pero no almacena contraseñas, tokens ni información de autenticación.

En el estado actual del backend no existe todavía un Bounded Context IAM implementado en la rama `develop`. Por esta razón, tampoco se encuentra implementado un `IAMQueryAdapter`, `IdentityReferenceAdapter` o componente equivalente dentro de Profile.

La validación directa de referencias contra IAM queda pendiente para una etapa posterior de implementación, una vez que dicho Bounded Context proporcione una interfaz pública que pueda ser consumida sin generar acoplamiento directo entre los modelos internos de ambos contextos.

Esta decisión mantiene preparado el diseño para una futura integración sin incorporar actualmente dependencias hacia componentes inexistentes.

#### 2.6.4.5. Bounded Context Software Architecture Component Level Diagrams

La Figura 2.54 presenta la arquitectura a nivel de componentes propuesta para el Bounded Context **Profile**. La vista representa la organización general necesaria para administrar perfiles de usuario, perfiles de personas bajo cuidado, relaciones de cuidado y preferencias de aplicación.

<a id="figura-2-54"></a>**Figura 2.54.** Diagrama de componentes del Bounded Context Profile

![Profile Component Level Diagram](../assets/images/chapterII/Profile/ProofileComponents.png)

La **Interface Layer** se representa mediante los componentes REST responsables de exponer las operaciones del contexto hacia los clientes de Guardian+. En la implementación actual estas responsabilidades se encuentran distribuidas entre `UserProfilesController`, `CareRecipientProfilesController`, `CareRelationshipsController` y `UserPreferencesController`.

Las solicitudes recibidas son delegadas hacia la Application Layer, implementada mediante Command Services y Query Services específicos para cada Aggregate Root. Esta capa coordina los casos de uso sin incorporar directamente las reglas propias del dominio.

La lógica principal del dominio se concentra en cuatro Aggregate Roots: `UserProfile`, `CareRecipientProfile`, `CareRelationship` y `UserPreferences`. Adicionalmente, `CareRelationshipPolicy` encapsula la regla que evita establecer relaciones activas duplicadas entre un mismo usuario y una misma persona bajo cuidado.

El diagrama conserva algunos elementos correspondientes al diseño arquitectónico planteado para etapas posteriores del proyecto. En particular, la integración directa mediante un adaptador hacia IAM permanece pendiente debido a que dicho Bounded Context todavía no se encuentra implementado en el backend actual. Profile mantiene por el momento `UserId` únicamente como referencia externa.

La **Infrastructure Layer** implementada actualmente incluye los Repository Adapters, entidades JPA, Persistence Repositories, Persistence Assemblers, converters requeridos y la configuración técnica del contexto. La persistencia se realiza sobre las tablas propias de Profile y los Domain Events registrados por los Aggregate Roots son publicados utilizando la infraestructura de eventos proporcionada por Spring.

De esta manera, el diagrama se mantiene como representación arquitectónica del contexto, mientras que la implementación desarrollada para el presente avance cubre las capacidades principales de Profile y deja las integraciones dependientes de otros Bounded Contexts para los siguientes incrementos.

#### 2.6.4.6. Bounded Context Software Architecture Code Level Diagrams

En esta sección se documenta la estructura interna del Bounded Context **Profile** a nivel de código. Los diagramas se mantienen como referencia del diseño planteado para el contexto y se complementan con la descripción de los elementos efectivamente implementados durante el presente Sprint.

##### 2.6.4.6.1. Bounded Context Domain Layer Class Diagrams

El diagrama UML de la Figura 2.55 presenta la organización general de la Domain Layer de **Profile**.

<a id="figura-2-55"></a>**Figura 2.55.** Diagrama de clases de la Domain Layer de Profile

![Profile Domain Layer Class Diagram](../assets/images/chapterII/Profile/ProfileCodeLevelDiagrams.png)

`UserProfile` mantiene la información descriptiva de un usuario de Guardian+ y `CareRecipientProfile` la de una persona bajo cuidado. `CareRelationship` vincula a ambos indicando el tipo de relación y su vigencia, mientras que `UserPreferences` concentra las preferencias de idioma y accesibilidad de cada usuario. Los contactos de emergencia no pertenecen a este contexto: son gobernados por `Emergency & Alerting`, que los mantiene sincronizados a partir de los eventos de relación de cuidado.

El dominio utiliza los Value Objects `UserProfileId`, `CareRecipientProfileId`, `CareRelationshipId`, `UserPreferencesId`, `FontScale` y `UserId` —este último como referencia a la identidad administrada por IAM— para representar conceptos que poseen validaciones y comportamiento propios.


##### 2.6.4.6.2. Bounded Context Database Design Diagram

La Figura 2.56 representa el diseño de persistencia correspondiente al Bounded Context **Profile**. Las tablas reflejan la información que debe almacenarse en el backend para administrar perfiles, personas bajo cuidado, relaciones de cuidado y preferencias.

<a id="figura-2-56"></a>**Figura 2.56.** Diagrama de base de datos de Profile

![Profile Database Design Diagram](../assets/images/chapterII/Profile/ProfileDatabaseDesigDiagram.png)

`user_profiles` almacena la información descriptiva asociada a las cuentas administradas por IAM, mientras que `care_recipient_profiles` representa las personas bajo cuidado registradas en Guardian+.

La relación entre usuarios y personas bajo cuidado se representa mediante `care_relationships`, permitiendo establecer asociaciones entre familiares o cuidadores y los perfiles correspondientes. Finalmente, `user_preferences` mantiene las configuraciones de idioma, accesibilidad y experiencia de uso asociadas a cada usuario.

### 2.6.5. Bounded Context: Care Routines & Wellness

El Bounded Context **Care Routines & Wellness** pertenece al Supporting Domain de Guardian+. Su responsabilidad consiste en asegurar que las rutinas de bienestar de la persona bajo cuidado se cumplan: recordatorios de medicación, citas médicas, actividad física e hidratación; registro y clasificación de ciclos de sueño; detección de inactividad física prolongada; y control del stock de medicamentos con sugerencia de reabastecimiento.

Este contexto recibe la telemetría de actividad y de sueño del wearable mediante sus consumidores de mensajes y publica los eventos de integración `ProlongedInactivityDetected`, `ReminderReissued` y `MedicationRestockSuggested`, que Emergency & Alerting consume para notificar al cuidador o al familiar. Care Routines & Wellness no evalúa signos vitales ni gestiona el escalamiento de las alertas.

La arquitectura táctica se implementa sobre Java y Spring Boot con una estructura de paquetes dividida en cuatro capas: domain, interfaces, application e infrastructure. Su código se organiza en el paquete `com.healthify.guardian.platform.careroutineswellness` del repositorio `guardian-plus-platform`, con la siguiente estructura:

```
com.healthify.guardian.platform.careroutineswellness/
├── domain/
│   ├── model/
│   │   ├── aggregates/
│   │   ├── commands/
│   │   ├── events/
│   │   ├── queries/
│   │   └── valueobjects/
│   ├── repositories/
│   └── services/
├── interfaces/
│   ├── events/
│   ├── messaging/
│   └── rest/
│       ├── resources/
│       └── transform/
├── application/
│   ├── commandservices/
│   ├── internal/
│   │   ├── commandservices/
│   │   ├── eventhandlers/
│   │   └── queryservices/
│   └── queryservices/
└── infrastructure/
    ├── configuration/
    ├── messaging/
    ├── persistence/
    │   └── jpa/
    │       ├── adapters/
    │       ├── assemblers/
    │       ├── converters/
    │       ├── entities/
    │       └── repositories/
    └── scheduling/
```

#### 2.6.5.1. Domain Layer

Encapsula la lógica pura de rutina y bienestar, las invariantes de ciclo de vida de cada recordatorio y las decisiones de programación temporal embebidas en los propios agregados, Value Objects y Domain Services.

##### Aggregates

*   **Reminder**
    *   Agregado raíz principal que representa un recordatorio individual de rutina (medicación, cita médica, actividad física o hidratación) y su ciclo de vida completo.
    *   Hereda de `AbstractDomainAggregateRoot<Reminder>` para registrar y publicar eventos de dominio.
    *   Protege las transiciones válidas de estado; delega en `ReminderIssuancePolicy` y `ReminderReissuePolicy` la decisión de cuándo emitir, suprimir o reemitir, sin evaluar dichas condiciones por sí mismo.
    *   *Atributos:*
        *   `id: ReminderId`
        *   `personUnderCareId: PersonUnderCareId`
        *   `type: ReminderType`
        *   `scheduledTime: Instant`
        *   `issuedAt: Instant`
        *   `status: ReminderStatus`
        *   `reissueCount: Integer`
    *   *Métodos:*
        *   `Reminder(ScheduleReminderCommand command)`
        *   `issue(IssuanceOutcome outcome, Instant currentTime): void`
        *   `confirm(): void`
        *   `cancel(): void`
        *   `reissue(): void`
        *   `isActive(): Boolean`

*   **SleepCycleRecord**
    *   Agregado raíz que representa un ciclo de sueño cerrado del adulto mayor, persona con discapacidad o en situación de dependencia.
    *   *Atributos:*
        *   `id: SleepCycleRecordId`
        *   `personUnderCareId: PersonUnderCareId`
        *   `startTime: Instant`
        *   `endTime: Instant`
        *   `interruptionCount: Integer`
        *   `classification: SleepClassification`
    *   *Métodos:*
        *   `SleepCycleRecord(RecordSleepCycleCommand command)`
        *   `classify(): SleepClassification`

*   **ActivityMonitor**
    *   Agregado raíz que representa el estado de actividad física de una persona bajo cuidado a lo largo del día.
    *   *Atributos:*
        *   `id: ActivityMonitorId`
        *   `personUnderCareId: PersonUnderCareId`
        *   `status: ActivityStatus`
        *   `inactivitySince: Instant`
    *   *Métodos:*
        *   `recordProlongedInactivity(Instant detectedAt): void`
        *   `recordActivityResumed(Instant resumedAt): void`
        *   `isInactive(): Boolean`

*   **MedicationStock**
    *   Agregado raíz que representa el balance de dosis restantes de un tratamiento de medicación y determina, junto a `MedicationStockPolicy`, cuándo corresponde sugerir su reabastecimiento.
    *   *Atributos:*
        *   `id: MedicationStockId`
        *   `personUnderCareId: PersonUnderCareId`
        *   `remainingDoses: Integer`
        *   `dailyConsumption: Decimal`
        *   `lastAcquisitionDate: Instant`
    *   *Métodos:*
        *   `registerConsumption(Integer dosesConsumed): void`
        *   `confirmAcquisition(Integer dosesAdded): void`
        *   `remainingDaysOfSupply(): Decimal`

##### Value Objects

*   **ReminderId:** Identificador inmutable de un recordatorio.
*   **SleepCycleRecordId:** Identificador inmutable de un ciclo de sueño registrado.
*   **ActivityMonitorId:** Identificador inmutable de un monitor de actividad.
*   **MedicationStockId:** Identificador inmutable de un control de stock de medicación.
*   **PersonUnderCareId:** Identificador de referencia inmutable a la persona bajo cuidado; evita incorporar directamente el modelo del contexto Profile dentro de Care Routines & Wellness.
*   **ReminderType:** Enum (`MEDICATION`, `APPOINTMENT`, `PHYSICAL_ACTIVITY`, `HYDRATION`).
*   **ReminderStatus:** Enum (`SCHEDULED`, `ISSUED`, `CONFIRMED`, `CANCELLED`, `REISSUED`, `SUPPRESSED`).
*   **ActivityStatus:** Enum (`NORMAL`, `INACTIVITY_DETECTED`).
*   **SleepClassification:** Enum (`REGULAR`, `FRAGMENTED`).
*   **IssuanceOutcome:** Enum (`ISSUE`, `SUPPRESS`). Resultado de `ReminderIssuancePolicy` que el aggregate `Reminder` aplica en `issue()`.
*   **SleepWindow:** Intervalo horario inmutable configurado para la persona bajo cuidado, utilizado por `ReminderIssuancePolicy` para determinar la supresión de recordatorios de hidratación.

##### Domain Services

*   **ReminderIssuancePolicy:** Evalúa si un recordatorio debe emitirse normalmente o suprimirse al cumplirse su horario programado, considerando el tipo de recordatorio y la ventana de sueño configurada.
    *   `determineIssuanceOutcome(Reminder reminder, Instant currentTime, SleepWindow sleepWindow): IssuanceOutcome`
*   **ReminderReissuePolicy:** Determina si un recordatorio de medicación emitido requiere reemisión por falta de confirmación dentro del tiempo de tolerancia definido (10 minutos).
    *   `requiresReissue(Reminder reminder, Instant currentTime): Boolean`
*   **MedicationStockPolicy:** Determina si el balance vigente de un control de stock amerita sugerir reabastecimiento.
    *   `requiresRestockSuggestion(MedicationStock stock): Boolean`

##### Commands & Queries (Domain Model)

*   `ScheduleReminderCommand(UUID personUnderCareId, ReminderType type, Instant scheduledTime)`
*   `IssueReminderCommand(UUID reminderId)`
*   `ConfirmReminderCommand(UUID reminderId)`
*   `CancelReminderCommand(UUID reminderId)`
*   `ReissueReminderCommand(UUID reminderId)`
*   `RecordSleepCycleCommand(UUID personUnderCareId, Instant startTime, Instant endTime, Integer interruptionCount)`
*   `RecordProlongedInactivityCommand(UUID personUnderCareId, Instant detectedAt)`
*   `RecordActivityResumedCommand(UUID personUnderCareId, Instant resumedAt)`
*   `SuggestMedicationRestockCommand(UUID personUnderCareId)`
*   `ConfirmMedicationAcquisitionCommand(UUID personUnderCareId, Integer dosesAdded)`
*   `GetReminderStatusByIdQuery(ReminderId reminderId)`
*   `GetRemindersByPersonUnderCareIdQuery(PersonUnderCareId personUnderCareId)`
*   `GetMedicationStockStatusQuery(PersonUnderCareId personUnderCareId)`

##### Domain Events

*   `ReminderScheduledEvent`: Emitido al programarse un nuevo recordatorio.
*   `ReminderIssuedEvent`: Emitido cuando `ReminderIssuancePolicy` determina que el recordatorio debe emitirse.
*   `ReminderConfirmedEvent`: Emitido cuando la persona bajo cuidado confirma el recordatorio.
*   `ReminderCancelledEvent`: Emitido al cancelarse un recordatorio.
*   `ReminderReissuedEvent`: Emitido cuando `ReminderReissuePolicy` determina que corresponde una reemisión.
*   `ReminderSuppressedEvent`: Emitido cuando `ReminderIssuancePolicy` determina que el recordatorio debe suprimirse (recordatorio de hidratación dentro de la ventana de sueño).
*   `SleepCycleRecordedEvent`: Emitido tras registrar y clasificar un ciclo de sueño.
*   `ProlongedInactivityDetectedEvent`: Emitido al transicionar `ActivityMonitor` de `NORMAL` a `INACTIVITY_DETECTED`.
*   `ActivityResumedEvent`: Emitido al resetear `ActivityMonitor` a `NORMAL`.
*   `MedicationRestockSuggestedEvent`: Emitido cuando `MedicationStockPolicy` determina que corresponde sugerir reabastecimiento.
*   `MedicationStockUpdatedEvent`: Emitido tras confirmarse la adquisición de un nuevo envase.

##### Repositories (Domain Interfaces)

*   **ReminderRepository:**
    *   `findById(ReminderId id): Optional<Reminder>`
    *   `findDueForIssuance(Instant currentTime): List<Reminder>`
    *   `findOverdueForReissue(Instant currentTime): List<Reminder>`
    *   `save(Reminder reminder): Reminder`
*   **SleepCycleRecordRepository:**
    *   `findByPersonUnderCareId(PersonUnderCareId personUnderCareId): List<SleepCycleRecord>`
    *   `save(SleepCycleRecord record): SleepCycleRecord`
*   **ActivityMonitorRepository:**
    *   `findByPersonUnderCareId(PersonUnderCareId personUnderCareId): Optional<ActivityMonitor>`
    *   `save(ActivityMonitor monitor): ActivityMonitor`
*   **MedicationStockRepository:**
    *   `findByPersonUnderCareId(PersonUnderCareId personUnderCareId): Optional<MedicationStock>`
    *   `save(MedicationStock stock): MedicationStock`

#### 2.6.5.2. Interface Layer

Traduce estímulos externos (solicitudes HTTP de cuidadores/familiares y telemetría del dispositivo wearable) hacia comandos y consultas de aplicación, expone contratos HTTP RESTful y canaliza eventos de integración.

##### REST Controllers

*   **RemindersController** (`/api/v1/reminders`):
    *   `POST /`: Programa un nuevo recordatorio.
    *   `PUT /{reminderId}/confirm`: Confirma un recordatorio emitido.
    *   `DELETE /{reminderId}`: Cancela un recordatorio programado o emitido.
    *   `GET /citizen/{personUnderCareId}`: Lista los recordatorios de una persona bajo cuidado.
*   **MedicationStockController** (`/api/v1/medication-stock`):
    *   `PUT /{stockId}/acquisition`: Confirma la adquisición de un nuevo envase de medicamento.
    *   `GET /citizen/{personUnderCareId}`: Consulta el estado vigente del stock.

##### Message Consumers

*   **ActivityTelemetryConsumer:** Recibe la telemetría de movimiento e inactividad enviada por el dispositivo wearable y la traduce en `RecordProlongedInactivityCommand` o `RecordActivityResumedCommand`.
*   **SleepTelemetryConsumer:** Recibe la telemetría de ciclos de sueño enviada por el dispositivo wearable y la traduce en `RecordSleepCycleCommand`.

##### Resources & Assemblers

*   *Resources (DTOs):* `ScheduleReminderResource`, `ReminderResource`, `ConfirmMedicationAcquisitionResource`, `MedicationStockResource`.
*   *Assemblers (Mappers):* `ScheduleReminderCommandFromResourceAssembler`, `ReminderResourceFromEntityAssembler`, `ConfirmMedicationAcquisitionCommandFromResourceAssembler`, `MedicationStockResourceFromEntityAssembler`.

##### Integration Events

*   `ProlongedInactivityDetectedIntegrationEvent`: Publicado cuando se detecta inactividad prolongada, consumido por `Emergency & Alerting`.
*   `ReminderReissuedIntegrationEvent`: Publicado cuando un recordatorio de medicación es reemitido, consumido por `Emergency & Alerting` para notificar al cuidador.
*   `MedicationRestockSuggestedIntegrationEvent`: Publicado cuando se sugiere un reabastecimiento, consumido por `Emergency & Alerting` para notificar al familiar.

#### 2.6.5.3. Application Layer

Orquesta los flujos de casos de uso de rutina y bienestar delegando las reglas de negocio en los agregados y Domain Services correspondientes.

##### Command Services

*   **ReminderCommandService & ReminderCommandServiceImpl:**
    *   `handle(ScheduleReminderCommand command): Result<Reminder, ApplicationError>`: Construye y persiste `Reminder` en estado `SCHEDULED`.
    *   `handle(IssueReminderCommand command): Result<Reminder, ApplicationError>`: Recupera el agregado, consulta `ReminderIssuancePolicy` y aplica el resultado mediante `issue()`.
    *   `handle(ConfirmReminderCommand command): Result<Reminder, ApplicationError>`: Confirma el recordatorio si su estado lo permite.
    *   `handle(CancelReminderCommand command): Result<Reminder, ApplicationError>`: Cancela el recordatorio.
    *   `handle(ReissueReminderCommand command): Result<Reminder, ApplicationError>`: Reemite el recordatorio de medicación.
*   **SleepCycleRecordCommandService & SleepCycleRecordCommandServiceImpl:**
    *   `handle(RecordSleepCycleCommand command): Result<SleepCycleRecord, ApplicationError>`: Construye y persiste el ciclo de sueño clasificado.
*   **ActivityMonitorCommandService & ActivityMonitorCommandServiceImpl:**
    *   `handle(RecordProlongedInactivityCommand command): Result<ActivityMonitor, ApplicationError>`.
    *   `handle(RecordActivityResumedCommand command): Result<ActivityMonitor, ApplicationError>`.
*   **MedicationStockCommandService & MedicationStockCommandServiceImpl:**
    *   `handle(SuggestMedicationRestockCommand command): Result<Void, ApplicationError>`: Evalúa `MedicationStockPolicy` y registra la sugerencia.
    *   `handle(ConfirmMedicationAcquisitionCommand command): Result<MedicationStock, ApplicationError>`: Actualiza el balance tras la adquisición.

##### Query Services

*   **ReminderQueryService & ReminderQueryServiceImpl:** Resuelve `GetReminderStatusByIdQuery` y `GetRemindersByPersonUnderCareIdQuery`.
*   **MedicationStockQueryService & MedicationStockQueryServiceImpl:** Resuelve `GetMedicationStockStatusQuery`.

##### Event Handlers

*   `ReminderConfirmedEventHandler`: Reacciona a `ReminderConfirmedEvent` cuando `type == MEDICATION`, registrando el consumo correspondiente en `MedicationStock` y evaluando `MedicationStockPolicy`.
*   `ProlongedInactivityDetectedEventHandler`: Reacciona a `ProlongedInactivityDetectedEvent` (interno) republicándolo como `ProlongedInactivityDetectedIntegrationEvent` hacia `Emergency & Alerting`.
*   `ReminderReissuedEventHandler`: Reacciona a `ReminderReissuedEvent` (interno) republicándolo como `ReminderReissuedIntegrationEvent` hacia `Emergency & Alerting`.
*   `MedicationRestockSuggestedEventHandler`: Reacciona a `MedicationRestockSuggestedEvent` (interno) republicándolo como `MedicationRestockSuggestedIntegrationEvent` hacia `Emergency & Alerting`.

#### 2.6.5.4. Infrastructure Layer

Implementa la persistencia técnica en PostgreSQL, la comunicación con el broker MQTT del dispositivo wearable y los componentes de programación temporal que traducen las políticas de tiempo del dominio.

##### Persistence JPA Entities

*   `ReminderPersistenceEntity`: Mapea la tabla `reminders`. Columnas: `id`, `person_under_care_id`, `type`, `scheduled_time`, `issued_at`, `status`, `reissue_count`. Hereda campos de auditoría de `AuditableAbstractPersistenceEntity`.
*   `SleepCycleRecordPersistenceEntity`: Mapea la tabla `sleep_cycle_records`. Columnas: `id`, `person_under_care_id`, `start_time`, `end_time`, `interruption_count`, `classification`.
*   `ActivityMonitorPersistenceEntity`: Mapea la tabla `activity_monitors`. Columnas: `id`, `person_under_care_id`, `status`, `inactivity_since`.
*   `MedicationStockPersistenceEntity`: Mapea la tabla `medication_stocks`. Columnas: `id`, `person_under_care_id`, `remaining_doses`, `daily_consumption`, `last_acquisition_date`.

##### Spring Data Repositories & Adapters

*   `ReminderPersistenceRepository`: Extiende `JpaRepository<ReminderPersistenceEntity, UUID>`.
*   `SleepCycleRecordPersistenceRepository`: Extiende `JpaRepository<SleepCycleRecordPersistenceEntity, UUID>`.
*   `ActivityMonitorPersistenceRepository`: Extiende `JpaRepository<ActivityMonitorPersistenceEntity, UUID>`.
*   `MedicationStockPersistenceRepository`: Extiende `JpaRepository<MedicationStockPersistenceEntity, UUID>`.
*   `ReminderRepositoryImpl`: Implementa `ReminderRepository` usando `ReminderPersistenceAssembler` para traducir bidireccionalmente entre entidad JPA y aggregate.
*   `SleepCycleRecordRepositoryImpl`, `ActivityMonitorRepositoryImpl`, `MedicationStockRepositoryImpl`: Implementan sus respectivos puertos de dominio siguiendo el mismo patrón.

##### Persistence Assemblers

*   `ReminderPersistenceAssembler`: Traduce los tipos primitivos de `ReminderPersistenceEntity` hacia los Value Objects del aggregate (`ReminderType`, `ReminderStatus`, etc.) y recompone `Reminder`.
*   `SleepCycleRecordPersistenceAssembler`, `ActivityMonitorPersistenceAssembler`, `MedicationStockPersistenceAssembler`: Traducen entre su entidad JPA correspondiente y su aggregate de dominio.

##### Messaging

*   `WearableTelemetryBrokerAdapter`: Implementa la conexión técnica con el broker MQTT, suscribiéndose a los tópicos de telemetría de actividad/inactividad y de sueño, y entregando los mensajes a `ActivityTelemetryConsumer` y `SleepTelemetryConsumer` respectivamente.

##### Scheduling

*   `ReminderDueCheckScheduler`: Tarea periódica anotada con `@Scheduled(fixedDelay = 30000)` que consulta `ReminderRepository.findDueForIssuance(Instant.now())` e invoca `IssueReminderCommand` por cada resultado.
*   `ReminderReissueScheduler`: Tarea periódica anotada con `@Scheduled(fixedDelay = 60000)` que consulta `ReminderRepository.findOverdueForReissue(Instant.now())` e invoca `ReissueReminderCommand` por cada resultado.

#### 2.6.5.5. Bounded Context Software Architecture Component Level Diagrams

La Figura 2.57 presenta las cuatro capas del Bounded Context **Care Routines & Wellness**, su relación con la aplicación móvil y con el firmware del wearable, y los eventos de integración que publica hacia Emergency & Alerting.

<a id="figura-2-57"></a>**Figura 2.57.** Diagrama de componentes del Bounded Context Care Routines & Wellness

![Care Routines & Wellness Component Diagram](../assets/images/chapterII/tactical-level-domain-driven-desing/care-routines-and-wellness-bc/care-routines-and-wellness-component.png)

#### 2.6.5.6. Bounded Context Software Architecture Code Level Diagrams

En esta sección se presenta la estructura interna del Bounded Context **Care Routines & Wellness** a nivel de código, mediante el diagrama de clases de su Domain Layer y el diseño de su base de datos.

##### 2.6.5.6.1. Bounded Context Domain Layer Class Diagrams

El diagrama UML de la Figura 2.58 presenta la Domain Layer de **Care Routines & Wellness**, con los agregados `Reminder`, `SleepCycleRecord`, `ActivityMonitor` y `MedicationStock`, sus Value Objects y los Domain Services que aplican las políticas de emisión y reemisión de recordatorios y de stock de medicamentos.

<a id="figura-2-58"></a>**Figura 2.58.** Diagrama de clases de la Domain Layer de Care Routines & Wellness

![Care Routines & Wellness Domain Class Diagram](../assets/images/chapterII/tactical-level-domain-driven-desing/care-routines-and-wellness-bc/care-routines-and-welness.svg)

##### 2.6.5.6.2. Bounded Context Database Design Diagram

La Figura 2.59 presenta el diseño de persistencia del Bounded Context **Care Routines & Wellness**, derivado directamente de sus agregados: `reminders` conserva el ciclo de vida de cada recordatorio junto con su contador de reemisiones, `sleep_cycle_records` almacena cada ciclo de sueño cerrado con su clasificación, `activity_monitors` mantiene un único registro de actividad por persona bajo cuidado y `medication_stocks` el balance de dosis restantes que alimenta la sugerencia de reabastecimiento.

Las columnas `person_under_care_id` y `wearable_device_id` referencian, respectivamente, los perfiles gobernados por el Bounded Context Profile y los dispositivos gobernados por Health Monitoring, de modo que la telemetría registrada mantiene su trazabilidad hacia el dispositivo que la originó sin que este contexto administre ninguna de las dos entidades.

<a id="figura-2-59"></a>**Figura 2.59.** Diagrama de base de datos de Care Routines & Wellness

![Care Routines & Wellness Database Design Diagram](../assets/images/chapterII/databaseDiagrams/care-routines-and-wellnes-db-diagram.png)

### 2.6.6. Bounded Context: Mobility & Geofencing

El Bounded Context **Mobility & Geofencing** pertenece al Supporting Domain de Guardian+. Su responsabilidad consiste en gestionar el seguimiento de ubicación de un Fragile Citizen, administrar las Safe Zones configuradas y evaluar las ubicaciones recibidas para determinar si la persona permanece dentro de una zona segura o si se ha producido una Safe Zone Violation.

Este contexto recibe la ubicación del Wearable Device, valida las coordenadas, mantiene el estado de ubicación y publica el evento de integración `SafeZoneViolation` cuando detecta una salida de la zona segura, que Emergency & Alerting consume para gestionar la respuesta y el escalamiento. A diferencia de Health Monitoring, no interpreta signos vitales, y su responsabilidad termina en la detección y el registro de los eventos de ubicación.

La arquitectura táctica se implementa sobre Java y Spring Boot con una estructura de paquetes dividida en cuatro capas: domain, interfaces, application e infrastructure. Su código se organiza en el paquete `com.healthify.guardian.platform.mobilitygeofencing` del repositorio `guardian-plus-platform`, con la siguiente estructura:

```
com.healthify.guardian.platform.mobilitygeofencing/
├── domain/
│   ├── model/
│   │   ├── aggregates/
│   │   ├── commands/
│   │   ├── entities/
│   │   ├── events/
│   │   ├── queries/
│   │   └── valueobjects/
│   ├── repositories/
│   └── services/
├── interfaces/
│   ├── events/
│   ├── rest/
│   │   ├── controllers/
│   │   ├── resources/
│   │   └── transform/
│   └── transform/
├── application/
│   ├── internal/
│   │   ├── commandservices/
│   │   └── queryservices/
│   └── ports/
│       └── inbound/
└── infrastructure/
    ├── persistence/
    │   └── jpa/
    │       ├── adapters/
    │       ├── assemblers/
    │       ├── entities/
    │       └── repositories/
    └── publisher/
```

#### 2.6.6.1. Domain Layer

Encapsula la lógica pura del dominio de movilidad y geocercas, las reglas de configuración de zonas seguras y la evaluación de las ubicaciones recibidas desde el dispositivo wearable. El dominio determina si una ubicación se encuentra dentro o fuera de una SafeZone y registra una violación cuando corresponde, sin asumir responsabilidades propias de Emergency & Alerting, como la generación de alertas, escalamiento o gestión de incidentes.

##### Aggregates

*   **SafeZone**
    *   Agregado raíz que representa una zona geográfica segura configurada para un Fragile Citizen.
    *   Mantiene las reglas y límites necesarios para determinar si una ubicación pertenece a la zona.
    *   Es responsable de preservar la consistencia de la configuración de la zona, incluyendo su estado activo.
    *   *Atributos:*
        *   id: SafeZoneId
        *   fragileCitizenId: FragileCitizenId
        *   name: String
        *   boundary: SafeZoneBoundary
        *   status: SafeZoneStatus
        *   createdAt: Instant
        *   updatedAt: Instant
    *   *Métodos:*
        *   SafeZone(CreateSafeZoneCommand command)
        *   updateBoundary(SafeZoneBoundary boundary): void
        *   activate(): void
        *   deactivate(): void
        *   contains(Location location): boolean
        *   isActive(): boolean

*   **LocationTracking**
    *   Agregado raíz que representa el registro de seguimiento de ubicación de un Fragile Citizen.
    *   Cada ubicación recibida se procesa y conserva como parte del historial de seguimiento, evitando que el agregado SafeZone tenga que mantener una colección potencialmente ilimitada de ubicaciones.
    *   *Atributos:*
        *   id: LocationTrackingId
        *   fragileCitizenId: FragileCitizenId
        *   currentLocation: Location
        *   currentStatus: LocationStatus
        *   lastUpdatedAt: Instant
    *   *Métodos:*
        *   LocationTracking(FragileCitizenId fragileCitizenId)
        *   recordLocation(Location location, LocationStatus status): void
        *   getCurrentLocation(): Location
        *   getCurrentStatus(): LocationStatus

##### Entities

*   **ZoneViolation**
    *   Entidad que representa el registro de una ubicación que fue determinada como externa a una SafeZone activa.
    *   Su propósito es conservar la ocurrencia de la violación dentro del contexto de movilidad. La generación y gestión de la alerta correspondiente pertenece a Emergency & Alerting.
    *   *Atributos:*
        *   id: ZoneViolationId
        *   safeZoneId: SafeZoneId
        *   fragileCitizenId: FragileCitizenId
        *   location: Location
        *   detectedAt: Instant
    *   *Métodos:*
        *   ZoneViolation(SafeZoneId safeZoneId, FragileCitizenId fragileCitizenId, Location location)
        *   getLocation(): Location
        *   getDetectedAt(): Instant

##### Value Objects

*   **Coordinates:** Encapsula las coordenadas geográficas de una ubicación (latitude: Double, longitude: Double). Invariante: latitud entre $-90.0$ y $90.0$, longitud entre $-180.0$ y $180.0$. Método: isValid().
*   **Location:** Representa una ubicación capturada por el wearable (coordinates: Coordinates, recordedAt: Instant, accuracyInMeters: Double). Es inmutable y representa el valor recibido para un instante determinado.
*   **SafeZoneBoundary:** Encapsula los límites geográficos de una SafeZone mediante un centro y un radio (center: Coordinates, radiusInMeters: Double). Invariante: radio mayor que 0. Método: contains(Coordinates coordinates).
*   **LocationStatus:** Representa el resultado de la evaluación de una ubicación respecto a una zona segura. Valores: WITHIN_SAFE_ZONE, OUTSIDE_SAFE_ZONE.
*   **SafeZoneStatus:** Representa el estado de una zona segura. Valores: ACTIVE, INACTIVE.
*   **SafeZoneId:** Identificador inmutable de una zona segura, basado en UUID.
*   **LocationTrackingId:** Identificador inmutable del agregado de seguimiento, basado en UUID.
*   **ZoneViolationId:** Identificador inmutable de una violación de zona, basado en UUID.
*   **FragileCitizenId:** Identificador de referencia inmutable del Fragile Citizen monitoreado.

##### Domain Services

*   **GeofenceEvaluationService**
    *   Servicio de dominio encargado de evaluar una ubicación contra los límites de una SafeZone.
    *   Se utiliza porque la evaluación geográfica no representa una responsabilidad exclusiva de una única entidad y requiere aplicar una regla espacial del dominio.
    *   *Métodos:*
        *   evaluate(Location location, SafeZoneBoundary boundary): LocationStatus
        *   isInside(Location location, SafeZoneBoundary boundary): boolean

##### Commands & Queries (Domain Model)

*   CreateSafeZoneCommand(UUID fragileCitizenId, String name, Coordinates center, Double radiusInMeters)
*   UpdateSafeZoneCommand(UUID safeZoneId, String name, Coordinates center, Double radiusInMeters)
*   ActivateSafeZoneCommand(UUID safeZoneId)
*   DeactivateSafeZoneCommand(UUID safeZoneId)
*   ReceiveLocationCommand(UUID fragileCitizenId, Coordinates coordinates, Double accuracyInMeters, Instant recordedAt)
*   EvaluateLocationCommand(UUID fragileCitizenId, UUID locationTrackingId)
*   GetCurrentLocationQuery(FragileCitizenId fragileCitizenId)
*   GetLocationHistoryQuery(FragileCitizenId fragileCitizenId, Instant periodStart, Instant periodEnd)
*   GetActiveSafeZoneQuery(FragileCitizenId fragileCitizenId)
*   GetLocationStatusQuery(FragileCitizenId fragileCitizenId)

##### Domain Events

*   SafeZoneCreatedEvent: Emitido después de crear correctamente una nueva SafeZone.
*   LocationReceivedEvent: Emitido después de validar y registrar una ubicación proveniente del wearable.
*   LocationStatusUpdatedEvent: Emitido después de evaluar una ubicación y determinar su estado respecto a la SafeZone.
*   SafeZoneViolationDetectedEvent: Emitido cuando una ubicación válida es evaluada como OUTSIDE_SAFE_ZONE. Este evento puede ser publicado hacia Emergency & Alerting, que se encarga de iniciar el flujo correspondiente de alertamiento.

##### Repositories (Domain Interfaces)

*   **SafeZoneRepository:**
    *   save(SafeZone safeZone): SafeZone
    *   findById(SafeZoneId id): Optional<SafeZone>
    *   findActiveByFragileCitizenId(FragileCitizenId citizenId): Optional<SafeZone>
    *   findAllByFragileCitizenId(FragileCitizenId citizenId): List<SafeZone>
*   **LocationTrackingRepository:**
    *   save(LocationTracking tracking): LocationTracking
    *   findByFragileCitizenId(FragileCitizenId citizenId): Optional<LocationTracking>
    *   findHistoryByFragileCitizenId(FragileCitizenId citizenId, Instant periodStart, Instant periodEnd): List<Location>
*   **ZoneViolationRepository:**
    *   save(ZoneViolation violation): ZoneViolation
    *   findByFragileCitizenId(FragileCitizenId citizenId): List<ZoneViolation>
    *   findBySafeZoneId(SafeZoneId safeZoneId): List<ZoneViolation>

#### 2.6.6.2. Interface Layer

Expone las capacidades del Bounded Context Mobility & Geofencing hacia clientes externos y sistemas con los que se integra. Esta capa transforma las solicitudes externas en comandos del dominio y adapta los eventos de dominio para su publicación hacia otros contextos, sin contener reglas propias de negocio.

##### REST Controllers

*   **SafeZoneController**
    *   Expone las operaciones relacionadas con la administración de SafeZone.
    *   Permite crear, actualizar, activar y desactivar zonas seguras.
    *   *Endpoints:*
        *   `POST /api/v1/safe-zones`
        *   `PUT /api/v1/safe-zones/{safeZoneId}`
        *   `PATCH /api/v1/safe-zones/{safeZoneId}/activate`
        *   `PATCH /api/v1/safe-zones/{safeZoneId}/deactivate`
        *   `GET /api/v1/safe-zones/fragile-citizen/{fragileCitizenId}/active`

*   **LocationTrackingController**
    *   Expone las operaciones relacionadas con la consulta del seguimiento de ubicación.
    *   Permite consultar la ubicación actual, el estado actual y el historial de ubicaciones de un Fragile Citizen.
    *   *Endpoints:*
        *   `GET /api/v1/location-tracking/{fragileCitizenId}/current`
        *   `GET /api/v1/location-tracking/{fragileCitizenId}/status`
        *   `GET /api/v1/location-tracking/{fragileCitizenId}/history`

##### Inbound Adapters (Wearable Integration)

*   **WearableLocationConsumer**
    *   Adaptador de entrada responsable de recibir las ubicaciones enviadas por el Wearable Device.
    *   Convierte el mensaje externo del dispositivo en un `ReceiveLocationCommand`.
    *   No realiza directamente la evaluación de la geocerca; delega el procesamiento al Application Layer.
    *   *Métodos:*
        *   consumeLocation(WearableLocationMessage message): void
        *   toCommand(WearableLocationMessage message): ReceiveLocationCommand

*   **WearableLocationMessage**
    *   Representa el mensaje externo recibido desde el dispositivo wearable.
    *   *Atributos:*
        *   fragileCitizenId: UUID
        *   latitude: Double
        *   longitude: Double
        *   accuracyInMeters: Double
        *   recordedAt: Instant

##### REST Resources

*   **SafeZoneResource**
    *   Representa la respuesta HTTP asociada a una SafeZone.
    *   *Atributos:*
        *   id: UUID
        *   fragileCitizenId: UUID
        *   name: String
        *   latitude: Double
        *   longitude: Double
        *   radiusInMeters: Double
        *   status: String

*   **CurrentLocationResource**
    *   Representa la ubicación actual del Fragile Citizen.
    *   *Atributos:*
        *   fragileCitizenId: UUID
        *   latitude: Double
        *   longitude: Double
        *   accuracyInMeters: Double
        *   status: String
        *   recordedAt: Instant

*   **LocationHistoryResource**
    *   Representa un elemento individual del historial de ubicaciones.
    *   *Atributos:*
        *   latitude: Double
        *   longitude: Double
        *   accuracyInMeters: Double
        *   status: String
        *   recordedAt: Instant

##### Transformers & Assemblers

*   **SafeZoneResourceAssembler**
    *   Transforma entidades del dominio SafeZone en `SafeZoneResource` para respuestas REST.
    *   *Métodos:*
        *   toResource(SafeZone safeZone): SafeZoneResource

*   **LocationResourceAssembler**
    *   Transforma objetos del dominio Location y LocationTracking en recursos REST.
    *   *Métodos:*
        *   toCurrentResource(LocationTracking tracking): CurrentLocationResource
        *   toHistoryResource(Location location): LocationHistoryResource

*   **WearableLocationTransformer**
    *   Convierte la carga útil del wearable en el comando ejecutable por el Application Layer.
    *   *Métodos:*
        *   toCommand(WearableLocationMessage message): ReceiveLocationCommand

##### Outbound Adapters (Event Publishers)

*   **MobilityEventPublisher**
    *   Adaptador de salida responsable de publicar eventos de integración hacia otros Bounded Contexts.
    *   Publica principalmente `SafeZoneViolationDetectedEvent` hacia Emergency & Alerting.
    *   No crea ni gestiona alertas; únicamente comunica el hecho ocurrido en Mobility & Geofencing.
    *   *Métodos:*
        *   publish(SafeZoneViolationDetectedEvent event): void

##### Responsabilidades de la Interface Layer

*   Recibir solicitudes HTTP provenientes de clientes autorizados.
*   Recibir mensajes de telemetría de ubicación provenientes del Wearable Device.
*   Validar el formato y estructura básica de los datos de entrada.
*   Transformar DTOs y mensajes externos en comandos de aplicación.
*   Transformar resultados del dominio en recursos de respuesta normalizados.
*   Publicar eventos de integración hacia otros Bounded Contexts.
*   Mantener desacoplada la infraestructura de transporte respecto a la lógica de negocio del dominio.

#### 2.6.6.3. Application Layer

Orquesta los casos de uso del Bounded Context Mobility & Geofencing, coordinando comandos, consultas, agregados, repositorios y eventos de dominio. Esta capa define los flujos de aplicación, pero delega las reglas de negocio y las invariantes al Domain Layer.

##### Command Services

*   **SafeZoneCommandService**
    *   Coordina los casos de uso relacionados con la administración del ciclo de vida de SafeZone.
    *   *Métodos:*
        *   createSafeZone(CreateSafeZoneCommand command): SafeZone
        *   updateSafeZone(UpdateSafeZoneCommand command): SafeZone
        *   activateSafeZone(ActivateSafeZoneCommand command): void
        *   deactivateSafeZone(DeactivateSafeZoneCommand command): void

*   **LocationTrackingCommandService**
    *   Coordina la recepción y procesamiento de las ubicaciones provenientes del wearable.
    *   Utiliza `GeofenceEvaluationService` para determinar si la ubicación se encuentra dentro o fuera de la zona segura.
    *   Cuando se detecta una salida de la zona, coordina el registro de la `ZoneViolation` y la publicación del evento correspondiente.
    *   *Métodos:*
        *   receiveLocation(ReceiveLocationCommand command): void
        *   evaluateLocation(EvaluateLocationCommand command): LocationStatus

##### Query Services

*   **SafeZoneQueryService**
    *   Proporciona consultas de solo lectura relacionadas con las zonas seguras configuradas.
    *   *Métodos:*
        *   getActiveSafeZone(GetActiveSafeZoneQuery query): Optional<SafeZone>
        *   getSafeZonesByFragileCitizen(FragileCitizenId fragileCitizenId): List<SafeZone>

*   **LocationTrackingQueryService**
    *   Proporciona información de seguimiento sin modificar el estado del dominio.
    *   *Métodos:*
        *   getCurrentLocation(GetCurrentLocationQuery query): Optional<Location>
        *   getLocationHistory(GetLocationHistoryQuery query): List<Location>
        *   getLocationStatus(GetLocationStatusQuery query): Optional<LocationStatus>

##### Command Handlers

*   **CreateSafeZoneCommandHandler**
    *   Recibe `CreateSafeZoneCommand` y delega la creación al `SafeZoneCommandService`.
*   **UpdateSafeZoneCommandHandler**
    *   Procesa `UpdateSafeZoneCommand` y coordina la actualización de los límites de una zona existente.
*   **ActivateSafeZoneCommandHandler**
    *   Procesa `ActivateSafeZoneCommand` y activa la zona segura correspondiente.
*   **DeactivateSafeZoneCommandHandler**
    *   Procesa `DeactivateSafeZoneCommand` y desactiva la zona segura correspondiente.
*   **ReceiveLocationCommandHandler**
    *   Recibe `ReceiveLocationCommand` y valida que la ubicación pueda ser procesada.
    *   Obtiene la SafeZone activa del Fragile Citizen y coordina la evaluación espacial de la ubicación.
    *   Actualiza el seguimiento de ubicación (`LocationTracking`).
    *   Si la ubicación se encuentra fuera de la zona segura, coordina el registro de la `ZoneViolation`.

##### Event Handlers

*   **LocationReceivedEventHandler**
    *   Procesa `LocationReceivedEvent`.
    *   Coordina la evaluación de la ubicación recibida respecto a la SafeZone activa.
*   **LocationStatusUpdatedEventHandler**
    *   Procesa `LocationStatusUpdatedEvent`.
    *   Si el resultado es `OUTSIDE_SAFE_ZONE`, coordina el registro de la violación y la generación de `SafeZoneViolationDetectedEvent`.
*   **SafeZoneViolationDetectedEventHandler**
    *   Responsable de preparar la publicación del evento de integración hacia Emergency & Alerting a través del puerto de salida correspondiente.
    *   No genera una alerta ni determina su severidad; su responsabilidad se limita a comunicar que se detectó una violación de zona.

##### Internal Application Services

*   **LocationEvaluationApplicationService**
    *   Coordina el flujo de extremo a extremo en la evaluación de una ubicación:
        1. Recupera la SafeZone activa.
        2. Invoca el `GeofenceEvaluationService`.
        3. Actualiza el agregado `LocationTracking`.
        4. Registra una `ZoneViolation` cuando corresponde.
        5. Publica los eventos de dominio resultantes.
    *   *Flujo principal:*
        *   `ReceiveLocationCommand` $\rightarrow$ `LocationTrackingCommandService` $\rightarrow$ `SafeZoneRepository` $\rightarrow$ `GeofenceEvaluationService` $\rightarrow$ `LocationTrackingRepository` $\rightarrow$ `ZoneViolationRepository` $\rightarrow$ `SafeZoneViolationDetectedEvent`

##### Application Ports

*   **Inbound Ports:**
    *   **WearableLocationInputPort:** Puerto de entrada utilizado para recibir ubicaciones provenientes del adaptador del wearable.
        *   *Métodos:*
            *   receiveLocation(ReceiveLocationCommand command): void
*   **Outbound Ports:**
    *   **MobilityEventOutputPort:** Puerto de salida utilizado para publicar eventos de integración hacia otros Bounded Contexts.
        *   *Métodos:*
            *   publish(SafeZoneViolationDetectedEvent event): void

##### Responsabilidades de la Application Layer

*   Orquestar los casos de uso del Bounded Context.
*   Coordinar Commands, Queries y Domain Events.
*   Invocar los agregados y servicios del dominio.
*   Utilizar las interfaces de repositorio definidas en el Domain Layer.
*   Coordinar la recepción y evaluación de ubicaciones.
*   Coordinar el registro de `ZoneViolation`.
*   Publicar `SafeZoneViolationDetectedEvent` hacia Emergency & Alerting.
*   Mantener la lógica de negocio compleja fuera de esta capa.
*   No gestionar alertas, incidentes, severidad ni escalamiento, ya que esas responsabilidades pertenecen a Emergency & Alerting.

#### 2.6.6.4. Infrastructure Layer

Implementa los mecanismos técnicos que permiten persistir la información del Bounded Context Mobility & Geofencing, recibir ubicaciones desde el Wearable Device y publicar eventos hacia otros Bounded Contexts. Esta capa contiene las implementaciones concretas de los puertos definidos por las capas Domain y Application, sin introducir reglas de negocio propias.

##### Persistence Implementations (Repositories)

*   **SafeZoneRepositoryImpl**
    *   Implementación concreta de `SafeZoneRepository`.
    *   Utiliza Spring Data JPA para persistir y recuperar agregados `SafeZone`.
    *   *Métodos:*
        *   save(SafeZone safeZone): SafeZone
        *   findById(SafeZoneId id): Optional<SafeZone>
        *   findActiveByFragileCitizenId(FragileCitizenId citizenId): Optional<SafeZone>
        *   findAllByFragileCitizenId(FragileCitizenId citizenId): List<SafeZone>

*   **LocationTrackingRepositoryImpl**
    *   Implementación concreta de `LocationTrackingRepository`.
    *   Gestiona la persistencia del estado actual y el historial de ubicaciones.
    *   *Métodos:*
        *   save(LocationTracking tracking): LocationTracking
        *   findByFragileCitizenId(FragileCitizenId citizenId): Optional<LocationTracking>
        *   findHistoryByFragileCitizenId(FragileCitizenId citizenId, Instant periodStart, Instant periodEnd): List<Location>

*   **ZoneViolationRepositoryImpl**
    *   Implementación concreta de `ZoneViolationRepository`.
    *   Persiste las violaciones de zonas seguras detectadas por el dominio.
    *   *Métodos:*
        *   save(ZoneViolation violation): ZoneViolation
        *   findByFragileCitizenId(FragileCitizenId citizenId): List<ZoneViolation>
        *   findBySafeZoneId(SafeZoneId safeZoneId): List<ZoneViolation>

##### JPA Entities

*   **SafeZoneJpaEntity**
    *   Representación persistente del agregado SafeZone en base de datos relacional.
    *   *Atributos:*
        *   id: UUID
        *   fragileCitizenId: UUID
        *   name: String
        *   latitude: Double
        *   longitude: Double
        *   radiusInMeters: Double
        *   status: String
        *   createdAt: Instant
        *   updatedAt: Instant

*   **LocationTrackingJpaEntity**
    *   Representación persistente del seguimiento actual de un Fragile Citizen.
    *   *Atributos:*
        *   id: UUID
        *   fragileCitizenId: UUID
        *   currentLatitude: Double
        *   currentLongitude: Double
        *   accuracyInMeters: Double
        *   currentStatus: String
        *   lastUpdatedAt: Instant

*   **LocationRecordJpaEntity**
    *   Representa un registro individual e inmutable del historial de ubicaciones.
    *   *Atributos:*
        *   id: UUID
        *   locationTrackingId: UUID
        *   latitude: Double
        *   longitude: Double
        *   accuracyInMeters: Double
        *   status: String
        *   recordedAt: Instant

*   **ZoneViolationJpaEntity**
    *   Representación persistente de una violación de zona segura detectada.
    *   *Atributos:*
        *   id: UUID
        *   safeZoneId: UUID
        *   fragileCitizenId: UUID
        *   latitude: Double
        *   longitude: Double
        *   detectedAt: Instant

##### Spring Data JPA Repositories

*   **SafeZoneJpaRepository**
    *   Repositorio Spring Data utilizado por `SafeZoneRepositoryImpl`.
    *   *Métodos:*
        *   findById(UUID id)
        *   findByFragileCitizenIdAndStatus(UUID fragileCitizenId, String status)
        *   findAllByFragileCitizenId(UUID fragileCitizenId)

*   **LocationTrackingJpaRepository**
    *   Repositorio Spring Data utilizado para acceder al seguimiento actual.
    *   *Métodos:*
        *   findByFragileCitizenId(UUID fragileCitizenId)

*   **LocationRecordJpaRepository**
    *   Repositorio Spring Data utilizado para consultar el historial de telemetría de ubicaciones.
    *   *Métodos:*
        *   findByLocationTrackingIdAndRecordedAtBetween(UUID trackingId, Instant start, Instant end)

*   **ZoneViolationJpaRepository**
    *   Repositorio Spring Data utilizado para consultar las violaciones registradas.
    *   *Métodos:*
        *   findByFragileCitizenId(UUID fragileCitizenId)
        *   findBySafeZoneId(UUID safeZoneId)

##### Assemblers & Converters

*   **SafeZonePersistenceAssembler**
    *   Convierte bidireccionalmente entre el agregado de dominio `SafeZone` y `SafeZoneJpaEntity`.
    *   *Métodos:*
        *   toEntity(SafeZone safeZone): SafeZoneJpaEntity
        *   toDomain(SafeZoneJpaEntity entity): SafeZone

*   **LocationTrackingPersistenceAssembler**
    *   Convierte bidireccionalmente entre `LocationTracking` y `LocationTrackingJpaEntity`.
    *   *Métodos:*
        *   toEntity(LocationTracking tracking): LocationTrackingJpaEntity
        *   toDomain(LocationTrackingJpaEntity entity): LocationTracking

*   **ZoneViolationPersistenceAssembler**
    *   Convierte bidireccionalmente entre `ZoneViolation` y `ZoneViolationJpaEntity`.
    *   *Métodos:*
        *   toEntity(ZoneViolation violation): ZoneViolationJpaEntity
        *   toDomain(ZoneViolationJpaEntity entity): ZoneViolation

*   **CoordinatesConverter**
    *   Convierte el Value Object `Coordinates` a los campos persistentes `latitude` y `longitude`, y viceversa.

##### Inbound Infrastructure Adapters

*   **WearableLocationAdapter**
    *   Implementa el mecanismo técnico utilizado para recibir las ubicaciones provenientes del Wearable Device (mediante HTTP, MQTT u otro protocolo IoT).
    *   Convierte el mensaje externo recibido en `WearableLocationMessage` y lo entrega al `WearableLocationInputPort`.
    *   No contiene lógica de evaluación de geocercas.

##### Outbound Infrastructure Adapters (Messaging)

*   **MobilityEventPublisherAdapter**
    *   Implementa el puerto de salida `MobilityEventOutputPort`.
    *   Publica eventos de integración mediante el mecanismo de mensajería (Message Broker: RabbitMQ/Kafka).
    *   Publica principalmente `SafeZoneViolationDetectedEvent` hacia Emergency & Alerting.
    *   *Métodos:*
        *   publish(SafeZoneViolationDetectedEvent event): void

*   **SafeZoneViolationIntegrationEvent**
    *   Representación serializable del evento de integración enviado fuera del Bounded Context.
    *   *Atributos:*
        *   eventId: UUID
        *   fragileCitizenId: UUID
        *   safeZoneId: UUID
        *   latitude: Double
        *   longitude: Double
        *   detectedAt: Instant

##### Infrastructure Configuration

*   **MobilityPersistenceConfiguration:** Configura los componentes de persistencia JPA, conexiones al pool de base de datos y gestión de transacciones.
*   **MobilityMessagingConfiguration:** Configura el broker de mensajería, exchanges/topics, serialización JSON y canales de publicación de eventos.
*   **WearableIntegrationConfiguration:** Configura el conector y los endpoints del protocolo técnico de comunicación con el Wearable Device.

##### Responsabilidades de la Infrastructure Layer

*   Implementar técnicamente los repositorios definidos por el Domain Layer.
*   Persistir de forma consistente `SafeZone`, `LocationTracking`, `LocationRecord` y `ZoneViolation`.
*   Implementar la capa técnica de transporte y comunicación con el Wearable Device.
*   Publicar eventos de integración hacia el broker para el consumo de Emergency & Alerting.
*   Configurar los beans de Spring para JPA, base de datos y mensajería asíncrona.
*   Transformar objetos de dominio a entidades de persistencia y viceversa (aislando la base de datos).
*   Mantener los detalles tecnológicos y dependencias de frameworks fuera del Domain y Application Layer.
*   No implementar reglas de negocio como la evaluación de geocercas o la determinación de violaciones; estas responsabilidades pertenecen estrictamente al Domain Layer.

#### 2.6.6.5. Bounded Context Software Architecture Component Level Diagrams

La Figura 2.60 presenta los componentes del Bounded Context **Mobility & Geofencing**: el consumidor de ubicación del wearable y los controladores REST en la Interface Layer; los servicios de comandos y consultas en la Application Layer; los agregados `SafeZone` y `LocationTracking`, la entidad `ZoneViolation` y el servicio de evaluación de geocercas en la Domain Layer; y los adaptadores de persistencia, la ACL hacia Profile y el publicador de eventos en la Infrastructure Layer.

<a id="figura-2-60"></a>**Figura 2.60.** Diagrama de componentes del Bounded Context Mobility & Geofencing

![Mobility & Geofencing Component Diagram](../assets/images/chapterII/c4-diagrams/MobilityandGeofencing.png)

#### 2.6.6.6. Bounded Context Software Architecture Code Level Diagrams

En esta sección se presenta la estructura interna del Bounded Context **Mobility & Geofencing** a nivel de código, mediante el diagrama de clases de su Domain Layer y el diseño de su base de datos.

##### 2.6.6.6.1. Bounded Context Domain Layer Class Diagrams

El diagrama UML de la Figura 2.61 presenta la Domain Layer del Bounded Context **Mobility & Geofencing**, organizada alrededor de los agregados `SafeZone` y `LocationTracking`, la entidad `ZoneViolation` y el Domain Service `GeofenceEvaluationService`, que concentra la regla espacial de evaluación de una ubicación contra los límites de una zona segura.

<a id="figura-2-61"></a>**Figura 2.61.** Diagrama de clases de la Domain Layer de Mobility & Geofencing

![Mobility & Geofencing Domain Class Diagram](../assets/images/chapterII/classDiagrams/geofecingDomainLayerClassDiagram.png)

##### 2.6.6.6.2. Bounded Context Database Design Diagram

La Figura 2.62 presenta el diseño de persistencia del Bounded Context **Mobility & Geofencing**, derivado de sus agregados: `safe_zones` guarda la configuración de cada zona segura con su centro y radio, `location_trackings` mantiene el estado de ubicación vigente de un Fragile Citizen, `location_records` conserva el historial inmutable de ubicaciones recibidas y `zone_violations` registra cada evaluación que resultó externa a una zona segura activa.

Las columnas `fragile_citizen_id` y `wearable_device_id` referencian los perfiles gobernados por el Bounded Context Profile y los dispositivos gobernados por Health Monitoring. La resolución de una violación no se persiste en este contexto: su responsabilidad termina en la detección y el registro, mientras que la atención y el cierre pertenecen a Emergency & Alerting.

<a id="figura-2-62"></a>**Figura 2.62.** Diagrama de base de datos de Mobility & Geofencing

![Mobility & Geofencing Database Design Diagram](../assets/images/chapterII/databaseDiagrams/mobility-and-geofencing-db-diagram.png)

### 2.6.7. Bounded Context: IAM

El Bounded Context **IAM** pertenece al Generic Domain de Guardian+. Su responsabilidad consiste en gestionar la identidad digital de cuidadores y familiares: el registro y la verificación de credenciales mediante correo electrónico, la autenticación reforzada con un segundo factor opcional (OTP) y la recuperación segura de la contraseña.

A diferencia de los demás contextos, IAM no consume eventos de integración de ningún otro Bounded Context: es el contexto más upstream del dominio y actúa como Open Host Service (OHS), publicando un Published Language (PL) basado en JSON Web Tokens (JWT) firmados que cada contexto descendente valida localmente, sin consultar la base de datos de identidad.

La arquitectura táctica se diseñó sobre Java y Spring Boot con la misma estructura de paquetes de cuatro capas que el resto de Bounded Contexts: domain, interfaces, application e infrastructure. Su código se organizará en el paquete `com.healthify.guardian.platform.iam` del repositorio `guardian-plus-platform`, con la siguiente estructura:

```
com.healthify.guardian.platform.iam/
├── domain/
│   ├── model/
│   │   ├── aggregates/
│   │   ├── commands/
│   │   ├── events/
│   │   ├── queries/
│   │   ├── services/
│   │   └── valueobjects/
│   └── repositories/
├── interfaces/
│   ├── acl/
│   ├── events/
│   └── rest/
│       ├── controllers/
│       ├── resources/
│       └── transform/
├── application/
│   ├── acl/
│   ├── commandservices/
│   ├── internal/
│   │   ├── commandservices/
│   │   ├── eventhandlers/
│   │   └── queryservices/
│   └── queryservices/
└── infrastructure/
    ├── notifications/
    │   └── adapters/
    ├── persistence/
    │   └── jpa/
    │       ├── adapters/
    │       ├── assemblers/
    │       ├── converters/
    │       ├── entities/
    │       └── repositories/
    ├── scheduling/
    └── security/
        └── adapters/
```

#### 2.6.7.1. Domain Layer

Encapsula las reglas de identidad y acceso: la unicidad del correo electrónico, la obligatoriedad de verificación de la cuenta, la vigencia y el consumo de un solo uso de los códigos de segundo factor y de los tokens de recuperación de contraseña. Del Design-Level EventStorming se desprende una decisión de modelado central: los secretos de vida corta se separan de `UserAccount` en agregados propios (`OneTimePassword` y `PasswordResetToken`), ya que poseen un ciclo de vida independiente —emisión, vigencia, consumo— que no debe acoplarse a las invariantes permanentes de la cuenta. Esta separación es la que el diseño de base de datos refleja mediante las tablas `otp_codes` y `password_reset_tokens`.

Ninguno de los secretos se conserva en claro: el dominio almacena únicamente su hash (`code_hash` y `token_hash`), de modo que una filtración de la base de datos no permite reconstruir el código enviado al usuario.

##### Aggregates

*   **UserAccount**
    *   Agregado raíz que representa la identidad digital de un cuidador o familiar registrado en Guardian+.
    *   Hereda de `AbstractDomainAggregateRoot<UserAccount>` para registrar y publicar eventos de dominio.
    *   Gobierna de forma autónoma su ciclo de vida (`PENDING_EMAIL_VERIFICATION → ACTIVE`), rechazando la autenticación mientras el correo no haya sido verificado. El indicador `emailVerified` registra el hecho de la verificación y `status` gobierna la habilitación para autenticarse; la cuenta transiciona a `ACTIVE` únicamente cuando el correo queda verificado.
    *   El correo electrónico es la única credencial de identificación: la autenticación no admite nombre de usuario.
    *   *Atributos:*
        *   `id: UserAccountId`
        *   `email: Email`
        *   `passwordHash: HashedPassword`
        *   `emailVerified: Boolean`
        *   `twoFactorEnabled: Boolean`
        *   `status: UserAccountStatus`
        *   `createdAt: Instant`
        *   `updatedAt: Instant`
    *   *Métodos:*
        *   `UserAccount(RegisterUserCredentialsCommand command, HashedPassword passwordHash)`
        *   `confirmEmailVerification(): void`
        *   `validateCredentials(String rawPassword, PasswordHasher hasher): boolean`
        *   `changePassword(HashedPassword newPasswordHash): void`
        *   `enableTwoFactor(): void`
        *   `disableTwoFactor(): void`
        *   `requiresSecondFactor(): boolean`
        *   `canAuthenticate(): boolean`
        *   `isEmailVerified(): boolean`

*   **OneTimePassword**
    *   Agregado raíz que representa un código de un solo uso emitido hacia el correo del usuario, ya sea como segundo factor de un intento de login o como confirmación de la verificación de la cuenta. El propósito de la emisión se declara en `purpose`.
    *   Su estado no se persiste como columna: se deriva de `usedAt` y `expiresAt`, de modo que un código es utilizable únicamente mientras no haya sido consumido ni haya vencido.
    *   *Atributos:*
        *   `id: OtpId`
        *   `userAccountId: UserAccountId`
        *   `codeHash: HashedSecret`
        *   `purpose: OtpPurpose`
        *   `expiresAt: Instant`
        *   `usedAt: Instant`
        *   `createdAt: Instant`
    *   *Métodos:*
        *   `OneTimePassword(GenerateOtpCommand command, HashedSecret codeHash, Instant expiresAt)`
        *   `verify(String candidateCode, SecretHasher hasher, Instant now): boolean`
        *   `markAsUsed(Instant now): void`
        *   `isUsable(Instant now): boolean`
        *   `isExpired(Instant now): boolean`
        *   `isUsed(): boolean`

*   **PasswordResetToken**
    *   Agregado raíz que representa un token opaco de un solo uso emitido para restablecer la contraseña de una cuenta. Se modela como agregado propio porque una cuenta puede acumular varios tokens a lo largo del tiempo, cada uno con su vigencia y su consumo independiente.
    *   *Atributos:*
        *   `id: PasswordResetTokenId`
        *   `userAccountId: UserAccountId`
        *   `tokenHash: HashedSecret`
        *   `expiresAt: Instant`
        *   `usedAt: Instant`
        *   `createdAt: Instant`
    *   *Métodos:*
        *   `PasswordResetToken(RequestPasswordResetCommand command, UserAccountId userAccountId, HashedSecret tokenHash, Instant expiresAt)`
        *   `matches(String rawToken, SecretHasher hasher): boolean`
        *   `markAsUsed(Instant now): void`
        *   `isUsable(Instant now): boolean`
        *   `isExpired(Instant now): boolean`

Este contexto no requiere entidades internas: los tres agregados son de único nivel, sin objetos hijos con identidad propia.

##### Value Objects

*   **Email:** Encapsula el correo electrónico (`value: String`). Invariante: formato RFC 5322 válido. Método: `matches(String other)`.
*   **HashedPassword:** Encapsula el hash irreversible de la contraseña (`hash: String`). Nunca expone ni acepta la contraseña en texto plano fuera del `PasswordHasher`.
*   **HashedSecret:** Encapsula el hash irreversible de un secreto de vida corta (`hash: String`), utilizado tanto para los códigos OTP (`code_hash`) como para los tokens de recuperación (`token_hash`).
*   **UserAccountStatus:** Enum (`PENDING_EMAIL_VERIFICATION`, `ACTIVE`). Método: `canAuthenticate()`.
*   **OtpPurpose:** Enum (`LOGIN`, `EMAIL_VERIFICATION`) que declara para qué fue emitido un código de un solo uso.
*   **UserAccountId / OtpId / PasswordResetTokenId:** Identificadores inmutables tipo UUID.

##### Domain Services (Puertos)

*   **PasswordHasher:** `hash(String rawPassword): HashedPassword`; `matches(String rawPassword, HashedPassword hash): boolean`. Implementado en infraestructura mediante BCrypt.
*   **SecretGenerator:** `generateNumericCode(int digits): String`; `generateOpaqueToken(): String`. Genera los códigos OTP y los tokens de recuperación mediante un generador criptográficamente seguro.
*   **SecretHasher:** `hash(String rawSecret): HashedSecret`; `matches(String rawSecret, HashedSecret hash): boolean`. Permite verificar un código o token sin conservarlo en claro.

##### Commands & Queries (Domain Model)

*   `RegisterUserCredentialsCommand(String email, String rawPassword)`
*   `GenerateOtpCommand(UUID userAccountId, String purpose)`
*   `VerifyEmailCommand(UUID userAccountId, String code)`
*   `LoginCommand(String email, String rawPassword)`
*   `VerifyOtpCommand(UUID userAccountId, String code)`
*   `AuthenticateUserCommand(UUID userAccountId)`
*   `EnableTwoFactorCommand(UUID userAccountId)`
*   `DisableTwoFactorCommand(UUID userAccountId)`
*   `RequestPasswordResetCommand(String email)`
*   `ResetPasswordCommand(String token, String newRawPassword)`
*   `GetUserAccountByIdQuery(UserAccountId userAccountId)`
*   `GetUserAccountByEmailQuery(Email email)`
*   `GetEmailAvailabilityQuery(String email)`
*   `GetUsableOtpByUserAccountIdAndPurposeQuery(UserAccountId userAccountId, OtpPurpose purpose)`

##### Domain Events

*   `UserCredentialsRegisteredEvent`: Emitido al registrar exitosamente las credenciales, con la cuenta en estado `PENDING_EMAIL_VERIFICATION`.
*   `OtpGeneratedEvent`: Emitido tras emitir un código de un solo uso, portando su propósito y su vencimiento; el código en claro viaja únicamente hacia el adaptador de notificaciones y nunca se persiste.
*   `OtpVerifiedEvent`: Emitido cuando el código ingresado coincide con el hash almacenado dentro de la ventana de vigencia.
*   `EmailVerifiedEvent`: Emitido cuando el usuario confirma su correo con un código de propósito `EMAIL_VERIFICATION`; transiciona la cuenta a `ACTIVE`.
*   `CredentialsValidatedEvent`: Emitido cuando `Login` valida correctamente el correo y la contraseña.
*   `UserAuthenticatedEvent`: Emitido al concluir exitosamente el flujo de autenticación; dispara la emisión del JWT firmado.
*   `TwoFactorSettingChangedEvent`: Emitido al habilitar o deshabilitar el segundo factor de una cuenta.
*   `PasswordResetTokenIssuedEvent`: Emitido al emitir un token de recuperación de contraseña, portando su vencimiento.
*   `PasswordResetCompletedEvent`: Emitido al completar el cambio de contraseña con un token vigente, que queda consumido.

##### Repositories (Domain Interfaces)

*   **UserAccountRepository:**
    *   `save(UserAccount account): UserAccount`
    *   `findById(UserAccountId id): Optional<UserAccount>`
    *   `findByEmail(Email email): Optional<UserAccount>`
    *   `existsByEmail(Email email): boolean`
*   **OneTimePasswordRepository:**
    *   `save(OneTimePassword otp): OneTimePassword`
    *   `findById(OtpId id): Optional<OneTimePassword>`
    *   `findLatestUsableByUserAccountIdAndPurpose(UserAccountId userAccountId, OtpPurpose purpose, Instant now): Optional<OneTimePassword>`
    *   `deleteExpiredUnusedBefore(Instant threshold): int`
*   **PasswordResetTokenRepository:**
    *   `save(PasswordResetToken token): PasswordResetToken`
    *   `findById(PasswordResetTokenId id): Optional<PasswordResetToken>`
    *   `findUsableByTokenHash(HashedSecret tokenHash, Instant now): Optional<PasswordResetToken>`
    *   `deleteExpiredUnusedBefore(Instant threshold): int`

#### 2.6.7.2. Interface Layer

Traduce estímulos externos hacia comandos y consultas de aplicación y expone contratos HTTP RESTful para la app móvil. Al ser el contexto más upstream del dominio, no canaliza eventos de integración entrantes.

##### REST Controllers

*   **AuthController** (`/api/v1/auth`):
    *   `POST /register`: Registra nuevas credenciales de usuario.
    *   `POST /verify-email`: Confirma el correo electrónico mediante el código de propósito `EMAIL_VERIFICATION` enviado.
    *   `POST /verify-email/resend`: Reemite el código de verificación de correo.
    *   `POST /login`: Valida correo y contraseña y, si la cuenta tiene el segundo factor habilitado, dispara el desafío OTP.
    *   `POST /otp/verify`: Verifica el código OTP de propósito `LOGIN` y, de ser correcto, emite el JWT de sesión.
    *   `POST /password-reset/request`: Emite y envía el token de recuperación de contraseña.
    *   `POST /password-reset/confirm`: Establece la nueva contraseña a partir de un token vigente y no consumido.
*   **UserAccountsController** (`/api/v1/user-accounts`):
    *   `GET /{userAccountId}`: Recupera el detalle de una cuenta.
    *   `GET /availability`: Consulta la disponibilidad de un correo electrónico (`Email Available?`).
    *   `PUT /{userAccountId}/two-factor`: Habilita o deshabilita el segundo factor de autenticación de la cuenta.

##### Resources & Assemblers

*   *Resources (DTOs):* `RegisterUserCredentialsResource`, `VerifyEmailResource`, `LoginResource`, `VerifyOtpResource`, `TwoFactorSettingResource`, `RequestPasswordResetResource`, `ResetPasswordResource`, `UserAccountResource`, `AuthenticatedSessionResource`.
*   *Assemblers (Mappers):* `RegisterUserCredentialsCommandFromResourceAssembler`, `LoginCommandFromResourceAssembler`, `VerifyOtpCommandFromResourceAssembler`, `TwoFactorCommandFromResourceAssembler`, `UserAccountResourceFromEntityAssembler`, `AuthenticatedSessionResourceFromTokenAssembler`.

Los recursos de salida nunca exponen el hash de la contraseña ni el de un código o token: `UserAccountResource` publica únicamente el identificador, el correo, el estado, la verificación del correo y la habilitación del segundo factor.

##### Integration Events & ACL Facade

*   *Eventos publicados (outbound):*
    *   `UserAccountRegisteredIntegrationEvent`: Notifica a `Profile` el alta de una nueva identidad, mediante Event-Carried State Transfer, para la creación del perfil asociado.
    *   `UserAccountVerifiedIntegrationEvent`: Notifica la activación definitiva de la cuenta.
*   *Eventos consumidos (inbound):* Ninguno. IAM no depende de señales de negocio de otros contextos.
*   `IamContextFacade`: Interfaz expuesta para la validación síncrona de tokens y la consulta puntual de existencia de una `UserAccount` desde otros contextos, sin exponer el modelo interno de credenciales.

#### 2.6.7.3. Application Layer

Orquesta los flujos de registro, verificación, autenticación y recuperación de contraseña delegando las reglas de negocio en los agregados correspondientes. Los Event Handlers materializan directamente las policies identificadas en el Design-Level EventStorming.

##### Command Services

*   **UserAccountCommandService & UserAccountCommandServiceImpl:**
    *   `handle(RegisterUserCredentialsCommand command): Optional<UserAccount>`: Valida la disponibilidad del correo, aplica `PasswordHasher` y persiste el agregado en estado `PENDING_EMAIL_VERIFICATION`, con `emailVerified` en falso.
    *   `handle(VerifyEmailCommand command): void`: Recupera el código utilizable de propósito `EMAIL_VERIFICATION`, lo verifica contra su hash, lo marca como usado y transiciona la cuenta a `ACTIVE`.
    *   `handle(EnableTwoFactorCommand command): void` y `handle(DisableTwoFactorCommand command): void`: Modifican la exigencia del segundo factor de la cuenta.
    *   `handle(ResetPasswordCommand command): void`: Recupera el token utilizable por su hash, lo marca como usado y reemplaza el `HashedPassword` de la cuenta asociada.
*   **PasswordResetCommandService & PasswordResetCommandServiceImpl:**
    *   `handle(RequestPasswordResetCommand command): Optional<PasswordResetToken>`: Emite un token opaco mediante `SecretGenerator`, persiste únicamente su hash y publica `PasswordResetTokenIssuedEvent`. Si el correo no corresponde a ninguna cuenta, la operación no revela esa condición al solicitante.
*   **AuthenticationCommandService & AuthenticationCommandServiceImpl:**
    *   `handle(LoginCommand command): void`: Valida credenciales mediante `PasswordHasher.matches()`, verifica que la cuenta pueda autenticarse y publica `CredentialsValidatedEvent`.
    *   `handle(GenerateOtpCommand command): Optional<OneTimePassword>`: Construye y persiste el agregado `OneTimePassword` con el hash del código generado por `SecretGenerator`, según el propósito recibido.
    *   `handle(VerifyOtpCommand command): void`: Recupera el código utilizable del propósito `LOGIN` y lo verifica dentro de su vigencia, marcándolo como usado.
    *   `handle(AuthenticateUserCommand command): String`: Emite el JWT firmado con `UserId` y roles tras la validación exitosa del flujo de autenticación.

##### Query Services

*   **UserAccountQueryService & UserAccountQueryServiceImpl:** Resuelve `GetUserAccountByIdQuery`, `GetUserAccountByEmailQuery` y `GetEmailAvailabilityQuery`.
*   **OneTimePasswordQueryService & OneTimePasswordQueryServiceImpl:** Resuelve `GetUsableOtpByUserAccountIdAndPurposeQuery`.

##### Event Handlers

*   `UserCredentialsRegisteredEventHandler`: Implementa la policy **Mandatory Email Verification**. Despacha `GenerateOtpCommand` con propósito `EMAIL_VERIFICATION` tras el registro.
*   `CredentialsValidatedEventHandler`: Implementa la policy **Two-Factor OTP Authentication**. Si la cuenta tiene el segundo factor habilitado, despacha `GenerateOtpCommand` con propósito `LOGIN`; en caso contrario despacha directamente `AuthenticateUserCommand`.
*   `OtpGeneratedEventHandler`: Despacha el envío del código por correo mediante el adaptador de notificaciones, según el propósito de la emisión.
*   `OtpVerifiedEventHandler`: Despacha `AuthenticateUserCommand` cuando el propósito es `LOGIN`, cerrando el flujo de autenticación.
*   `EmailVerifiedEventHandler`: Publica `UserAccountVerifiedIntegrationEvent` hacia los contextos descendentes.
*   `PasswordResetTokenIssuedEventHandler`: Despacha el envío del correo con el enlace de recuperación, que porta el token en claro una única vez.

##### Application ACL Implementation

*   `IamContextFacadeImpl`: Implementa la fachada de acceso público del contexto (validación de tokens y existencia de cuentas).

#### 2.6.7.4. Infrastructure Layer

Implementa la persistencia técnica en PostgreSQL, el hashing de contraseñas, la firma/validación de JWT, la integración con el proveedor de correo electrónico y los componentes de programación temporal que sostienen la vigencia de tokens y códigos OTP.

##### Persistence JPA Entities

*   `UserAccountPersistenceEntity`: Mapea la tabla `user_accounts`. Columnas: `id`, `email` (única), `password_hash`, `email_verified`, `two_factor_enabled`, `status`, `created_at`, `updated_at`. Hereda campos de auditoría de `AuditableAbstractPersistenceEntity`.
*   `OneTimePasswordPersistenceEntity`: Mapea la tabla `otp_codes`. Columnas: `id`, `user_id`, `code_hash`, `purpose`, `expires_at`, `used_at`, `created_at`.
*   `PasswordResetTokenPersistenceEntity`: Mapea la tabla `password_reset_tokens`. Columnas: `id`, `user_id`, `token_hash`, `expires_at`, `used_at`, `created_at`.
*   *Converters:* `UserAccountStatusConverter` y `OtpPurposeConverter` traducen los enums de dominio hacia columnas `VARCHAR(30)`.

##### Spring Data Repositories & Adapters

*   `UserAccountPersistenceRepository`, `OneTimePasswordPersistenceRepository` y `PasswordResetTokenPersistenceRepository`: Extienden `JpaRepository<..., UUID>`.
*   `UserAccountRepositoryImpl`, `OneTimePasswordRepositoryImpl` y `PasswordResetTokenRepositoryImpl`: Implementan las interfaces de dominio usando los assemblers de persistencia para traducir bidireccionalmente entre entidades JPA y agregados.

##### Persistence Assemblers

*   `UserAccountPersistenceAssembler`: Traduce entre `UserAccountPersistenceEntity` y el agregado `UserAccount`, recomponiendo `Email`, `HashedPassword` y `UserAccountStatus`.
*   `OneTimePasswordPersistenceAssembler` y `PasswordResetTokenPersistenceAssembler`: Traducen entre sus respectivas entidades JPA y agregados, recomponiendo `HashedSecret` y, en el caso del OTP, `OtpPurpose`.

##### Security Adapters

*   `BCryptPasswordHasherAdapter`: Implementa `PasswordHasher` sobre el algoritmo BCrypt.
*   `BCryptSecretHasherAdapter`: Implementa `SecretHasher` para el hashing y la comparación de los códigos OTP y de los tokens de recuperación.
*   `SecureRandomSecretGeneratorAdapter`: Implementa `SecretGenerator` sobre un generador criptográficamente seguro, produciendo códigos numéricos de seis dígitos y tokens opacos.
*   `JwtTokenProviderAdapter`: Implementa la emisión y validación de JWT firmados (RS256) con `UserId` y roles como claims; materializa el Published Language del Open Host Service de IAM.

##### Notification Adapters

*   `EmailProviderAdapter`: Envía los correos de verificación de cuenta, los códigos OTP y los enlaces de recuperación de contraseña.

##### Scheduling

*   `ExpiredSecretsCleanupScheduler`: Tarea periódica que purga de `otp_codes` y `password_reset_tokens` los secretos vencidos y no consumidos, invocando `deleteExpiredUnusedBefore`. La invalidación no requiere una transición de estado persistida: un secreto deja de ser utilizable en cuanto vence su `expires_at` o se registra su `used_at`.

#### 2.6.7.5. Bounded Context Software Architecture Component Level Diagrams

La Figura 2.63 presenta las cuatro capas del Bounded Context **IAM**, su relación con la aplicación móvil, la base de datos y el proveedor de correo, y la emisión del JWT firmado que validan los Bounded Contexts descendentes.

<a id="figura-2-63"></a>**Figura 2.63.** Diagrama de componentes del Bounded Context IAM

![IAM Component Diagram](../assets/images/chapterII/c4-diagrams/IAM_Components.png)

#### 2.6.7.6. Bounded Context Software Architecture Code Level Diagrams

En esta sección se presenta la estructura interna del Bounded Context **IAM** a nivel de código, mediante el diagrama de clases de su Domain Layer y el diseño de su base de datos.

##### 2.6.7.6.1. Bounded Context Domain Layer Class Diagrams

El diagrama UML de la Figura 2.64 presenta la Domain Layer de **IAM**, con los agregados `UserAccount`, `OneTimePassword` y `PasswordResetToken`, sus Value Objects y enumeraciones, y las interfaces de repositorio y de hashing que utiliza.

<a id="figura-2-64"></a>**Figura 2.64.** Diagrama de clases de la Domain Layer de IAM

![IAM Domain Class Diagram](../assets/images/chapterII/classDiagrams/IAM-class-diagram.png)

##### 2.6.7.6.2. Bounded Context Database Design Diagram

La Figura 2.65 presenta el diseño de persistencia de **IAM**: `user_accounts` almacena las cuentas con su correo, su contraseña cifrada y su estado, mientras que `otp_codes` y `password_reset_tokens` registran los códigos de segundo factor y los tokens de recuperación de contraseña de cada cuenta.

<a id="figura-2-65"></a>**Figura 2.65.** Diagrama de base de datos de IAM

![IAM Database Design Diagram](../assets/images/chapterII/databaseDiagrams/IAM-database.png)

### Guardian+ Physical Database Schema

Como complemento a los Database Design Diagrams definidos individualmente para cada Bounded Context, la Figura 2.66 presenta una vista consolidada del esquema físico de persistencia de **Guardian+**.

El Physical Schema ERD integra las principales tablas utilizadas por los distintos contextos del sistema y permite visualizar de manera conjunta sus claves primarias, claves foráneas y relaciones. Esta representación facilita la comprensión de cómo los datos persistentes de identidad, perfiles, suscripciones, monitoreo de salud, alertas, rutinas de cuidado y demás capacidades de Guardian+ se relacionan dentro de la infraestructura de almacenamiento.

<a id="figura-2-66"></a>**Figura 2.66.** Esquema físico consolidado de la base de datos de Guardian+

![Guardian+ Physical Schema ERD](../assets/images/chapterII/databaseDiagrams/PhysicalSchemaERD.png)

El modelo mantiene la separación lógica definida mediante los Bounded Contexts, mientras que las referencias necesarias entre sus datos persistentes se representan mediante identificadores y relaciones explícitas. De esta manera, el esquema físico proporciona una visión integral de la persistencia sin sustituir los Database Design Diagrams particulares documentados previamente para cada contexto.
