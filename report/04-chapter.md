# Capítulo IV: Product Implementation & Validation

## 4.1. Software Configuration Management

### 4.1.1. Software Development Environment Configuration

En esta sección se especifican los productos de software que utilizan los integrantes del equipo para colaborar durante el ciclo de vida de Guardian+. Para cada producto se indica su propósito dentro del proyecto, su tipo de uso y la ruta de referencia, en el caso de servicios SaaS, o la ruta de descarga, en el caso de herramientas que se instalan en el computador de cada integrante. Las herramientas se agrupan según la actividad del ciclo de vida en la que se utilizan.

#### Project Management

| Product | Purpose | Type | Reference / Download URL |
|---|---|---|---|
| **ClickUp** | Gestión del Product Backlog, planificación de Sprints, estimación con Story Points, asignación de tareas y seguimiento de su estado. | SaaS | [Tablero de Guardian+](https://sharing.clickup.com/9013201240/b/h/6-1400350000000524-2/1612e210bce4708) |
| **WhatsApp** | Comunicación diaria del equipo y coordinación rápida de avances y bloqueos. | SaaS / Mobile | [whatsapp.com](https://www.whatsapp.com/download) |
| **Discord** | Reuniones sincrónicas del equipo, revisiones de avance y sesiones de trabajo colaborativo. | SaaS / Desktop | [discord.com](https://discord.com/download) |

#### Requirements Management

| Product | Purpose | Type | Reference / Download URL |
|---|---|---|---|
| **ClickUp** | Registro y priorización de User Stories, Technical Stories y Epics dentro del Product Backlog. | SaaS | [clickup.com](https://clickup.com) |
| **UXPressia** | Elaboración de User Personas, Empathy Maps, User Journey Maps e Impact Maps. | SaaS | [uxpressia.com](https://uxpressia.com) |
| **Miro** | Sesiones de EventStorming, Big Picture EventStorming y descubrimiento de Bounded Contexts candidatos. | SaaS | [miro.com](https://miro.com) |

#### Product UX/UI Design

| Product | Purpose | Type | Reference / Download URL |
|---|---|---|---|
| **Figma** | Diseño de Style Guidelines, wireframes, mock-ups y prototipos del Landing Page y de la aplicación móvil. | SaaS | [figma.com](https://www.figma.com) |

#### Software Architecture & Modeling

| Product | Purpose | Type | Reference / Download URL |
|---|---|---|---|
| **Structurizr** | Elaboración de los diagramas de arquitectura bajo el C4 Model. | SaaS | [structurizr.com](https://structurizr.com) |
| **Mermaid** | Diagramas como código para diagramas de clases, componentes, Domain Message Flows y mapas de navegación, versionados junto al informe. | Library / SaaS | [mermaid.js.org](https://mermaid.js.org) |
| **Graphviz** | Generación de los diagramas de base de datos a partir de archivos `.dot` versionados en el repositorio del informe. | Desktop | [graphviz.org/download](https://graphviz.org/download/) |

#### Software Development

| Product | Purpose | Type | Reference / Download URL |
|---|---|---|---|
| **Git** | Control de versiones distribuido para todos los repositorios del proyecto. | Desktop | [git-scm.com/downloads](https://git-scm.com/downloads) |
| **GitHub** | Alojamiento de repositorios, revisión de cambios mediante Pull Requests e integración de ramas bajo GitFlow. | SaaS | [Organización Healthify](https://github.com/upc-pre-202620-1asi0238-13980-Healthify) |
| **Visual Studio Code** | Editor de código para el desarrollo del Landing Page y la edición del informe en Markdown. | Desktop | [code.visualstudio.com/download](https://code.visualstudio.com/download) |
| **Node.js y npm** | Entorno de ejecución y gestor de paquetes para instalar dependencias, ejecutar y compilar el Landing Page. | Desktop | [nodejs.org/en/download](https://nodejs.org/en/download) |
| **IntelliJ IDEA** | IDE para el desarrollo de los RESTful Web Services en Java con Spring Boot. | Desktop | [jetbrains.com/idea/download](https://www.jetbrains.com/idea/download/) |
| **Java Development Kit (JDK)** | Compilación y ejecución de los Web Services. | Desktop | [oracle.com/java/technologies/downloads](https://www.oracle.com/java/technologies/downloads/) |
| **Apache Maven** | Gestión de dependencias y construcción del proyecto de Web Services mediante Maven Wrapper. | Desktop | [maven.apache.org/download.cgi](https://maven.apache.org/download.cgi) |
| **PostgreSQL** | Base de datos relacional utilizada por los Web Services durante el desarrollo local. | Desktop | [postgresql.org/download](https://www.postgresql.org/download/) |
| **Docker Desktop** | Construcción y ejecución local de la imagen de contenedor de los Web Services antes de su despliegue. | Desktop | [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/) |
| **Android Studio** | IDE para el desarrollo de la aplicación móvil nativa en Kotlin, incluyendo Android SDK y Android Emulator. | Desktop | [developer.android.com/studio](https://developer.android.com/studio) |
| **Python** | Lenguaje de implementación y ejecución del IoT Simulator. | Desktop | [python.org/downloads](https://www.python.org/downloads/) |
| **Google Cloud (Compute Engine)** | Despliegue del IoT Simulator y del broker MQTT en una máquina virtual con IP pública fija. | SaaS | [cloud.google.com/compute](https://cloud.google.com/compute) |
| **Terraform** | Infraestructura como código: aprovisiona la máquina virtual, la IP fija, el firewall y la cuenta de servicio del IoT Simulator. | CLI | [developer.hashicorp.com/terraform/install](https://developer.hashicorp.com/terraform/install) |
| **Google Cloud Shell** | Terminal en el navegador desde la que se ejecuta Terraform sin instalar herramientas locales. | SaaS | [cloud.google.com/shell](https://cloud.google.com/shell) |
| **Eclipse Mosquitto** | Broker MQTT al que el IoT Simulator publica la telemetría y al que se suscribe el backend. | Library | [mosquitto.org](https://mosquitto.org) |

#### Software Testing

| Product | Purpose | Type | Reference / Download URL |
|---|---|---|---|
| **JUnit 5 y Mockito** | Pruebas unitarias y de integración de los Web Services, incluidas en los starters de prueba de Spring Boot. | Library | [junit.org/junit5](https://junit.org/junit5/) |
| **Cucumber** | Ejecución de los escenarios de aceptación escritos en Gherkin a partir de los criterios de aceptación de las User Stories. | Library | [cucumber.io](https://cucumber.io) |
| **Swagger UI** | Prueba manual de los endpoints expuestos por los Web Services a partir de su especificación OpenAPI. | Library | [swagger.io/tools/swagger-ui](https://swagger.io/tools/swagger-ui/) |
| **JUnit, Espresso y Compose UI Test** | Pruebas unitarias e instrumentadas de la aplicación móvil. | Library | [developer.android.com/training/testing](https://developer.android.com/training/testing) |
| **Jest y React Testing Library** | Pruebas de los componentes del Landing Page. | Library | [jestjs.io](https://jestjs.io) |
| **Lighthouse** | Evaluación de accesibilidad, rendimiento y buenas prácticas SEO del Landing Page. | Browser tool | [developer.chrome.com/docs/lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) |

#### Software Deployment

| Product | Purpose | Type | Reference / Download URL |
|---|---|---|---|
| **Cloudflare Pages** | Publicación del Landing Page con despliegue automático desde la rama `main` de su repositorio. | SaaS | [pages.cloudflare.com](https://pages.cloudflare.com) |
| **Render** | Despliegue de los Web Services como contenedor Docker, con despliegue automático desde la rama `main`. | SaaS | [render.com](https://render.com) |
| **Neon** | Servicio gestionado de PostgreSQL para la base de datos de los Web Services desplegados. | SaaS | [neon.tech](https://neon.tech) |
| **Firebase App Distribution** | Distribución de las versiones de prueba de la aplicación móvil a los testers y usuarios de validación. | SaaS | [firebase.google.com/products/app-distribution](https://firebase.google.com/products/app-distribution) |

#### Software Documentation

| Product | Purpose | Type | Reference / Download URL |
|---|---|---|---|
| **GitHub y Markdown** | Elaboración colaborativa y versionamiento del informe del proyecto. | SaaS | [guardian-plus-report](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-report) |
| **OpenAPI Specification vía Swagger** | Documentación de los endpoints de los Web Services, generada con springdoc-openapi. | Library | [springdoc.org](https://springdoc.org) |

#### Technology Stack

Las versiones de lenguajes y frameworks corresponden a las configuradas actualmente en los repositorios de cada producto.

| Product | Technology | Version |
|---|---|---|
| **Landing Page** | React | 19.3 |
| | React Scripts | 5.0.1 |
| **Web Services** | Java | 27 |
| | Spring Boot | 4.1.1 |
| | springdoc-openapi | 3.1.0 |
| | PostgreSQL | Driver JDBC gestionado por Spring Boot |
| **Mobile Application** | Kotlin | 2.2.10 |
| | Android Gradle Plugin | 9.4.1 |
| | Jetpack Compose BOM | 2026.02.01 |
| | Material Design 3 | Gestionado por Compose BOM |
| | Android SDK | `compileSdk` y `targetSdk` 37, `minSdk` 24 |
| **IoT Simulator** | Python | 3.14 (imagen Docker); Python 3 de Debian 12 en la VM |
| | Flask | 3.1.0 |
| | paho-mqtt | 2.1.0 |
| | requests | 2.32.3 |
| | Eclipse Mosquitto | Paquete de Debian 12 |

### 4.1.2. Source Code Management

El equipo utiliza Git como sistema de control de versiones distribuido y GitHub como plataforma para almacenar y administrar los repositorios de los productos que conforman Guardian+. Esta organización permite mantener trazabilidad sobre los cambios realizados, separar el trabajo de cada integrante y revisar las modificaciones mediante Pull Requests antes de integrarlas a las ramas principales.

Los repositorios utilizados por Guardian+ son los siguientes:

| Product / Artifact | Repository | Purpose |
|---|---|---|
| Project Report | [guardian-plus-report](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-report) | Documentación colaborativa del proyecto elaborada en Markdown. |
| Landing Page | [guardian-plus-website](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-website) | Código fuente correspondiente al sitio web público de Guardian+. |
| Web Services | [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | Backend y RESTful Web Services que soportan los procesos de negocio de Guardian+. |
| Mobile Application | [guardian-plus-mobile-app](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-mobile-app) | Aplicación móvil Android desarrollada para familiares y cuidadores. |
| IoT Simulator | [guardian-plus-iot-simulator](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-iot-simulator) | Simulación de los datos y eventos generados por el dispositivo wearable durante el desarrollo y las pruebas. |

En la iteración actual no se mantiene una Web Application operativa independiente. La experiencia web pública corresponde a la Landing Page, mientras que las principales funcionalidades operativas son proporcionadas mediante la aplicación móvil y los Web Services.

#### 4.1.2.1. GitFlow & Branching Strategy

Guardian+ adopta GitFlow como estrategia de organización de ramas para mantener separado el código estable, el trabajo de integración y el desarrollo de nuevas funcionalidades. Los cambios se desarrollan en ramas independientes y se integran mediante Pull Requests, evitando realizar modificaciones directas sobre las ramas principales.

Las ramas consideradas en el workflow son las siguientes:

| Branch | Purpose | Origin | Destination |
|---|---|---|---|
| `main` | Contiene las versiones estables del producto y representa el estado preparado para una release. | — | — |
| `develop` | Rama de integración que concentra los cambios aprobados durante el desarrollo de cada Sprint. | `main` | `main` mediante una release |
| `feat/*` | Rama temporal utilizada para desarrollar una nueva funcionalidad, artefacto o capacidad de forma aislada. | `develop` | `develop` |
| `release/*` | Rama temporal utilizada para estabilizar una versión antes de integrarla a producción. Solo admite correcciones necesarias para completar la release. | `develop` | `main` y `develop` |
| `hotfix/*` | Rama temporal destinada a corregir errores críticos detectados sobre una versión estable. | `main` | `main` y `develop` |
| `fix/*` | Rama complementaria utilizada para correcciones identificadas durante el desarrollo antes de una release. | `develop` | `develop` |

##### Branch Naming Conventions

Los nombres de las ramas se escriben en inglés, utilizando minúsculas y palabras separadas mediante guiones. El nombre debe indicar claramente el propósito del cambio.

| Branch Type | Convention | Example |
|---|---|---|
| Feature | `feat/<scope>-<short-description>` | `feat/profile-settings` |
| Development Fix | `fix/<scope>-<short-description>` | `fix/subscriptions-entitlement-alignment` |
| Release | `release/v<major>.<minor>.<patch>` | `release/v1.0.0` |
| Hotfix | `hotfix/v<major>.<minor>.<patch>-<short-description>` | `hotfix/v1.0.1-login-error` |

Una nueva funcionalidad comienza desde `develop`. Una vez finalizada y revisada, se crea un Pull Request hacia `develop`. De esta manera, los cambios permanecen aislados hasta que sean aprobados e incorporados a la rama de integración.

El flujo utilizado para una funcionalidad es:

`develop` → `feat/*` → Pull Request → `develop`

Cuando el conjunto de funcionalidades correspondiente a una versión se encuentra preparado para estabilización, se crea una rama `release/*` desde `develop`. Las correcciones realizadas durante esta etapa permanecen limitadas a los ajustes necesarios para completar la versión. Finalmente, la rama se integra tanto a `main` como a `develop`.

El flujo de una release es:

`develop` → `release/vX.Y.Z` → `main` + `develop`

Si se detecta un error crítico en una versión que ya se encuentra en `main`, se crea una rama `hotfix/*` directamente desde `main`. Una vez solucionado el problema, el cambio se integra nuevamente tanto a `main` como a `develop` para evitar diferencias entre la versión estable y la versión en desarrollo.

El flujo de un hotfix es:

`main` → `hotfix/vX.Y.Z-description` → `main` + `develop`

##### Pull Request Strategy

Las ramas `main` y `develop` se utilizan como ramas de integración y no como espacios de desarrollo directo. Las funcionalidades y correcciones se implementan en ramas independientes y posteriormente se integran mediante Pull Requests.

Antes de aceptar un Pull Request se verifica que:

- el cambio corresponda al propósito definido para la rama;
- no se incluyan modificaciones ajenas al alcance del Pull Request;
- no existan conflictos pendientes;
- la documentación o código modificado mantenga consistencia con el proyecto;
- los commits sigan la convención definida por el equipo.

##### Conventional Commits

Los mensajes de commit siguen Conventional Commits con el objetivo de comunicar claramente la naturaleza de cada modificación y mantener un historial legible.

La estructura utilizada es:

`<type>(<scope>): <description>`

Los tipos principales adoptados por el equipo son:

| Type | Usage |
|---|---|
| `feat` | Incorporación de una nueva funcionalidad o capacidad. |
| `fix` | Corrección de un error. |
| `docs` | Modificaciones relacionadas exclusivamente con documentación. |
| `test` | Creación o modificación de pruebas. |
| `refactor` | Reestructuración interna sin modificar el comportamiento funcional esperado. |
| `chore` | Tareas de mantenimiento que no modifican directamente la funcionalidad del producto. |
| `build` | Cambios relacionados con dependencias o configuración del proceso de construcción. |
| `ci` | Cambios relacionados con procesos de integración o despliegue continuo. |

Ejemplos aplicados al proyecto:

`feat(profile): add care relationship management`

`fix(subscriptions): correct entitlement synchronization`

`docs(chapterIV): document gitflow strategy`

`test(alerting): add incident service unit tests`

El `scope` identifica el componente, bounded context o sección afectada y la descripción se redacta de manera breve y específica.

##### Semantic Versioning

Guardian+ adopta Semantic Versioning para identificar las releases mediante la estructura:

`MAJOR.MINOR.PATCH`

Cada componente representa:

- **MAJOR:** se incrementa cuando una versión introduce cambios incompatibles con la versión anterior.
- **MINOR:** se incrementa cuando se añaden funcionalidades manteniendo compatibilidad con la versión anterior.
- **PATCH:** se incrementa cuando se incorporan correcciones compatibles con la versión existente.

Las versiones se representan mediante tags con el prefijo `v`.

Ejemplos:

`v1.0.0` — primera versión estable.

`v1.1.0` — incorporación de nuevas funcionalidades compatibles.

`v1.1.1` — corrección de un error sin introducir cambios incompatibles.

Las ramas de release utilizan la versión que se está preparando, por ejemplo `release/v1.0.0`. Una vez integrada la release en `main`, se crea el tag correspondiente para identificar de manera inequívoca el estado del código asociado a dicha versión.

### 4.1.3. Source Code Style Guide & Conventions

Guardian+ establece convenciones de código comunes para mantener consistencia, legibilidad y mantenibilidad entre los diferentes productos que forman parte de la solución. Las reglas se aplican de acuerdo con las tecnologías utilizadas actualmente en los repositorios del proyecto y toman como referencia las convenciones oficiales o ampliamente adoptadas para cada lenguaje y framework.

Todos los nombres utilizados en el código fuente, incluyendo clases, métodos, variables, componentes, archivos, paquetes y escenarios de pruebas, se redactan en inglés.

Las convenciones documentadas en esta sección corresponden únicamente a las tecnologías que forman parte de la implementación actual de Guardian+.

| Product | Language / Technology | Application in Guardian+ |
|---|---|---|
| Landing Page | HTML5, CSS3, JavaScript | Estructura, presentación y comportamiento de la experiencia web pública. |
| Web Services | Java, Spring Boot | Implementación de los RESTful Web Services y lógica correspondiente a los Bounded Contexts. |
| Mobile Application | Kotlin, Android | Implementación de la aplicación móvil nativa de Guardian+. |
| IoT Simulator | Python | Simulación y procesamiento de datos y eventos asociados al dispositivo wearable. |
| Automated Acceptance Tests | Gherkin | Especificación de escenarios BDD relacionados con User Stories y criterios de aceptación. |

#### General Coding Conventions

Independientemente del lenguaje utilizado, el equipo adopta las siguientes convenciones generales:

- Los identificadores y nombres de elementos de código se escriben en inglés.
- Los nombres deben expresar claramente la responsabilidad del elemento y evitar abreviaturas ambiguas.
- Se mantiene una única responsabilidad por clase, función o componente siempre que sea posible.
- Se evita duplicar lógica y se reutilizan funciones, componentes o servicios cuando representan el mismo comportamiento.
- Los comentarios se utilizan para explicar decisiones o comportamientos que no sean evidentes a partir del propio código, evitando comentarios redundantes.
- No se mantiene código comentado dentro del repositorio. El historial de Git se utiliza para recuperar implementaciones anteriores.
- Las credenciales, API keys, tokens y otros datos sensibles no deben almacenarse directamente en el código fuente.
- Los archivos y directorios deben organizarse de acuerdo con el módulo, funcionalidad o Bounded Context al que pertenecen.
- El código debe mantener la separación de responsabilidades definida por la arquitectura de cada producto.
- Antes de integrar cambios mediante Pull Request, el código debe compilar o ejecutarse correctamente y las pruebas relacionadas con la funcionalidad modificada deben completarse satisfactoriamente.

#### HTML Coding Conventions

Para los documentos HTML utilizados en la Landing Page se adoptan las siguientes reglas:

- Se utiliza HTML5 y elementos semánticos siempre que correspondan, como `header`, `nav`, `main`, `section`, `article` y `footer`.
- Los nombres de elementos y atributos se escriben en minúsculas.
- Los valores de los atributos se delimitan mediante comillas dobles.
- La estructura del documento mantiene una indentación consistente de dos espacios.
- Las imágenes informativas incluyen el atributo `alt` con una descripción significativa.
- Los elementos interactivos utilizan etiquetas apropiadas para su función.
- Se utilizan atributos ARIA cuando sean necesarios para complementar la accesibilidad.
- Los identificadores y nombres de clases se redactan en inglés.
- Se evita agregar estilos directamente mediante el atributo `style`, manteniendo la presentación en los archivos CSS correspondientes.
- Se mantiene una estructura jerárquica clara de encabezados y secciones.

Ejemplo:

```html
<section class="subscription-plans" aria-labelledby="plans-title">
  <h2 id="plans-title">Subscription Plans</h2>

  <article class="subscription-card">
    <h3>Premium Plan</h3>
    <button type="button">View details</button>
  </article>
</section>
```

#### CSS Coding Conventions

Las hojas de estilo de Guardian+ siguen las siguientes convenciones:

- Los selectores de clase utilizan `kebab-case`.
- Los nombres describen el elemento o propósito visual y se redactan en inglés.
- Cada declaración CSS se coloca en una línea independiente.
- Se utiliza una indentación de dos espacios.
- Se prioriza el uso de clases frente a selectores excesivamente específicos.
- Se evita el uso de `!important`, excepto cuando exista una justificación técnica.
- Los valores reutilizables, como colores, dimensiones o espaciados, se centralizan mediante variables CSS cuando corresponda.
- Los estilos deben respetar los colores, tipografía, spacing y demás decisiones establecidas en los Style Guidelines de Guardian+.
- Los estilos responsive utilizan breakpoints consistentes y evitan la duplicación innecesaria de reglas.
- Se evita utilizar identificadores como selectores exclusivamente para aplicar estilos.

Ejemplo:

```css
.subscription-card {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  padding: 1.5rem;
}

.subscription-card__title {
  font-weight: 600;
}
```

#### JavaScript Coding Conventions

JavaScript se utiliza para implementar el comportamiento e interacción de la Landing Page.

Se aplican las siguientes convenciones:

- Las variables y funciones utilizan `camelCase`.
- Las clases utilizan `PascalCase`.
- Las constantes globales utilizan `UPPER_SNAKE_CASE`.
- Los nombres se redactan en inglés y deben expresar claramente su propósito.
- Se utiliza `const` por defecto cuando una referencia no requiere reasignación.
- Se utiliza `let` únicamente cuando el valor necesita ser reasignado.
- Se evita utilizar `var`.
- Se utiliza comparación estricta mediante `===` y `!==`.
- Las funciones se mantienen pequeñas y enfocadas en una única responsabilidad.
- Se evita modificar innecesariamente el estado global.
- Las operaciones relacionadas con el DOM se mantienen separadas de la lógica que pueda reutilizarse.
- Los eventos se gestionan mediante `addEventListener`.
- Se verifica la existencia de los elementos del DOM antes de operar con ellos cuando corresponda.
- Se evita duplicar selectores, valores o lógica cuando pueden almacenarse en una variable o función reutilizable.

Ejemplo:

```javascript
const planButtons = document.querySelectorAll(".subscription-card__button");

function handlePlanSelection(event) {
  const selectedPlan = event.currentTarget.dataset.plan;

  if (!selectedPlan) {
    return;
  }

  console.log(`Selected plan: ${selectedPlan}`);
}

planButtons.forEach((button) => {
  button.addEventListener("click", handlePlanSelection);
});
```

#### Java and Spring Boot Coding Conventions

Los Web Services de Guardian+ se implementan mediante Java y Spring Boot.

Las convenciones utilizadas son:

- Las clases, interfaces, enumeraciones y records utilizan `PascalCase`.
- Los métodos, variables y atributos utilizan `camelCase`.
- Las constantes utilizan `UPPER_SNAKE_CASE`.
- Los packages utilizan únicamente minúsculas.
- Las clases se organizan de acuerdo con el Bounded Context y la capa arquitectónica correspondiente.
- Los Controllers se mantienen enfocados en recibir solicitudes y delegar el procesamiento hacia la Application Layer.
- Las reglas de negocio permanecen en la Domain Layer y no se implementan directamente en Controllers o componentes de infraestructura.
- Los Commands, Queries y Events representan acciones o hechos relevantes del dominio mediante nombres explícitos.
- Los Handlers coordinan los casos de uso definidos en la Application Layer.
- Las interfaces Repository pertenecientes al modelo se mantienen separadas de sus implementaciones tecnológicas.
- Las implementaciones de persistencia, integración con servicios externos y otros detalles técnicos se mantienen en Infrastructure.
- Las dependencias se proporcionan mediante inyección por constructor.
- Las estructuras utilizadas para solicitudes y respuestas REST se mantienen separadas del modelo de dominio cuando corresponda.
- Las excepciones representan condiciones significativas y no se utilizan como mecanismo habitual de control de flujo.

La organización del código mantiene la separación establecida durante el Tactical-Level Domain-Driven Design:

```text
com.guardianplus.platform.<boundedcontext>
├── domain
├── application
├── interfaces
└── infrastructure
```

Ejemplo:

```java
public final class ActivateSubscriptionHandler {

    private final SubscriptionRepository subscriptionRepository;

    public ActivateSubscriptionHandler(
            SubscriptionRepository subscriptionRepository) {
        this.subscriptionRepository = subscriptionRepository;
    }

    public void handle(ActivateSubscriptionCommand command) {
        Subscription subscription =
                subscriptionRepository.findById(command.subscriptionId());

        subscription.activate();

        subscriptionRepository.save(subscription);
    }
}
```

#### Kotlin and Android Coding Conventions

La aplicación móvil nativa de Guardian+ utiliza Kotlin para Android.

Las convenciones principales son:

- Las clases, interfaces, objects y enumeraciones utilizan `PascalCase`.
- Las variables, propiedades, funciones y métodos utilizan `camelCase`.
- Las constantes utilizan `UPPER_SNAKE_CASE`.
- Los packages utilizan nombres en minúsculas.
- Se utiliza `val` en lugar de `var` siempre que un valor no requiera modificación.
- Se aprovechan las características de null safety proporcionadas por Kotlin y se evita utilizar valores nullable cuando no son necesarios.
- Los nombres de archivos corresponden al principal elemento declarado en ellos.
- La lógica de presentación se mantiene separada de las operaciones de red, persistencia y reglas de negocio.
- Los estados de UI se modelan mediante estructuras explícitas y se favorece la inmutabilidad.
- Los textos visibles por el usuario se mantienen en recursos para facilitar su mantenimiento e internacionalización.
- Los colores, tipografías y estilos reutilizables utilizan los recursos o temas definidos para la aplicación.
- Las funciones se mantienen pequeñas y orientadas a una responsabilidad específica.
- Se evita utilizar valores literales repetidos cuando pueden representarse mediante constantes o recursos.

Ejemplo:

```kotlin
data class ProfileUiState(
    val isLoading: Boolean = false,
    val displayName: String = "",
    val errorMessage: String? = null
)

class ProfileViewModel {
    fun updateProfile(profileId: String) {
        // Application interaction
    }
}
```

#### Python Coding Conventions

El IoT Simulator de Guardian+ utiliza Python para representar el comportamiento y los eventos generados por el dispositivo wearable, siguiendo como referencia la guía PEP 8.

Se aplican las siguientes convenciones:

- Las clases utilizan `PascalCase`.
- Las funciones, métodos, variables y módulos utilizan `snake_case`.
- Las constantes utilizan `UPPER_SNAKE_CASE`.
- Los elementos de uso interno de una clase o módulo se identifican con un guion bajo inicial.
- Los identificadores se redactan en inglés y describen claramente su responsabilidad.
- Las funciones y métodos públicos declaran los tipos de sus parámetros y de su retorno mediante type hints.
- La indentación es de cuatro espacios.
- Los valores literales repetidos, como umbrales clínicos o canales, se representan mediante constantes con nombres significativos.
- Los datos recibidos del backend se validan antes de ser procesados, y los datos simulados se mantienen coherentes en el tiempo mediante el estado de cada dispositivo.
- La lógica que genera las señales se mantiene separada de la lógica que las publica y de la que expone la API HTTP.
- La configuración se obtiene de variables de entorno o de argumentos de línea de comandos, sin valores sensibles en el código.
- Los recursos externos, como la conexión al broker, se gestionan para que la ausencia del broker o del backend no detenga la ejecución del simulador.

Ejemplo:

~~~python
BATTERY_LOW_THRESHOLD = 20
BATTERY_CRITICAL_THRESHOLD = 5


def classify_battery(level: float) -> str:
    if level <= BATTERY_CRITICAL_THRESHOLD:
        return "BATTERY_CRITICAL"
    if level <= BATTERY_LOW_THRESHOLD:
        return "BATTERY_LOW"
    return "OK"
~~~

#### Gherkin and BDD Feature File Conventions

Los Acceptance Tests implementados bajo el enfoque Behavior-Driven Development utilizan archivos `.feature` escritos mediante Gherkin. Estos escenarios mantienen trazabilidad con las User Stories y Acceptance Criteria definidos para Guardian+.

Se adoptan las siguientes convenciones:

- Cada archivo `.feature` representa una funcionalidad o comportamiento claramente delimitado.
- Los nombres de los archivos utilizan `kebab-case`, por ejemplo `emergency-alert.feature`.
- Los escenarios se redactan en inglés.
- Las palabras clave `Feature`, `Scenario`, `Given`, `When`, `Then`, `And` y `But` se utilizan de acuerdo con su propósito.
- `Given` establece las precondiciones necesarias para ejecutar el escenario.
- `When` representa la acción o evento que desencadena el comportamiento.
- `Then` expresa el resultado observable esperado.
- `And` y `But` complementan pasos sin modificar su propósito semántico.
- Los escenarios describen comportamiento observable y evitan detalles internos de implementación.
- Cada escenario se enfoca en validar un comportamiento específico.
- Los escenarios pueden identificarse mediante tags relacionados con la User Story correspondiente.
- Cuando una misma situación requiere validarse con diferentes conjuntos de datos se utiliza `Scenario Outline` junto con `Examples`.
- Los nombres de los escenarios deben expresar claramente el comportamiento que se está validando.

Ejemplo:

```gherkin
@US08
Feature: Emergency alert after fall detection

  Scenario: Generate an emergency alert after a confirmed fall
    Given a care recipient has an active care relationship
    And the wearable device is connected
    When a fall is confirmed
    Then an emergency alert should be created
    And the registered care circle should be notified
```

Los Step Definitions asociados a los archivos `.feature` se implementan utilizando el lenguaje correspondiente al proyecto de testing y contienen únicamente el código necesario para ejecutar los pasos definidos, sin duplicar reglas de negocio que pertenezcan a la solución.

#### Naming Conventions Summary

| Element | Convention | Example |
|---|---|---|
| Java / Kotlin class | `PascalCase` | `CareRelationship` |
| Python class | `PascalCase` | `MqttPublisher` |
| Method / Function | `camelCase` | `activateSubscription()` |
| Variable / Property | `camelCase` | `currentPeriodEnd` |
| Constant | `UPPER_SNAKE_CASE` | `MAX_RETRY_ATTEMPTS` |
| Java / Kotlin package | lowercase | `com.guardianplus.platform.profile` |
| JavaScript file | `kebab-case` | `subscription-plans.js` |
| CSS class | `kebab-case` | `subscription-card` |
| Gherkin file | `kebab-case.feature` | `emergency-alert.feature` |
| REST resource | plural lowercase noun | `/subscriptions` |

Estas convenciones permiten mantener un criterio común entre los diferentes productos de Guardian+, facilitar las revisiones de código y conservar la separación arquitectónica definida durante el diseño e implementación de la solución.

### 4.1.4. Software Deployment Configuration

En esta sección se especifica la configuración de despliegue de cada producto digital de Guardian+, incluyendo los pasos necesarios para que, a partir de su repositorio de código fuente, se logre su publicación satisfactoria. El despliegue se integra con la estrategia de GitFlow definida en la sección 4.1.2: los productos se publican en producción a partir de la rama `main`, mientras que el desarrollo y la integración se realizan en las ramas `feat/*` y `develop`. Las credenciales y cadenas de conexión se configuran como variables de entorno en cada plataforma y no se almacenan en los repositorios.

#### Deployment Overview

| Product | Repository | Platform | Deployment Trigger | Public Access |
|---|---|---|---|---|
| **Landing Page** | [guardian-plus-website](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-website) | Cloudflare Pages | Integración de cambios en `main` | [guardian-plus.pages.dev](https://guardian-plus.pages.dev) |
| **Web Services** | [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | Render (Docker) y Neon (PostgreSQL) | Integración de cambios en `main` | URL pública aún no disponible; se registrará en esta sección tras el primer despliegue, junto con la ruta de su documentación en Swagger UI |
| **Mobile Application** | [guardian-plus-mobile-app](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-mobile-app) | Firebase App Distribution | Publicación de una release versionada con Semantic Versioning, por ejemplo `v1.0.0` | Invitación por correo a los testers registrados |
| **IoT Simulator** | [guardian-plus-iot-simulator](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-iot-simulator) | Google Cloud Compute Engine (VM Debian 12 aprovisionada con Terraform) | Manual: `terraform apply` sobre el código de la rama `main`, que la VM clona al arrancar | API de monitoreo en `http://34.45.141.10:5000` y broker MQTT en `34.45.141.10:1883` (WebSocket en `9001`), con acceso restringido por firewall a las IP autorizadas |

#### Deployment Environments

| Environment | Branch | Landing Page | Web Services | Mobile Application | IoT Simulator |
|---|---|---|---|---|---|
| **Local** | `feat/*`, `develop` | `npm start` en `localhost:3000` | `./mvnw spring-boot:run` con PostgreSQL local | Android Emulator desde Android Studio | `python simulator/cli.py serve` con un broker Mosquitto local |
| **Preview** | Pull Request | Preview Deployment generado automáticamente por Cloudflare Pages | — | — | — |
| **Production** | `main` | Cloudflare Pages Production | Render y Neon | Firebase App Distribution | Máquina virtual en Google Compute Engine |

#### Landing Page Deployment

| Step | Action |
|---|---|
| **1** | Verificar que `node_modules/` y `build/` estén incluidos en `.gitignore` y que `npm run build` se ejecute sin errores. |
| **2** | Iniciar sesión en Cloudflare, ingresar a *Workers & Pages* y seleccionar *Create → Pages → Connect to Git*. |
| **3** | Autorizar la aplicación de Cloudflare en la organización de GitHub del equipo e importar el repositorio `guardian-plus-website`. |
| **4** | Configurar el proyecto: *Project name* `guardian-plus`, *Production branch* `main`, *Framework preset* `Create React App`, *Build command* `npm run build` y *Build output directory* `build`. |
| **5** | Registrar la variable de entorno `NODE_VERSION` con el valor `24`, junto con las variables `REACT_APP_*` del Landing Page a medida que estén disponibles. |
| **6** | Ejecutar *Save and Deploy* y registrar la URL pública asignada por Cloudflare Pages, con el formato `https://<project-name>.pages.dev`. |
| **7** | Validar la navegación entre secciones, el formulario de contacto, los meta tags definidos en la sección 3.1.2.3 y los resultados de accesibilidad y rendimiento en Lighthouse. |

Una vez configurado, cada integración en `main` publica automáticamente una nueva versión del Landing Page, y cada Pull Request genera una URL de vista previa que permite revisar los cambios antes de integrarlos.

#### Web Services Deployment

**Preparación del repositorio**

| Step | Action |
|---|---|
| **1** | Agregar un `Dockerfile` multi-stage en la raíz del repositorio: una etapa de construcción con Maven y JDK 27 que ejecuta `./mvnw -DskipTests package`, y una etapa de ejecución con JRE 27 que copia el archivo `.jar` generado y lo inicia con `java -jar`. |
| **2** | Agregar un `.dockerignore` que excluya `target/`, `.idea/` y otros archivos locales. |
| **3** | Configurar `server.port=${PORT:8080}` en `application.properties`, de modo que la aplicación utilice el puerto asignado por Render. |
| **4** | Verificar que la conexión a la base de datos se obtenga de las variables de entorno `SPRING_DATASOURCE_*`, sin credenciales en el código fuente. |

**Base de datos en Neon**

| Step | Action |
|---|---|
| **5** | Crear el proyecto `guardian-plus` en Neon, en la región AWS us-east-1 (N. Virginia). |
| **6** | Crear la base de datos `guardian_plus` y obtener los datos de conexión (host, usuario y contraseña), utilizando `sslmode=require`. |

**Servicio en Render**

| Step | Action |
|---|---|
| **7** | En Render, seleccionar *New → Web Service* y conectar el repositorio `guardian-plus-platform`. |
| **8** | Configurar *Language* `Docker`, *Branch* `main`, *Region* `Virginia (US East)` e *Instance Type* `Free`. |
| **9** | Registrar las variables de entorno indicadas en la tabla siguiente. |
| **10** | Configurar `/v3/api-docs` como *Health Check Path* y mantener activo *Auto-Deploy* ante cada commit en `main`. |
| **11** | Ejecutar el despliegue y validar el acceso público a la documentación de los Web Services en la ruta `/swagger-ui/index.html` del dominio asignado por Render. |

| Variable | Description | Source |
|---|---|---|
| `SPRING_DATASOURCE_URL` | Cadena de conexión JDBC de la base de datos `guardian_plus`, con el parámetro `sslmode=require`. | Neon |
| `SPRING_DATASOURCE_USERNAME` | Usuario de la base de datos. | Neon |
| `SPRING_DATASOURCE_PASSWORD` | Contraseña de la base de datos. | Neon |
| `JWT_SECRET` | Clave utilizada por IAM para firmar los JWT de sesión. | Generada por el equipo |
| `STRIPE_SECRET_KEY` | Clave secreta de Stripe en modo de prueba. | Stripe Dashboard |
| `GOOGLE_MAPS_API_KEY` | Clave para las consultas de geocodificación. | Google Cloud Console |
| `FIREBASE_CREDENTIALS` | Credenciales de la cuenta de servicio de Firebase, codificadas en Base64, para el envío de notificaciones push. | Firebase Console |

Las variables de integraciones externas se registran a medida que cada integración se implementa. Asimismo, la instancia gratuita de Render se suspende tras un periodo de inactividad, por lo que la primera solicitud posterior puede demorar alrededor de un minuto; antes de cada demostración se realiza una solicitud previa para reactivar el servicio.

#### Mobile Application Deployment

| Step | Action |
|---|---|
| **1** | Crear el proyecto `guardian-plus` en Firebase y registrar la aplicación Android con su `applicationId` definitivo. Este identificador no puede modificarse después sin registrar una nueva aplicación. |
| **2** | Descargar `google-services.json` y ubicarlo en el módulo `app/`. El archivo se excluye del repositorio mediante `.gitignore` y se comparte con el equipo por un canal privado. |
| **3** | Definir en `BuildConfig` la URL base de la API (`API_BASE_URL`), apuntando al servicio de Render en el build de release, y registrar la API key de Google Maps en `local.properties`. |
| **4** | Generar el keystore de firma desde *Build → Generate Signed App Bundle or APK* y almacenarlo fuera del repositorio, junto con sus credenciales. |
| **5** | Desde la rama `release/*`, actualizar `versionName` con la versión semántica de la release e incrementar `versionCode`. |
| **6** | Generar el APK de release firmado desde Android Studio o mediante `./gradlew assembleRelease`. |
| **7** | En Firebase Console, ingresar a *App Distribution*, cargar el APK, redactar las notas de la versión y asignarlo al grupo de testers `validation-testers`. |
| **8** | Verificar que los testers reciban la invitación por correo e instalen la aplicación mediante Firebase App Tester. |

#### IoT Simulator Deployment

El IoT Simulator se despliega en una máquina virtual de Google Compute Engine aprovisionada con Terraform, cuyos archivos se encuentran en la carpeta `infra/terraform` del repositorio. En esa misma máquina se ejecutan, como servicios de `systemd`, el broker MQTT Eclipse Mosquitto y el simulador, de modo que este último publica la telemetría hacia un broker local y el backend se suscribe a él mediante MQTT sobre WebSocket.

El repositorio incluye además un `Dockerfile` para ejecutar el simulador de forma local en contenedor. El despliegue en producción no utiliza la imagen, porque el simulador requiere un broker MQTT junto a él y la imagen contiene únicamente el simulador.

**Recursos aprovisionados**

| Resource | Description |
|---|---|
| **Máquina virtual `guardian-iot-sim`** | Debian 12, tipo `e2-small`, disco de 20 GB, zona `us-central1-a`, con Secure Boot y OS Login habilitados. |
| **Dirección IP externa estática** | Permite que el backend conozca siempre la dirección del broker. |
| **Regla de firewall `guardian-iot-sim-app`** | Permite el tráfico TCP hacia los puertos 5000 (API del simulador), 1883 (MQTT) y 9001 (MQTT sobre WebSocket) únicamente desde las direcciones autorizadas: el equipo de desarrollo y el servidor del backend. |
| **Regla de firewall `guardian-iot-sim-ssh`** | Permite el acceso SSH por el puerto 22 únicamente desde el rango de Identity-Aware Proxy de Google. |
| **Cuenta de servicio** | Identidad de la máquina virtual, limitada a los roles `logging.logWriter` y `monitoring.metricWriter`. |

**Preparación y despliegue**

| Step | Action |
|---|---|
| **1** | Verificar que la rama `main` del repositorio contiene el código a desplegar, ya que la máquina virtual lo clona desde GitHub al arrancar. |
| **2** | Seleccionar o crear un proyecto en Google Cloud con facturación habilitada y abrir Google Cloud Shell. |
| **3** | Habilitar las APIs `iam.googleapis.com` y `cloudresourcemanager.googleapis.com` con `gcloud services enable`. La API de Compute es habilitada por el propio Terraform. |
| **4** | Instalar Terraform (versión 1.5 o superior) en el directorio personal de Cloud Shell, ya que no viene preinstalado. |
| **5** | Clonar el repositorio, ingresar a `infra/terraform` y copiar `terraform.tfvars.example` como `terraform.tfvars`. |
| **6** | Completar las variables indicadas en la tabla siguiente. |
| **7** | Ejecutar `terraform init` y `terraform apply`, y aprobar el plan de 8 recursos. |
| **8** | Esperar que el script de arranque termine de instalar Mosquitto y el simulador, y validar el estado en `http://<external_ip>:5000/health`. |
| **9** | Registrar el valor `mqtt_websocket_broker` entregado por Terraform en la variable `HEALTH_MONITORING_MQTT_BROKER_URL` del backend. |

| Terraform Variable | Description |
|---|---|
| `project_id` | Identificador del proyecto de Google Cloud donde se despliegan los recursos. |
| `allowed_source_ranges` | Direcciones IP autorizadas a acceder a la API del simulador y al broker: el equipo de desarrollo y el servidor del backend. El broker permite conexiones anónimas, por lo que esta lista se mantiene lo más acotada posible. |
| `backend_devices_url` | Endpoint del backend desde el que el simulador obtiene los wearables (`/api/v1/wearable-devices`). |
| `mqtt_max_rate` / `mqtt_burst` | Límite de mensajes por segundo hacia el broker (20) y tamaño de ráfaga permitido (20). Las alertas críticas no esperan. |
| `mqtt_retain` | Indica que el broker conserva el último mensaje de cada tópico para suscriptores que se conecten tarde (`true`). |

Las variables de entorno que Terraform entrega al servicio del simulador son las siguientes:

| Variable | Description | Value |
|---|---|---|
| `MQTT_HOST` / `MQTT_PORT` | Broker al que se publica la telemetría. | `localhost` / `1883` |
| `MQTT_TOPIC_PREFIX` | Prefijo de los tópicos (`<prefijo>/<canal>/<deviceId>`). | `guardian` |
| `BACKEND_DEVICES_URL` | Endpoint del backend desde el que se cargan los wearables. | Definido en `terraform.tfvars` |
| `SIMULATOR_PORT` | Puerto de la API HTTP del simulador. | `5000` |
| `EMIT_INTERVAL_SECONDS` | Segundos entre ciclos de simulación. | `10` |
| `MQTT_MAX_RATE` / `MQTT_BURST` / `MQTT_RETAIN` | Control de tasa y retención de mensajes. | `20` / `20` / `true` |

Si el backend no está disponible al iniciar el simulador, este arranca igualmente y los dispositivos pueden cargarse posteriormente mediante `POST /update` o de forma manual mediante `PUT /devices`. Al terminar las demostraciones, la infraestructura se elimina con `terraform destroy` para evitar costos.

#### Deployment Considerations

| Decision | Description |
|---|---|
| **Transporte de telemetría** | En la presente iteración, la pulsera es reemplazada por el IoT Simulator, que publica la telemetría y los eventos del dispositivo mediante MQTT en canales independientes (`vitals`, `alerts`, `location`, `activity` y `sleep`), de modo que cada Bounded Context se suscriba únicamente a lo que consume. El broker Mosquitto se despliega en la misma máquina virtual y el backend se suscribe mediante MQTT sobre WebSocket. Las alertas críticas se publican con QoS 1 y la telemetría de rutina con QoS 0. Un broker gestionado, como HiveMQ Cloud o EMQX, podrá reemplazar a Mosquitto cuando se integre la pulsera física, modificando únicamente la dirección configurada en el backend. |
| **Seguridad del simulador y del broker** | El broker permite conexiones anónimas y la API del simulador no implementa autenticación, además de utilizar el servidor de desarrollo de Flask. Por ello, el acceso se restringe mediante el firewall de la red a las direcciones IP del equipo y del backend, y el simulador se utiliza únicamente como herramienta de desarrollo y validación. |
| **Ciclo de vida de la infraestructura** | La infraestructura del simulador se encuentra definida como código y puede crearse o destruirse con un solo comando, por lo que se mantiene activa únicamente durante las pruebas y demostraciones. |
| **Eventos de integración** | Debido a que los Bounded Contexts se despliegan dentro de una única REST API, los eventos de integración entre ellos se publican en memoria mediante Spring Application Events, sin requerir infraestructura adicional. Los puertos de salida definidos en cada contexto, como `MobilityEventOutputPort`, permiten reemplazar este mecanismo por un Message Broker como RabbitMQ si en el futuro los contextos se despliegan de forma independiente. |
| **Ubicación de los servicios** | La REST API y la base de datos se despliegan en la región US East para reducir la latencia entre ambos. |

#### Deployment Diagram

El siguiente diagrama, elaborado con Structurizr bajo el C4 Model, presenta la distribución de los contenedores de Guardian+ en el entorno de producción. Su explicación detallada se encuentra en la sección 2.5.3.4.

![deployment-diagram](../assets/images/chapterII/c4-diagrams/deployment.png)

## 4.2. Landing Page & Mobile Application Implementation

### 4.2.1. Sprint 1

#### 4.2.1.1. Sprint Planning 1

El Sprint 1 constituye el primer Sprint de implementación de Guardian+ y se ejecuta entre el 7 y el 27 de septiembre de 2026. Su planificación se realizó en una reunión sincrónica del equipo al inicio del Sprint, en la que se revisó el Product Backlog priorizado de la sección 2.4.3, se acordó la capacidad de trabajo del equipo y se seleccionaron las User Stories que componen el alcance comprometido.

El criterio de selección combinó dos referencias. La primera es la prioridad de negocio establecida en el Product Backlog, que sitúa en los primeros lugares las historias de detección y respuesta ante emergencias por constituir la propuesta de valor central del producto. La segunda es el alcance esperado para el Stage Review de la semana 7, que requiere la Landing Page desplegada, el backend desplegado al 70% y las pantallas core de la aplicación en funcionamiento. De la intersección de ambas resulta el alcance comprometido: el circuito completo de emergencia —desde la pulsera hasta el teléfono del contacto de auxilio—, la geolocalización en tiempo real y la totalidad de las historias de la Landing Page.

Las pantallas core que se habilitan en este Sprint son, en consecuencia, las del circuito de emergencia: *Inicio*, con el estado general de la persona bajo cuidado; *Alertas*, con las alertas activas, el detalle del incidente y la configuración de contactos; y *Ubicación*, con la posición en tiempo real. Las pantallas de *Salud* y *Rutinas* dependen de historias planificadas para los Sprints siguientes. El siguiente cuadro resume los acuerdos de la reunión de planificación.

| Sprint # | Sprint 1 |
|---|---|
| **Sprint Planning Background** | |
| Date | 2026-09-27 |
| Time | 07:00 PM |
| Location | Reunión virtual mediante Discord, en el canal de voz del equipo. |
| Prepared By | Equipo Healthify — Guardian+ |
| Attendees (to planning meeting) | Azama Fukuda, Juan Pablo / Lopez Monroy, Rodrigo Alfredo / Luis Miranda, Diego Andres / Mechan Montenegro, Luciana Carolina / Sanchez Cuadrado, Juan Antonio |
| Sprint 0 Review Summary | No aplica. El Sprint 1 es el primer Sprint de implementación del proyecto, por lo que no existe un Sprint previo del cual reportar resultados de software. El antecedente inmediato es el hito AV1, en el que se entregaron los Capítulos I y II del informe: el análisis de los segmentos objetivo, el Product Backlog con 33 User Stories estimadas en Story Points y el diseño estratégico del dominio con sus cinco Bounded Contexts. Esos artefactos constituyen la línea base sobre la que se planifica este Sprint. |
| Sprint 0 Retrospective Summary | No aplica por la misma razón. En su lugar, el equipo estableció en esta reunión los acuerdos de trabajo que regirán el Sprint: la estrategia de ramificación GitFlow y las convenciones de nomenclatura de ramas definidas en la sección 4.1.2.1, el uso de Conventional Commits, la obligatoriedad de revisión por Pull Request antes de integrar a `develop` y el registro del avance de cada tarea en el tablero de ClickUp. |
| **Sprint Goal & User Stories** | |
| Sprint 1 Goal | *Our focus is on letting a family reach Guardian+ and be warned in time: a person interested in the service can find it, understand it and choose a plan on their own, and a family that already uses it is warned on the phone when the person under their care suffers a fall or asks for help, wherever they are.*<br><br>*We believe it delivers to families and caregivers the peace of mind of knowing that a critical event will not go unnoticed during their absence, which is the reason they hire the service.*<br><br>*This will be confirmed when an interested visitor completes on their own the path from discovering Guardian+ to requesting information or choosing a plan, and when a fall or an SOS raised on the wrist of the person under care reaches their family's phone, is acknowledged from it, and is passed on to another contact of the care circle if nobody answers.*<br><br>**Métrica de cumplimiento:** un visitante recorre la Landing Page pública y envía una solicitud de contacto o selecciona un plan sin asistencia; una caída detectada o una activación del botón SOS llega al teléfono del contacto primario en menos de 5 segundos desde su detección (US08) y se escala a los contactos secundarios transcurridos 60 segundos sin reconocimiento (US11); el familiar reconoce la alerta y consulta la ubicación de la persona bajo cuidado desde la aplicación; y las 10 User Stories del alcance quedan verificadas contra sus criterios de aceptación (39 Story Points completados). |
| Sprint 1 Velocity | 40 Story Points. Corresponde a la capacidad estimada del equipo de cinco integrantes para un Sprint de tres semanas, calculada sobre una dedicación promedio de ocho horas semanales por integrante. Al ser el primer Sprint, este valor es una estimación inicial que será ajustada en la planificación del Sprint 2 con la velocidad real observada. |
| Sum of Story Points | 39 Story Points. |

Las User Stories que conforman el alcance comprometido del Sprint 1 son las siguientes, tomadas del Product Backlog en su orden de prioridad:

| # Orden | User Story Id | Título | Story Points | Bounded Context / Producto |
|---|---|---|---|---|
| 1 | US15 | Activación de auxilio mediante botón SOS en pulsera | 5 | Emergency & Alerting |
| 2 | US08 | Detección automática de caídas y despacho de emergencia | 8 | Emergency & Alerting |
| 3 | US09 | Generación de alertas por transgresión de umbrales biomédicos | 5 | Emergency & Alerting |
| 4 | US11 | Escalamiento automatizado de alertas críticas no atendidas | 5 | Emergency & Alerting |
| 5 | US16 | Administración de agenda de contactos de auxilio | 2 | Emergency & Alerting |
| 6 | US18 | Telemetría de geolocalización en tiempo real | 5 | Mobility & Geofencing |
| 7 | US30 | Navegación entre secciones informativas de la Landing Page | 1 | Landing Page |
| 8 | US31 | Presentación de características y beneficios clave del sistema | 2 | Landing Page |
| 9 | US32 | Captura y procesamiento de solicitudes de contacto institucional | 3 | Landing Page |
| 10 | US33 | Visualización comparativa de planes de suscripción Guardian+ | 3 | Landing Page |
| | | **Total** | **39** | |

La suma de 39 Story Points se ubica por debajo de la velocidad establecida de 40, dejando un margen deliberado para las tareas de configuración inicial del entorno de desarrollo, del repositorio y del despliegue descritas en la sección 4.1, que el equipo debe completar durante este primer Sprint y que no están representadas como User Stories en el Product Backlog.

#### 4.2.1.2. Aspect Leaders and Collaborators

Para el Sprint 1 el equipo organizó el trabajo en ocho aspectos: el **UX/UI Design**, que comprende la guía de estilos, la arquitectura de información, los wireframes y los mock-ups; los Bounded Contexts **Health Monitoring**, **Emergency & Alerting**, **Mobility & Geofencing**, **Care Routines & Wellness**, **IAM** y **Profile & Subscriptions**; y el **Testing**, con las pruebas unitarias, de integración y de aceptación del Sprint.

La siguiente Leadership-and-Collaboration Matrix (LACX) indica el líder (L) y los colaboradores (C) de cada aspecto.

| Team Member (Last Name, First Name) | GitHub Username | UX/UI Design | Health Monitoring | Emergency & Alerting | Mobility & Geofencing | Care Routines & Wellness | IAM | Profile & Subscriptions | Testing |
|---|---|---|---|---|---|---|---|---|---|
| Azama Fukuda, Juan Pablo | Llummo | L | L | C | C | C | L | C | C |
| Mechan Montenegro, Luciana Carolina | luuu6 | C | C | C | C | L | C | C | C |
| Luis Miranda, Diego Andres | Andrewdmr | C | C | C | L | C | C | C | C |
| López Monroy, Rodrigo Alfredo | rodrigolopezu | C | C | L | C | C | C | C | C |
| Sanchez Cuadrado, Juan Antonio | JuanASC05 | C | C | C | C | C | C | L | L |

#### 4.2.1.3. Sprint Backlog 1

El objetivo del Sprint 1 es que una persona interesada pueda conocer Guardian+ desde la Landing Page y que una familia que ya usa el servicio reciba en su teléfono las alertas de caída o SOS de la persona bajo cuidado. Para lograrlo, el equipo organizó el trabajo del Sprint en ClickUp, distribuyendo las tareas de diseño, configuración, implementación y documentación entre los integrantes.

El tablero del Sprint 1 está disponible en el siguiente enlace: [Sprint Backlog 1 — Guardian+](https://sharing.clickup.com/9013201240/b/h/6-1400350000000524-2/1612e210bce4708)

![sprint-1-board-1](../assets/images/chatper4/sprint1/sprint-1-board-1.png)

![sprint-1-board-2](../assets/images/chatper4/sprint1/sprint-1-board-2.png)

La siguiente tabla detalla las tareas del Sprint 1 y su estado.

| Sprint # | Sprint 1 | | | | | | |
|---|---|---|---|---|---|---|---|
| **User Story Id** | **User Story Title** | **Work-Item / Task Id** | **Work-Item / Task Title** | **Description** | **Estimation (Hours)** | **Assigned To** | **Status** |
| — | — | TA-01 | General Style Guidelines | Definir la guía de estilos general: branding, tipografía, colores, espaciado y tono de comunicación. | 6 | Azama Fukuda, Juan Pablo | Done |
| — | — | TA-02 | Organization Systems | Documentar los sistemas de organización del contenido de la Landing Page y la aplicación. | 3 | Mechan Montenegro, Luciana Carolina | Done |
| — | — | TA-03 | Labelling Systems | Definir las etiquetas de las secciones y opciones de la Landing Page y la aplicación. | 3 | Lopez Monroy, Rodrigo Alfredo | Done |
| — | — | TA-04 | SEO Tags and Meta Tags | Definir los meta tags de la Landing Page y los metadatos de la aplicación para tiendas. | 2 | Sanchez Cuadrado, Juan Antonio | Done |
| — | — | TA-05 | Searching Systems | Documentar las opciones de búsqueda y filtrado de la aplicación. | 3 | Azama Fukuda, Juan Pablo | Done |
| — | — | TA-06 | Navigation Systems | Documentar la navegación entre secciones de la Landing Page y pantallas de la aplicación. | 3 | Lopez Monroy, Rodrigo Alfredo | Done |
| — | — | TA-07 | Landing Page Wireframe | Diseñar los wireframes de la Landing Page para escritorio y móvil. | 5 | Mechan Montenegro, Luciana Carolina | Done |
| — | — | TA-08 | Landing Page Mock-up | Diseñar los mock-ups de la Landing Page aplicando la guía de estilos. | 6 | Mechan Montenegro, Luciana Carolina | Done |
| — | — | TA-09 | Software Development Environment Configuration | Documentar las herramientas y el entorno de desarrollo del proyecto. | 3 | Lopez Monroy, Rodrigo Alfredo | Done |
| — | — | TA-10 | Source Code Management | Configurar los repositorios en GitHub y documentar su gestión. | 2 | Luis Miranda, Diego Andres / Azama Fukuda, Juan Pablo | To-do |
| — | — | TA-11 | GitFlow & Branching Strategy | Definir la estrategia GitFlow y las convenciones de ramas y commits. | 2 | Sanchez Cuadrado, Juan Antonio | Done |
| — | — | TA-12 | Source Code Style Guide & Coding Conventions | Definir las guías de estilo y convenciones de código por lenguaje. | 3 | Sanchez Cuadrado, Juan Antonio | Done |
| — | — | TA-13 | Software Deployment Configuration | Configurar y documentar el despliegue de la Landing Page y los Web Services. | 4 | Luis Miranda, Diego Andres / Lopez Monroy, Rodrigo Alfredo | Done |
| — | — | TA-14 | Sprint 1 Planning | Elaborar el Sprint Planning con el objetivo, la velocidad y las User Stories del Sprint. | 3 | Azama Fukuda, Juan Pablo | Done |
| — | — | TA-15 | Aspect Leaders and Collaborators Matrix | Elaborar la matriz de líderes y colaboradores por aspecto del Sprint. | 1 | Azama Fukuda, Juan Pablo | To-do |
| — | — | TA-16 | Sprint 1 Backlog | Elaborar el Sprint Backlog con el tablero y la tabla de tareas del Sprint. | 2 | Azama Fukuda, Juan Pablo | To-do |
| — | — | TA-17 | Development Evidence for Sprint 1 | Registrar los commits de implementación de cada repositorio. | 2 | Luis Miranda, Diego Andres | To-do |
| — | — | TA-18 | Execution Evidence for Sprint 1 | Registrar capturas y video de las funcionalidades implementadas. | 3 | Azama Fukuda, Juan Pablo | To-do |
| — | — | TA-19 | Testing Suite | Implementar las pruebas unitarias, de integración y de aceptación del Sprint. | 8 | Sanchez Cuadrado, Juan Antonio / Azama Fukuda, Juan Pablo / Mechan Montenegro, Luciana Carolina / Lopez Monroy, Rodrigo Alfredo / Luis Miranda, Diego Andres | To-Review |
| — | — | TA-20 | Services Documentation Evidence for Sprint 1 | Documentar los endpoints de los Web Services con OpenAPI. | 3 | Lopez Monroy, Rodrigo Alfredo | To-do |
| — | — | TA-21 | Software Deployment Evidence for Sprint 1 | Registrar la evidencia del despliegue de la Landing Page y los Web Services. | 2 | Luis Miranda, Diego Andres | To-do |
| — | — | TA-22 | Team Collaboration Insights for Sprint 1 | Registrar las analíticas de colaboración de los repositorios. | 1 | Azama Fukuda, Juan Pablo | To-do |
| — | — | TA-23 | Interview Design | Elaborar el guion de entrevistas de validación. | 2 | Mechan Montenegro, Luciana Carolina | To-do |
| — | — | TA-24 | Interview Registry | Realizar y registrar entre 3 y 5 entrevistas de validación. | 5 | Azama Fukuda, Juan Pablo / Sanchez Cuadrado, Juan Antonio / Mechan Montenegro, Luciana Carolina / Lopez Monroy, Rodrigo Alfredo / Luis Miranda, Diego Andres | To-do |
| — | — | TA-25 | Heuristic Evaluations | Evaluar la usabilidad de la Landing Page y la aplicación con principios heurísticos. | 4 | Mechan Montenegro, Luciana Carolina / Lopez Monroy, Rodrigo Alfredo / Sanchez Cuadrado, Juan Antonio / Luis Miranda, Diego Andres | Done |
| — | — | TA-26 | Prototyping Development Flow | Diseñar los flujos, wireframes y mock-ups de la aplicación por Bounded Context. | 10 | Azama Fukuda, Juan Pablo / Mechan Montenegro, Luciana Carolina / Sanchez Cuadrado, Juan Antonio / Lopez Monroy, Rodrigo Alfredo / Luis Miranda, Diego Andres | To-do |
| — | — | TA-27 | Version Registry | Registrar las versiones del informe y sus cambios. | 1 | Azama Fukuda, Juan Pablo | To-do |
| — | — | TA-28 | Fill in Student Outcome | Completar la sección de Student Outcome del informe. | 2 | Mechan Montenegro, Luciana Carolina / Sanchez Cuadrado, Juan Antonio / Luis Miranda, Diego Andres / Azama Fukuda, Juan Pablo / Lopez Monroy, Rodrigo Alfredo | In-Process |

#### 4.2.1.4. Development Evidence for Sprint Review

En esta sección se registran los commits que implementan las User Stories del Sprint 1 en cada repositorio.

##### Web Services — Emergency & Alerting

Implementación del Bounded Context Emergency & Alerting (US08, US09, US11, US15 y US16), integrada a `develop` mediante los Pull Requests [#7](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform/pull/7) y [#6](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform/pull/6). Este último corrige el manejo compartido de solicitudes mal formadas.

| Repository | Branch | Commit Id | Commit Message | Committed on |
|---|---|---|---|---|
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `fix/shared-invalid-request-parameters` | `b49811f` | `fix(shared): return client error statuses for malformed or rejected requests` | 2026-10-01 |
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `feat/emergency-alerting-core-flow` | `6ef2a84` | `feat(emergency-alerting): add domain model, commands, queries and events` | 2026-09-30 |
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `feat/emergency-alerting-core-flow` | `62512c5` | `feat(emergency-alerting): add jpa persistence entities and repositories` | 2026-09-30 |
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `feat/emergency-alerting-core-flow` | `785c9bb` | `feat(emergency-alerting): implement command and query services` | 2026-09-30 |
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `feat/emergency-alerting-core-flow` | `92371b3` | `feat(emergency-alerting): add event handlers, integration events and context facade` | 2026-09-30 |
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `feat/emergency-alerting-core-flow` | `54b5ce7` | `fix(emergency-alerting): retry alert commands that lose an optimistic-lock race` | 2026-10-01 |
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `feat/emergency-alerting-core-flow` | `b704e95` | `feat(emergency-alerting): send alert notifications through channel adapters` | 2026-10-01 |
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `feat/emergency-alerting-core-flow` | `05d11e7` | `feat(emergency-alerting): add fall confirmation and acknowledgement timeout schedulers` | 2026-10-01 |
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `feat/emergency-alerting-core-flow` | `849eea9` | `fix(emergency-alerting): keep deliveries in dispatch order and avoid update deadlocks` | 2026-10-01 |
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `feat/emergency-alerting-core-flow` | `7df392d` | `feat(emergency-alerting): add rest controllers, resources and assemblers` | 2026-10-01 |
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `feat/emergency-alerting-core-flow` | `e19fb0a` | `docs(readme): document emergency and alerting bounded context` | 2026-10-01 |

##### Web Services — Care Routines & Wellness

Implementación anticipada del Bounded Context Care Routines & Wellness (US06, US13, US14, US17, US26, US27 y US29), correspondiente a la épica EP02, planificada para Sprints posteriores. Se integró a `develop` mediante los Pull Requests [#3](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform/pull/3) y [#5](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform/pull/5).

| Repository | Branch | Commit Id | Commit Message | Committed on |
|---|---|---|---|---|
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `feat/care-routines-and-wellness` | `6ce3850` | `feat(care-routines-wellness): add domain model, commands and queries` | 2026-09-29 |
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `feat/care-routines-and-wellness` | `c06a556` | `feat(care-routines-wellness): implement command and query services` | 2026-09-29 |
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `feat/care-routines-and-wellness` | `dcd1955` | `feat(care-routines-wellness): add jpa repositories` | 2026-09-29 |
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `feat/care-routines-and-wellness` | `1ac4bfb` | `feat(care-routines-wellness): add rest controllers, resources and assemblers` | 2026-09-29 |
| [guardian-plus-platform](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform) | `refactor/pluralize-medication-stock-endpoint` | `ce653fc` | `refactor(care-routines-wellness): pluralize medication stock endpoint path` | 2026-09-30 |

##### IoT Simulator

Implementación del simulador de la pulsera Guardian+: catálogo de señales y generador con estado por dispositivo, publicación por MQTT en canales por Bounded Context, API HTTP de control y monitoreo, y CLI. La imagen de contenedor del simulador se integró a `main` mediante el Pull Request [#1](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-iot-simulator/pull/1).

| Repository | Branch | Commit Id | Commit Message | Committed on |
|---|---|---|---|---|
| [guardian-plus-iot-simulator](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-iot-simulator) | `main` | `e264c53` | `chore: scaffold project structure and dependencies` | 2026-09-27 |
| [guardian-plus-iot-simulator](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-iot-simulator) | `main` | `db68bde` | `feat(model): add signal catalogue and stateful generator` | 2026-09-27 |
| [guardian-plus-iot-simulator](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-iot-simulator) | `main` | `259769a` | `feat(interfaces): add MQTT publisher and simulator HTTP API` | 2026-09-27 |
| [guardian-plus-iot-simulator](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-iot-simulator) | `main` | `c2a8dd1` | `feat(cli): add control and monitoring CLI` | 2026-09-27 |
| [guardian-plus-iot-simulator](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-iot-simulator) | `main` | `c8d4eb9` | `docs: document signals, thresholds and usage` | 2026-09-27 |
| [guardian-plus-iot-simulator](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-iot-simulator) | `build/docker-image` | `67eec4a` | `build(docker): add simulator container image` | 2026-10-06 |
| [guardian-plus-iot-simulator](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-iot-simulator) | `build/docker-image` | `12e0b64` | `feat: simulator functions now` | 2026-10-06 |

#### 4.2.1.5. Testing Suite Evidence for Sprint Review

Durante el presente Sprint se incorporaron pruebas automatizadas como parte del proceso de implementación de los Web Services de Guardian+. El objetivo de estas pruebas es verificar los comportamientos principales de los componentes desarrollados y reducir la posibilidad de introducir errores antes de integrar los cambios hacia las ramas principales del proyecto.

De acuerdo con el alcance del Sprint, que contempla el desarrollo progresivo del backend, las pruebas se implementan de manera incremental junto con las funcionalidades correspondientes a cada Bounded Context.

Para el Bounded Context **Profile** se desarrollaron Unit Tests orientados principalmente a validar los Aggregate Roots del dominio y un Application Service. Las pruebas fueron implementadas utilizando **JUnit Jupiter**, mientras que **Mockito** fue utilizado para aislar dependencias externas en las pruebas de servicios de aplicación.

Las pruebas siguen el patrón **Arrange - Act - Assert (AAA)**:

- **Arrange:** preparación de datos, objetos y dependencias necesarias para ejecutar el escenario.
- **Act:** ejecución de la operación o comportamiento que se desea comprobar.
- **Assert:** verificación de que el resultado obtenido corresponda con el comportamiento esperado.

En el presente avance, la evidencia automatizada desarrollada para Profile corresponde a **Unit Tests**. Los Integration Tests y Acceptance Tests bajo BDD no forman parte todavía de la implementación actual y podrán incorporarse en siguientes incrementos conforme se completen las integraciones entre Bounded Contexts y los flujos funcionales del producto.

##### Unit Tests - Bounded Context Profile

Las pruebas desarrolladas para Profile verifican las principales reglas y comportamientos de los Aggregate Roots `UserProfile`, `CareRecipientProfile`, `CareRelationship` y `UserPreferences`.

Adicionalmente, se incluye una prueba del servicio `UserProfileCommandServiceImpl`, utilizando Mockito para reemplazar temporalmente la implementación del repositorio y verificar el comportamiento del servicio de manera aislada.

| Test Class | Class Under Test | Test | Behavior Verified |
|---|---|---|---|
| `UserProfileTest` | `UserProfile` | `shouldCreateUserProfileWithValidData` | Verifica que un perfil de usuario pueda crearse correctamente cuando recibe información válida. |
| `UserProfileTest` | `UserProfile` | `shouldUpdatePersonalInformation` | Verifica la actualización del nombre y apellido del perfil de usuario. |
| `UserProfileTest` | `UserProfile` | `shouldUpdateContactInformation` | Verifica la actualización de la información de contacto asociada al perfil. |
| `UserProfileTest` | `UserProfile` | `shouldRejectBlankPersonalInformation` | Verifica que el Aggregate Root rechace información personal inválida o vacía. |
| `CareRecipientProfileTest` | `CareRecipientProfile` | `shouldCreateCareRecipientProfileWithValidData` | Verifica la creación correcta de un perfil de persona bajo cuidado. |
| `CareRecipientProfileTest` | `CareRecipientProfile` | `shouldUpdatePersonalInformation` | Verifica la actualización de nombres y fecha de nacimiento de la persona bajo cuidado. |
| `CareRecipientProfileTest` | `CareRecipientProfile` | `shouldUpdateProfileImage` | Verifica la actualización de la imagen del perfil de la persona bajo cuidado. |
| `CareRecipientProfileTest` | `CareRecipientProfile` | `shouldRejectNullBirthDate` | Verifica que el Aggregate Root rechace una fecha de nacimiento inválida. |
| `CareRelationshipTest` | `CareRelationship` | `shouldEstablishCareRelationshipWithValidData` | Verifica que una relación de cuidado válida sea creada correctamente con estado `ACTIVE`. |
| `CareRelationshipTest` | `CareRelationship` | `shouldEndActiveCareRelationship` | Verifica la transición de una relación de cuidado desde `ACTIVE` hacia `ENDED`. |
| `CareRelationshipTest` | `CareRelationship` | `shouldRejectEndingRelationshipTwice` | Verifica que una relación que ya fue finalizada no pueda volver a finalizarse. |
| `CareRelationshipTest` | `CareRelationship` | `shouldRejectNullRelationshipType` | Verifica que no pueda establecerse una relación de cuidado sin un tipo válido. |
| `UserPreferencesTest` | `UserPreferences` | `shouldCreateUserPreferencesWithDefaultValues` | Verifica la creación de preferencias con los valores iniciales definidos por Guardian+. |
| `UserPreferencesTest` | `UserPreferences` | `shouldUpdateApplicationPreferences` | Verifica la actualización de las preferencias generales de aplicación. |
| `UserPreferencesTest` | `UserPreferences` | `shouldUpdateLanguageAndAccessibilityPreferences` | Verifica la actualización conjunta de idioma, alto contraste, reducción de movimiento y tamaño de fuente. |
| `UserPreferencesTest` | `UserPreferences` | `shouldRejectNullLanguage` | Verifica que el dominio rechace una actualización cuando no se proporciona un idioma válido. |
| `UserProfileCommandServiceImplTest` | `UserProfileCommandServiceImpl` | `shouldCreateUserProfileWhenUserHasNoProfile` | Verifica que el servicio cree y persista un nuevo perfil cuando el usuario todavía no posee uno. |
| `UserProfileCommandServiceImplTest` | `UserProfileCommandServiceImpl` | `shouldReturnConflictWhenUserAlreadyHasProfile` | Verifica que el servicio retorne un conflicto y no persista un nuevo perfil cuando el usuario ya posee uno. |

##### Domain Unit Tests

Las pruebas `UserProfileTest`, `CareRecipientProfileTest`, `CareRelationshipTest` y `UserPreferencesTest` se ejecutan directamente sobre los Aggregate Roots del Bounded Context Profile.

Estas pruebas no requieren inicializar Spring, una base de datos ni contenedores Docker, debido a que su objetivo es comprobar de manera aislada las reglas propias del dominio.

Entre los principales comportamientos validados se encuentran:

- creación de Aggregate Roots con información válida;
- modificación de información personal;
- actualización de información de contacto;
- actualización de imágenes de perfil;
- control del ciclo de vida de las relaciones de cuidado;
- validación de estados inválidos;
- configuración y modificación de preferencias de usuario;
- validación de parámetros obligatorios.

##### Application Service Unit Test

`UserProfileCommandServiceImplTest` verifica el comportamiento de la capa de aplicación.

En este caso se utiliza **Mockito** debido a que `UserProfileCommandServiceImpl` depende de `UserProfileRepository`.

El repositorio es reemplazado mediante un mock para controlar sus respuestas durante cada escenario de prueba.

Se verifican principalmente dos comportamientos:

- cuando el usuario todavía no posee un perfil, el servicio crea el Aggregate Root y ejecuta la operación de persistencia;
- cuando ya existe un perfil asociado al mismo usuario, el servicio retorna un resultado de conflicto y evita realizar una nueva operación de persistencia.

De esta manera, se comprueba el comportamiento del Application Service sin depender de una base de datos real.

##### Testing Execution Evidence

Los Unit Tests del Bounded Context **Profile** fueron ejecutados mediante Maven.

Para ejecutar únicamente las pruebas correspondientes a Profile se utilizó:

~~~powershell
.\mvnw.cmd "-Dtest=UserProfileTest,CareRecipientProfileTest,CareRelationshipTest,UserPreferencesTest,UserProfileCommandServiceImplTest" test
~~~

La siguiente evidencia muestra la ejecución de las pruebas correspondientes a `UserProfileCommandServiceImplTest`, `CareRecipientProfileTest`, `CareRelationshipTest`, `UserPreferencesTest` y `UserProfileTest`.

![Profile Unit Tests Execution](../assets/images/chapterIV/testing/profile-unit-tests-execution.png)

La ejecución comprende un total de **18 Unit Tests** distribuidos entre los cuatro Aggregate Roots principales de Profile y el Application Service `UserProfileCommandServiceImpl`.

Los resultados obtenidos fueron:

- `UserProfileCommandServiceImplTest`: 2 tests ejecutados.
- `CareRecipientProfileTest`: 4 tests ejecutados.
- `CareRelationshipTest`: 4 tests ejecutados.
- `UserPreferencesTest`: 4 tests ejecutados.
- `UserProfileTest`: 4 tests ejecutados.

La ejecución finalizó correctamente con los siguientes resultados:

~~~text
Tests run: 18, Failures: 0, Errors: 0, Skipped: 0
BUILD SUCCESS
~~~

Esto confirma que los Unit Tests implementados para el Bounded Context **Profile** se ejecutan satisfactoriamente y validan los comportamientos definidos tanto en los Aggregate Roots como en el Application Service probado.

##### Integration Tests and Acceptance Tests

Estas pruebas podrán incorporarse en siguientes incrementos cuando se encuentren disponibles las integraciones necesarias entre los diferentes Bounded Contexts y se implementen los flujos funcionales completos correspondientes a los User Stories del producto.


##### Testing Repository

Las pruebas automatizadas de Profile se encuentran dentro del mismo repositorio utilizado para la implementación de los Web Services de Guardian+.

**Repository:**

`upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform`

**Branch:**

`feat/profile-bounded-context`

**Testing source path:**

~~~text
src/test/java/com/healthify/guardian/platform/profile
~~~

La estructura principal utilizada para las pruebas es:

~~~text
profile
├── application
│   └── internal
│       └── commandservices
│           └── UserProfileCommandServiceImplTest.java
│
└── domain
    └── model
        └── aggregates
            ├── UserProfileTest.java
            ├── CareRecipientProfileTest.java
            ├── CareRelationshipTest.java
            └── UserPreferencesTest.java
~~~

##### Testing Commits

El siguiente commit contiene la implementación de los Unit Tests correspondientes al Bounded Context Profile durante el presente Sprint.

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Committed on (Date) |
|---|---|---|---|---|---|
| `upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-platform` | `feat/profile-bounded-context` | `711c50c` | `test(profile): add unit tests for profile bounded context` | — | `2026-10-03` |

Este commit incorpora las pruebas unitarias correspondientes a los cuatro Aggregate Roots principales de Profile y la prueba del Application Service `UserProfileCommandServiceImpl`.



#### 4.2.1.6. Execution Evidence for Sprint Review

Al cierre del Sprint 1, Guardian+ cuenta con el Landing Page desplegado y con una primera versión de la aplicación móvil conectada a los Web Services. En el Landing Page se completaron las User Stories US30, US31, US32 y US33: el visitante puede recorrer las secciones del sitio desde el menú, conocer las funcionalidades y beneficios de la pulsera y la aplicación, comparar los planes de suscripción y enviar una solicitud de contacto. En la aplicación móvil se implementaron el inicio de sesión, la pantalla de Inicio, la sección de Salud y la sección de Alertas con sus alertas activas, el detalle de cada alerta, el historial, la configuración de alertas y los contactos de emergencia.

##### Landing Page

El Landing Page se encuentra publicado en [guardian-plus.pages.dev](https://guardian-plus.pages.dev). La siguiente captura muestra la sección principal del sitio en su versión de escritorio.

![landing-page-execution](../assets/images/chatper4/sprint1/landing-page-execution.png)

| Producto | Video de ejecución |
|---|---|
| Landing Page | [Guardian+ — Landing Page (Sprint 1)](https://youtu.be/ZqqCONDHst8) |

##### Mobile Application

| Producto | Video de ejecución |
|---|---|
| Mobile Application | [Guardian+ — Mobile Application (Sprint 1)](https://www.youtube.com/watch?v=Q-VMpyzhfJM) |

#### 4.2.1.7. Services Documentation Evidence for Sprint Review

Los Web Services se documentan con OpenAPI mediante springdoc-openapi. La especificación se publica en `/v3/api-docs` y puede explorarse en Swagger UI (`/swagger-ui/index.html`). Los errores siguen un formato común (`code`, `message`, `details`) con los códigos `400`, `404`, `409` y `422`.

##### Emergency & Alerting

| Verbo | Endpoint | Acción | Parámetros | Respuesta |
|---|---|---|---|---|
| POST | `/api/v1/alerts` | Dispara una alerta de caída o SOS desde el wearable | Body: `careRecipientProfileId`, `sourceType`, `sourceReferenceId` | 201 `AlertResource` |
| GET | `/api/v1/alerts` | Historial paginado | Query: `careRecipientProfileId`, `severity`, `from`, `to`, `page`, `size` | 200 `PageResource` |
| GET | `/api/v1/alerts/active/care-recipient/{careRecipientProfileId}` | Alertas activas de la persona bajo cuidado | Path: `careRecipientProfileId` | 200 lista |
| GET | `/api/v1/alerts/pending/recipient/{userId}` | Alertas pendientes de reconocimiento (canal in-app) | Path: `userId` | 200 lista |
| GET | `/api/v1/alerts/{alertId}` | Detalle con entregas y respuestas | Path: `alertId` | 200 / 404 |
| POST | `/api/v1/alerts/{alertId}/dismiss` | Descarta una caída dentro de los 20 s | Path: `alertId` | 200 / 422 |
| POST | `/api/v1/alerts/{alertId}/acknowledge` | Reconoce la alerta y abre el incidente | Body: `userId` | 200 / 422 |
| POST | `/api/v1/alerts/{alertId}/responses` | Asume la respuesta y avisa al Care Circle | Body: `responderUserId` | 201 / 422 |
| POST | `/api/v1/alerts/{alertId}/responses/{responseId}/complete` | Registra el resultado de la intervención | Body: `notes` | 200 |
| GET | `/api/v1/incidents/{incidentId}` | Detalle del incidente | Path: `incidentId` | 200 / 404 |
| GET | `/api/v1/incidents/alert/{alertId}` | Incidente de una alerta | Path: `alertId` | 200 / 404 |
| POST | `/api/v1/incidents/{incidentId}/stabilize` | Declara estabilizada la situación | Body: `notes` | 200 / 422 |
| POST | `/api/v1/incidents/{incidentId}/close` | Cierra el incidente y resuelve la alerta | Body: `notes` | 200 / 422 |
| GET | `/api/v1/alert-settings/care-recipient/{careRecipientProfileId}` | Configuración de alertamiento | Path: `careRecipientProfileId` | 200 |
| PUT | `/api/v1/alert-settings/care-recipient/{careRecipientProfileId}` | Actualiza tiempo de espera y escalamiento | Body: `primaryAckTimeoutSec`, `escalationEnabled`, `broadcastCriticalImmediately` | 200 / 400 |
| POST / DELETE | `/api/v1/alert-settings/care-recipient/{careRecipientProfileId}/silent-mode` | Activa o desactiva el modo silencioso | Path: `careRecipientProfileId` | 200 |
| GET | `/api/v1/emergency-contacts/care-recipient/{careRecipientProfileId}` | Contactos de emergencia por prioridad | Path: `careRecipientProfileId` | 200 lista |
| POST | `/api/v1/emergency-contacts` | Registra un contacto de emergencia | Body: `careRecipientProfileId`, `userId`, `displayName`, `relationship`, `phoneNumber`, `priorityOrder` | 201 / 400 / 409 |
| PUT | `/api/v1/emergency-contacts/care-recipient/{careRecipientProfileId}/order` | Reordena las prioridades | Body: `orderedEmergencyContactIds` | 200 / 400 |
| DELETE | `/api/v1/emergency-contacts/{emergencyContactId}` | Da de baja un contacto | Path: `emergencyContactId` | 200 / 422 |
| GET | `/api/v1/alert-channel-settings/user/{userId}` | Canales de notificación del usuario | Path: `userId` | 200 lista |
| PUT | `/api/v1/alert-channel-settings/user/{userId}/channels/{channel}` | Habilita o deshabilita un canal | Body: `enabled`, `deviceToken` | 200 / 422 |
| POST | `/api/v1/webhooks/notification-deliveries` | Resultado de una entrega informado por el proveedor | Body: `alertId`, `deliveryId`, `status` | 204 / 404 |

##### Health Monitoring

| Verbo | Endpoint | Acción | Parámetros | Respuesta |
|---|---|---|---|---|
| POST | `/api/v1/vital-signs` | Registra una lectura enviada por el wearable y evalúa su rango normal | Body: `wearableDeviceId`, `careRecipientProfileId`, `vitalSignType`, `value`, `measuredAt` | 201 `VitalSignResource` / 400 / 404 / 409 / 422 |
| POST | `/api/v1/vital-signs/batches` | Sincroniza las lecturas almacenadas por el wearable sin conexión | Body: `readings` | 202 `TelemetryBatchResultResource` / 400 / 422 |
| POST | `/api/v1/vital-signs/{vitalSignId}/emit` | Reemite una lectura para la vista en vivo | Path: `vitalSignId` | 200 / 404 / 422 |
| GET | `/api/v1/vital-signs/{vitalSignId}` | Detalle de una lectura | Path: `vitalSignId` | 200 / 404 |
| GET | `/api/v1/vital-signs/live/{careRecipientProfileId}` | Última lectura de cada signo vital con su clasificación | Path: `careRecipientProfileId` | 200 `LiveVitalSignsResource` |
| GET | `/api/v1/vital-signs/history/{careRecipientProfileId}` | Historial de lecturas en un periodo | Path: `careRecipientProfileId`; Query: `from`, `to` | 200 lista / 400 |
| GET | `/api/v1/vital-sign-types` | Tipos de signo vital con rango normal y límites físicos | - | 200 lista |
| POST | `/api/v1/wearable-devices` | Vincula un wearable a la persona bajo cuidado | Body: `careRecipientProfileId`, `serialNumber`, `deviceType` | 201 / 400 / 409 |
| GET | `/api/v1/wearable-devices` | Lista todos los wearables vinculados | - | 200 lista |
| GET | `/api/v1/wearable-devices/care-recipient/{careRecipientProfileId}` | Wearables de la persona bajo cuidado | Path: `careRecipientProfileId` | 200 lista |
| POST | `/api/v1/health-reports` | Genera un reporte de salud del periodo indicado | Body: `careRecipientProfileId`, `generatedByUserId`, `periodStart`, `periodEnd` | 201 `HealthReportResource` / 400 / 422 |
| GET | `/api/v1/health-reports/{reportId}` | Detalle de un reporte de salud | Path: `reportId` | 200 / 404 |
| GET | `/api/v1/health-reports/care-recipient/{careRecipientProfileId}` | Reportes de la persona bajo cuidado, del más reciente al más antiguo | Path: `careRecipientProfileId` | 200 lista |

#### 4.2.1.8. Software Deployment Evidence for Sprint Review

En este Sprint se realizó el primer despliegue del Landing Page de Guardian+ en Cloudflare Pages, siguiendo la configuración descrita en la sección 4.1.4. El despliegue se integra con GitFlow: cada integración en la rama `main` del repositorio publica automáticamente una nueva versión del sitio.

##### Landing Page

| Aspecto | Detalle |
|---|---|
| **Plataforma** | Cloudflare Pages |
| **URL pública** | [guardian-plus.pages.dev](https://guardian-plus.pages.dev) |
| **Repositorio** | [guardian-plus-website](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-website) |
| **Rama de producción** | `main` |
| **Versión desplegada** | `v1.0.0` |
| **Configuración de build** | *Framework preset* `Create React App`, *Build command* `npm run build`, *Build output directory* `build` y `NODE_VERSION` con el valor `24` |

El despliegue se realizó en los siguientes pasos:

| Step | Acción | Resultado |
|---|---|---|
| **1** | Integración de la rama `feat/landing-page-first-iteration` en `develop` mediante el Pull Request #1. | Implementación de las User Stories US30, US31, US32 y US33 disponible en la rama de integración. |
| **2** | Creación del proyecto `guardian-plus` en Cloudflare Pages conectado al repositorio. | El primer build, ejecutado sobre el commit inicial de `main`, falló en la instalación de dependencias porque el `package-lock.json` no era compatible con npm 10, versión incluida en el entorno de build. |
| **3** | Creación de la rama `release/v1.0.0` desde `develop`, actualización de la versión a `1.0.0` y regeneración del `package-lock.json` para que `npm ci` funcione con npm 10 y npm 11. | Build y 26 pruebas automatizadas ejecutadas satisfactoriamente sobre una instalación limpia. |
| **4** | Integración de `release/v1.0.0` en `main` mediante el Pull Request #2. | Despliegue automático en Cloudflare Pages y publicación del sitio en la URL pública. |
| **5** | Validación del sitio publicado. | Navegación entre secciones, meta tags de la sección 3.1.2.3 y resultados de Lighthouse verificados. |

Resultados de Lighthouse sobre la URL pública:

| Categoría | Mobile | Desktop |
|---|---|---|
| **Performance** | 71 | 85 |
| **Accessibility** | 97 | 97 |
| **Best Practices** | 100 | 100 |
| **SEO** | 100 | 100 |

![landing-page-deployment](../assets/images/chatper4/sprint1/landing-page-deployment.png)

##### IoT Simulator

En este Sprint se desplegó el IoT Simulator en Google Cloud siguiendo la configuración descrita en la sección 4.1.4.

| Aspecto | Detalle |
|---|---|
| **Plataforma** | Google Cloud Compute Engine, aprovisionada con Terraform |
| **Acceso** | `http://34.45.141.10:5000` (API) y `34.45.141.10:1883` (MQTT), restringido por firewall |
| **Repositorio** | [guardian-plus-iot-simulator](https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-iot-simulator) |
| **Rama desplegada** | `main` |
| **Infraestructura** | VM `e2-small` con Debian 12, IP estática, 2 reglas de firewall y cuenta de servicio con permisos mínimos |
| **Servicios en la VM** | `mosquitto` y `guardian-simulator` (`systemd`, con reinicio automático) |

El despliegue se realizó en los siguientes pasos:

| Step | Acción | Resultado |
|---|---|---|
| **1** | Instalación de Terraform en Google Cloud Shell, que no lo incluía preinstalado. | Terraform 1.9.8 disponible en el directorio personal. |
| **2** | Configuración de `terraform.tfvars` y ejecución de `terraform init` y `terraform apply`. | Se crearon la IP estática y las dos reglas de firewall. La creación de la cuenta de servicio falló porque la API de IAM estaba deshabilitada en el proyecto. |
| **3** | Habilitación de `iam.googleapis.com` y `cloudresourcemanager.googleapis.com`, y nueva ejecución de `terraform apply`. | Se crearon la cuenta de servicio, sus permisos y la máquina virtual. En total, 8 recursos. |
| **4** | Ejecución del script de arranque de la VM. | Mosquitto y el simulador quedaron instalados y en ejecución como servicios. |
| **5** | Validación del estado en `/health`. | El simulador responde `status: ok`, con `mqttConnected: true` y `loopRunning: true`. |
| **6** | Carga de los wearables desde `GET /api/v1/wearable-devices` y verificación en `/signals`. | <completar cuando haya dispositivos cargados> |


#### 4.2.1.9. Team Collaboration Insights during Sprint

Durante el Sprint 1 (del 6 de septiembre al 6 de octubre de 2026), el equipo trabajó en los repositorios de cada producto mediante ramas por funcionalidad integradas con pull requests. A continuación se muestran las analíticas de colaboración (Pulse) de cada repositorio.

**Backend (Web Services):** 13 pull requests fusionados y 1 abierto, con 180 commits de 5 autores en todas las ramas.

![backend-insights](../assets/images/chatper4/sprint1/insights/backend-insights.png)

**Mobile App:** 6 pull requests fusionados, con 46 commits de 2 autores en todas las ramas.

![mobile-app-insights](../assets/images/chatper4/sprint1/insights/mobile-app-insights.png)

**Website (Landing Page):** 4 pull requests fusionados, con 25 commits de 2 autores en main.

![website-insights](../assets/images/chatper4/sprint1/insights/website-insights.png)

**IoT Simulator:** 1 pull request fusionado, con 7 commits de 1 autor en main.

![iot-simulator-insights](../assets/images/chatper4/sprint1/insights/iot-simulator-insights.png)

## 4.3. Validation Interviews

### 4.3.1. Diseño de Entrevistas

## Diseño de Entrevistas — Validación del Landing Page

La sesión de validación consiste en un recorrido guiado (think-aloud) por el Landing Page de Guardian+, en el mismo orden en que está estructurado el sitio: Hero → Pain Points → Cómo funciona → Pulsera → Beneficios → Tour de la app → Zonas Seguras → Por qué Guardian+ → Planes → Contacto. El objetivo de cada pregunta es verificar si, según su segmento, el entrevistado entiende y percibe el valor real que ofrece Guardian+ en esa sección, por lo que todas las preguntas buscan que el entrevistado se explaye y justifique su respuesta, evitando preguntas cerradas de sí/no.

### Segmento 1 — Familiares

1. **Hero:** Después de leer esta primera pantalla, ¿qué entiendes que hace Guardian+ por ti y tu familia, en tus propias palabras? ¿Por qué lo entiendes así?
2. **Pain Points:** ¿Cuál de estas tres preguntas refleja mejor una preocupación que tú mismo has tenido con tu familiar, y por qué esa en particular?
3. **Cómo funciona:** ¿Qué entiendes que pasa, paso a paso, si tu familiar sufre una emergencia? ¿Qué parte del proceso te queda más clara y cuál más confusa?
4. **Pulsera:** ¿Cuáles de estas funciones de la pulsera usarías con tu familiar, y qué tranquilidad específica te daría cada una?
5. **Beneficios:** ¿Cuáles de estos seis beneficios te parecen más importantes para decidir si usarías Guardian+, y qué necesidad tuya resuelve cada uno?
6. **Tour de la app:** Al ver la pantalla de Inicio ¿qué tan bien reflejan la forma en que tú querrías enterarte del estado de tu familiar durante el día? ¿Por qué?
7. **Zonas Seguras:** ¿De qué manera esta función cambiaría tu tranquilidad o tu rutina actual con tu familiar? ¿Por qué?
8. **Por qué Guardian+:** ¿Qué tan identificado te sientes con el testimonio mostrado, y qué parte de esa historia se parece más a la tuya?
9. **Planes:** Viendo los tres planes, ¿cuál elegirías para tu familia y qué fue lo que más pesó en tu decisión?
10. **Contacto:** Si tuvieras dudas sobre qué plan elegir, ¿qué información esperarías recibir al usar este formulario de contacto?

### Segmento 2 — Cuidadores

1. **Hero:** Si estuvieras buscando una herramienta que te apoye en tu trabajo de cuidado, ¿qué entiendes que te ofrece Guardian+ a partir de esta pantalla? ¿Por qué lo entiendes así?
2. **Pain Points:** ¿Cuál de estas preguntas representa mejor un riesgo que tú monitoreas en tu trabajo diario, y por qué ese en particular?
3. **Cómo funciona:** Viendo estos 3 pasos, ¿en qué se parece o se diferencia esto de cómo actúas tú actualmente ante una emergencia con tu paciente?
4. **Pulsera:** ¿Cuáles de estas funciones de la pulsera usarías en tu trabajo diario, y qué problema puntual de tu rutina de cuidado te resolvería cada una?
5. **Beneficios:** ¿Cuáles de estos beneficios te ahorrarían tiempo o esfuerzo en tu rutina diaria de cuidado, y de qué manera lo harían?
6. **Tour de la app:** Al ver la pantalla de Inicio con el estado del paciente, ¿qué tan útil te resulta esa información para hacer seguimiento durante tu jornada? ¿Qué le agregarías o quitarías?
7. **Zonas Seguras:** ¿De qué manera esta función reduciría la supervisión constante que haces actualmente? ¿Por qué?
8. **Por qué Guardian+:** Como cuidador profesional, ¿qué tanta confianza te generan estos diferenciadores frente a lo que usas hoy, y por qué?
9. **Planes:** Si tú recomendaras un plan a la familia de tu paciente, ¿cuál sugerirías según las necesidades que observas en tu trabajo, y por qué ese?
10. **Contacto:** Si necesitaras orientación sobre el plan adecuado para tu paciente, ¿qué información esperarías recibir al usar este formulario de contacto?

### 4.3.2. Registro de Entrevistas

A continuación se presenta el registro de las entrevistas de validación del Landing Page, incluyendo la ficha de cada entrevistado, la captura de pantalla correspondiente y el análisis de sus respuestas.

##### Segmento 2: Cuidadores

**Entrevistado 1**

**Enlace a la grabación de la entrevista:** [Ver grabación en SharePoint](https://upcedupe-my.sharepoint.com/:v:/g/personal/u202411310_upc_edu_pe/IQD8oJT2Z8TpSoJBUXSMSMGhAfeo7eDVGKMqM2Pu5ygx8Ys?e=Uh9lJl&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

| Campo | Valor |
|---|---|
| Nombre y apellido | Roxana Paola Diana |
| Edad | 39 |
| Distrito | Surco |

![Captura Entrevista Validación Cuidador 1](../assets/images/chatper4/validation-interviews/entrevista_validacion_cuidador_1.png)

**Análisis de la entrevista:** Roxana Paola Diana recorrió el Landing Page de Guardian+ y validó la mayoría de sus secciones, comprendiendo la propuesta de valor y el funcionamiento del servicio a partir de la pulsera, la aplicación y la respuesta ante emergencias. Desde su experiencia como cuidadora, consideró que la información más relevante del sitio es la detección de caídas, el recordatorio de medicaciones, la detección de signos vitales y el envío de alertas, ya que son los aspectos que más se relacionan con su rutina diaria de cuidado. Como oportunidad de mejora, sugirió hacer el Landing Page más dinámico para captar mejor la atención del visitante durante el recorrido.

### 4.3.3. Evaluaciones según heurísticas

### UX Heuristics & Principles Evaluation
**Usability - Inclusive Design - Information Architecture**

| | |
|---|---|
| **CARRERA** | Ingeniería de Software |
| **CURSO** | 1ACC0238 Aplicaciones para dispositivos móviles |
| **NRC** | 13980 |
| **PROFESORES** | Todos |
| **AUDITOR** | Healthify |
| **CLIENTE(S)** | Azama Fukuda, Juan Pablo, Mechan Montenegro, Luciana Carolina,Luis Miranda, Diego Andres, López Monroy, Rodrigo Alfredo, Sanchez Cuadrado, Juan Antonio |

**SITE o APP A EVALUAR:** Guardian+ (prototipo de alta fidelidad — módulos de Salud, Alertas, Rutinas y Ubicación)

**TAREAS A EVALUAR:**

El alcance de esta evaluación incluye la revisión de la usabilidad de las siguientes tareas:

1. Programar un nuevo recordatorio de medicación, cita médica o actividad (Care Routines & Wellness)
2. Consultar el historial de signos vitales y aplicar filtros de búsqueda (Health Monitoring)
3. Exportar el expediente de signos vitales seleccionando un periodo de tiempo (Health Monitoring)
4. Agregar, editar y reordenar contactos de emergencia (Emergency & Alerting)

No están incluidas en esta versión de la evaluación las siguientes tareas:

1. Gestión de planes de suscripción y pagos
2. Configuración de cuenta e IAM (inicio de sesión, recuperación de contraseña)
3. Ubicación en tiempo real, zonas seguras y videollamada
4. Flujo de onboarding inicial del wearable

**ESCALA DE SEVERIDAD:**

| Nivel | Descripción |
|---|---|
| 1 | Problema superficial: Puede ser fácilmente superado por el usuario y ocurre con muy poca frecuencia. No necesita ser arreglado a no ser que exista disponibilidad de tiempo. |
| 2 | Problema menor: Puede ocurrir un poco más frecuentemente o es un poco más difícil de superar para el usuario. Se le debería asignar una prioridad baja para resolverlo de cara al siguiente release. |
| 3 | Problema mayor: Ocurre frecuentemente o los usuarios no son capaces de resolverlos. Es importante que sean corregidos y se les debe asignar una prioridad alta. |
| 4 | Problema muy grave: Un error de gran impacto que impide al usuario continuar con el uso de la herramienta. Es imperativo que sea corregido antes del lanzamiento. |


**TABLA RESUMEN:**

| # | Problema | Escala de severidad | Heurística/Principio violada(o) |
|---|---|---|---|
| 1 | Los campos de fecha/hora en "Nueva toma", "Nueva cita" y "Nueva actividad" se muestran vacíos, sin placeholder ni formato de referencia (ej. HH:MM) | 2 | Usability: Prevención de errores |
| 2 | El reordenamiento de contactos de emergencia solo puede hacerse mediante gesto de "mantener presionado y arrastrar", sin alternativa accesible (botones subir/bajar) | 3 | Inclusive Design: Proporciona experiencias comparables |
| 3 | Las opciones del panel "Buscar y filtrar" se muestran como filas de texto plano, sin checkbox ni indicador visual de selección, pese a ser una selección múltiple con contador ("Aplicar · 0") | 2 | Usability: Reconocimiento antes que recuerdo |
| 4 | En "Exportar expediente", las opciones de periodo se listan en orden "Últimos 30 días" → "Últimos 7 días", invirtiendo la progresión lógica de menor a mayor duración | 1 | Information Architecture: Organization Systems |
| 5 | El gráfico de "Sueño" usa tonos de verde muy similares entre sí (Profundo/Ligero) junto con un tono naranja (Despierta) para diferenciar tres estados, sin patrón o textura adicional | 2 | Inclusive Design: Proporciona experiencias comparables |


**PROBLEMA #1: Campos de fecha/hora sin placeholder ni formato de referencia**

**Severidad:** 2
**Heurística violada:** Usability - Prevención de errores

**Problema:**
En las pantallas "Nueva toma", "Nueva cita" y "Nueva actividad" del módulo de Rutinas, los campos "Hora de la toma", "Fecha"/"Hora" y "Hora del aviso" se muestran como recuadros completamente vacíos, sin placeholder (ej. "14:00" o "HH:MM") ni un ícono de reloj/calendario que indique que son selectores. Esto contrasta con el formulario "Nuevo contacto de emergencia" del módulo de Alertas, que sí incluye placeholders claros (ej. "Ej. Carlos Rojas", "999 999 999"), evidenciando además una inconsistencia de patrones entre bounded contexts.

![Vista de nueva toma de medicamento](../assets/images/chatper4/heuristics-evaluations/routines-and-care-screen-1.png)

![Vista de agendar nueva cita](../assets/images/chatper4/heuristics-evaluations/routines-and-care-screen-2.png)

![Vista para registrar una nueva actividad](../assets/images/chatper4/heuristics-evaluations/routines-and-care-screen-3.png)

**Recomendación:**
Agregar placeholders con el formato esperado y un ícono reconocible de reloj/calendario en todos los campos de fecha/hora, replicando el estándar de placeholders ya usado en el módulo de contactos de emergencia.

---
**PROBLEMA #2: Reordenamiento de contactos de emergencia sin alternativa accesible al gesto de arrastre**

**Severidad:** 3
**Heurística violada:** Inclusive Design - Proporciona experiencias comparables

**Problema:**
En "Contactos de emergencia", el único mecanismo para cambiar la prioridad de un contacto es "Mantén presionado y arrastra", un gesto que puede ser difícil de ejecutar con precisión para usuarios con limitaciones motrices o destreza reducida —un perfil de usuario especialmente relevante considerando que muchos cuidadores y familiares de Guardian+ son personas de edad avanzada. No se ofrece una alternativa como botones de subir/bajar o un menú de "mover a posición".

![Vista de contactos de emergencia](../assets/images/chatper4/heuristics-evaluations/emergency-contacts.png)

**Recomendación:**
Agregar una alternativa accesible al drag-and-drop, como botones de flecha arriba/abajo en el menú de tres puntos de cada contacto, o una opción "Cambiar prioridad" dentro de "Editar contacto".

---

**PROBLEMA #3: Opciones de filtro sin indicador visual de selección**

**Severidad:** 2
**Heurística violada:** Usability - Reconocimiento antes que recuerdo

**Problema:**
En el panel "Buscar y filtrar" del módulo Salud, las opciones (Ritmo cardíaco, Presión arterial, Día, Semana, etc.) se muestran como filas de texto plano, sin checkbox, radio button ni ningún indicador visual de selección. Sin embargo, el botón inferior "Aplicar · 0" confirma que se trata de una selección múltiple con conteo. El usuario no puede reconocer a simple vista qué opciones están disponibles para seleccionar ni cuáles ya eligió.

![Vista de buscar y filtrar del módulo de salud](../assets/images/chatper4/heuristics-evaluations/search-and-filter.png)

**Recomendación:**
Agregar checkboxes o un estado visual claro (cambio de fondo/borde) a cada fila seleccionada, de forma que el usuario pueda reconocer su selección sin necesidad de recordarla.

---

**PROBLEMA #4: Orden no intuitivo de las opciones de periodo**

**Severidad:** 1
**Heurística violada:** Information Architecture - Organization Systems

**Problema:**
En "Exportar expediente", las opciones de periodo se presentan en el orden "Últimos 30 días" → "Últimos 7 días" → "Personalizado", invirtiendo la progresión lógica esperada de menor a mayor duración (7 días antes que 30 días), lo que puede dificultar que el usuario escanee rápidamente la opción que busca.

![Vista de exportar expediente](../assets/images/chatper4/heuristics-evaluations/export-file.png)

**Recomendación:**
Reordenar las opciones de forma ascendente: "Últimos 7 días", "Últimos 30 días", "Personalizado".

---

**PROBLEMA #5: Diferenciación de estados de sueño basada en tonos de color muy similares**

**Severidad:** 2
**Heurística violada:** Inclusive Design - Proporciona experiencias comparables

**Problema:**
En la pantalla "Sueño", el gráfico de barras distingue tres estados (Profundo, Ligero, Despierta) usando dos tonos de verde muy cercanos entre sí y un tono naranja, sin ningún patrón, textura o forma adicional que refuerce la diferencia. Para personas con daltonismo (especialmente deuteranopia, la forma más común), distinguir entre los dos tonos de verde puede ser difícil, dejándolos sin una forma confiable de leer el gráfico.

![Vista de registro del sueño](../assets/images/chatper4/heuristics-evaluations/sleep-record.png)

**Recomendación:**
Usar colores con mayor contraste entre sí (ej. verde oscuro, celeste y naranja) o agregar un patrón/textura distinto a cada barra además del color, siguiendo WCAG 1.4.1 (no depender únicamente del color para transmitir información).