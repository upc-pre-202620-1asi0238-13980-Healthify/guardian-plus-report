<div style="page-break-before: always; break-before: page;"></div>

# Capítulo III: Solution UI/UX Design

En este capítulo se presenta el diseño de la experiencia y de la interfaz de Guardian+: la guía de estilos, la arquitectura de información, el diseño del Landing Page y el diseño de la aplicación móvil, desde sus wireframes hasta el prototipo navegable.

## 3.1. Product design

En esta sección se presenta el diseño de producto de Guardian+, que parte de la guía de estilos y la arquitectura de información para definir el Landing Page y la aplicación móvil.

### 3.1.1. Style Guidelines

Las presentes directrices de estilo definen el lenguaje visual, los componentes y las convenciones de interfaz para la plataforma Guardian+, abarcando tanto el sitio web estático (Landing Page) como la aplicación móvil nativa y multiplataforma. Este sistema asegura consistencia, accesibilidad universal y un entorno confiable para familiares, cuidadores y ciudadanos en situación de vulnerabilidad o dependencia.

**Concepto de diseño.** Todas las decisiones que siguen responden a una misma intención: que la interfaz se perciba como *una casa tranquila y no como una sala de hospital*. Guardian+ traslada información clínica a un entorno doméstico y de uso cotidiano, por lo que su lenguaje visual no puede adoptar la estética de un equipo médico —oscura, saturada, densa en datos— ni la de una aplicación de fitness —festiva, competitiva, gamificada—. La primera trasladaría a la casa la tensión de una unidad de cuidados intensivos; la segunda trivializaría una responsabilidad que para el usuario es afectiva antes que deportiva. El sistema se sitúa deliberadamente entre ambas: rigor en la estructura y en la precisión de los datos, calidez en el color, la forma y el espacio.

Esta intención se deriva del valor central que el Capítulo I identifica en los segmentos objetivo: lo que familiares y cuidadores buscan, antes que cualquier funcionalidad, es *tranquilidad*. Un producto que promete calma no puede generar tensión visual al abrirse. De ahí que el estado normal —la situación mayoritaria, la que el usuario verá casi siempre— se represente con un lenguaje sereno y silencioso, y que la intensidad visual esté racionada y reservada para lo excepcional. La jerarquía del sistema no se organiza por importancia funcional, sino por urgencia: el diseño permanece callado mientras todo está bien y solo eleva la voz cuando algo ocurre.

#### 3.1.1.1. General Style Guidelines

La guía de estilos general define los lineamientos que comparten el Landing Page y la aplicación móvil: el tono de comunicación, la paleta de colores, la tipografía y el uso de espaciado, bordes y elevaciones.

##### A. Tono de Comunicación y Lenguaje

El tono de Guardian+ equilibra la precisión médica con la serenidad humana indispensable para mitigar la ansiedad en situaciones de riesgo continuo:

*   **Formal / Casual:** *Formal y Profesional*. Proyecta rigor clínico, seguridad en la gestión de telemetría biométrica y solidez en los protocolos de auxilio.
*   **Entusiasta / Sereno:** *Sereno y Calmo*. Prioriza la claridad analítica y la templanza en estados de alarma crítica, evitando elementos alarmistas que susciten pánico infundado.
*   **Respetuoso / Irreverente:** *Estrictamente Respetuoso*. Reconoce la dignidad, privacidad y autonomía de las personas bajo cuidado y la responsabilidad de sus redes de apoyo.
*   **Divertido / Serio:** *Serio y Confiable*. Enfocado en la eficiencia operativa, la legibilidad inmediata de signos vitales y la rapidez de respuesta ante emergencias.

**Justificación de diseño.** El tono es la voz de la marca y define qué clase de acompañante es el producto. Guardian+ elige el registro de un profesional de confianza que informa sin sobresaltar: la misma manera en que un médico comunica una novedad a una familia. Los dos extremos disponibles fueron descartados por razones de contexto. Un tono entusiasta y motivacional, propio de las aplicaciones de actividad física, convertiría el cuidado de una persona vulnerable en un juego de logros y felicitaciones, algo que el usuario percibiría como una falta de seriedad frente a un asunto que le resulta afectivamente delicado. Un tono estrictamente clínico, construido sobre terminología técnica y cifras sin interpretación, trasladaría a la casa la frialdad del entorno hospitalario y dejaría al familiar con el dato pero sin la conclusión, que es precisamente lo que necesita.

La serenidad es agradable porque devuelve al usuario la sensación que compró: un mensaje como *Elena está bien · Actualizado hace 2 min* comunica normalidad de manera afirmativa, mientras que la ausencia de avisos podría interpretarse como una falla del sistema. El producto habla incluso cuando no hay novedades, y ese hábito de confirmar la calma es lo que construye el vínculo cotidiano con la aplicación. En el otro extremo, la emergencia se comunica con frases cortas y una acción evidente, sin signos de exclamación ni lenguaje dramático, porque en ese momento el usuario necesita dirección y no énfasis. El respeto es una decisión de diseño explícita y no una cortesía: la persona bajo cuidado es un sujeto con nombre propio dentro de la interfaz, nunca *el paciente* ni *el monitoreado*, y la pulsera le habla a ella directamente. Esta elección sostiene que el producto es un acompañamiento y no un instrumento de vigilancia, distinción que determina si la persona acepta usar el dispositivo.

**Justificación de usabilidad.** El tono traduce la terminología médica a expresiones de uso cotidiano y acompaña cada cifra de una interpretación en palabras (*Normal*, *Requiere atención*), porque familiares y cuidadores no son personal clínico. El registro sereno atiende además al contexto real de uso: quien abre la aplicación tras recibir una alerta lo hace bajo estrés, condición en la que la capacidad de procesamiento se reduce y un lenguaje alarmista incrementa el tiempo de reacción en lugar de acortarlo. Reservar las expresiones de urgencia para las emergencias reales evita también la fatiga de alertas: si todo aviso se comunica como crítico, el usuario deja de distinguir prioridades y termina desatendiendo las que sí lo son.

##### B. Paleta de Colores

La paleta cromática se estructura bajo las especificaciones técnicas del design system implementado, garantizando cumplimiento de contraste WCAG 2.1 nivel AA y AAA para usuarios con visión reducida:

| Token de Color | Código Hex | Rol en Interfaz | Conformidad WCAG |
| :--- | :--- | :--- | :--- |
| **Primary** | `#167A62` | Verde esmeralda clínico para botones primarios, estados activos y cabeceras | AA (4.8:1 sobre blanco) |
| **Primary Foreground** | `#FFFFFF` | Texto e iconos interactivos sobre contenedores primarios | AAA (> 7.0:1) |
| **Secondary (Pastel)** | `#D3F8F0` | Fondo de métricas estables, insignias y estados de sincronización | AA con Foreground |
| **Secondary Foreground** | `#169084` | Etiquetas, iconografía médica de soporte y enlaces secundarios | AA (4.5:1 sobre pastel) |
| **Accent Mint** | `#D9F0E7` | Relleno de chips interactivos y zonas de selección activa | AAA (> 7.0:1) |
| **Accent Foreground** | `#123128` | Verde bosque profundo para títulos y datos numéricos de alta jerarquía | AAA (12.2:1 sobre acento) |
| **Neutral Background** | `#F8FBF9` | Fondo base de las vistas móviles y secciones de la Landing Page | AAA (> 14.0:1 con texto) |
| **Neutral Foreground** | `#123128` | Color principal de lectura para párrafos, valores y etiquetas | AAA (14.5:1 sobre fondo) |
| **Neutral Muted** | `#EEF4F1` | Contenedores neutros secundarios y divisores estructurales | AA |
| **Muted Foreground** | `#587168` | Texto secundario, unidades de medida (bpm, mmHg) y marcas de tiempo | AA (4.6:1 sobre fondo) |
| **Border** | `#CFE0D8` | Líneas de división de tablas y bordes de tarjetas contenedoras | Componente UI |
| **Surface Card** | `#FFFFFF` | Superficie de tarjetas de métricas biométricas y tarjetas de incidentes | AAA con Foreground |
| **Card Foreground** | `#123128` | Texto principal de métricas y estados dentro de tarjetas | AAA (> 14.0:1) |
| **Destructive / Alert** | `#C53B3B` | Indicador de emergencias críticas, picos de presión y botón SOS activo | AA (4.7:1 sobre blanco) |
| **Destructive Foreground** | `#FFFFFF` | Tipografía de advertencias críticas sobre fondos destructivos | AAA (> 7.0:1) |
| **Pastel Orange (Warning)** | `#FFE6CC` | Advertencias de batería baja, umbrales en observación y rutinas pendientes | AAA con `#7A3E00` |
| **Pastel Orange Text** | `#B25900` | Etiquetas de advertencia preventiva y estados de tolerancia | AA (4.6:1 sobre fondo) |
| **Pastel Yellow (Notice)**| `#FFF4CC` | Alertas informativas de geocercas, recordatorios y revisiones programadas | AAA con `#665200` |
| **Pastel Yellow Text** | `#806600` | Tipografía de notificaciones preventivas y estados de sincronización | AA (4.5:1 sobre fondo) |

![style-guidelines-colors](../assets/images/chapterIII/general-style-guidelines/color-guidelines.png)

**Justificación de diseño.** *Por qué verde como color principal.* El verde es el color con el que la cultura visual de la salud representa la estabilidad: es el tono en que los monitores clínicos muestran un signo vital dentro de rango y el que el usuario ya asocia con *todo está en orden*. Como el estado normal es el que la aplicación muestra la mayor parte del tiempo, el color de marca y el color del bienestar coinciden, y la pantalla habitual resulta afirmativa por sí misma, sin necesidad de mensajes adicionales. Se descartó el azul, opción por defecto en el software médico y corporativo, por dos razones: comunica tecnología y procedimiento antes que cuidado, y resulta distante en un producto que media una relación familiar. El verde, en cambio, pertenece al registro de lo vivo, lo natural y lo sano.

*Por qué este verde y no otro.* El tono elegido, `#167A62`, es un esmeralda profundo con desviación hacia el azul verdoso. Esa inclinación es intencional: recoge del azul la seriedad y la sensación de competencia técnica que exige un producto que administra datos de salud, y del verde la vitalidad y la cercanía. Su saturación es moderada y su luminosidad baja, de modo que el color se lee sobrio y adulto; un verde más brillante o más amarillento habría evocado el vocabulario visual de lo *eco*, lo orgánico o lo infantil, y habría restado autoridad a la información clínica. El resultado es un color que puede sostener una cabecera y un botón de acción principal sin cansar ni banalizar el contenido.

*Por qué una paleta pastel y de baja saturación.* Los secundarios `#D3F8F0` y `#D9F0E7` son variaciones muy claras del mismo verde, lo que produce una armonía monocromática: la pantalla se percibe como una sola atmósfera y no como una suma de elementos que compiten. Esta es la decisión que más contribuye a que la interfaz resulte agradable en un uso frecuente y prolongado, porque el color saturado en superficies amplias genera tensión y fatiga visual, mientras que el pastel actúa como tela, madera o pintura de pared: materiales del entorno doméstico al que el producto pertenece. Al mantener toda la paleta en un rango cromático bajo, el sistema conserva además un recurso escaso —el color intenso— disponible únicamente para lo urgente.

*Por qué los avisos siguen el código del semáforo.* Los estados intermedios se resuelven con el naranja `#FFE6CC` y el amarillo `#FFF4CC`, y la emergencia con el rojo `#C53B3B`. La secuencia verde–ámbar–rojo es la convención de urgencia más extendida y no requiere aprendizaje alguno, ventaja decisiva para usuarios de edad avanzada o con poca familiaridad digital, que comprenden el nivel de gravedad antes de leer la etiqueta. Los tonos cálidos actúan como contrapunto del verde dominante y por ello destacan con claridad, pero se aplican en versión pastel para que el aviso preventivo llame la atención sin producir sobresalto. El rojo, en cambio, es un ladrillo ligeramente desaturado y no un rojo puro de máxima intensidad: transmite urgencia inequívoca y conserva un carácter contenido, coherente con un producto que evita el alarmismo incluso en su momento más crítico.

*Por qué el texto no es negro y el fondo no es blanco.* El color de lectura `#123128` es un verde bosque muy oscuro en lugar de negro puro. El negro sobre blanco produce el contraste máximo posible y con él una vibración incómoda en lecturas largas; un oscuro con matiz verde suaviza esa dureza, integra la tipografía en la misma familia cromática que el resto del sistema y da al conjunto un acabado más cuidado. Por la misma lógica, el fondo `#F8FBF9` es un blanco con una mínima presencia de verde: el blanco puro remite a lo estéril y clínico, deslumbra en el uso nocturno propio del monitoreo continuo, y no permitiría que las tarjetas blancas se distinguieran del lienzo. Con este fondo apenas teñido, las superficies blancas de las tarjetas emergen como hojas de papel sobre una mesa, y la jerarquía se construye con luz en lugar de con bordes o color.

**Justificación de usabilidad.** Todos los pares de texto y fondo superan el mínimo de 4.5:1 exigido por el criterio WCAG 2.1 1.4.3 y los textos de lectura prolongada alcanzan el nivel AAA, decisión motivada por el perfil de los usuarios: la pérdida de sensibilidad al contraste y la presbicia son frecuentes tanto en la persona bajo cuidado como en los familiares de mayor edad que integran el círculo de cuidado. El significado nunca se transmite únicamente por color, conforme al criterio 1.4.1: cada estado combina el token cromático con un ícono y una etiqueta textual, de modo que un usuario con deuteranopia —la deficiencia más común, y especialmente sensible a la distinción entre el verde primario y el rojo destructivo— continúa diferenciando una lectura normal de una emergencia. La exclusividad del rojo cumple asimismo una función perceptiva: el color saturado se detecta de forma preatencional, antes de leer la pantalla, y pierde esa capacidad si aparece en elementos rutinarios.

##### C. Tipografía

La selección tipográfica maximiza la legibilidad en pantallas móviles de diversa densidad de píxeles y en paneles de visualización web:

*   **Familia Primaria (UI & Body Text):** `Inter`, Sans-Serif. Empleada en interfaces de usuario, etiquetas de navegación, formularios y texto de soporte general por su alta legibilidad en tamaños reducidos.
*   **Familia Secundaria (Display & Metrics):** `Plus Jakarta Sans`, Sans-Serif geométrica. Empleada en encabezados principales, paneles analíticos y lecturas de telemetría en tiempo real (frecuencia cardíaca, SpO₂).
*   **Familia Monospaciada (Data & Logs):** `JetBrains Mono`, Monospace. Empleada en coordenadas GPS, códigos identificadores de incidentes, tramas de telemetría y sellos temporales.

Escala tipográfica normalizada:

| Nivel Jerárquico | Familia Tipográfica | Peso | Tamaño (Desktop) | Tamaño (Mobile) | Line Height |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **H1 Display** | Plus Jakarta Sans | Bold (700) | 36px | 28px | 1.2 |
| **H2 Section** | Plus Jakarta Sans | SemiBold (600) | 24px | 22px | 1.3 |
| **H3 Subsection** | Plus Jakarta Sans | Medium (500) | 18px | 16px | 1.4 |
| **Body Large** | Inter | Regular (400) | 16px | 16px | 1.5 |
| **Body Base** | Inter | Regular (400) | 14px | 14px | 1.5 |
| **Caption / Meta**| Inter | Medium (500) | 12px | 12px | 1.4 |
| **Data Metric** | JetBrains Mono | Medium (500) | 28px | 24px | 1.1 |

![typography-guidelines](../assets/images/chapterIII/general-style-guidelines/typography-guidelines.png)

**Justificación de diseño.** *Por qué `Inter` en el cuerpo de texto.* `Inter` es una tipografía deliberadamente neutra, diseñada desde su origen para interfaces digitales. Esa neutralidad es el argumento a favor: en Guardian+ el protagonista debe ser el dato —una frecuencia cardíaca, una hora de medicación, el nombre de la persona bajo cuidado— y no la letra que lo escribe. Una tipografía con personalidad marcada añadiría una capa de estilo que competiría con la información y, en un producto de salud, restaría credibilidad. La carga emocional del sistema se deposita en el color y en el espacio; la tipografía de cuerpo aporta transparencia.

*Por qué `Plus Jakarta Sans` en los titulares.* La familia de despliegue es geométrica, con trazos de construcción limpia y detalles de corte humanista. Aporta al producto un carácter contemporáneo y amable que lo aleja del aspecto institucional de un sistema clínico, y lo hace únicamente en los titulares, donde el volumen de texto es breve y una tipografía con personalidad resulta un acierto en lugar de un obstáculo. La combinación funciona porque el contraste entre ambas familias es de estructura y no de estilo: las dos son sans-serif de proporciones afines, de modo que conviven sin disonancia. Se descartó emparejar una serif con una sans, recurso frecuente en diseño editorial, porque la serif habría dado al producto un aire tradicional, jurídico o institucional, incompatible con la inmediatez de una aplicación de monitoreo, además de degradarse en pantallas pequeñas.

*Por qué una monoespaciada para los datos.* `JetBrains Mono` cumple una función semántica: su forma comunica *medición* e *instrumento*, y basta ver una coordenada GPS o un identificador de incidente para entender que se trata de un valor registrado por el sistema y no de un texto redactado. Su ventaja decisiva en este producto es el ancho fijo de los dígitos: cuando una lectura biométrica se actualiza en tiempo real, las cifras cambian sin que el número se desplace ni el bloque se reacomode. Esa quietud es lo que permite mirar un valor que cambia continuamente sin que la pantalla resulte inquieta, y es también el motivo de que las métricas —y no solo los códigos— se compongan en esta familia.

*Por qué esta escala.* La escala es corta y de saltos amplios: siete niveles, sin tamaños intermedios que obliguen a decidir entre opciones equivalentes. El resultado es una jerarquía que se reconoce sin comparar, porque la diferencia entre un nivel y el siguiente siempre es evidente. Su rasgo característico es el peso otorgado al dato: una lectura biométrica se compone a 28px, un tamaño mayor que el del titular de su propia sección en móvil. Esta inversión de la jerarquía convencional define la estética del tablero —el número es la figura y todo lo demás es contexto— y responde al modo real de consulta: el usuario abre la aplicación para ver una cifra, no para leer una pantalla. Los niveles pequeños quedan reservados a la información que acompaña, como unidades y marcas de tiempo, que deben estar presentes pero nunca disputar la atención.

**Justificación de usabilidad.** Las tres familias son sans-serif de altura de x elevada y formas abiertas, características que sostienen la legibilidad en tamaños reducidos y en pantallas de baja densidad. `JetBrains Mono` diferencia además de manera inequívoca los caracteres 0/O y 1/l/I, lo que previene errores de lectura y de transcripción cuando un familiar dicta una ubicación o un código a un servicio de emergencia. La escala fija el cuerpo base en 14px y el de lectura extensa en 16px, sin descender por debajo de 12px, tamaño limitado a metadatos no críticos: ningún dato indispensable depende del nivel tipográfico más pequeño. El interlineado de 1.5 en los niveles de cuerpo cumple el criterio WCAG 2.1 1.4.12 y facilita el seguimiento de línea a usuarios con dislexia o con visión reducida. Limitar el sistema a tres familias y siete niveles refuerza, por último, la consistencia entre la Landing Page y la aplicación: el usuario aprende una sola vez qué significa cada jerarquía y la reconoce en ambos productos.


##### D. Espaciado, Bordes y Elevaciones (Effects)

*   **Sistema de Espaciado:** Cuadrícula base de 8px (incrementos de 4px, 8px, 12px, 16px, 24px, 32px, 48px).
*   **Border Radius:** 
    *   *Default (Tokens UI):* `12px` para tarjetas contenedoras, bloques analíticos y campos de entrada.
    *   *Subtle:* `6px` para botones de acción secundaria y etiquetas de estado.
    *   *Large:* `20px` para hojas inferiores modales (bottom sheets) y diálogos de confirmación.
    *   *Full:* `9999px` para botones de llamada directa, avatares e indicadores de pulso SOS.
*   **Elevaciones (Sombras CSS):**
    *   *Flat:* Sin sombra (`box-shadow: none`), demarcado por borde `#CFE0D8`.
    *   *Low:* `0px 1px 3px rgba(18, 49, 40, 0.06), 0px 1px 2px rgba(18, 49, 40, 0.04)` para tarjetas estáticas.
    *   *Mid:* `0px 4px 6px -1px rgba(18, 49, 40, 0.08), 0px 2px 4px -1px rgba(18, 49, 40, 0.04)` para elementos interactivos en foco y barras flotantes.
    *   *High:* `0px 10px 15px -3px rgba(18, 49, 40, 0.1), 0px 4px 6px -2px rgba(18, 49, 40, 0.05)` para modales de emergencia crítica.

    ![espaciado bordes y elevaciones](../assets/images/chapterIII/general-style-guidelines/elevations.png)

**Justificación de diseño.** *Por qué una cuadrícula de 8px y espacios generosos.* La retícula no se elige por comodidad de implementación, sino porque la alineación es lo que el usuario lee como calidad: una pantalla donde todos los márgenes son múltiplos de una misma unidad se percibe cuidada y, por extensión, fiable. En un producto cuyo argumento de venta es la confianza, la pulcritud de la composición forma parte de la promesa. El espacio en blanco que resulta de aplicar esa retícula con holgura cumple una función expresiva propia: una aplicación de monitoreo administra muchos indicadores a la vez y, sin aire entre ellos, adoptaría el aspecto de un panel de control saturado, precisamente la sensación que el producto quiere evitar. Al distribuir las tarjetas con márgenes amplios, la pantalla se lee reposada y la abundancia de datos deja de percibirse como complejidad.

*Por qué esquinas redondeadas y por qué estos radios.* La esquina viva se asocia a lo técnico, industrial y normativo; la redondeada, a lo blando y cercano. En un producto que entra en la casa para hablar de una persona querida, la forma debía ser amable, y por eso ningún contenedor del sistema tiene ángulos rectos. El valor de 12px es el punto de equilibrio buscado: suaviza el contorno de las tarjetas sin llegar al redondeo pronunciado que daría al producto un aire de juguete y le quitaría la seriedad que su contenido exige. Los radios crecen con la superficie —6px en las etiquetas y botones secundarios, 20px en las hojas inferiores y los diálogos— porque un mismo radio aplicado a superficies de tamaños muy distintos se percibe desigual: el elemento grande parece rígido y el pequeño, deformado. Escalarlo mantiene constante la sensación de suavidad en todo el sistema.

*Por qué la llamada y el SOS son circulares.* El círculo completo es la forma más física del sistema: remite a un botón real, pulsable, y es la única figura que se distingue del resto sin necesidad de leer nada. Reservarla para la llamada directa y para el indicador de pulso SOS hace que la acción de auxilio sea reconocible por su silueta en el instante en que el usuario está menos disponible para leer, y recupera además el lenguaje visual que la telefonía ha usado siempre para la misma acción.

*Por qué estas sombras y no más.* Las sombras están teñidas con el verde oscuro de la paleta, `#123128`, y no con negro neutro. Es una decisión de coherencia lumínica: sobre un fondo con matiz verde, una sombra gris se percibe sucia y ajena, mientras que una sombra del mismo matiz que el entorno parece proyectada por la luz de la propia escena. Sus opacidades son muy bajas, de modo que la profundidad se insinúa como luz difusa de día y no como un foco dirigido, en línea con la contención del resto del sistema. Esa moderación tiene una consecuencia deliberada: al mantener la interfaz casi plana en su uso habitual, la sombra pronunciada del modal de emergencia crítica se convierte en un acontecimiento visual. La profundidad, como el color intenso, es un recurso que el sistema administra con escasez para que signifique algo cuando aparece.

**Justificación de usabilidad.** La cuadrícula agrupa por proximidad los elementos de un mismo conjunto —valor, unidad y marca de tiempo de una métrica— y separa los conjuntos entre sí, de modo que la estructura de la pantalla se percibe antes de leer su contenido. Ese mismo espaciado garantiza que los controles interactivos conserven un área táctil mínima de 48dp y una separación suficiente entre ellos, condición necesaria cuando el usuario opera con una sola mano, con prisa o con destreza reducida por temblor o artrosis: cuanto mayor es el objetivo y menor la distancia, menor es el tiempo y la tasa de error al alcanzarlo, y un toque accidental sobre *Reconocer* o *Llamar* tiene consecuencias reales. El nivel *Flat*, por su parte, sustituye la sombra por un borde explícito `#CFE0D8`, de manera que la delimitación de los contenedores se mantiene visible en modos de alto contraste, donde las sombras dejan de percibirse.


![ejemplo de componentes](../assets/images/chapterIII/general-style-guidelines/example_1.png)

![ejemplo de vista](../assets/images/chapterIII/general-style-guidelines/example.png)

### 3.1.2. Information Architecture

La arquitectura de información define cómo se organiza, etiqueta, encuentra y recorre el contenido de Guardian+. En esta sección se presentan los sistemas de organización, etiquetado, búsqueda y navegación, junto con las etiquetas SEO del Landing Page.

#### 3.1.2.1. Organization Systems

Guardian+ organiza su información combinando estructuras visuales y esquemas de categorización según el tipo de contenido y la necesidad del usuario en cada momento.

##### Estructuras de organización

**Jerárquica (Visual Hierarchy).** Se aplica a la navegación principal de la app: desde el Inicio se accede a las 5 secciones core (Monitoreo de Salud, Rutinas y Bienestar, Alertas, Ubicación, Perfil), y dentro de cada una la información se prioriza visualmente según su criticidad — por ejemplo, en Alertas, las alertas activas se muestran por encima del historial de incidentes ya resueltos.

**Secuencial (Step-by-step).** Se usa en procesos donde el orden de los pasos es obligatorio: el flujo de autenticación y registro (Email → Contraseña → Iniciar Sesión), la respuesta ante una emergencia (alerta generada → ventana de confirmación → escalamiento a contactos), y la configuración inicial de la pulsera al vincular un nuevo dispositivo.

**Matricial (Matrix).** Se aplica donde el usuario necesita comparar información en dos dimensiones a la vez: el calendario semanal de recordatorios de medicación (horarios × días de la semana) y la comparación de planes de suscripción (beneficios × plan).

##### Esquemas de categorización

**Alfabético.** Para listas donde el usuario busca un ítem puntual por nombre: la lista de contactos de emergencia y el listado de medicamentos registrados.

**Cronológico.** Para todo lo que representa una secuencia en el tiempo: el historial de signos vitales, el historial de incidentes/alertas y el historial de pagos, donde lo más reciente aparece primero.

**Por tópico.** Es el criterio principal de la navegación de la app — cada sección agrupa funcionalidad relacionada siguiendo directamente los Bounded Contexts del dominio (Salud, Rutinas, Alertas, Ubicación, Perfil), de modo que el usuario siempre sabe en qué "mundo" de la app está.


![organizacion-systems](../assets/images/chapterIII/organization-systems/organization-systems-diagram.jpg)

#### 3.1.2.2. Labelling Systems

Guardian+ define un sistema de etiquetas breve y consistente para que familiares, cuidadores y visitantes identifiquen cada conjunto de información sin necesidad de interpretar términos técnicos. Las etiquetas parten del Ubiquitous Language definido en el Capítulo II, pero se expresan en un lenguaje cotidiano y sereno, coherente con el tono de comunicación establecido en las Style Guidelines. Una misma etiqueta representa siempre el mismo concepto, tanto en la Landing Page como en la aplicación móvil.

##### Criterios de etiquetado

| Criterio | Aplicación en Guardian+ |
|---|---|
| **Mínimo de palabras** | Las etiquetas de navegación y los botones utilizan entre una y tres palabras. Las acciones se expresan con verbos en infinitivo (*Reconocer*, *Llamar*, *Exportar reporte*). |
| **Lenguaje cotidiano** | Los términos del dominio se traducen a palabras de uso común. Por ejemplo, *Fragile Citizen* se presenta como *Persona bajo cuidado* o directamente por su nombre. |
| **Tono sereno** | Los estados se comunican sin alarmismo: se utiliza *Requiere atención* en lugar de expresiones como *¡Peligro!*, reservando el color rojo y la palabra *Crítica* para emergencias reales. |
| **Ícono acompañado de texto** | Las opciones de navegación, los tipos de alerta y los estados combinan siempre ícono y texto. El color nunca es el único medio para transmitir un significado. |
| **Unidades visibles** | Cada valor biométrico muestra su unidad junto al número: lpm, mmHg, %, °C y rpm. |
| **Consistencia entre productos** | Las etiquetas compartidas entre la Landing Page y la aplicación (*Zonas seguras*, *Círculo de cuidado*, nombres de planes) se escriben exactamente igual en ambos productos. |

##### Del Ubiquitous Language a las etiquetas de interfaz

La siguiente tabla establece la correspondencia entre los términos del dominio y la etiqueta que el usuario visualiza, asegurando que la interfaz y el modelo de dominio hablen del mismo concepto.

| Término del dominio | Etiqueta en la interfaz | Ubicación en la app |
|---|---|---|
| **Fragile Citizen** | Persona bajo cuidado (o su nombre, por ejemplo *Elena*) | Inicio, Perfil |
| **Care Circle** | Círculo de cuidado | Perfil |
| **Family / Caregiver** | Familiar / Cuidador | Registro, Círculo de cuidado |
| **Vital Signs** | Signos vitales | Salud |
| **Health History** | Historial | Salud, Alertas |
| **Care Routine** | Rutinas | Navegación principal |
| **Medication Reminder** | Medicación | Rutinas |
| **Medical Appointment** | Citas médicas | Rutinas |
| **Alert** | Alerta | Alertas |
| **Incident** | Incidente | Alertas › Historial |
| **Acknowledgment** | Reconocer | Detalle de alerta |
| **Emergency Contact** | Contactos de emergencia | Alertas › Configuración |
| **Escalation Chain** | Escalamiento | Alertas › Configuración |
| **Alert Settings** | Configuración de alertas | Alertas › Configuración |
| **Silent Mode** | Silenciar alertas no críticas | Alertas › Configuración |
| **Safe Zone** | Zonas seguras | Ubicación |
| **Care Plan** | Mi plan | Perfil |
| **Wearable Device** | Pulsera | Perfil, Onboarding |

##### Etiquetas del Landing Page

Las etiquetas del Landing Page coinciden con las secciones presentadas en los wireframes y mock-ups. Cada una funciona como una promesa de contenido: el visitante asocia la etiqueta con la información que encontrará al seleccionarla, sin que toda la información se concentre en un mismo lugar.

| Etiqueta | Tipo | Asociación (qué encuentra el visitante) |
|---|---|---|
| **Cómo funciona** | Menú principal | Proceso de uso de Guardian+ explicado en tres pasos. |
| **Beneficios** | Menú principal | Las seis funcionalidades principales del producto. |
| **Por qué Guardian+** | Menú principal | Diferenciación frente a relojes fitness y botones SOS, junto con un testimonio. |
| **Precios** | Menú principal | Comparación de los planes Esencial, Guardian+ y Cuidado Pro. |
| **Contacto** | Menú principal | Formulario de contacto, teléfono y horario de atención. |
| **Conocer los planes** | CTA primario | Desplaza al visitante a la sección Precios. |
| **Ver cómo funciona** | CTA secundario | Desplaza al visitante a la sección Cómo funciona. |
| **Saber más** | Enlace de tarjeta | Amplía la descripción de una funcionalidad específica. |
| **Más elegido** | Distintivo | Identifica el plan recomendado para la mayoría de familias. |
| **Comenzar gratis** | CTA de plan | Inicia el uso del plan Esencial. |
| **Elegir este plan** | CTA de plan | Inicia la contratación de un plan de pago. |
| **Quiero más información** | Botón de formulario | Envía la solicitud de contacto al equipo de Guardian+. |
| **Privacidad · Términos** | Enlace de footer | Políticas de privacidad y términos de uso. |

Los campos del formulario de contacto utilizan etiquetas visibles sobre cada campo: *Nombre*, *Teléfono*, *Correo electrónico*, *¿A quién deseas cuidar?* y *Cuéntanos qué necesitas*.

Asimismo, las funcionalidades presentadas en la sección Beneficios anticipan las secciones que el usuario encontrará dentro de la aplicación, reforzando la asociación entre ambos productos:

| Funcionalidad en el Landing Page | Sección asociada en la app |
|---|---|
| **Salud en tiempo real** | Salud |
| **Detección de caídas + SOS** | Alertas |
| **Ubicación y zonas seguras** | Ubicación |
| **Rutinas sin olvidos** | Rutinas |
| **Prevención activa** | Alertas (inactividad prolongada) |
| **Siempre cerca** | Inicio (videollamada) |

##### Etiquetas de la aplicación móvil

La navegación principal de la aplicación se compone de cinco etiquetas, cada una asociada a un Bounded Context del dominio. El acceso a Perfil se ubica en el avatar de la barra superior.

| Etiqueta | Ícono | Contenido asociado | Bounded Context | User Stories |
|---|---|---|---|---|
| **Inicio** | Casa | Estado general de la persona bajo cuidado, accesos rápidos y próximos recordatorios. | Vista integradora | US23 |
| **Salud** | Pulso | Signos vitales en tiempo real, historial y reportes de salud. | Health Monitoring | US01–US05, US07, US19, US21, US24 |
| **Rutinas** | Calendario | Medicación, citas médicas, actividad física, hidratación y descanso. | Care Routines & Wellness | US06, US13, US14, US17, US26, US27, US29 |
| **Alertas** | Campana | Alertas activas, historial de incidentes, contactos de emergencia y configuración de alertas. | Emergency & Alerting | US08–US12, US15, US16, US20, US22, US25 |
| **Ubicación** | Marcador de mapa | Ubicación actual y zonas seguras. | Mobility & Geofencing | US18, US28 |
| **Perfil** | Avatar | Datos del usuario, persona bajo cuidado, círculo de cuidado, pulsera, plan y sesión. | Profile, IAM, Subscriptions | — |

Dentro de cada sección se utilizan las siguientes etiquetas:

| Sección | Pestañas | Etiquetas de contenido | Acciones |
|---|---|---|---|
| **Inicio** | — | *Elena está bien*, *Actualizado hace 2 min*, *Próximos recordatorios*, *Última alerta* | Llamar, Videollamada, Ver ubicación |
| **Salud** | Ahora · Historial | *Ritmo cardíaco (lpm)*, *Presión arterial (mmHg)*, *Oxígeno (%)*, *Temperatura (°C)*, *Respiración (rpm)*; filtros *Día · Semana · Mes* | Exportar reporte, Ver reporte semanal |
| **Rutinas** | Hoy · Semana | *Medicación*, *Citas médicas*, *Actividad*, *Hidratación*, *Descanso*, *Por agotarse* | Nuevo recordatorio, Reponer medicina |
| **Alertas** | Activas · Historial | *Caída*, *SOS*, *Signo vital fuera de rango*, *Salida de zona segura*, *Inactividad*, *Batería baja* | Reconocer, Llamar, Marcar estabilizado, Cerrar incidente, Configurar |
| **Ubicación** | Mapa · Zonas seguras | *Ubicación actual*, *Dentro de zona segura*, *Fuera de zona segura*, *Última actualización* | Nueva zona, Editar zona |
| **Perfil** | — | *Mis datos*, *Persona bajo cuidado*, *Círculo de cuidado*, *Pulsera*, *Mi plan* | Cerrar sesión |

Los flujos de acceso utilizan las etiquetas *Iniciar sesión*, *Crear cuenta*, *Correo electrónico*, *Contraseña*, *Código de verificación*, *¿Olvidaste tu contraseña?* y *Vincular pulsera*.

##### Etiquetas de estado

Los estados del dominio se presentan mediante etiquetas breves acompañadas del color semántico definido en la paleta de las Style Guidelines.

| Concepto | Valor del dominio | Etiqueta | Color semántico |
|---|---|---|---|
| **Severidad de alerta** | `CRITICAL` / `HIGH` / `MEDIUM` | Crítica / Alta / Media | Destructive / Pastel Orange / Pastel Yellow |
| **Estado de alerta** | `PENDING_CONFIRMATION` | Confirmando | Pastel Yellow |
| | `TRIGGERED` / `ESCALATED` | Nueva / Escalada | Destructive |
| | `ACKNOWLEDGED` | Reconocida | Pastel Orange |
| | `DISMISSED` / `RESOLVED` | Descartada / Resuelta | Neutral Muted |
| **Estado de incidente** | `IN_ATTENTION` / `STABILIZED` / `CLOSED` | En atención / Estabilizado / Cerrado | Pastel Orange / Secondary / Neutral Muted |
| **Estado de recordatorio** | `SCHEDULED` / `ISSUED` / `REISSUED` | Programado / Pendiente / Reenviado | Neutral Muted / Pastel Yellow / Pastel Orange |
| | `CONFIRMED` / `CANCELLED` / `SUPPRESSED` | Confirmado / Cancelado / Omitido | Secondary / Neutral Muted / Neutral Muted |
| **Lectura de signo vital** | Rango normal / elevado / bajo / sin señal | Normal / Elevado / Bajo / Sin señal | Secondary / Pastel Orange / Pastel Orange / Neutral Muted |
| **Zona segura** | Dentro / fuera del perímetro | En su zona segura / Fuera de zona segura | Secondary / Pastel Yellow |
| **Pulsera** | Conectada / sin señal / batería baja | Conectada / Sin conexión / Batería baja | Secondary / Neutral Muted / Pastel Orange |

##### Etiquetas de la pulsera

La pulsera presenta un conjunto mínimo de etiquetas, pensadas para ser comprendidas por la persona bajo cuidado en una pantalla reducida.

| Etiqueta | Función | User Story |
|---|---|---|
| **SOS** | Solicita ayuda inmediata a los contactos de emergencia. | US15 |
| **Estoy bien** | Confirma, dentro de la ventana de 30 segundos, que la persona se encuentra a salvo tras una advertencia, evitando movilizar al círculo de cuidado. | US10 |
| **Confirmar** | Registra que la medicación o la actividad recordada fue realizada. | US06, US14, US26 |
| **Responder** | Acepta la videollamada o la llamada de voz iniciada por un familiar. Disponible únicamente en los modelos de pulsera con capacidad de comunicación bidireccional. | US23 |

#### 3.1.2.3. SEO Tags and Meta Tags

  Guardian+ define elementos de Search Engine Optimization (SEO) para mejorar la identificación y visibilidad de su experiencia web en motores de búsqueda. Asimismo, se establecen elementos de App Store Optimization (ASO) para describir y posicionar adecuadamente la aplicación móvil en plataformas de distribución de aplicaciones.

##### Landing Page

La Landing Page constituye la presencia web pública de Guardian+ y tiene como propósito presentar la propuesta de valor de la solución, sus principales funcionalidades, beneficios, planes de suscripción y canales de contacto para familiares y cuidadores.

Debido a que la experiencia se estructura como una página informativa con navegación entre secciones, se utiliza un conjunto común de metadatos a nivel del documento principal.

| SEO Element | Value |
|---|---|
| **Title** | Guardian+ \| Cuidado y monitoreo remoto |
| **Meta Description** | Guardian+ conecta a familiares y cuidadores con personas bajo cuidado mediante monitoreo remoto, alertas oportunas, geolocalización y tecnología wearable. |
| **Meta Keywords** | Guardian+, cuidado remoto, cuidadores, familiares, personas bajo cuidado, monitoreo de salud, alertas de emergencia, wearable, geolocalización, planes de suscripción |
| **Meta Author** | Healthify Team |

La configuración SEO definida para la Landing Page se incorporará en el documento principal mediante las etiquetas HTML correspondientes a `title`, `description`, `keywords` y `author`. Asimismo, se considera la configuración de `viewport` para garantizar una correcta visualización en dispositivos móviles.

| HTML Tag | Value |
|---|---|
| `<title>` | Guardian+ \| Cuidado y monitoreo remoto |
| `<meta name="description">` | Guardian+ conecta a familiares y cuidadores con personas bajo cuidado mediante monitoreo remoto, alertas oportunas, geolocalización y tecnología wearable. |
| `<meta name="keywords">` | Guardian+, cuidado remoto, cuidadores, familiares, personas bajo cuidado, monitoreo de salud, alertas de emergencia, wearable, geolocalización, planes de suscripción |
| `<meta name="author">` | Healthify Team |
| `<meta name="viewport">` | width=device-width, initial-scale=1.0 |

Los términos seleccionados se relacionan con las principales secciones definidas para la Landing Page, como la explicación del funcionamiento de Guardian+, sus beneficios, características diferenciadoras, planes de suscripción y canales de contacto.

##### Web Application

En la arquitectura actual de Guardian+ no se contempla una Web Application operativa independiente. La experiencia web corresponde a la Landing Page pública, mientras que las funcionalidades operativas de monitoreo, alertas, ubicación, rutinas, perfiles y suscripciones son proporcionadas mediante la aplicación móvil.

Por este motivo, en la presente iteración no se definen SEO Tags ni Meta Tags adicionales para una Web Application separada, concentrándose la estrategia SEO de la experiencia web en la Landing Page.

##### Mobile Application — ASO Elements

La aplicación móvil constituye el principal medio de interacción para familiares y cuidadores dentro de Guardian+. Para su publicación y presentación en plataformas de distribución de aplicaciones se definen los siguientes elementos de App Store Optimization (ASO):

| ASO Element | Value |
|---|---|
| **App Title** | Guardian+ |
| **App Subtitle/Short Description** | Cuidado y monitoreo remoto |
| **App Keywords** | cuidado remoto, cuidadores, familiares, adulto mayor, persona bajo cuidado, monitoreo, salud, alertas, emergencia, wearable, ubicación, seguridad |
| **App Description** | Guardian+ es una aplicación de apoyo para familiares y cuidadores que permite centralizar el seguimiento de personas bajo cuidado. Integrada con un dispositivo wearable, facilita el monitoreo remoto, la consulta de información relevante, la gestión de alertas ante situaciones de riesgo, el seguimiento de ubicación y el apoyo a rutinas de cuidado, permitiendo una respuesta más oportuna incluso cuando el responsable no se encuentra físicamente presente. |

Los elementos ASO definidos buscan comunicar de forma clara el propósito de Guardian+ y favorecer su identificación mediante términos relacionados con cuidado remoto, monitoreo, seguridad, alertas, ubicación y asistencia a personas bajo cuidado.

#### 3.1.2.4. Searching Systems

Guardian+ resuelve la totalidad de sus búsquedas con un único patrón de interacción, el **desplegable con búsqueda** (*searchable dropdown*), y un único mecanismo de filtrado, las **etiquetas** (*tags*). Todas las secciones que permiten consultar información —Salud, Rutinas, Alertas, Ubicación y Perfil— emplean estos dos componentes con el mismo comportamiento, de modo que el usuario aprende una sola mecánica de búsqueda y la reutiliza en el resto del producto. La búsqueda libre por texto abierto se descarta como mecanismo principal y se limita a los listados de nombres propios.

##### Justificación del patrón elegido

El desplegable con búsqueda combina las dos formas de localizar información sin obligar al usuario a elegir entre ellas: al abrirse muestra la lista completa de valores disponibles, lo que permite **reconocer** la opción buscada sin recordarla, y admite al mismo tiempo la escritura de unos pocos caracteres para **reducir** esa lista de inmediato. Esta doble vía resuelve la diferencia de uso entre los dos segmentos del producto: el familiar, que abre la aplicación de forma ocasional y no conoce de memoria las opciones, recorre la lista; el cuidador, que la usa varias veces al día y sabe qué busca, escribe dos letras y selecciona.

La razón de fondo para preferirlo a un campo de búsqueda abierto es que el vocabulario del dominio de Guardian+ es cerrado y conocido: existen cinco signos vitales, seis tipos de alerta, cinco tipos de rutina y un conjunto acotado de estados, todos ellos ya definidos en el Labelling Systems. Un campo de texto libre obligaría al usuario a adivinar ese vocabulario y produciría resultados vacíos cada vez que escribiera un término que el sistema no reconoce —*presión alta* en lugar de *Presión arterial*, *desmayo* en lugar de *Caída*—. El desplegable elimina por completo esa posibilidad: como solo ofrece valores existentes, ninguna consulta puede quedar sin resultados por un error de escritura o de terminología. En un producto usado bajo tensión y por personas de edad avanzada, evitar el callejón sin salida del *sin resultados* importa más que ofrecer la flexibilidad de la escritura libre.

El componente aporta además ventajas concretas en el contexto móvil. Cada opción es un objetivo táctil que cumple el área mínima definida en las Style Guidelines, por lo que seleccionar es más rápido y menos propenso a error que escribir en un teclado en pantalla, especialmente para un usuario con destreza reducida. Al no requerir ortografía exacta, tolera los términos clínicos difíciles de escribir. Y al mostrar siempre las opciones disponibles, informa al usuario de lo que el sistema puede hacer, en lugar de dejarlo frente a un campo vacío del que no sabe qué esperar.

Las etiquetas, por su parte, se eligen como mecanismo de filtrado porque hacen visible el estado de la consulta. Un filtro aplicado desde un menú que se cierra deja al usuario ante una lista incompleta sin explicación aparente, situación especialmente riesgosa en un historial de alertas, donde una lista filtrada puede leerse como *no hay más incidentes*. Cada etiqueta activa permanece en pantalla como un *chip* que declara el criterio vigente y que se elimina con un solo toque, de modo que el usuario siempre sabe por qué está viendo lo que ve y cómo volver atrás. Las etiquetas reutilizan literalmente las etiquetas de estado definidas en el Labelling Systems, con su mismo texto y su mismo color semántico, por lo que el vocabulario con el que se filtra es el mismo con el que se lee la información.

##### Anatomía del desplegable con búsqueda

| Elemento | Comportamiento |
|---|---|
| **Campo disparador** | Muestra la selección vigente o el texto de invitación de la sección (*Todos los signos vitales*, *Todos los tipos de alerta*). Presenta radio de 12px y un ícono de cheurón descendente. |
| **Panel desplegable** | Se abre como hoja inferior en móvil, con radio de 20px y elevación *High*, ocupando como máximo el 70% de la altura de la pantalla. |
| **Campo de búsqueda interno** | Se ubica en la cabecera del panel y filtra la lista a medida que el usuario escribe, sin distinguir mayúsculas ni acentos. |
| **Lista de opciones** | Presenta todas las opciones disponibles con su ícono y, cuando corresponde, su color semántico. Las coincidencias con el texto escrito se resaltan en negrita. |
| **Selección múltiple** | Los desplegables que admiten más de un valor incorporan casillas de verificación y un contador de seleccionados en el campo disparador (*2 tipos de alerta*). |
| **Acciones del panel** | *Aplicar* confirma la selección y cierra el panel; *Limpiar* restablece el valor por defecto de la sección. |
| **Estado sin coincidencias** | Cuando el texto escrito no coincide con ninguna opción, el panel indica que no existe ese criterio y ofrece la acción *Ver todas las opciones*, evitando que el usuario quede sin salida. |

##### Filtrado por etiquetas

| Elemento | Comportamiento |
|---|---|
| **Barra de etiquetas activas** | Se sitúa bajo la cabecera de la sección y muestra un *chip* por cada criterio aplicado, con su color semántico y un ícono de cierre. |
| **Combinación de criterios** | Las etiquetas de una misma familia se combinan de forma inclusiva —*Crítica* junto con *Alta* devuelve ambas severidades— mientras que las etiquetas de familias distintas se combinan de forma restrictiva: *Crítica* junto con *Semana* devuelve las alertas críticas de la última semana. |
| **Eliminación** | Cada *chip* se retira individualmente con un toque en su ícono de cierre. La acción *Limpiar filtros* retira todos a la vez. |
| **Recuento de resultados** | Junto a la barra de etiquetas se indica la cantidad de registros que satisfacen la consulta (*12 resultados*). |
| **Persistencia** | Las etiquetas aplicadas se conservan al navegar al detalle de un registro y regresar, en coherencia con la regla de retorno predecible definida en los Navigation Systems. |
| **Resultado vacío** | Si ninguna combinación de etiquetas devuelve registros, la sección informa que no existen coincidencias para los criterios activos y ofrece la acción *Limpiar filtros*, en lugar de presentar una lista vacía sin explicación. |

##### Aplicación por sección

| Sección | Desplegable con búsqueda | Etiquetas de filtrado | Presentación de resultados |
|---|---|---|---|
| **Salud** | Selector del parámetro biométrico: *Ritmo cardíaco*, *Presión arterial*, *Oxígeno*, *Temperatura*, *Respiración*. | Periodo (*Día · Semana · Mes*) y estado de la lectura (*Normal*, *Elevado*, *Bajo*, *Sin señal*). | Gráfica de tendencia del parámetro seleccionado y, bajo ella, la lista cronológica de lecturas con su etiqueta de estado. |
| **Rutinas** | Selector del recordatorio por nombre del medicamento, de la cita o de la rutina, con la lista completa visible al abrirse. | Tipo (*Medicación*, *Citas médicas*, *Actividad*, *Hidratación*, *Descanso*) y estado de cumplimiento (*Programado*, *Pendiente*, *Confirmado*, *Omitido*, *Reenviado*). | Agenda del periodo activo agrupada por franja horaria, con la etiqueta de estado de cada recordatorio. |
| **Alertas** | Selector del tipo de alerta: *Caída*, *SOS*, *Signo vital fuera de rango*, *Salida de zona segura*, *Inactividad*, *Batería baja*. Admite selección múltiple. | Severidad (*Crítica*, *Alta*, *Media*), estado del incidente (*En atención*, *Estabilizado*, *Cerrado*) y periodo (*Día · Semana · Mes*). | Lista cronológica descendente con la insignia de severidad de cada incidente y el acceso directo a su detalle. |
| **Ubicación** | Selector de la zona segura por nombre (*Casa*, *Parque*, *Club*), con la lista de zonas configuradas visible al abrirse. | Estado del perímetro (*En su zona segura*, *Fuera de zona segura*) y periodo (*Día · Semana · Mes*). | Mapa con la zona seleccionada resaltada y el registro de entradas y salidas del periodo. |
| **Perfil › Círculo de cuidado** | Selector del contacto por nombre, apellido o parentesco. Es el único caso en que la escritura libre opera sobre nombres propios, por lo que el desplegable acepta cualquier texto y filtra la lista de contactos registrados. | Rol (*Familiar*, *Cuidador*) y posición en el escalamiento (*Primario*, *Secundario*). | Lista ordenada alfabéticamente, con la posición de auxilio de cada contacto y la posibilidad de reordenarla. |

En la Landing Page no se incorpora un sistema de búsqueda: al tratarse de una página informativa de extensión acotada, la localización de contenido se resuelve mediante la navegación entre secciones descrita en los Navigation Systems.

#### 3.1.2.5. Navigation Systems

Guardian+ combina distintos sistemas de navegación para que visitantes y usuarios recorran el contenido sin perder de vista dónde se encuentran ni cómo volver. En el Landing Page, la navegación acompaña un recorrido narrativo que conduce al visitante hacia la elección de un plan o el contacto con el equipo. En la aplicación móvil, la navegación prioriza el acceso inmediato al estado de la persona bajo cuidado y la respuesta rápida ante una emergencia.

##### Landing Page

| Mecanismo | Componente | Descripción |
|---|---|---|
| **Navegación global** | Header fijo | Presenta el menú *Cómo funciona · Beneficios · Por qué Guardian+ · Precios · Contacto* en el mismo orden en que aparecen las secciones al hacer scroll. Permanece visible durante todo el recorrido y cada enlace desplaza al visitante a su sección (US30). |
| **Navegación global (mobile)** | Menú hamburguesa | En pantallas móviles el menú se agrupa en un ícono de hamburguesa que despliega las mismas cinco opciones. |
| **Navegación secuencial** | Scroll narrativo | Las secciones siguen el orden problema → solución → diferenciación → precio → acción, guiando al visitante de forma progresiva hacia la conversión. |
| **Navegación contextual** | CTAs | *Conocer los planes* lleva a Precios, *Ver cómo funciona* lleva a Cómo funciona y *Saber más* amplía cada funcionalidad sin abandonar la página. |
| **Navegación de conversión** | CTAs de planes y formulario | *Comenzar gratis* y *Elegir este plan* redirigen a la descarga de la aplicación móvil, donde se completa el registro. *Quiero más información* envía la solicitud de contacto y muestra un mensaje de confirmación. |
| **Navegación de retorno** | Logo y footer | El logo devuelve al inicio de la página. El footer repite el menú principal e incluye los enlaces *Privacidad · Términos*. |

![landing-page-navigation](../assets/images/chapterIII/navigation-systems/landing-page-navigation.png)

##### Aplicación móvil

| Tipo de navegación | Componente | Uso en Guardian+ |
|---|---|---|
| **Global** | Bottom navigation bar | Cinco destinos permanentes: *Inicio · Salud · Rutinas · Alertas · Ubicación*. Se muestra en todas las pantallas principales y se oculta en los flujos secuenciales y en la alerta a pantalla completa, para que el usuario se concentre en una sola tarea. |
| **Suplementaria** | Barra superior | Muestra el título de la pantalla, la flecha de regreso en pantallas secundarias y el avatar que conduce a Perfil. En Alertas incluye el acceso a *Configurar*. |
| **Local** | Pestañas | Cada sección organiza su contenido en pestañas: *Ahora · Historial* en Salud, *Hoy · Semana* en Rutinas, *Activas · Historial* en Alertas y *Mapa · Zonas seguras* en Ubicación. |
| **Contextual** | Tarjetas y enlaces internos | Las tarjetas de Inicio llevan a la sección correspondiente; el detalle de una alerta enlaza con *Ver ubicación* y con el historial de signos vitales del momento del evento. |
| **Secuencial** | Flujos paso a paso | El registro sigue los pasos *Crear cuenta → Código de verificación → Vincular pulsera → Persona bajo cuidado → Contactos de emergencia*, con un indicador de progreso (*Paso 2 de 5*). La creación de una zona segura también se realiza paso a paso. |
| **Por notificaciones** | Notificaciones push | Cada notificación abre directamente la pantalla relacionada: una alerta abre su detalle, un recordatorio abre Rutinas y la salida de una zona segura abre Ubicación. |
| **Indicadores de estado** | Badges | La pestaña Alertas muestra la cantidad de alertas activas, de modo que el usuario las identifica desde cualquier sección. |

Adicionalmente, se establecen las siguientes reglas de navegación:

| Regla | Descripción |
|---|---|
| **Profundidad máxima** | Ninguna pantalla se encuentra a más de tres niveles desde la navegación principal (sección → detalle → edición). |
| **Retorno predecible** | La flecha de regreso y el gesto del sistema siempre devuelven a la pantalla anterior, sin perder filtros ni pestañas seleccionadas. |
| **Estado por sección** | Cada destino de la bottom navigation bar conserva su propio estado; al volver a una sección, el usuario la encuentra donde la dejó. |
| **Prioridad de emergencia** | Una alerta crítica se superpone a cualquier pantalla y lleva al usuario a la acción *Reconocer* en un máximo de dos toques. |

##### Ruta de emergencia

La ruta de emergencia es el recorrido más crítico del producto, por lo que se diseña con el menor número de pasos posible.

| Paso | Pantalla | Acción del usuario | Resultado |
|---|---|---|---|
| **1** | Notificación push | Toca la notificación | Se abre el detalle de la alerta a pantalla completa. |
| **2** | Detalle de alerta | Toca *Reconocer* | Se detiene el escalamiento y se abre el incidente con estado *En atención*. |
| **3** | Incidente en atención | *Llamar*, *Ver ubicación* o *Videollamada* | El usuario se comunica con la persona bajo cuidado o acude a su ubicación. |
| **4** | Incidente en atención | *Marcar estabilizado* y luego *Cerrar incidente* | El incidente se registra en *Alertas › Historial* y en el historial de salud. |

Si la alerta no es reconocida dentro del tiempo de espera configurado, el sistema la escala al siguiente contacto de emergencia según la cadena de escalamiento definida en *Configuración de alertas*.

##### Mapa de navegación de la aplicación

El siguiente diagrama presenta la distribución de las pantallas de la aplicación móvil y las rutas entre ellas.

![mobile-app-navigation-map](../assets/images/chapterIII/navigation-systems/mobile-app-navigation-map.png)

### 3.1.3. Landing Page UI Design

En esta sección se presenta el diseño de la interfaz del Landing Page de Guardian+, primero como wireframes y luego como mock-ups, en sus versiones para escritorio y para dispositivos móviles.

#### 3.1.3.1. Landing Page Wireframe

Los wireframes del Landing Page definen la estructura y la jerarquía de contenido de cada sección del sitio (Cómo funciona, Beneficios, Por qué Guardian+, Precios y Contacto), sin aplicar todavía la paleta de colores del Style Guide.

##### Landing page wireframe desktop

###### Wireframe desktop - Cómo funciona

![landing page wireframe - Cómo funciona](../assets/images/chapterIII/landing-page-wireframes/landing_wireframe__wireframe_1.png)

###### Wireframe desktop - Beneficios

![landing page wireframe - Beneficios](../assets/images/chapterIII/landing-page-wireframes/landing_wireframe__wireframe_2.png)

###### Wireframe desktop - Por qué Guardian+

![landing page wireframe - Por qué Guardian+](../assets/images/chapterIII/landing-page-wireframes/landing_wireframe__wireframe_3.png)

###### Wireframe desktop - Precios

![landing page wireframe - Precios](../assets/images/chapterIII/landing-page-wireframes/landing_wireframe__wireframe_4.png)

###### Wireframe desktop - Contacto

![landing page wireframe - Contacto](../assets/images/chapterIII/landing-page-wireframes/landing_wireframe__wireframe_5.png)

##### Landing page wireframe mobile

<table>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/landing-page-wireframes/landing_wireframe__wireframe_mobile_1.png" alt="landing page wireframe - Cómo funciona" width="200"><br><sub>Cómo funciona</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/landing-page-wireframes/landing_wireframe__wireframe_mobile_2.png" alt="landing page wireframe - Beneficios" width="200"><br><sub>Beneficios</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/landing-page-wireframes/landing_wireframe__wireframe_mobile_3.png" alt="landing page wireframe - Por qué Guardian+" width="200"><br><sub>Por qué Guardian+</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/landing-page-wireframes/landing_wireframe__wireframe_mobile_4.png" alt="landing page wireframe - Precios" width="200"><br><sub>Precios</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/landing-page-wireframes/landing_wireframe__wireframe_mobile_5.png" alt="landing page wireframe - Contacto" width="200"><br><sub>Contacto</sub></td>
  </tr>
</table>


El wireframe de Guardian+ se estructura en escala de grises para validar la arquitectura de información antes de introducir color, tipografía final o imágenes: header de navegación, hero con CTA, sección de 3 preguntas del dolor del usuario, proceso en 3 pasos, grilla de 6 funcionalidades, bloque de diferenciación de marca, tabla de 3 planes de suscripción, formulario de contacto y footer. El menú de navegación (Cómo funciona → Beneficios → Por qué Guardian+ → Precios → Contacto) refleja exactamente ese mismo orden de scroll, siguiendo un flujo narrativo secuencial (problema → solución → diferenciación → precio → acción) coherente con lo definido en Organization Systems.

Jerarquía visual: cada bloque respeta un orden claro de lectura (título grande → subtítulo → contenido de apoyo → acción), reforzado por tamaño y peso tipográfico, no por color — esto permite validar que la jerarquía funciona incluso sin la paleta final.

Principios de diseño aplicados: alineación en grilla de 3 columnas para las tarjetas de pasos, funcionalidades y planes; proximidad (ícono + título + descripción + CTA agrupados en un mismo contenedor); repetición del mismo patrón de tarjeta en las 3 secciones de contenido, para que el usuario reconozca el patrón sin esfuerzo.

Diseño inclusivo: textos cortos y escaneables (títulos de 3-6 palabras, descripciones de una línea), CTAs con texto explícito ("Conocer los planes", no solo un ícono), y formulario de contacto con etiquetas visibles sobre cada campo (no solo placeholder), reduciendo la carga cognitiva para el público objetivo — familiares y cuidadores que buscan tranquilidad, no fricción técnica.

Versión Mobile: las mismas secciones se apilan en una sola columna, el menú colapsa a ícono de hamburguesa, y las grillas de 3 columnas pasan a apilarse verticalmente, manteniendo el mismo orden de lectura que en desktop.

#### 3.1.3.2. Landing Page Mock-up

Los mock-ups del Landing Page aplican sobre los wireframes la paleta de colores, la tipografía y los componentes definidos en el Style Guide, para las mismas secciones del sitio en escritorio y en dispositivos móviles.

##### Landing page mockup desktop

###### Mockup desktop - Cómo funciona

![landing page mockup - Cómo funciona](../assets/images/chapterIII/landing-page-mockups/landing-page-mockups-desktop-1.png)

###### Mockup desktop - Beneficios

![landing page mockup - Beneficios](../assets/images/chapterIII/landing-page-mockups/landing-page-mockups-desktop-2.png)

###### Mockup desktop - Por qué guardian+

![landing page mockup - Por qué guardian plus](../assets/images/chapterIII/landing-page-mockups/landing-page-mockups-desktop-3.png)

###### Mockup desktop - Precios

![landing page mockup - Precios](../assets/images/chapterIII/landing-page-mockups/landing-page-mockups-desktop-4.png)

###### Mockup desktop - Contacto

![landing page mockup - Contacto](../assets/images/chapterIII/landing-page-mockups/landing-page-mockups-desktop-5.png)

##### Landing page mockup mobile

<table>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/landing-page-mockups/landing-page-mockups-mobile-1.png" alt="landing page mockup - Cómo funciona" width="200"><br><sub>Cómo funciona</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/landing-page-mockups/landing-page-mockups-mobile-2.png" alt="landing page mockup - Beneficios" width="200"><br><sub>Beneficios</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/landing-page-mockups/landing-page-mockups-mobile-5.png" alt="landing page mockup - Por qué guardian+" width="200"><br><sub>Por qué guardian+</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/landing-page-mockups/landing-page-mockups-mobile-3.png" alt="landing page mockup - Precios" width="200"><br><sub>Precios</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/landing-page-mockups/landing-page-mockups-mobile-4.png" alt="landing page mockup - Contacto" width="200"><br><sub>Contacto</sub></td>
  </tr>
</table>

### 3.1.4. Mobile Applications UX/UI Design

En esta sección se presenta el diseño de la aplicación móvil de Guardian+ organizado por Bounded Context: los wireframes, los wireflows, los mock-ups, los user flow diagrams y el prototipo navegable.

#### 3.1.4.1. Mobile Applications Wireframes

Los wireframes de la aplicación móvil definen la estructura de las pantallas principales de cada sección. A continuación se presentan agrupados por Bounded Context.

##### Health Monitoring Bounded Context

Los wireframes del Bounded Context **Health Monitoring** definen, en escala de grises, la estructura y jerarquía de las pantallas de la sección **Salud** de la aplicación móvil, sin aplicar todavía la paleta de colores del Style Guide. Cubren las User Stories US01–US05, US07, US19, US21 y US24.

| Pantalla | Descripción |
|---|---|
| Inicio | Pantalla principal del Cuidador. Resume el estado actual del Fragile Citizen, el estado de conexión y batería de la pulsera, las acciones rápidas (Llamar, Videollamada, Ubicación), un resumen de los cinco signos vitales, lo próximo en la agenda y la última alerta. Es el punto de partida de todos los flujos del contexto. |
| Salud · Ahora | Vista en tiempo real del contexto Health Monitoring. Destaca la frecuencia cardíaca con su tendencia reciente y presenta tarjetas de presión arterial, saturación de oxígeno, temperatura y respiración, cada una con su etiqueta de estado. Incluye la tarjeta “Sincronización activa” que comunica el estado del envío de lecturas tomadas sin conexión (US21). |
| Salud · Historial · Ritmo cardíaco | Pestaña Historial con el chip Ritmo seleccionado. Muestra el promedio semanal, mínimo y máximo, la gráfica de tendencia por día y las últimas lecturas registradas con su estado. Da acceso a Exportar PDF y Reporte semanal (US01). |
| Salud · Historial · Presión arterial | Pestaña Historial con el chip Presión seleccionado. Presenta la presión sistólica y diastólica en mmHg, su tendencia semanal y la clasificación de cada lectura (US02). |
| Salud · Historial · Saturación de oxígeno | Pestaña Historial con el chip SpO₂ seleccionado. Presenta el porcentaje de saturación de oxígeno, su tendencia semanal y el estado de cada lectura (US03). |
| Salud · Historial · Temperatura corporal | Pestaña Historial con el chip Temp seleccionado. Presenta la temperatura corporal en °C, su tendencia semanal y el estado de cada lectura para detectar fiebre o hipotermia (US04). |
| Salud · Historial · Frecuencia respiratoria | Pestaña Historial con el chip Respir seleccionado. Presenta la frecuencia respiratoria en rpm, su tendencia semanal y el estado de cada lectura (US05). |
| Buscar y filtrar | Hoja inferior que se abre desde el buscador “Todos los signos vitales”. Permite buscar entre las opciones y combinar criterios por signo vital, periodo (Día, Semana, Mes) y estado, con las acciones Limpiar y Aplicar (US07). |
| Exportar expediente | Hoja inferior que se abre desde Exportar PDF. Permite elegir el periodo (Últimos 30 días, Últimos 7 días o Personalizado), revisar las métricas incluidas y generar el expediente en PDF (US19). |
| Reporte semanal | Hoja inferior que se abre desde Reporte semanal. Resume la estabilidad de signos vitales, las alertas disparadas y la adherencia a la medicación, el comportamiento por parámetro y un aviso cuando se detecta un parámetro recurrente (US24). |

<table>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireframe health monitoring - Inicio" width="200"><br><sub>Inicio</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Monitoreo%20Wireflow.png" alt="wireframe health monitoring - Salud · Ahora" width="200"><br><sub>Salud · Ahora</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Ritmo%20Wireflow.png" alt="wireframe health monitoring - Salud · Historial · Ritmo cardíaco" width="200"><br><sub>Salud · Historial · Ritmo cardíaco</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Presion%20Wireflow.png" alt="wireframe health monitoring - Salud · Historial · Presión arterial" width="200"><br><sub>Salud · Historial · Presión arterial</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Saturacion%20Wireflow.png" alt="wireframe health monitoring - Salud · Historial · Saturación de oxígeno" width="200"><br><sub>Salud · Historial · Saturación de oxígeno</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Temperatura%20Wireflow.png" alt="wireframe health monitoring - Salud · Historial · Temperatura corporal" width="200"><br><sub>Salud · Historial · Temperatura corporal</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Respiracion%20Wireflow.png" alt="wireframe health monitoring - Salud · Historial · Frecuencia respiratoria" width="200"><br><sub>Salud · Historial · Frecuencia respiratoria</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Buscar%20y%20Filtrar%20signos%20Wireflow.png" alt="wireframe health monitoring - Buscar y filtrar" width="200"><br><sub>Buscar y filtrar</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Exportar%20expediente%20Wireflow.png" alt="wireframe health monitoring - Exportar expediente" width="200"><br><sub>Exportar expediente</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Reporte%20semanal%20Wireflow.png" alt="wireframe health monitoring - Reporte semanal" width="200"><br><sub>Reporte semanal</sub></td>
  </tr>
</table>

##### Profile, IAM & Subscriptions

Los siguientes wireframes representan las vistas complementarias de Guardian+ relacionadas con la gestión del perfil, la información de la persona bajo cuidado, el dispositivo asociado, la suscripción y las preferencias de uso. Las pantallas se presentan en escala de grises, conservando la estructura y jerarquía visual definida para los mock-ups finales.

| Pantalla | Descripción |
|---|---|
| Perfil y datos personales | Estas vistas permiten al familiar o cuidador acceder a las principales opciones de su perfil y consultar o actualizar su información personal y de contacto. |
| Persona bajo cuidado | Vista que permite al familiar o cuidador consultar la información principal de la persona bajo cuidado vinculada a su perfil. Presenta los datos de Elena Rojas y la relación existente con el usuario. |
| Círculo de cuidado | Vista que reúne a las personas vinculadas al cuidado de Elena. Permite consultar los integrantes del círculo de cuidado y localizar contactos mediante búsqueda y filtros por rol. |
| Pulsera | Vista destinada a consultar el estado del dispositivo wearable asociado a la persona bajo cuidado. Presenta información de conexión, batería, sincronización e identificación del dispositivo. |
| Mi plan | Vista que permite al familiar o cuidador consultar la suscripción activa de Guardian+, sus beneficios principales y el estado general del plan contratado. |
| Configuración | Vista que centraliza las preferencias generales de la aplicación. Permite acceder a las opciones de idioma, accesibilidad y a la información complementaria de Guardian+. |
| Idioma | Vista que permite seleccionar el idioma de la aplicación entre las opciones disponibles y guardar la preferencia elegida. |
| Accesibilidad | Vista que permite al usuario ajustar preferencias de accesibilidad de la aplicación, incluyendo tamaño de texto, contraste y reducción de movimiento. |
| Acerca de Guardian+ | Vista informativa que presenta datos generales de Guardian+, incluyendo su propósito, versión de la aplicación y acceso a información complementaria del producto. |
| Cerrar sesión | Diálogo de confirmación que permite al usuario cerrar su sesión de Guardian+ de forma segura antes de abandonar la aplicación. |

<table>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-perfil.png" alt="wireframe extras - Perfil" width="200"><br><sub>Perfil</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-mis-datos.png" alt="wireframe extras - Mis datos" width="200"><br><sub>Mis datos</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-persona-bajo-cuidado.png" alt="wireframe extras - Persona bajo cuidado" width="200"><br><sub>Persona bajo cuidado</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-circulo-cuidado.png" alt="wireframe extras - Círculo de cuidado" width="200"><br><sub>Círculo de cuidado</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-pulsera.png" alt="wireframe extras - Pulsera" width="200"><br><sub>Pulsera</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-mi-plan.png" alt="wireframe extras - Mi plan" width="200"><br><sub>Mi plan</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-configuracion.png" alt="wireframe extras - Configuración" width="200"><br><sub>Configuración</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-idioma.png" alt="wireframe extras - Idioma" width="200"><br><sub>Idioma</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-accesibilidad.png" alt="wireframe extras - Accesibilidad" width="200"><br><sub>Accesibilidad</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-acerca-guardian.png" alt="wireframe extras - Acerca de Guardian+" width="200"><br><sub>Acerca de Guardian+</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-cerrar-sesion.png" alt="wireframe extras - Cerrar sesión" width="200"><br><sub>Cerrar sesión</sub></td>
  </tr>
</table>

##### Emergency & Alerting Bounded Context

Los wireframes de la sección **Alertas** presentan en escala de grises las pantallas con las que el familiar o cuidador recibe, atiende y revisa las alertas de la persona bajo cuidado. Cubren las User Stories US08, US09, US10, US11, US15 y US16.

<table>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/emergency-alerting/wireframes/alertas-activas.png" alt="wireframe emergency alerting - Alertas activas" width="200"><br><sub>Alertas activas</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/emergency-alerting/wireframes/detalle-alerta-critica.png" alt="wireframe emergency alerting - Detalle de alerta crítica" width="200"><br><sub>Detalle de alerta crítica</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/emergency-alerting/wireframes/alerta-sos.png" alt="wireframe emergency alerting - Alerta SOS" width="200"><br><sub>Alerta SOS</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/emergency-alerting/wireframes/historial-alertas.png" alt="wireframe emergency alerting - Historial de alertas" width="200"><br><sub>Historial de alertas</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/emergency-alerting/wireframes/alerta-estabilizada.png" alt="wireframe emergency alerting - Alerta estabilizada" width="200"><br><sub>Alerta estabilizada</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/emergency-alerting/wireframes/contactos-emergencia.png" alt="wireframe emergency alerting - Contactos de emergencia" width="200"><br><sub>Contactos de emergencia</sub></td>
  </tr>
</table>

##### Care Routines & Wellness Bounded Context

Los wireframes de la sección **Rutinas** muestran el resumen diario de rutinas y las pantallas para programar tomas de medicación, citas médicas y actividad ligera. Cubren las User Stories US06, US13 y US14.

<table>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/care-routines/wireframes/rutinas.png" alt="wireframe care routines - Rutinas" width="200"><br><sub>Rutinas</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/care-routines/wireframes/medicacion.png" alt="wireframe care routines - Medicación" width="200"><br><sub>Medicación</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/care-routines/wireframes/nueva-toma.png" alt="wireframe care routines - Nueva toma" width="200"><br><sub>Nueva toma</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/care-routines/wireframes/citas-medicas.png" alt="wireframe care routines - Citas médicas" width="200"><br><sub>Citas médicas</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/care-routines/wireframes/nueva-cita.png" alt="wireframe care routines - Nueva cita" width="200"><br><sub>Nueva cita</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/care-routines/wireframes/actividad-ligera.png" alt="wireframe care routines - Actividad ligera" width="200"><br><sub>Actividad ligera</sub></td>
  </tr>
</table>


#### 3.1.4.2. Mobile Applications Wireflow Diagrams

Los wireflow diagrams combinan los wireframes con las interacciones que conectan cada pantalla y muestran cómo el usuario cumple cada user goal. Se presentan agrupados por Bounded Context.

##### Health Monitoring Bounded Context

Los wireflows del Bounded Context **Health Monitoring** combinan los wireframes de la sección **Salud** con las interacciones que conectan cada pantalla. Cada wireflow corresponde a un user goal del Cuidador y muestra la secuencia de pantallas, de izquierda a derecha, y la acción que dispara cada transición.

###### Wireflow 1 - Consultar ritmo cardíaco (US01)

**User goal:** Como cuidador, quiero consultar la lectura actual del ritmo cardíaco de la persona bajo cuidado, para monitorear su estabilidad cardiovascular e identificar irregularidades oportunamente.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow US01 - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca “Salud”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Monitoreo%20Wireflow.png" alt="wireflow US01 - Salud · Ahora" width="170"><br><sub>Salud · Ahora</sub></td>
    <td align="center"><sub>Toca “Historial” y el chip “Ritmo”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Ritmo%20Wireflow.png" alt="wireflow US01 - Ritmo cardíaco" width="170"><br><sub>Ritmo cardíaco</sub></td>
  </tr>
</table>

###### Wireflow 2 - Consultar presión arterial (US02)

**User goal:** Como cuidador, quiero consultar la presión arterial sistólica y diastólica de la persona bajo cuidado, para evaluar su condición hemodinámica y prevenir descompensaciones.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow US02 - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca “Salud”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Monitoreo%20Wireflow.png" alt="wireflow US02 - Salud · Ahora" width="170"><br><sub>Salud · Ahora</sub></td>
    <td align="center"><sub>Toca “Historial” y el chip “Presión”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Presion%20Wireflow.png" alt="wireflow US02 - Presión arterial" width="170"><br><sub>Presión arterial</sub></td>
  </tr>
</table>

###### Wireflow 3 - Consultar saturación de oxígeno (US03)

**User goal:** Como cuidador, quiero consultar la saturación de oxígeno de la persona bajo cuidado, para identificar hipoxemia o dificultad respiratoria.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow US03 - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca “Salud”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Monitoreo%20Wireflow.png" alt="wireflow US03 - Salud · Ahora" width="170"><br><sub>Salud · Ahora</sub></td>
    <td align="center"><sub>Toca “Historial” y el chip “SpO₂”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Saturacion%20Wireflow.png" alt="wireflow US03 - Saturación de oxígeno" width="170"><br><sub>Saturación de oxígeno</sub></td>
  </tr>
</table>

###### Wireflow 4 - Supervisar temperatura corporal (US04)

**User goal:** Como cuidador, quiero supervisar la temperatura corporal de la persona bajo cuidado, para detectar oportunamente fiebre o hipotermia.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow US04 - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca “Salud”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Monitoreo%20Wireflow.png" alt="wireflow US04 - Salud · Ahora" width="170"><br><sub>Salud · Ahora</sub></td>
    <td align="center"><sub>Toca “Historial” y el chip “Temp”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Temperatura%20Wireflow.png" alt="wireflow US04 - Temperatura corporal" width="170"><br><sub>Temperatura corporal</sub></td>
  </tr>
</table>

###### Wireflow 5 - Consultar frecuencia respiratoria (US05)

**User goal:** Como cuidador, quiero consultar la frecuencia respiratoria de la persona bajo cuidado, para identificar taquipnea o bradipnea.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow US05 - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca “Salud”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Monitoreo%20Wireflow.png" alt="wireflow US05 - Salud · Ahora" width="170"><br><sub>Salud · Ahora</sub></td>
    <td align="center"><sub>Toca “Historial” y el chip “Respir”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Respiracion%20Wireflow.png" alt="wireflow US05 - Frecuencia respiratoria" width="170"><br><sub>Frecuencia respiratoria</sub></td>
  </tr>
</table>

###### Wireflow 6 - Analizar tendencias históricas (US07)

**User goal:** Como cuidador, quiero revisar tendencias históricas de signos vitales, para identificar patrones de deterioro y compartir información con el médico.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow US07 - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca “Salud”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Monitoreo%20Wireflow.png" alt="wireflow US07 - Salud · Ahora" width="170"><br><sub>Salud · Ahora</sub></td>
    <td align="center"><sub>Toca “Todos los signos vitales”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Buscar%20y%20Filtrar%20signos%20Wireflow.png" alt="wireflow US07 - Buscar y filtrar" width="170"><br><sub>Buscar y filtrar</sub></td>
    <td align="center"><sub>Elige signo y periodo y toca “Aplicar”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Ritmo%20Wireflow.png" alt="wireflow US07 - Tendencia filtrada" width="170"><br><sub>Tendencia filtrada</sub></td>
  </tr>
</table>

###### Wireflow 7 - Exportar historial de telemetría (US19)

**User goal:** Como cuidador, quiero generar y exportar el historial de signos vitales, para respaldar las consultas médicas presenciales.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow US19 - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca “Salud”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Monitoreo%20Wireflow.png" alt="wireflow US19 - Salud · Ahora" width="170"><br><sub>Salud · Ahora</sub></td>
    <td align="center"><sub>Toca “Historial”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Ritmo%20Wireflow.png" alt="wireflow US19 - Historial" width="170"><br><sub>Historial</sub></td>
    <td align="center"><sub>Toca “Exportar PDF”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Exportar%20expediente%20Wireflow.png" alt="wireflow US19 - Exportar expediente" width="170"><br><sub>Exportar expediente</sub></td>
  </tr>
</table>

###### Wireflow 8 - Sincronizar telemetría sin conexión (US21)

**User goal:** Como cuidador, quiero que las lecturas tomadas sin red se almacenen y sincronicen al recuperar conexión, para conservar íntegro el historial.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow US21 - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca “Salud”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Monitoreo%20Wireflow.png" alt="wireflow US21 - Salud · Ahora (tarjeta “Sincronización activa”)" width="170"><br><sub>Salud · Ahora (tarjeta “Sincronización activa”)</sub></td>
  </tr>
</table>

###### Wireflow 9 - Revisar reporte semanal de salud (US24)

**User goal:** Como cuidador, quiero recibir una síntesis semanal del estado de salud, para evaluar la evolución global sin revisar la telemetría continuamente.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow US24 - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca “Salud”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Monitoreo%20Wireflow.png" alt="wireflow US24 - Salud · Ahora" width="170"><br><sub>Salud · Ahora</sub></td>
    <td align="center"><sub>Toca “Historial”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Ritmo%20Wireflow.png" alt="wireflow US24 - Historial" width="170"><br><sub>Historial</sub></td>
    <td align="center"><sub>Toca “Reporte semanal”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Reporte%20semanal%20Wireflow.png" alt="wireflow US24 - Reporte semanal" width="170"><br><sub>Reporte semanal</sub></td>
  </tr>
</table>

##### Extras

Los wireflows de **Extras** combinan los wireframes relacionados con el perfil, el entorno de cuidado, la suscripción, las preferencias de la aplicación y la gestión de sesión. Cada wireflow corresponde a un user goal del Familiar o Cuidador y muestra la secuencia de pantallas, de izquierda a derecha, junto con la acción que dispara cada transición.

###### Wireflow 1 - Gestionar información personal

User goal: Como familiar o cuidador, quiero consultar y actualizar mis datos personales y de contacto, para mantener correcta la información asociada a mi perfil en Guardian+.
<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow extras - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca su avatar</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-perfil.png" alt="wireflow extras - Perfil" width="170"><br><sub>Perfil</sub></td>
    <td align="center"><sub>Toca “Mis datos”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-mis-datos.png" alt="wireflow extras - Mis datos" width="170"><br><sub>Mis datos</sub></td>
  </tr>
</table>

###### Wireflow 2 - Consultar entorno de cuidado

**User goal:** Como familiar o cuidador, quiero consultar la información de Elena, las personas vinculadas a su cuidado y el estado de su pulsera, para mantenerme informado sobre su entorno de cuidado.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow extras - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca su avatar</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-perfil.png" alt="wireflow extras - Perfil" width="170"><br><sub>Perfil</sub></td>
    <td align="center"><sub>Toca “Persona bajo cuidado”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-persona-bajo-cuidado.png" alt="wireflow extras - Persona bajo cuidado" width="170"><br><sub>Persona bajo cuidado</sub></td>
  </tr>
</table>

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow extras - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca su avatar</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-perfil.png" alt="wireflow extras - Perfil" width="170"><br><sub>Perfil</sub></td>
    <td align="center"><sub>Toca “Círculo de cuidado”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-circulo-cuidado.png" alt="wireflow extras - Círculo de cuidado" width="170"><br><sub>Círculo de cuidado</sub></td>
  </tr>
</table>

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow extras - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca su avatar</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-perfil.png" alt="wireflow extras - Perfil" width="170"><br><sub>Perfil</sub></td>
    <td align="center"><sub>Toca “Pulsera”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-pulsera.png" alt="wireflow extras - Pulsera" width="170"><br><sub>Pulsera</sub></td>
  </tr>
</table>

###### Wireflow 3 - Consultar suscripción actual

**User goal:** Como familiar o cuidador, quiero consultar mi plan actual y sus beneficios, para conocer las funcionalidades disponibles en mi suscripción de Guardian+.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow extras - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca su avatar</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-perfil.png" alt="wireflow extras - Perfil" width="170"><br><sub>Perfil</sub></td>
    <td align="center"><sub>Toca “Mi plan”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-mi-plan.png" alt="wireflow extras - Mi plan" width="170"><br><sub>Mi plan</sub></td>
  </tr>
</table>

###### Wireflow 4 - Configurar preferencias de la aplicación

**User goal:** Como familiar o cuidador, quiero ajustar el idioma y las opciones de accesibilidad de Guardian+, para adaptar la aplicación a mis necesidades de uso.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow extras - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca su avatar</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-perfil.png" alt="wireflow extras - Perfil" width="170"><br><sub>Perfil</sub></td>
    <td align="center"><sub>Toca “Configuración”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-configuracion.png" alt="wireflow extras - Configuración" width="170"><br><sub>Configuración</sub></td>
    <td align="center"><sub>Toca “Idioma”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-idioma.png" alt="wireflow extras - Idioma" width="170"><br><sub>Idioma</sub></td>
  </tr>
</table>

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow extras - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca su avatar</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-perfil.png" alt="wireflow extras - Perfil" width="170"><br><sub>Perfil</sub></td>
    <td align="center"><sub>Toca “Configuración”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-configuracion.png" alt="wireflow extras - Configuración" width="170"><br><sub>Configuración</sub></td>
    <td align="center"><sub>Toca “Accesibilidad”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-accesibilidad.png" alt="wireflow extras - Accesibilidad" width="170"><br><sub>Accesibilidad</sub></td>
  </tr>
</table>

###### Wireflow 5 - Cerrar sesión de forma segura

**User goal:** Como familiar o cuidador, quiero cerrar mi sesión de Guardian+, para proteger el acceso a la información de la persona bajo cuidado cuando termine de utilizar la aplicación.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow extras - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca su avatar</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-perfil.png" alt="wireflow extras - Perfil" width="170"><br><sub>Perfil</sub></td>
    <td align="center"><sub>Toca “Cerrar sesión”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/extras/mockups/wireframe-cerrar-sesion.png" alt="wireflow extras - Confirmar cierre de sesión" width="170"><br><sub>Confirmar cierre de sesión</sub></td>
  </tr>
</table>


##### Emergency & Alerting Bounded Context

Los wireflows de **Alertas** siguen el recorrido de los tres tipos de alerta de Guardian+: una caída detectada por la pulsera, un pedido de auxilio con el botón SOS y una alerta por signos vitales fuera de rango.

###### Wireflow 1 - Atender una alerta de caída (US08, US11)

**User goal:** Como familiar de Elena, quiero enterarme de inmediato cuando la pulsera detecte una caída y atenderla, para asegurarme de que reciba ayuda a tiempo.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/emergency-alerting/wireframes/alertas-activas.png" alt="wireflow emergency alerting - Alertas activas" width="170"><br><sub>Alertas activas</sub></td>
    <td align="center"><sub>Toca la alerta de caída</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/emergency-alerting/wireframes/detalle-alerta-critica.png" alt="wireflow emergency alerting - Detalle de alerta crítica" width="170"><br><sub>Detalle de alerta crítica</sub></td>
    <td align="center"><sub>Reconoce la alerta y cierra el incidente</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/emergency-alerting/wireframes/historial-alertas.png" alt="wireflow emergency alerting - Historial" width="170"><br><sub>Historial</sub></td>
  </tr>
</table>

###### Wireflow 2 - Responder a un SOS (US15)

**User goal:** Como cuidadora de Elena, quiero recibir su pedido de auxilio en cuanto presione el botón SOS de la pulsera, para saber dónde está y actuar sin perder tiempo.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png" alt="wireflow emergency alerting - Inicio" width="170"><br><sub>Inicio</sub></td>
    <td align="center"><sub>Toca la notificación SOS</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/emergency-alerting/wireframes/alerta-sos.png" alt="wireflow emergency alerting - Alerta SOS" width="170"><br><sub>Alerta SOS</sub></td>
    <td align="center"><sub>Reconoce la alerta y atiende a Elena</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/emergency-alerting/wireframes/historial-alertas.png" alt="wireflow emergency alerting - Historial" width="170"><br><sub>Historial</sub></td>
  </tr>
</table>

###### Wireflow 3 - Seguir una alerta de signos vitales (US09, US10)

**User goal:** Como familiar de Elena, quiero enterarme cuando sus signos vitales salgan del rango seguro y seguir la alerta hasta que se normalicen, para intervenir solo cuando realmente haga falta.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/emergency-alerting/wireframes/alertas-activas.png" alt="wireflow emergency alerting - Alertas activas" width="170"><br><sub>Alertas activas</sub></td>
    <td align="center"><sub>Reconoce la alerta de ritmo cardíaco</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/emergency-alerting/wireframes/alerta-estabilizada.png" alt="wireflow emergency alerting - Alerta estabilizada" width="170"><br><sub>Alerta estabilizada</sub></td>
    <td align="center"><sub>Toca “Cerrar incidente”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/emergency-alerting/wireframes/historial-alertas.png" alt="wireflow emergency alerting - Historial" width="170"><br><sub>Historial</sub></td>
  </tr>
</table>

##### Care Routines & Wellness Bounded Context

Los wireflows de **Rutinas** muestran cómo el cuidador programa un recordatorio desde el resumen diario de rutinas.

###### Wireflow 1 - Programar una toma de medicación (US06)

**User goal:** Como cuidador, deseo programar las tomas de medicación del Fragile Citizen y que su pulsera emita los avisos hápticos y sonoros en los horarios exactos para asegurar la adherencia al tratamiento prescrito.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/care-routines/wireframes/rutinas.png" alt="wireflow care routines - Rutinas" width="170"><br><sub>Rutinas</sub></td>
    <td align="center"><sub>Toca “Medicación”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/care-routines/wireframes/medicacion.png" alt="wireflow care routines - Medicación" width="170"><br><sub>Medicación</sub></td>
    <td align="center"><sub>Toca “+”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/care-routines/wireframes/nueva-toma.png" alt="wireflow care routines - Nueva toma" width="170"><br><sub>Nueva toma</sub></td>
  </tr>
</table>

###### Wireflow 2 - Agendar una cita médica (US13)

**User goal:** Como cuidador, deseo agendar los controles y citas médicas del Fragile Citizen para recibir avisos preventivos y evitar inasistencias a los centros de salud.

<table>
  <tr>
    <td align="center"><img src="../assets/images/chapterIII/care-routines/wireframes/rutinas.png" alt="wireflow care routines - Rutinas" width="170"><br><sub>Rutinas</sub></td>
    <td align="center"><sub>Toca “Citas médicas”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/care-routines/wireframes/citas-medicas.png" alt="wireflow care routines - Citas médicas" width="170"><br><sub>Citas médicas</sub></td>
    <td align="center"><sub>Toca “+”</sub><br>&#10140;</td>
    <td align="center"><img src="../assets/images/chapterIII/care-routines/wireframes/nueva-cita.png" alt="wireflow care routines - Nueva cita" width="170"><br><sub>Nueva cita</sub></td>
  </tr>
</table>


#### 3.1.4.3. Mobile Applications Mock-ups

Los mock-ups aplican el Style Guide sobre los wireframes y representan la apariencia final de las pantallas de la aplicación móvil. Se presentan agrupados por Bounded Context.

##### Health Monitoring Bounded Context

Los mock-ups del Bounded Context **Health Monitoring** aplican sobre los wireframes la paleta de colores, tipografía, elevaciones y etiquetas de estado definidas en el Style Guide (3.1.1). El verde identifica las acciones primarias y los estados normales, y el ámbar resalta las lecturas “En Observación”.

| Pantalla | Descripción |
|---|---|
| Inicio | Pantalla principal del Cuidador. Resume el estado actual del Fragile Citizen, el estado de conexión y batería de la pulsera, las acciones rápidas (Llamar, Videollamada, Ubicación), un resumen de los cinco signos vitales, lo próximo en la agenda y la última alerta. Es el punto de partida de todos los flujos del contexto. |
| Salud · Ahora | Vista en tiempo real del contexto Health Monitoring. Destaca la frecuencia cardíaca con su tendencia reciente y presenta tarjetas de presión arterial, saturación de oxígeno, temperatura y respiración, cada una con su etiqueta de estado. Incluye la tarjeta “Sincronización activa” que comunica el estado del envío de lecturas tomadas sin conexión (US21). |
| Salud · Historial · Ritmo cardíaco | Pestaña Historial con el chip Ritmo seleccionado. Muestra el promedio semanal, mínimo y máximo, la gráfica de tendencia por día y las últimas lecturas registradas con su estado. Da acceso a Exportar PDF y Reporte semanal (US01). |
| Salud · Historial · Presión arterial | Pestaña Historial con el chip Presión seleccionado. Presenta la presión sistólica y diastólica en mmHg, su tendencia semanal y la clasificación de cada lectura (US02). |
| Salud · Historial · Saturación de oxígeno | Pestaña Historial con el chip SpO₂ seleccionado. Presenta el porcentaje de saturación de oxígeno, su tendencia semanal y el estado de cada lectura (US03). |
| Salud · Historial · Temperatura corporal | Pestaña Historial con el chip Temp seleccionado. Presenta la temperatura corporal en °C, su tendencia semanal y el estado de cada lectura para detectar fiebre o hipotermia (US04). |
| Salud · Historial · Frecuencia respiratoria | Pestaña Historial con el chip Respir seleccionado. Presenta la frecuencia respiratoria en rpm, su tendencia semanal y el estado de cada lectura (US05). |
| Buscar y filtrar | Hoja inferior que se abre desde el buscador “Todos los signos vitales”. Permite buscar entre las opciones y combinar criterios por signo vital, periodo (Día, Semana, Mes) y estado, con las acciones Limpiar y Aplicar (US07). |
| Exportar expediente | Hoja inferior que se abre desde Exportar PDF. Permite elegir el periodo (Últimos 30 días, Últimos 7 días o Personalizado), revisar las métricas incluidas y generar el expediente en PDF (US19). |
| Reporte semanal | Hoja inferior que se abre desde Reporte semanal. Resume la estabilidad de signos vitales, las alertas disparadas y la adherencia a la medicación, el comportamiento por parámetro y un aviso cuando se detecta un parámetro recurrente (US24). |

<table>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen.png" alt="mockup health monitoring - Inicio" width="200"><br><sub>Inicio</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Monitoreo.png" alt="mockup health monitoring - Salud · Ahora" width="200"><br><sub>Salud · Ahora</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Ritmo.png" alt="mockup health monitoring - Salud · Historial · Ritmo cardíaco" width="200"><br><sub>Salud · Historial · Ritmo cardíaco</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Presion.png" alt="mockup health monitoring - Salud · Historial · Presión arterial" width="200"><br><sub>Salud · Historial · Presión arterial</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Saturacion.png" alt="mockup health monitoring - Salud · Historial · Saturación de oxígeno" width="200"><br><sub>Salud · Historial · Saturación de oxígeno</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Temperatura.png" alt="mockup health monitoring - Salud · Historial · Temperatura corporal" width="200"><br><sub>Salud · Historial · Temperatura corporal</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Respiracion.png" alt="mockup health monitoring - Salud · Historial · Frecuencia respiratoria" width="200"><br><sub>Salud · Historial · Frecuencia respiratoria</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Buscar%20y%20Filtrar%20signos.png" alt="mockup health monitoring - Buscar y filtrar" width="200"><br><sub>Buscar y filtrar</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Exportar%20expediente.png" alt="mockup health monitoring - Exportar expediente" width="200"><br><sub>Exportar expediente</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Reporte%20semanal.png" alt="mockup health monitoring - Reporte semanal" width="200"><br><sub>Reporte semanal</sub></td>
  </tr>
</table>

##### Extras

Los mock-ups de **Extras** aplican el Design System de Guardian+ a las vistas relacionadas con el perfil, el entorno de cuidado, la suscripción, las preferencias de la aplicación y la gestión de sesión. Las pantallas mantienen la paleta, tipografía, jerarquía visual y componentes definidos en las Style Guidelines.

| Pantalla | Descripción |
|---|---|
| Perfil | Pantalla principal del perfil del familiar o cuidador. Centraliza el acceso a los datos personales, la información de la persona bajo cuidado, el círculo de cuidado, la pulsera, la suscripción, las preferencias de la aplicación y el cierre de sesión. |
| Mis datos | Vista destinada a consultar y actualizar la información personal y de contacto del familiar o cuidador, incluyendo nombre, correo electrónico, teléfono y datos adicionales asociados al perfil. |
| Persona bajo cuidado | Vista que permite al familiar o cuidador consultar la información principal de la persona bajo cuidado vinculada a su perfil, mostrando sus datos generales y la relación existente con el usuario. |
| Círculo de cuidado | Vista que presenta a las personas vinculadas al cuidado de Elena. Permite consultar los integrantes del círculo de cuidado y localizar contactos mediante búsqueda y filtros por rol. |
| Pulsera | Vista que permite consultar el estado del dispositivo wearable asociado a la persona bajo cuidado, incluyendo información de conexión, batería, sincronización y datos de identificación del dispositivo. |
| Mi plan | Vista que permite al familiar o cuidador consultar la suscripción activa de Guardian+, sus beneficios principales y el estado general del plan contratado. |
| Configuración | Vista que centraliza las preferencias generales de la aplicación y proporciona acceso a las opciones de idioma, accesibilidad e información complementaria de Guardian+. |
| Idioma | Vista que permite seleccionar el idioma de la aplicación entre las opciones disponibles y guardar la preferencia elegida. |
| Accesibilidad | Vista que permite ajustar preferencias de accesibilidad de la aplicación, incluyendo tamaño de texto, contraste y reducción de movimiento. |
| Acerca de Guardian+ | Vista informativa que presenta el propósito de Guardian+, la versión de la aplicación y el acceso a información complementaria del producto. |
| Cerrar sesión | Diálogo de confirmación que permite al usuario cerrar su sesión de Guardian+ de forma segura antes de abandonar la aplicación. |

<table>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/mockups/mockup-perfil.png" alt="mockup extras - Perfil" width="200"><br><sub>Perfil</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/mockups/mockup-mis-datos.png" alt="mockup extras - Mis datos" width="200"><br><sub>Mis datos</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/mockups/mockup-persona-bajo-cuidado.png" alt="mockup extras - Persona bajo cuidado" width="200"><br><sub>Persona bajo cuidado</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/mockups/mockup-circulo-cuidado.png" alt="mockup extras - Círculo de cuidado" width="200"><br><sub>Círculo de cuidado</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/mockups/mockup-pulsera.png" alt="mockup extras - Pulsera" width="200"><br><sub>Pulsera</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/mockups/mockup-mi-plan.png" alt="mockup extras - Mi plan" width="200"><br><sub>Mi plan</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/mockups/mockup-configuracion.png" alt="mockup extras - Configuración" width="200"><br><sub>Configuración</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/mockups/mockup-idioma.png" alt="mockup extras - Idioma" width="200"><br><sub>Idioma</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/mockups/mockup-accesibilidad.png" alt="mockup extras - Accesibilidad" width="200"><br><sub>Accesibilidad</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/mockups/mockup-acerca-guardian.png" alt="mockup extras - Acerca de Guardian+" width="200"><br><sub>Acerca de Guardian+</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/user-flow-diagrams/mockups/mockup-cerrar-sesion.png" alt="mockup extras - Cerrar sesión" width="200"><br><sub>Cerrar sesión</sub></td>
  </tr>
</table>

##### Emergency & Alerting Bounded Context

Los mock-ups de **Alertas** aplican el Style Guide (3.1.1) con un criterio de severidad: el rojo identifica las alertas críticas y el SOS, el ámbar las alertas de prioridad media y el verde las alertas estabilizadas o atendidas.

<table>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/emergency-alerting/mockups/alertas-activas.png" alt="mockup emergency alerting - Alertas activas" width="200"><br><sub>Alertas activas</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/emergency-alerting/mockups/detalle-alerta-critica.png" alt="mockup emergency alerting - Detalle de alerta crítica" width="200"><br><sub>Detalle de alerta crítica</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/emergency-alerting/mockups/alerta-sos.png" alt="mockup emergency alerting - Alerta SOS" width="200"><br><sub>Alerta SOS</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/emergency-alerting/mockups/historial-alertas.png" alt="mockup emergency alerting - Historial de alertas" width="200"><br><sub>Historial de alertas</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/emergency-alerting/mockups/alerta-estabilizada.png" alt="mockup emergency alerting - Alerta estabilizada" width="200"><br><sub>Alerta estabilizada</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/emergency-alerting/mockups/contactos-emergencia.png" alt="mockup emergency alerting - Contactos de emergencia" width="200"><br><sub>Contactos de emergencia</sub></td>
  </tr>
</table>

##### Care Routines & Wellness Bounded Context

Los mock-ups de **Rutinas** usan el verde para las rutinas completadas y las acciones principales, y el ámbar para las tomas pendientes y los avisos preventivos.

<table>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/care-routines/mockups/rutinas.png" alt="mockup care routines - Rutinas" width="200"><br><sub>Rutinas</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/care-routines/mockups/medicacion.png" alt="mockup care routines - Medicación" width="200"><br><sub>Medicación</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/care-routines/mockups/nueva-toma.png" alt="mockup care routines - Nueva toma" width="200"><br><sub>Nueva toma</sub></td>
  </tr>
  <tr>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/care-routines/mockups/citas-medicas.png" alt="mockup care routines - Citas médicas" width="200"><br><sub>Citas médicas</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/care-routines/mockups/nueva-cita.png" alt="mockup care routines - Nueva cita" width="200"><br><sub>Nueva cita</sub></td>
    <td align="center" valign="top"><img src="../assets/images/chapterIII/care-routines/mockups/actividad-ligera.png" alt="mockup care routines - Actividad ligera" width="200"><br><sub>Actividad ligera</sub></td>
  </tr>
</table>


#### 3.1.4.4. Mobile Applications User Flow Diagrams

Los user flow diagrams describen, para cada user goal, la secuencia de acciones del usuario en la aplicación y las respuestas del sistema. Cada diagrama se acompaña de la User Persona, el número de flujo y el user goal que representa, y se presentan agrupados por Bounded Context.

##### Mobility & Geofencing Bounded Context

Los user flows de Mobility & Geofencing cubren la consulta de la ubicación en tiempo real de la persona bajo cuidado, la comunicación directa con ella mediante llamada o videollamada y la configuración de zonas seguras.

<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Cuidador</td>
    <td class="header">Número</td>
    <td>1</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como Cuidador, quiero consultar en tiempo real la ubicación del Fragile Citizen mediante las coordenadas de geolocalización de su pulsera, para verificar su paradero y actuar rápidamente ante una posible desorientación.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
    <li>Cuidador inicia sesión en la aplicación</li>
    <li>El sistema muestra la pantalla principal con los Fragile Citizens asociados.</li>
    <li>Cuidador selecciona al Fragile Citizen que desea localizar.</li>
    <li>El sistema muestra la vista de Localización/Mapa.</li>
    <li>El Cuidador solicita la ubicación actual.</li>
    <li>El sistema consulta la telemetría de geolocalización de la pulsera</li>
    <li>¿Existe cobertura GNSS activa? Sí → el sistema obtiene la posición actual.</li>
    <li>El sistema recibe las coordenadas de latitud y longitud.</li>
    <li>El sistema verifica que la información tenga una marca de tiempo dentro de los últimos 30 segundos.</li>
    <li>El sistema muestra la ubicación actual del Fragile Citizen en el mapa</li>
    <li>Se muestran las coordenadas y la hora de última actualización. El Cuidador verifica el paradero del Fragile Citizen.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador selecciona al Fragile Citizen.</li>
    <li>El Cuidador solicita su ubicación actual.</li>
    <li>¿Existe cobertura GNSS activa? No → el sistema detecta que no existe una fijación satelital válida.</li>
    <li>El sistema recupera el último punto geográfico válido conocido.</li>
    <li>El sistema muestra dicho punto en el mapa.</li>
    <li>El sistema presenta una advertencia indicando que existe una pérdida momentánea de señal GNSS.</li>
    <li>El sistema muestra la marca de tiempo correspondiente al último punto válido, diferenciándola de una ubicación en tiempo real.</li>
    <li>El Cuidador puede continuar monitoreando la ubicación hasta que se restablezca la señal.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow diagram1 - Cuidador](../assets/images/chapterIII/user-flow-diagrams/user_flow_1.png)

<hr>
<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Famliar</td>
    <td class="header">Número</td>
    <td>2</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como Familiar, quiero iniciar una comunicación directa con el Fragile Citizen mediante videollamada o llamada de voz, según las capacidades de la pulsera, para verificar su condición ante una inquietud o situación cotidiana.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
    <li>El Familiar selecciona al Fragile Citizen desde la aplicación.</li>
    <li>Solicita iniciar una videollamada.</li>
    <li>El sistema verifica las capacidades de comunicación de la pulsera.</li>
    <li>La pulsera cuenta con cámara, pantalla y conexión de datos activa.</li>
    <li>El sistema establece la sesión de videollamada.</li>
    <li>Se confirma la conexión entre el Familiar y el Fragile Citizen.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ul>
    <li>Sin cámara: Si la pulsera permite comunicación por audio, pero no dispone de cámara, el sistema informa la limitación y cambia automáticamente la solicitud a una llamada de voz.</li>
    <li>Sin comunicación bidireccional: Si la pulsera solo permite telemetría, avisos hápticos y SOS, el sistema informa que no admite llamadas y ofrece realizar una llamada telefónica al número registrado.</li>
    <li>Llamada no contestada: Si el Fragile Citizen no responde después de 30 segundos, el sistema finaliza el intento y registra la llamada como no atendida en el historial.</li>
    </ul>
    </td>
  </tr>
</table>

![user flow diagram1 - Cuidador](../assets/images/chapterIII/user-flow-diagrams/user_flow_2.png)

<hr>
<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Cuidador</td>
    <td class="header">Número</td>
    <td>3</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como Cuidador, quiero configurar y monitorear múltiples zonas geográficas seguras para recibir alertas cuando el Fragile Citizen salga de los perímetros autorizados y ser informado cuando reingrese a una zona segura.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador configura una o más geocercas, como hogar, parque o club.</li>
    <li>Define las coordenadas y el radio de cada zona segura.</li>
    <li>El sistema activa las geocercas y comienza el monitoreo.</li>
    <li>El Fragile Citizen permanece dentro de una zona segura.</li>
    <li>El sistema verifica continuamente las coordenadas del dispositivo.</li>
    <li>Cuando el Fragile Citizen reingresa a una zona después de haber estado fuera, el sistema notifica el reingreso al perímetro seguro.</li>
    <li>Se restablece la condición de vigilancia regular.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ul>
    <li>Salida de todas las zonas seguras: Si las coordenadas se mantienen fuera de todas las geocercas activas, el sistema genera una alerta de egreso y la envía inmediatamente al Cuidador.</li>
    <li>Múltiples geocercas: Si existen varias zonas configuradas, el sistema debe verificar la posición respecto a todas las zonas activas antes de generar una alerta de salida.</li>
    <li>Reingreso: Si el Fragile Citizen vuelve a ingresar a cualquiera de las zonas autorizadas, el sistema notifica el reingreso y vuelve al estado de vigilancia regular.</li>
    </td>
    </ul>
  </tr>
</table>

![user flow diagram1 - Cuidador](../assets/images/chapterIII/user-flow-diagrams/user_flow_3.png)

<hr>

##### Health Monitoring Bounded Context

Los siguientes user flows corresponden al Bounded Context **Health Monitoring** y describen cómo la Cuidadora (User Persona: Roxana Paola Diana Ramírez) consulta, analiza, exporta y sincroniza los signos vitales del Fragile Citizen desde la sección **Salud**. Cada diagrama muestra el happy path con flechas continuas y el unhappy path con flechas discontinuas en rojo.

<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Cuidador (Roxana Paola Diana Ramírez)</td>
    <td class="header">Número</td>
    <td>1 · US01</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como cuidador, quiero consultar la lectura actual del ritmo cardíaco de la persona bajo cuidado, para monitorear su estabilidad cardiovascular e identificar irregularidades oportunamente.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador necesita revisar el indicador y se encuentra en la pantalla de Inicio.</li>
    <li>El Cuidador toca Salud.</li>
    <li>El sistema muestra la pantalla Salud con los signos vitales en tiempo real.</li>
    <li>El Cuidador selecciona Ritmo cardíaco.</li>
    <li>El sistema muestra la pantalla de consulta de ritmo cardíaco.</li>
    <li>¿Hay lectura válida? Sí → el sistema muestra el valor, la tendencia y el estado.</li>
    <li>El Cuidador comprende el estado cardíaco del Fragile Citizen.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador selecciona Ritmo cardíaco.</li>
    <li>¿Hay lectura válida? No → el sistema no recibe una lectura válida de la pulsera.</li>
    <li>El sistema muestra el último valor válido junto con el indicador “Sin señal”.</li>
    <li>El Cuidador puede continuar el seguimiento con contexto.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow diagram 1 - Health Monitoring - US01](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/flows/User%20Flow%201%20·%20US01%20·%20Consultar%20ritmo%20cardíaco.png)

<hr>
<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Cuidador (Roxana Paola Diana Ramírez)</td>
    <td class="header">Número</td>
    <td>2 · US02</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como cuidador, quiero consultar la presión arterial sistólica y diastólica de la persona bajo cuidado, para evaluar su condición hemodinámica y prevenir descompensaciones.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador necesita revisar el indicador y se encuentra en la pantalla de Inicio.</li>
    <li>El Cuidador toca Salud.</li>
    <li>El sistema muestra la pantalla Salud con los signos vitales en tiempo real.</li>
    <li>El Cuidador selecciona Presión arterial.</li>
    <li>El sistema muestra la pantalla de consulta de presión arterial.</li>
    <li>¿Lectura concluyente? Sí → el sistema muestra el valor en mmHg y su clasificación.</li>
    <li>El Cuidador evalúa la presión arterial del Fragile Citizen.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador selecciona Presión arterial.</li>
    <li>¿Lectura concluyente? No → la medición no es válida.</li>
    <li>El sistema descarta la medición inválida e informa el error.</li>
    <li>Se solicita una nueva lectura.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow diagram 2 - Health Monitoring - US02](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/flows/User%20Flow%202%20%C2%B7%20US02%20%C2%B7%20Consultar%20presi%C3%B3n%20arterial.png)

<hr>
<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Cuidador (Roxana Paola Diana Ramírez)</td>
    <td class="header">Número</td>
    <td>3 · US03</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como cuidador, quiero consultar la saturación de oxígeno de la persona bajo cuidado, para identificar hipoxemia o dificultad respiratoria.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador necesita revisar el indicador y se encuentra en la pantalla de Inicio.</li>
    <li>El Cuidador toca Salud.</li>
    <li>El sistema muestra la pantalla Salud con los signos vitales en tiempo real.</li>
    <li>El Cuidador selecciona Saturación O₂.</li>
    <li>El sistema muestra la pantalla de consulta de saturación de oxígeno.</li>
    <li>¿Hay contacto continuo? Sí → el sistema muestra el valor de SpO₂ y su estado.</li>
    <li>El Cuidador evalúa la oxigenación del Fragile Citizen.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador selecciona Saturación O₂.</li>
    <li>¿Hay contacto continuo? No → la pulsera no mantiene contacto continuo con la piel.</li>
    <li>El sistema conserva el último registro válido e indica que la lectura está incompleta.</li>
    <li>No se interpreta un dato incompleto.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow diagram 3 - Health Monitoring - US03](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/flows/User%20Flow%203%20%C2%B7%20US03%20%C2%B7%20Consultar%20saturaci%C3%B3n%20de%20ox%C3%ADgeno.png)

<hr>
<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Cuidador (Roxana Paola Diana Ramírez)</td>
    <td class="header">Número</td>
    <td>4 · US04</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como cuidador, quiero supervisar la temperatura corporal de la persona bajo cuidado, para detectar oportunamente fiebre o hipotermia.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador necesita revisar el indicador y se encuentra en la pantalla de Inicio.</li>
    <li>El Cuidador toca Salud.</li>
    <li>El sistema muestra la pantalla Salud con los signos vitales en tiempo real.</li>
    <li>El Cuidador selecciona Temperatura.</li>
    <li>El sistema muestra la pantalla de supervisión de temperatura corporal.</li>
    <li>¿Está en rango normal? Sí → el sistema muestra normotermia y registra la serie.</li>
    <li>El Cuidador supervisa la temperatura del Fragile Citizen.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador selecciona Temperatura.</li>
    <li>¿Está en rango normal? No → la temperatura está fuera del rango normal.</li>
    <li>El sistema destaca la fiebre o hipotermia y pide un control inmediato.</li>
    <li>La anomalía queda visible para que el Cuidador actúe.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow diagram 4 - Health Monitoring - US04](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/flows/User%20Flow%204%20%C2%B7%20US04%20%C2%B7%20Supervisar%20temperatura%20corporal.png)

<hr>
<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Cuidador (Roxana Paola Diana Ramírez)</td>
    <td class="header">Número</td>
    <td>5 · US05</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como cuidador, quiero consultar la frecuencia respiratoria de la persona bajo cuidado, para identificar taquipnea o bradipnea.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador necesita revisar el indicador y se encuentra en la pantalla de Inicio.</li>
    <li>El Cuidador toca Salud.</li>
    <li>El sistema muestra la pantalla Salud con los signos vitales en tiempo real.</li>
    <li>El Cuidador selecciona Respiración.</li>
    <li>El sistema muestra la pantalla de consulta de frecuencia respiratoria.</li>
    <li>¿Está entre 12–20 rpm? Sí → el sistema muestra un ritmo ventilatorio normal.</li>
    <li>El Cuidador evalúa la respiración del Fragile Citizen.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador selecciona Respiración.</li>
    <li>¿Está entre 12–20 rpm? No → la frecuencia respiratoria está fuera del rango.</li>
    <li>El sistema destaca el valor anómalo y actualiza la condición.</li>
    <li>El Cuidador identifica la alteración respiratoria.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow diagram 5 - Health Monitoring - US05](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/flows/User%20Flow%205%20%C2%B7%20US05%20%C2%B7%20Consultar%20frecuencia%20respiratoria.png)

<hr>
<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Cuidador (Roxana Paola Diana Ramírez)</td>
    <td class="header">Número</td>
    <td>6 · US07</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como cuidador, quiero revisar tendencias históricas de signos vitales, para identificar patrones de deterioro y compartir información con el médico.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador necesita revisar el indicador y se encuentra en la pantalla de Inicio.</li>
    <li>El Cuidador toca Salud.</li>
    <li>El sistema muestra la pantalla Salud con los signos vitales en tiempo real.</li>
    <li>El Cuidador abre “Buscar y filtrar” y elige el signo vital y el periodo.</li>
    <li>El sistema aplica los criterios seleccionados.</li>
    <li>¿Hay al menos 12 h válidas? Sí → el sistema consolida el promedio, mínimo, máximo y la gráfica.</li>
    <li>La tendencia queda disponible para el Cuidador.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador elige el signo vital y el periodo.</li>
    <li>¿Hay al menos 12 h válidas? No → el periodo no tiene suficientes datos.</li>
    <li>El sistema informa que el muestreo es insuficiente.</li>
    <li>El Cuidador elige otro periodo.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow diagram 6 - Health Monitoring - US07](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/flows/User%20Flow%206%20%C2%B7%20US07%20%C2%B7%20Analizar%20tendencias%20hist%C3%B3ricas.png)

<hr>
<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Cuidador (Roxana Paola Diana Ramírez)</td>
    <td class="header">Número</td>
    <td>7 · US19</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como cuidador, quiero generar y exportar el historial de signos vitales, para respaldar las consultas médicas presenciales.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador necesita revisar el indicador y se encuentra en la pantalla de Inicio.</li>
    <li>El Cuidador toca Salud.</li>
    <li>El sistema muestra la pantalla Salud con los signos vitales en tiempo real.</li>
    <li>El Cuidador abre Exportar PDF y elige el periodo.</li>
    <li>El sistema muestra la hoja “Exportar expediente”.</li>
    <li>¿El rango tiene registros? Sí → el sistema compila y genera el expediente en PDF.</li>
    <li>El expediente queda listo para compartir.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador abre Exportar PDF y elige el periodo.</li>
    <li>¿El rango tiene registros? No → el periodo seleccionado no contiene datos.</li>
    <li>El sistema bloquea la exportación y conserva el periodo seleccionado.</li>
    <li>El Cuidador selecciona otro rango.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow diagram 7 - Health Monitoring - US19](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/flows/User%20Flow%207%20%C2%B7%20US19%20%C2%B7%20Exportar%20historial%20de%20telemetr%C3%ADa.png)

<hr>
<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Cuidador (Roxana Paola Diana Ramírez)</td>
    <td class="header">Número</td>
    <td>8 · US21</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como cuidador, quiero que las lecturas tomadas sin red se almacenen y sincronicen al recuperar conexión, para conservar íntegro el historial.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador necesita revisar el indicador y se encuentra en la pantalla de Inicio.</li>
    <li>El Cuidador toca Salud.</li>
    <li>El sistema muestra la pantalla Salud con los signos vitales en tiempo real.</li>
    <li>El monitoreo recibe nuevas lecturas de la pulsera.</li>
    <li>El sistema muestra la tarjeta “Sincronización activa” en la pestaña Ahora.</li>
    <li>¿Hay conexión disponible? Sí → el sistema transmite y persiste la telemetría.</li>
    <li>El historial queda actualizado.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
    <li>El monitoreo recibe nuevas lecturas de la pulsera.</li>
    <li>¿Hay conexión disponible? No → no existe conexión de red.</li>
    <li>El sistema almacena las lecturas localmente y las sincroniza al reconectar.</li>
    <li>Los datos pendientes se recuperan en el historial.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow diagram 8 - Health Monitoring - US21](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/flows/User%20Flow%208%20%C2%B7%20US21%20%C2%B7%20Sincronizar%20telemetr%C3%ADa%20sin%20conexi%C3%B3n.png)

<hr>
<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Cuidador (Roxana Paola Diana Ramírez)</td>
    <td class="header">Número</td>
    <td>9 · US24</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como cuidador, quiero recibir una síntesis semanal del estado de salud, para evaluar la evolución global sin revisar la telemetría continuamente.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador necesita revisar el indicador y se encuentra en la pantalla de Inicio.</li>
    <li>El Cuidador toca Salud.</li>
    <li>El sistema muestra la pantalla Salud con los signos vitales en tiempo real.</li>
    <li>El Cuidador abre Reporte semanal.</li>
    <li>El sistema muestra la hoja de reporte semanal de salud.</li>
    <li>El sistema muestra la estabilidad de signos vitales, las alertas disparadas y la adherencia a la medicación.</li>
    <li>El Cuidador comprende la evolución de la semana.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
    <li>El Cuidador abre Reporte semanal.</li>
    <li>El sistema detecta anomalías recurrentes en un parámetro durante la semana.</li>
    <li>El sistema resalta la recurrencia y recomienda una revisión médica preventiva.</li>
    <li>El Cuidador identifica el riesgo recurrente.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow diagram 9 - Health Monitoring - US24](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/flows/User%20Flow%209%20%C2%B7%20US24%20%C2%B7%20Revisar%20reporte%20semanal%20de%20salud.png)

##### Extras

Los siguientes user flows corresponden a las vistas complementarias de **Extras** y describen cómo el Familiar o Cuidador gestiona su información personal, consulta su entorno de cuidado y suscripción, configura las preferencias de Guardian+ y administra el cierre de sesión. Cada diagrama presenta la ruta esperada o happy path y las rutas alternativas o unhappy paths.
<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Familiar / Cuidador</td>
    <td class="header">Número</td>
    <td>1</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como familiar o cuidador, quiero consultar y actualizar mis datos personales y de contacto, para mantener correcta la información asociada a mi perfil en Guardian+.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
      <li>El Familiar o Cuidador se encuentra en la pantalla de Inicio.</li>
      <li>El usuario toca su avatar.</li>
      <li>El sistema muestra la pantalla Perfil.</li>
      <li>El usuario selecciona “Mis datos”.</li>
      <li>El sistema muestra la información personal y de contacto registrada.</li>
      <li>El usuario modifica la información que desea actualizar y selecciona “Guardar cambios”.</li>
      <li>¿Los datos son válidos? Sí → el sistema guarda la información actualizada.</li>
      <li>El sistema confirma que los cambios fueron guardados correctamente.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
      <li>Datos inválidos: Si alguno de los datos ingresados no cumple con el formato esperado, el sistema mantiene la pantalla “Mis datos” y muestra el campo que debe corregirse.</li>
      <li>El usuario corrige el dato inválido y selecciona nuevamente “Guardar cambios”.</li>
      <li>Cancelar edición: Si el usuario selecciona “Cancelar”, el sistema regresa a Perfil sin guardar las modificaciones realizadas.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow diagram 1 - Extras - Gestionar información personal](../assets/images/chapterIII/user-flow-diagrams/extras/mockups/flows/user-flow-extras-1-gestionar-informacion-personal.png)

<hr>

<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Familiar / Cuidador</td>
    <td class="header">Número</td>
    <td>2</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como familiar o cuidador, quiero consultar la información de Elena, las personas vinculadas a su cuidado y el estado de su pulsera, para mantenerme informado sobre su entorno de cuidado.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
      <li>El Familiar o Cuidador se encuentra en la pantalla de Inicio.</li>
      <li>El usuario toca su avatar.</li>
      <li>El sistema muestra la pantalla Perfil.</li>
      <li>El usuario selecciona la información del entorno de cuidado que desea consultar.</li>
      <li>Si selecciona “Persona bajo cuidado”, el sistema muestra la información principal de Elena.</li>
      <li>Si selecciona “Pulsera”, el sistema muestra el estado y la información del dispositivo asociado.</li>
      <li>Si selecciona “Círculo de cuidado”, el sistema muestra las personas vinculadas al cuidado de Elena.</li>
      <li>El usuario puede buscar una persona por nombre o parentesco.</li>
      <li>¿Hay coincidencias? Sí → el sistema muestra los contactos que cumplen con el criterio de búsqueda.</li>
      <li>El usuario consulta la información requerida del entorno de cuidado.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
      <li>Sin coincidencias: Si la búsqueda no coincide con ninguna persona del círculo de cuidado, el sistema muestra el estado “No encontramos coincidencias”.</li>
      <li>El sistema mantiene disponible el campo de búsqueda y la acción para limpiar o modificar el criterio utilizado.</li>
      <li>El usuario modifica la búsqueda y el sistema vuelve a evaluar las coincidencias disponibles.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow diagram 2 - Extras - Consultar entorno de cuidado](../assets/images/chapterIII/user-flow-diagrams/extras/mockups/flows/user-flow-extras-2-consultar-entorno-cuidado.png)

<hr>

<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Familiar / Cuidador</td>
    <td class="header">Número</td>
    <td>3</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como familiar o cuidador, quiero consultar mi plan actual y sus beneficios, para conocer las funcionalidades disponibles en mi suscripción de Guardian+.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
      <li>El Familiar o Cuidador se encuentra en la pantalla de Inicio.</li>
      <li>El usuario toca su avatar.</li>
      <li>El sistema muestra la pantalla Perfil.</li>
      <li>El usuario selecciona “Mi plan”.</li>
      <li>¿La información del plan está disponible? Sí → el sistema muestra la suscripción activa.</li>
      <li>El sistema presenta el nombre del plan, sus beneficios y el estado general de la suscripción.</li>
      <li>El usuario consulta la información y los beneficios disponibles en su plan.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
      <li>Error de carga: Si la información del plan no está disponible, el sistema muestra el mensaje “No pudimos cargar tu plan”.</li>
      <li>El sistema informa que los datos de la suscripción no han sido modificados.</li>
      <li>El usuario selecciona “Reintentar”.</li>
      <li>El sistema vuelve a consultar la información del plan hasta que pueda mostrarla correctamente.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow diagram 3 - Extras - Consultar suscripción actual](../assets/images/chapterIII/user-flow-diagrams/extras/mockups/flows/user-flow-extras-3-consultar-suscripcion.png)

<hr>

<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Familiar / Cuidador</td>
    <td class="header">Número</td>
    <td>4</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como familiar o cuidador, quiero ajustar el idioma y las opciones de accesibilidad de Guardian+, para adaptar la aplicación a mis necesidades de uso.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
      <li>El Familiar o Cuidador se encuentra en la pantalla de Inicio.</li>
      <li>El usuario toca su avatar.</li>
      <li>El sistema muestra la pantalla Perfil.</li>
      <li>El usuario selecciona “Configuración”.</li>
      <li>El sistema muestra las preferencias disponibles de la aplicación.</li>
      <li>El usuario selecciona la preferencia que desea configurar: “Idioma” o “Accesibilidad”.</li>
      <li>Si selecciona “Idioma”, el sistema muestra los idiomas disponibles y el usuario selecciona el idioma deseado.</li>
      <li>Si selecciona “Accesibilidad”, el sistema muestra las opciones disponibles y el usuario ajusta sus preferencias.</li>
      <li>El usuario selecciona “Guardar cambios”.</li>
      <li>¿Se guardaron los cambios? Sí → el sistema actualiza la preferencia seleccionada y muestra una confirmación.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
      <li>Error al guardar idioma: Si la preferencia de idioma no puede guardarse, el sistema mantiene la selección realizada y muestra un mensaje de error.</li>
      <li>El usuario selecciona “Reintentar” y el sistema intenta guardar nuevamente la preferencia.</li>
      <li>Error al guardar accesibilidad: Si las preferencias de accesibilidad no pueden guardarse, el sistema mantiene los ajustes realizados y muestra un mensaje de error.</li>
      <li>El usuario selecciona “Reintentar” y el sistema intenta guardar nuevamente las preferencias.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow diagram 4 - Extras - Configurar preferencias](../assets/images/chapterIII/user-flow-diagrams/extras/mockups/flows/user-flow-extras-4-configurar-preferencias.png)

<hr>


##### Emergency & Alerting Bounded Context

Los siguientes user flows corresponden al Bounded Context **Emergency & Alerting** y describen cómo el familiar y la cuidadora atienden las alertas de Elena desde la sección **Alertas**. Cada diagrama muestra el happy path en verde y los unhappy paths en rojo.

<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Familiar (María Fernanda Rojas Ibáñez)</td>
    <td class="header">Número</td>
    <td>1 · US08, US11</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como familiar de Elena, quiero enterarme de inmediato cuando la pulsera detecte una caída y atenderla, para asegurarme de que reciba ayuda a tiempo.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
      <li>La pulsera detecta una caída y Elena no la cancela en 20 s.</li>
      <li>El familiar toca la notificación y abre la alerta desde Alertas activas.</li>
      <li>El sistema muestra el detalle de la alerta crítica con el escalamiento y la ubicación.</li>
      <li>¿Reconoce antes de 60 s? Sí → llama o hace videollamada a Elena.</li>
      <li>¿Elena está bien? Sí → cierra el incidente, que queda registrado en el Historial.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
      <li>Si no reconoce la alerta en 60 s, el sistema la envía a los contactos secundarios y el primero que la reconoce la atiende.</li>
      <li>Si Elena no está bien, el familiar llama a emergencias (SAMU 106) y el incidente se deriva.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow 1 - Emergency & Alerting - Atender una alerta de caída](../assets/images/chapterIII/emergency-alerting/user-flows/user-flow-1-alerta-caida.png)

<hr>

<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Cuidadora (Roxana Paola Diana Ramírez)</td>
    <td class="header">Número</td>
    <td>2 · US15, US25</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como cuidadora de Elena, quiero recibir su pedido de auxilio en cuanto presione el botón SOS de la pulsera, para saber dónde está y actuar sin perder tiempo.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
      <li>Elena mantiene presionado el botón SOS de la pulsera por al menos 3 s.</li>
      <li>El sistema muestra la Alerta SOS con la ubicación de Elena.</li>
      <li>¿La cuidadora la reconoce primero? Sí → revisa la ubicación en el mapa y llama a Elena.</li>
      <li>¿Es una emergencia real? Sí → llama al SAMU 106 y acude al lugar.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
      <li>Si Elena presiona el botón menos de 3 s, la pulsera descarta la acción y no se envía la alerta.</li>
      <li>Si otro contacto reconoce la alerta primero, la cuidadora ve quién la atiende y hace el seguimiento desde el detalle.</li>
      <li>Si no es una emergencia real, la cuidadora marca la alerta como falsa alarma y queda registrada como descartada en el Historial.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow 2 - Emergency & Alerting - Responder a un SOS](../assets/images/chapterIII/emergency-alerting/user-flows/user-flow-2-sos.png)

<hr>

<table>
  <tr>
    <td class="header">User Persona</td>
    <td>Familiar (María Fernanda Rojas Ibáñez)</td>
    <td class="header">Número</td>
    <td>3 · US09, US10</td>
  </tr>
  <tr>
    <td class="header">User Goal</td>
    <td colspan="3" class="italic bold">
    Como familiar de Elena, quiero enterarme cuando sus signos vitales salgan del rango seguro y seguir la alerta hasta que se normalicen, para intervenir solo cuando realmente haga falta.
    </td>
  </tr>
  <tr>
    <td class="header">Happy path</td>
    <td colspan="3">
    <ol>
      <li>Se registran tres lecturas seguidas del ritmo cardíaco fuera de rango y llega la alerta.</li>
      <li>El familiar reconoce la alerta desde Alertas activas y revisa los signos de Elena.</li>
      <li>¿Vuelve al rango seguro por 5 min? Sí → el sistema muestra la alerta como estabilizada.</li>
      <li>El familiar cierra el incidente, que queda registrado en el Historial.</li>
    </ol>
    </td>
  </tr>
  <tr>
    <td class="header">Unhappy Paths</td>
    <td colspan="3">
    <ol>
      <li>Antes de alertar, la pulsera muestra una advertencia preventiva a Elena; si confirma que está bien en 30 s, la alerta se descarta y queda en el Historial.</li>
      <li>Si los signos no vuelven al rango seguro, el familiar llama a Elena o ajusta los umbrales en Configuración de alertas, y la alerta sigue activa hasta normalizarse.</li>
    </ol>
    </td>
  </tr>
</table>

![user flow 3 - Emergency & Alerting - Seguir una alerta de signos vitales](../assets/images/chapterIII/emergency-alerting/user-flows/user-flow-3-signos-vitales.png)

<hr>


#### 3.1.4.5. Mobile Applications Prototyping

El prototipo de la aplicación móvil de Guardian+ se construyó en Figma, en la página *Prototype v2* del archivo *Guardian+ Prototyping*, a partir de los mock-ups de la sección 3.1.4.3. Reúne las 38 pantallas de las cinco secciones de la aplicación (Inicio, Salud, Alertas, Rutinas y Ubicación) y la sección de Perfil, conectadas en un único flujo llamado *Guardian+* que inicia en la pantalla de Inicio. Desde ese punto se puede llegar a todas las pantallas del prototipo y volver desde cada una de ellas, de modo que el recorrido de los User Flow Diagrams de la sección 3.1.4.4 puede reproducirse sin interrupciones.

##### Criterios de interacción

Las conexiones del prototipo siguen el sistema de navegación definido en la sección 3.1.2.5. Los criterios aplicados fueron los siguientes:

| Tipo de navegación | Decisión en el prototipo | Relación con la arquitectura de información |
|---|---|---|
| **Global** | La barra de navegación inferior está presente en las pantallas principales de cada sección y cada destino abre la pantalla raíz de su sección. El destino de la sección actual no tiene enlace para evitar recargar la misma pantalla. Alertas ocupa la posición central y se destaca con un botón circular. | Corresponde a los cinco destinos permanentes de la bottom navigation bar. Siguiendo la misma regla, la barra se oculta en las pantallas de detalle y en los formularios. |
| **Suplementaria** | El avatar de la barra superior del Inicio abre Perfil, desde donde se accede a Mis datos, Persona bajo cuidado, Círculo de cuidado, Pulsera, Mi plan, Configuración y Cerrar sesión. | Perfil se ubica en la barra superior y no en la inferior, que se limita a cinco destinos. |
| **Local** | Las pestañas *Ahora* e *Historial* de Salud y las pestañas *Activas* e *Historial* de Alertas alternan entre las dos vistas de su sección. En el historial de Salud, los chips Ritmo, Presión, SpO₂, Temp y Respir cambian entre los cinco signos vitales. | Cada sección organiza su contenido en vistas de la misma categoría, según los esquemas de organización de la sección 3.1.2.1. |
| **Contextual** | Las tarjetas y los enlaces del Inicio (*Ver detalle*, *Ver agenda*, *Ver alertas*, signos vitales, próxima toma y última alerta) llevan a la pantalla que amplía esa información. *Ver en mapa* lleva desde el detalle de una alerta a la ubicación en tiempo real. | El Inicio resume el estado de la persona bajo cuidado y cada bloque funciona como acceso directo a su sección. |
| **Retorno** | Las pantallas de detalle y los formularios de Rutinas, Alertas y Ubicación tienen un botón de volver que regresa a la pantalla anterior. Los formularios también regresan al confirmar con *Guardar recordatorio* o *Agendar cita*. | Aplica la regla de retorno predecible: el botón de volver regresa a la pantalla desde la que se abrió la secundaria y no a una pantalla fija. |
| **Hojas modales** | *Buscar y filtrar*, *Exportar expediente* y *Reporte semanal* se abren sobre la pantalla de Salud y se cierran con su acción principal o al tocar fuera de la hoja. | Son tareas puntuales sobre la información de Salud y no cambian de sección. |

Todas las interacciones se activan al tocar (*On tap*). En el Inicio, el contenido se desplaza verticalmente mientras la barra de navegación inferior permanece fija, igual que en la aplicación nativa.

##### Ruta de emergencia

El prototipo reproduce la ruta de emergencia de la sección 3.1.2.5. Como Figma no permite simular una notificación push, la campana del Inicio cumple ese papel y abre la alerta SOS enviada desde la pulsera. Desde Alertas, la tarjeta de la alerta crítica abre su detalle, que muestra el escalamiento a los contactos de emergencia y la ubicación de la persona bajo cuidado. En ambas pantallas, *Ver en mapa* abre la ubicación en tiempo real. Así, el cuidador llega al detalle de la emergencia en uno o dos toques desde la pantalla en la que se encuentre.

##### Flujos cubiertos por el prototipo

| Sección | Recorrido en el prototipo | User Stories |
|---|---|---|
| Salud | Inicio → Salud · Ahora → Historial del signo vital → cambio entre Ritmo, Presión, SpO₂, Temp y Respir. | US01, US02, US03, US04, US05, US07 |
| Salud | Historial → *Todos los signos vitales* → Buscar y filtrar → *Aplicar*. | US07 |
| Salud | Historial → *Exportar PDF* → Exportar expediente → *Generar y exportar PDF*. | US19 |
| Salud | Historial → *Reporte semanal* → Reporte semanal. | US24 |
| Alertas | Alertas activas → Detalle de alerta crítica → *Ver en mapa*. | US08, US11 |
| Alertas | Inicio → campana → Alerta SOS desde la pulsera → *Ver en mapa*. | US15 |
| Alertas | Alertas → Historial → Alerta de signos vitales estabilizada → *Ver en Salud*. | US09, US10 |
| Rutinas | Rutinas → Medicación → Nueva toma → *Guardar recordatorio*. | US06 |
| Rutinas | Rutinas → Citas médicas → Nueva cita → *Agendar cita*. | US13 |
| Rutinas | Rutinas → Actividad ligera → Nueva actividad. | US14 |
| Rutinas | Rutinas → Hidratación, Sueño e Inactividad. | US26, US17, US27 |
| Ubicación | Inicio → Ubicación → Ubicación en tiempo real. | US18 |
| Perfil | Inicio → Perfil → Mis datos, Persona bajo cuidado, Círculo de cuidado, Pulsera, Mi plan, Configuración (Idioma, Accesibilidad, Términos y condiciones, Acerca de Guardian+) y Cerrar sesión. | — |

Las acciones que dependen de servicios externos, como *Llamar* y *Videollamada*, se muestran en las pantallas pero no tienen conexión en el prototipo, ya que no cuentan con una pantalla propia.

##### Evidencia del prototipo

La siguiente captura muestra las conexiones del prototipo en la página *Prototype v2*, agrupadas por sección: Perfil, Inicio (*Dashboard*), Salud (*Monitoreo*), Alertas, Ubicación (*Mobility*) y Rutinas (*Care routines and wellness*).

![Conexiones del prototipo de Guardian+](../assets/images/chapterIII/prototyping/prototype-connections-overview.png)

En la sección de Salud se aprecian las conexiones entre la vista *Ahora*, el historial de cada signo vital y las hojas modales de búsqueda, exportación y reporte semanal.

![Conexiones de la sección Salud](../assets/images/chapterIII/prototyping/prototype-health-connections.png)

La siguiente captura corresponde a la ejecución del prototipo desde la pantalla de Inicio.

![Ejecución del prototipo de Guardian+](../assets/images/chapterIII/prototyping/prototype-execution-home.png)

| Recurso | Enlace |
|---|---|
| Prototipo en Figma | [Guardian+ Prototype](https://www.figma.com/proto/kxCl254LnsEBLOvjC65nD2/Guardian--Prototyping?node-id=436-1532&p=f&t=C4aAPKwd1OEPOhE6-1&scaling=min-zoom&content-scaling=fixed&page-id=436%3A1471&starting-point-node-id=436%3A1532) |
| Video del recorrido | [Guardian+ — Recorrido del prototipo móvil](https://youtu.be/rcKs9-MPEaE) |
