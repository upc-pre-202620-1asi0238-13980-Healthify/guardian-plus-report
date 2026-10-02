# Capítulo III: Solution UI/UX Design

## 3.1. Product design

### 3.1.1. Style Guidelines

Las presentes directrices de estilo definen el lenguaje visual, los componentes y las convenciones de interfaz para la plataforma Guardian+, abarcando tanto el sitio web estático (Landing Page) como la aplicación móvil nativa y multiplataforma. Este sistema asegura consistencia, accesibilidad universal y un entorno confiable para familiares, cuidadores y ciudadanos en situación de vulnerabilidad o dependencia.

**Concepto de diseño.** Todas las decisiones que siguen responden a una misma intención: que la interfaz se perciba como *una casa tranquila y no como una sala de hospital*. Guardian+ traslada información clínica a un entorno doméstico y de uso cotidiano, por lo que su lenguaje visual no puede adoptar la estética de un equipo médico —oscura, saturada, densa en datos— ni la de una aplicación de fitness —festiva, competitiva, gamificada—. La primera trasladaría a la casa la tensión de una unidad de cuidados intensivos; la segunda trivializaría una responsabilidad que para el usuario es afectiva antes que deportiva. El sistema se sitúa deliberadamente entre ambas: rigor en la estructura y en la precisión de los datos, calidez en el color, la forma y el espacio.

Esta intención se deriva del valor central que el Capítulo I identifica en los segmentos objetivo: lo que familiares y cuidadores buscan, antes que cualquier funcionalidad, es *tranquilidad*. Un producto que promete calma no puede generar tensión visual al abrirse. De ahí que el estado normal —la situación mayoritaria, la que el usuario verá casi siempre— se represente con un lenguaje sereno y silencioso, y que la intensidad visual esté racionada y reservada para lo excepcional. La jerarquía del sistema no se organiza por importancia funcional, sino por urgencia: el diseño permanece callado mientras todo está bien y solo eleva la voz cuando algo ocurre.

#### 3.1.1.1. General Style Guidelines

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
| **Silent Mode** | Modo silencioso | Pulsera, Perfil › Pulsera |
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
| **Modo silencioso** | Recibe notificaciones sin sonido, excepto ante alertas críticas. | US22 |
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

#### 3.1.3.1. Landing Page Wireframe

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

###### Wireframe mobile - Cómo funciona

![landing page wireframe - Cómo funciona](../assets/images/chapterIII/landing-page-wireframes/landing_wireframe__wireframe_mobile_1.png)

###### Wireframe mobile - Beneficios

![landing page wireframe - Beneficios](../assets/images/chapterIII/landing-page-wireframes/landing_wireframe__wireframe_mobile_2.png)

###### Wireframe mobile - Por qué Guardian+

![landing page wireframe - Por qué Guardian+](../assets/images/chapterIII/landing-page-wireframes/landing_wireframe__wireframe_mobile_3.png)

###### Wireframe mobile - Precios

![landing page wireframe - Precios](../assets/images/chapterIII/landing-page-wireframes/landing_wireframe__wireframe_mobile_4.png)

###### Wireframe mobile - Contacto

![landing page wireframe - Contacto](../assets/images/chapterIII/landing-page-wireframes/landing_wireframe__wireframe_mobile_5.png)


El wireframe de Guardian+ se estructura en escala de grises para validar la arquitectura de información antes de introducir color, tipografía final o imágenes: header de navegación, hero con CTA, sección de 3 preguntas del dolor del usuario, proceso en 3 pasos, grilla de 6 funcionalidades, bloque de diferenciación de marca, tabla de 3 planes de suscripción, formulario de contacto y footer. El menú de navegación (Cómo funciona → Beneficios → Por qué Guardian+ → Precios → Contacto) refleja exactamente ese mismo orden de scroll, siguiendo un flujo narrativo secuencial (problema → solución → diferenciación → precio → acción) coherente con lo definido en Organization Systems.

Jerarquía visual: cada bloque respeta un orden claro de lectura (título grande → subtítulo → contenido de apoyo → acción), reforzado por tamaño y peso tipográfico, no por color — esto permite validar que la jerarquía funciona incluso sin la paleta final.

Principios de diseño aplicados: alineación en grilla de 3 columnas para las tarjetas de pasos, funcionalidades y planes; proximidad (ícono + título + descripción + CTA agrupados en un mismo contenedor); repetición del mismo patrón de tarjeta en las 3 secciones de contenido, para que el usuario reconozca el patrón sin esfuerzo.

Diseño inclusivo: textos cortos y escaneables (títulos de 3-6 palabras, descripciones de una línea), CTAs con texto explícito ("Conocer los planes", no solo un ícono), y formulario de contacto con etiquetas visibles sobre cada campo (no solo placeholder), reduciendo la carga cognitiva para el público objetivo — familiares y cuidadores que buscan tranquilidad, no fricción técnica.

Versión Mobile: las mismas secciones se apilan en una sola columna, el menú colapsa a ícono de hamburguesa, y las grillas de 3 columnas pasan a apilarse verticalmente, manteniendo el mismo orden de lectura que en desktop.

#### 3.1.3.2. Landing Page Mock-up

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

###### Mockup mobile - Cómo funciona

![landing page mockup - Cómo funciona](../assets/images/chapterIII/landing-page-mockups/landing-page-mockups-mobile-1.png)

###### Mockup mobile - Beneficios

![landing page mockup - Beneficios](../assets/images/chapterIII/landing-page-mockups/landing-page-mockups-mobile-2.png)

###### Mockup mobile - Por qué guardian+


![landing page mockup - Por qué guardian+](../assets/images/chapterIII/landing-page-mockups/landing-page-mockups-mobile-5.png)

###### Mockup mobile - Precios

![landing page mockup - Precios](../assets/images/chapterIII/landing-page-mockups/landing-page-mockups-mobile-3.png)

###### Mockup mobile - Contacto

![landing page mockup - Contacto](../assets/images/chapterIII/landing-page-mockups/landing-page-mockups-mobile-4.png)

### 3.1.4. Mobile Applications UX/UI Design

#### 3.1.4.1. Mobile Applications Wireframes

##### Health Monitoring Bounded Context

Los wireframes del Bounded Context **Health Monitoring** definen, en escala de grises, la estructura y jerarquía de las pantallas de la sección **Salud** de la aplicación móvil, sin aplicar todavía la paleta de colores del Style Guide. Cubren las User Stories US01–US05, US07, US19, US21 y US24.

###### Wireframe - Inicio

Pantalla principal del Cuidador. Resume el estado actual del Fragile Citizen, el estado de conexión y batería de la pulsera, las acciones rápidas (Llamar, Videollamada, Ubicación), un resumen de los cinco signos vitales, lo próximo en la agenda y la última alerta. Es el punto de partida de todos los flujos del contexto.

![wireframe health monitoring - Inicio](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen%20Wireflow.png)

###### Wireframe - Salud · Ahora

Vista en tiempo real del contexto Health Monitoring. Destaca la frecuencia cardíaca con su tendencia reciente y presenta tarjetas de presión arterial, saturación de oxígeno, temperatura y respiración, cada una con su etiqueta de estado. Incluye la tarjeta “Sincronización activa” que comunica el estado del envío de lecturas tomadas sin conexión (US21).

![wireframe health monitoring - Salud · Ahora](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Monitoreo%20Wireflow.png)

###### Wireframe - Salud · Historial · Ritmo cardíaco

Pestaña Historial con el chip Ritmo seleccionado. Muestra el promedio semanal, mínimo y máximo, la gráfica de tendencia por día y las últimas lecturas registradas con su estado. Da acceso a Exportar PDF y Reporte semanal (US01).

![wireframe health monitoring - Salud · Historial · Ritmo cardíaco](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Ritmo%20Wireflow.png)

###### Wireframe - Salud · Historial · Presión arterial

Pestaña Historial con el chip Presión seleccionado. Presenta la presión sistólica y diastólica en mmHg, su tendencia semanal y la clasificación de cada lectura (US02).

![wireframe health monitoring - Salud · Historial · Presión arterial](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Presion%20Wireflow.png)

###### Wireframe - Salud · Historial · Saturación de oxígeno

Pestaña Historial con el chip SpO₂ seleccionado. Presenta el porcentaje de saturación de oxígeno, su tendencia semanal y el estado de cada lectura (US03).

![wireframe health monitoring - Salud · Historial · Saturación de oxígeno](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Saturacion%20Wireflow.png)

###### Wireframe - Salud · Historial · Temperatura corporal

Pestaña Historial con el chip Temp seleccionado. Presenta la temperatura corporal en °C, su tendencia semanal y el estado de cada lectura para detectar fiebre o hipotermia (US04).

![wireframe health monitoring - Salud · Historial · Temperatura corporal](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Temperatura%20Wireflow.png)

###### Wireframe - Salud · Historial · Frecuencia respiratoria

Pestaña Historial con el chip Respir seleccionado. Presenta la frecuencia respiratoria en rpm, su tendencia semanal y el estado de cada lectura (US05).

![wireframe health monitoring - Salud · Historial · Frecuencia respiratoria](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Respiracion%20Wireflow.png)

###### Wireframe - Buscar y filtrar

Hoja inferior que se abre desde el buscador “Todos los signos vitales”. Permite buscar entre las opciones y combinar criterios por signo vital, periodo (Día, Semana, Mes) y estado, con las acciones Limpiar y Aplicar (US07).

![wireframe health monitoring - Buscar y filtrar](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Buscar%20y%20Filtrar%20signos%20Wireflow.png)

###### Wireframe - Exportar expediente

Hoja inferior que se abre desde Exportar PDF. Permite elegir el periodo (Últimos 30 días, Últimos 7 días o Personalizado), revisar las métricas incluidas y generar el expediente en PDF (US19).

![wireframe health monitoring - Exportar expediente](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Exportar%20expediente%20Wireflow.png)

###### Wireframe - Reporte semanal

Hoja inferior que se abre desde Reporte semanal. Resume la estabilidad de signos vitales, las alertas disparadas y la adherencia a la medicación, el comportamiento por parámetro y un aviso cuando se detecta un parámetro recurrente (US24).

![wireframe health monitoring - Reporte semanal](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Reporte%20semanal%20Wireflow.png)


#### 3.1.4.2. Mobile Applications Wireflow Diagrams

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


#### 3.1.4.3. Mobile Applications Mock-ups

##### Health Monitoring Bounded Context

Los mock-ups del Bounded Context **Health Monitoring** aplican sobre los wireframes la paleta de colores, tipografía, elevaciones y etiquetas de estado definidas en el Style Guide (3.1.1). El verde identifica las acciones primarias y los estados normales, y el ámbar resalta las lecturas “En Observación”.

###### Mockup - Inicio

Pantalla principal del Cuidador. Resume el estado actual del Fragile Citizen, el estado de conexión y batería de la pulsera, las acciones rápidas (Llamar, Videollamada, Ubicación), un resumen de los cinco signos vitales, lo próximo en la agenda y la última alerta. Es el punto de partida de todos los flujos del contexto.

![mockup health monitoring - Inicio](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Homescreen.png)

###### Mockup - Salud · Ahora

Vista en tiempo real del contexto Health Monitoring. Destaca la frecuencia cardíaca con su tendencia reciente y presenta tarjetas de presión arterial, saturación de oxígeno, temperatura y respiración, cada una con su etiqueta de estado. Incluye la tarjeta “Sincronización activa” que comunica el estado del envío de lecturas tomadas sin conexión (US21).

![mockup health monitoring - Salud · Ahora](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Monitoreo.png)

###### Mockup - Salud · Historial · Ritmo cardíaco

Pestaña Historial con el chip Ritmo seleccionado. Muestra el promedio semanal, mínimo y máximo, la gráfica de tendencia por día y las últimas lecturas registradas con su estado. Da acceso a Exportar PDF y Reporte semanal (US01).

![mockup health monitoring - Salud · Historial · Ritmo cardíaco](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Ritmo.png)

###### Mockup - Salud · Historial · Presión arterial

Pestaña Historial con el chip Presión seleccionado. Presenta la presión sistólica y diastólica en mmHg, su tendencia semanal y la clasificación de cada lectura (US02).

![mockup health monitoring - Salud · Historial · Presión arterial](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Presion.png)

###### Mockup - Salud · Historial · Saturación de oxígeno

Pestaña Historial con el chip SpO₂ seleccionado. Presenta el porcentaje de saturación de oxígeno, su tendencia semanal y el estado de cada lectura (US03).

![mockup health monitoring - Salud · Historial · Saturación de oxígeno](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Saturacion.png)

###### Mockup - Salud · Historial · Temperatura corporal

Pestaña Historial con el chip Temp seleccionado. Presenta la temperatura corporal en °C, su tendencia semanal y el estado de cada lectura para detectar fiebre o hipotermia (US04).

![mockup health monitoring - Salud · Historial · Temperatura corporal](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Temperatura.png)

###### Mockup - Salud · Historial · Frecuencia respiratoria

Pestaña Historial con el chip Respir seleccionado. Presenta la frecuencia respiratoria en rpm, su tendencia semanal y el estado de cada lectura (US05).

![mockup health monitoring - Salud · Historial · Frecuencia respiratoria](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Respiracion.png)

###### Mockup - Buscar y filtrar

Hoja inferior que se abre desde el buscador “Todos los signos vitales”. Permite buscar entre las opciones y combinar criterios por signo vital, periodo (Día, Semana, Mes) y estado, con las acciones Limpiar y Aplicar (US07).

![mockup health monitoring - Buscar y filtrar](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Buscar%20y%20Filtrar%20signos.png)

###### Mockup - Exportar expediente

Hoja inferior que se abre desde Exportar PDF. Permite elegir el periodo (Últimos 30 días, Últimos 7 días o Personalizado), revisar las métricas incluidas y generar el expediente en PDF (US19).

![mockup health monitoring - Exportar expediente](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Exportar%20expediente.png)

###### Mockup - Reporte semanal

Hoja inferior que se abre desde Reporte semanal. Resume la estabilidad de signos vitales, las alertas disparadas y la adherencia a la medicación, el comportamiento por parámetro y un aviso cuando se detecta un parámetro recurrente (US24).

![mockup health monitoring - Reporte semanal](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/wireframes-mockups/Reporte%20semanal.png)


#### 3.1.4.4. Mobile Applications User Flow Diagrams

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

![user flow diagram 1 - Health Monitoring - US01](../assets/images/chapterIII/user-flow-diagrams/health-monitoring/flows/User%20Flow%201%20%C2%B7%20US01%20%C2%B7%20Consultar%20ritmo%20cardi%CC%81aco.png)

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

#### 3.1.4.5. Mobile Applications Prototyping