# Capítulo III: Solution UI/UX Design

## 3.1. Product design

### 3.1.1. Style Guidelines

Las presentes directrices de estilo definen el lenguaje visual, los componentes y las convenciones de interfaz para la plataforma Guardian+, abarcando tanto el sitio web estático (Landing Page) como la aplicación móvil nativa y multiplataforma. Este sistema asegura consistencia, accesibilidad universal y un entorno confiable para familiares, cuidadores y ciudadanos en situación de vulnerabilidad o dependencia.

#### 3.1.1.1. General Style Guidelines

##### A. Tono de Comunicación y Lenguaje

El tono de Guardian+ equilibra la precisión médica con la serenidad humana indispensable para mitigar la ansiedad en situaciones de riesgo continuo:

*   **Formal / Casual:** *Formal y Profesional*. Proyecta rigor clínico, seguridad en la gestión de telemetría biométrica y solidez en los protocolos de auxilio.
*   **Entusiasta / Sereno:** *Sereno y Calmo*. Prioriza la claridad analítica y la templanza en estados de alarma crítica, evitando elementos alarmistas que susciten pánico infundado.
*   **Respetuoso / Irreverente:** *Estrictamente Respetuoso*. Reconoce la dignidad, privacidad y autonomía de las personas bajo cuidado y la responsabilidad de sus redes de apoyo.
*   **Divertido / Serio:** *Serio y Confiable*. Enfocado en la eficiencia operativa, la legibilidad inmediata de signos vitales y la rapidez de respuesta ante emergencias.

##### B. Paleta de Colores

La paleta cromática se estructura bajo las especificaciones técnicas del design system implementado, garantizando cumplimiento de contraste WCAG 2.1 nivel AA y AAA para usuarios con visión reducida o adultos mayores:

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

### 3.1.2. Information Architecture

#### 3.1.2.1. Organization Systems

## Organization Systems

Guardian+ organiza su información combinando estructuras visuales y esquemas de categorización según el tipo de contenido y la necesidad del usuario en cada momento.

### Estructuras de organización

**Jerárquica (Visual Hierarchy).** Se aplica a la navegación principal de la app: desde el Inicio se accede a las 5 secciones core (Monitoreo de Salud, Rutinas y Bienestar, Alertas, Ubicación, Perfil), y dentro de cada una la información se prioriza visualmente según su criticidad — por ejemplo, en Alertas, las alertas activas se muestran por encima del historial de incidentes ya resueltos.

**Secuencial (Step-by-step).** Se usa en procesos donde el orden de los pasos es obligatorio: el flujo de autenticación y registro (Email → Contraseña → Iniciar Sesión), la respuesta ante una emergencia (alerta generada → ventana de confirmación → escalamiento a contactos), y la configuración inicial de la pulsera al vincular un nuevo dispositivo.

**Matricial (Matrix).** Se aplica donde el usuario necesita comparar información en dos dimensiones a la vez: el calendario semanal de recordatorios de medicación (horarios × días de la semana) y la comparación de planes de suscripción (beneficios × plan).

### Esquemas de categorización

**Alfabético.** Para listas donde el usuario busca un ítem puntual por nombre: la lista de contactos de emergencia y el listado de medicamentos registrados.

**Cronológico.** Para todo lo que representa una secuencia en el tiempo: el historial de signos vitales, el historial de incidentes/alertas y el historial de pagos, donde lo más reciente aparece primero.

**Por tópico.** Es el criterio principal de la navegación de la app — cada sección agrupa funcionalidad relacionada siguiendo directamente los Bounded Contexts del dominio (Salud, Rutinas, Alertas, Ubicación, Perfil), de modo que el usuario siempre sabe en qué "mundo" de la app está.


![organizacion-systems](../assets/images/chapterIII/organization-systems/organization-systems-diagram.jpg)

##### 3.1.2.2. Labelling Systems

##### 3.1.2.3. SEO Tags and Meta Tags

##### 3.1.2.4. Searching Systems

##### 3.1.2.5. Navigation Systems

#### 3.1.3. Landing Page UI Design

##### 3.1.3.1. Landing Page Wireframe

##### 3.1.3.2. Landing Page Mock-up

#### 3.1.4. Mobile Applications UX/UI Design

##### 3.1.4.1. Mobile Applications Wireframes

##### 3.1.4.2. Mobile Applications Wireflow Diagrams

##### 3.1.4.3. Mobile Applications Mock-ups

##### 3.1.4.4. Mobile Applications User Flow Diagrams

##### 3.1.4.5. Mobile Applications Prototyping