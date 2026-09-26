# Capítulo IV: Product Implementation & Validation

## 4.1. Software Configuration Management

### 4.1.1. Software Development Environment Configuration

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
| IoT Simulator | C++ | Simulación y procesamiento de datos y eventos asociados al dispositivo wearable. |
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

#### C++ Coding Conventions

El IoT Simulator de Guardian+ utiliza C++ para representar el comportamiento y los eventos generados por el dispositivo wearable.

Se aplican las siguientes convenciones:

- Las clases, estructuras y enumeraciones utilizan `PascalCase`.
- Las funciones y variables utilizan `camelCase`.
- Las constantes utilizan `UPPER_SNAKE_CASE`.
- Los identificadores se redactan en inglés y describen claramente su responsabilidad.
- Los archivos de cabecera y de implementación mantienen responsabilidades relacionadas.
- Se evita el uso de valores literales repetidos mediante constantes con nombres significativos.
- Las funciones deben mantenerse pequeñas y enfocadas en una operación específica.
- Los datos obtenidos o simulados deben validarse antes de ser procesados o transmitidos.
- La lógica encargada de producir datos se mantiene separada de la lógica utilizada para comunicarlos.
- Los recursos utilizados durante la ejecución deben gestionarse adecuadamente para evitar pérdidas de memoria o estados inválidos.
- Se utilizan referencias constantes cuando un parámetro no necesita modificarse.

Ejemplo:

```cpp
constexpr int MAX_HEART_RATE = 220;

bool isValidHeartRate(const int heartRate) {
    return heartRate > 0 && heartRate <= MAX_HEART_RATE;
}

void processHeartRate(const int heartRate) {
    if (!isValidHeartRate(heartRate)) {
        return;
    }

    // Process simulated wearable data
}
```

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
| C++ class / struct | `PascalCase` | `VitalSignReading` |
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

## 4.2. Landing Page & Mobile Application Implementation

### 4.2.1. Sprint n

#### 4.2.1.1. Sprint Planning n

#### 4.2.1.2. Aspect Leaders and Collaborators

#### 4.2.1.3. Sprint Backlog n

#### 4.2.1.4. Development Evidence for Sprint Review

#### 4.2.1.5. Testing Suite Evidence for Sprint Review

#### 4.2.1.6. Execution Evidence for Sprint Review

#### 4.2.1.7. Services Documentation Evidence for Sprint Review

#### 4.2.1.8. Software Deployment Evidence for Sprint Review

#### 4.2.1.9. Team Collaboration Insights during Sprint

## 4.3. Validation Interviews

### 4.3.1. Diseño de Entrevistas

### 4.3.2. Registro de Entrevistas

### 4.3.3. Evaluaciones según heurísticas