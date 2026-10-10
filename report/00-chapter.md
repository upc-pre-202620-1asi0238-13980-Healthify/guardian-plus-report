<div style="text-align: center; width: 100%;">

<img src="../assets/upc-logo.png" alt="UPC Logo" width="150"/>

<h1>Universidad Peruana de Ciencias Aplicadas</h1>

<h2>Carrera de Ingeniería de Software</h2>

<h2>1ACC0238</h2>

<p>Aplicaciones para Dispositivos Móviles</p>

<p>13980</p>

<p>Docente: <strong>Mayta Guillermo, Jorge Luis</strong></p>

<p>Informe del Trabajo Final</p>

<p>Equipo: Healthify</p>

<p>Proyecto: Guardian+</p>

<h2>Integrantes</h2>

<p>
u202411310 - Azama Fukuda, Juan Pablo<br>
u20241b843 - Mechan Montenegro, Luciana Carolina<br>
u20241d185 - Luis Miranda, Diego Andres<br>
u202421866 - López Monroy, Rodrigo Alfredo<br>
u202319404 - Sanchez Cuadrado, Juan Antonio
</p>

<p>2026 - 2</p>

<p><em>Octubre, 2026</em></p>

</div>

<div style="page-break-before: always; break-before: page;"></div>

# Registro de Versiones del Informe

| Versión | Fecha | Autor | Descripción de modificación |
|---|---|---|---|
| 1.0 | 16/09/2026 | u202411310 - Azama Fukuda, Juan Pablo<br>u20241b843 - Mechan Montenegro, Luciana Carolina<br>u20241d185 - Luis Miranda, Diego Andres<br>u202421866 - López Monroy, Rodrigo Alfredo<br>u202319404 - Sanchez Cuadrado, Juan Antonio | Se agregó la documentación relacionada a la investigación inicial de la problemática y el planteamiento de la solución. Asimismo, se agrego el diseño inicial basado en Domain Driven Design del Backend  |
| 2.0 | 05/10/2026 | u202411310 - Azama Fukuda, Juan Pablo<br>u20241b843 - Mechan Montenegro, Luciana Carolina<br>u20241d185 - Luis Miranda, Diego Andres<br>u202421866 - López Monroy, Rodrigo Alfredo<br>u202319404 - Sanchez Cuadrado, Juan Antonio | Se agregó el Capítulo III con la guía de estilos, la arquitectura de información, el diseño de la Landing Page y el prototipado de la aplicación móvil. Se agregó el Capítulo IV con la configuración del entorno de desarrollo, la gestión del código fuente, la configuración del despliegue y la implementación del Sprint 1. Asimismo, se corrigieron las User Stories y la coherencia de los Bounded Contexts del Capítulo II según la retroalimentación del AV1 |
| 3.0 | 10/10/2026 | u202411310 - Azama Fukuda, Juan Pablo<br>u20241b843 - Mechan Montenegro, Luciana Carolina<br>u20241d185 - Luis Miranda, Diego Andres<br>u202421866 - López Monroy, Rodrigo Alfredo<br>u202319404 - Sanchez Cuadrado, Juan Antonio | Se atendieron las observaciones de la revisión previa a la entrega. En formato: cada capítulo inicia en una nueva página, se homologó la presentación de los integrantes y de los Bounded Contexts, se agregó texto introductorio a cada sección y se numeraron y referenciaron las figuras y tablas, con sus índices. En Domain-Driven Design: se mejoró la presentación del EventStorming, del Domain Message Flow Modelling, de los Bounded Context Canvases (V5) y del Context Mapping según las guías de DDD Crew. Asimismo, se completaron las evidencias de ejecución y de documentación de los Web Services del Sprint 1, las entrevistas de validación y las conclusiones |

# Project Report Collaboration Insights

**URL del repositorio:** https://github.com/upc-pre-202620-1asi0238-13980-Healthify/guardian-plus-report.git

Las siguientes capturas muestran los insights del repositorio del informe, con los pull requests integrados y los commits de cada integrante durante cada entrega.

**AV1:**

![Insights del repositorio del informe en el AV1](<../assets/images/Insights/chapter 1/report-insights-cover.png>)

**TB1:**

![Insights del repositorio del informe en el TB1](../assets/images/Insights/tb1/report-insights-tb1.png)

<div style="page-break-before: always; break-before: page;"></div>

# Contenido

- [Índice de tablas](#índice-de-tablas)
- [Índice de figuras](#índice-de-figuras)
- [Capítulo I: Presentación](01-chapter.md#capítulo-i-presentación)
  - [1.1. Startup Profile](01-chapter.md#11-startup-profile)
    - [1.1.1. Descripción de la Startup](01-chapter.md#111-descripción-de-la-startup)
    - [1.1.2. Perfiles de integrantes del equipo](01-chapter.md#112-perfiles-de-integrantes-del-equipo)
  - [1.2. Solution Profile](01-chapter.md#12-solution-profile)
    - [1.2.1. Antecedentes y problemática](01-chapter.md#121-antecedentes-y-problemática)
    - [1.2.2. Lean UX Process](01-chapter.md#122-lean-ux-process)
      - [1.2.2.1. Lean UX Problem Statements](01-chapter.md#1221-lean-ux-problem-statements)
      - [1.2.2.2. Lean UX Assumptions](01-chapter.md#1222-lean-ux-assumptions)
      - [1.2.2.3. Lean UX Hypothesis Statements](01-chapter.md#1223-lean-ux-hypothesis-statements)
      - [1.2.2.4. Lean UX Canvas](01-chapter.md#1224-lean-ux-canvas)
  - [1.3. Segmentos objetivo](01-chapter.md#13-segmentos-objetivo)
- [Capítulo II: Requirements Development and Software Solution Design](02-chapter.md#capítulo-ii-requirements-development-and-software-solution-design)
  - [2.1. Competidores](02-chapter.md#21-competidores)
    - [2.1.1. Análisis competitivo](02-chapter.md#211-análisis-competitivo)
    - [2.1.2. Estrategias y tácticas frente a competidores](02-chapter.md#212-estrategias-y-tácticas-frente-a-competidores)
  - [2.2. Entrevistas](02-chapter.md#22-entrevistas)
    - [2.2.1. Diseño de entrevistas](02-chapter.md#221-diseño-de-entrevistas)
    - [2.2.2. Registro de entrevistas](02-chapter.md#222-registro-de-entrevistas)
    - [2.2.3. Análisis de entrevistas](02-chapter.md#223-análisis-de-entrevistas)
  - [2.3. Needfinding](02-chapter.md#23-needfinding)
    - [2.3.1. User Personas](02-chapter.md#231-user-personas)
    - [2.3.2. User Task Matrix](02-chapter.md#232-user-task-matrix)
    - [2.3.3. User Journey Mapping](02-chapter.md#233-user-journey-mapping)
    - [2.3.4. Empathy Mapping](02-chapter.md#234-empathy-mapping)
    - [2.3.5. Big Picture EventStorming](02-chapter.md#235-big-picture-eventstorming)
    - [2.3.6. Ubiquitous Language](02-chapter.md#236-ubiquitous-language)
  - [2.4. Requirements specification](02-chapter.md#24-requirements-specification)
    - [2.4.1. User Stories](02-chapter.md#241-user-stories)
    - [2.4.2. Impact Mapping](02-chapter.md#242-impact-mapping)
    - [2.4.3. Product Backlog](02-chapter.md#243-product-backlog)
  - [2.5. Strategic-Level Domain-Driven Design](02-chapter.md#25-strategic-level-domain-driven-design)
    - [2.5.1. EventStorming](02-chapter.md#251-eventstorming)
      - [2.5.1.1. Candidate Context Discovery](02-chapter.md#2511-candidate-context-discovery)
      - [2.5.1.2. Domain Message Flows Modeling](02-chapter.md#2512-domain-message-flows-modeling)
      - [2.5.1.3. Bounded Context Canvases](02-chapter.md#2513-bounded-context-canvases)
    - [2.5.2. Context Mapping](02-chapter.md#252-context-mapping)
      - [2.5.2.1. Heurísticas de Diseño y Exploración de Alternativas (What-If Analysis Global)](02-chapter.md#2521-heurísticas-de-diseño-y-exploración-de-alternativas-what-if-analysis-global)
      - [2.5.2.2. Discusión de Alternativas de Context Mapping Global](02-chapter.md#2522-discusión-de-alternativas-de-context-mapping-global)
      - [2.5.2.3. Context Map Global de Guardian+](02-chapter.md#2523-context-map-global-de-guardian)
      - [2.5.2.4. Catálogo de Relaciones y Patrones de Integración Global](02-chapter.md#2524-catálogo-de-relaciones-y-patrones-de-integración-global)
    - [2.5.3. Software Architecture](02-chapter.md#253-software-architecture)
      - [2.5.3.1. Software Architecture Context Level Diagrams](02-chapter.md#2531-software-architecture-context-level-diagrams)
      - [2.5.3.2. Software Architecture Container Level Diagrams](02-chapter.md#2532-software-architecture-container-level-diagrams)
      - [2.5.3.3. Software Architecture Components Level Diagrams](02-chapter.md#2533-software-architecture-components-level-diagrams)
      - [2.5.3.4. Software Architecture Deployment Diagrams](02-chapter.md#2534-software-architecture-deployment-diagrams)
  - [2.6. Tactical-Level Domain-Driven Design](02-chapter.md#26-tactical-level-domain-driven-design)
    - [2.6.1. Bounded Context: Emergency & Alerting](02-chapter.md#261-bounded-context-emergency--alerting)
      - [2.6.1.1. Domain Layer](02-chapter.md#2611-domain-layer)
      - [2.6.1.2. Interface Layer](02-chapter.md#2612-interface-layer)
      - [2.6.1.3. Application Layer](02-chapter.md#2613-application-layer)
      - [2.6.1.4. Infrastructure Layer](02-chapter.md#2614-infrastructure-layer)
      - [2.6.1.5. Bounded Context Software Architecture Component Level Diagrams](02-chapter.md#2615-bounded-context-software-architecture-component-level-diagrams)
      - [2.6.1.6. Bounded Context Software Architecture Code Level Diagrams](02-chapter.md#2616-bounded-context-software-architecture-code-level-diagrams)
        - [2.6.1.6.1. Bounded Context Domain Layer Class Diagrams](02-chapter.md#26161-bounded-context-domain-layer-class-diagrams)
        - [2.6.1.6.2. Bounded Context Database Design Diagram](02-chapter.md#26162-bounded-context-database-design-diagram)
    - [2.6.2. Bounded Context: Health Monitoring](02-chapter.md#262-bounded-context-health-monitoring)
      - [2.6.2.1. Domain Layer](02-chapter.md#2621-domain-layer)
      - [2.6.2.2. Interface Layer](02-chapter.md#2622-interface-layer)
      - [2.6.2.3. Application Layer](02-chapter.md#2623-application-layer)
      - [2.6.2.4. Infrastructure Layer](02-chapter.md#2624-infrastructure-layer)
      - [2.6.2.5. Bounded Context Software Architecture Component Level Diagrams](02-chapter.md#2625-bounded-context-software-architecture-component-level-diagrams)
      - [2.6.2.6. Bounded Context Software Architecture Code Level Diagrams](02-chapter.md#2626-bounded-context-software-architecture-code-level-diagrams)
        - [2.6.2.6.1. Bounded Context Domain Layer Class Diagrams](02-chapter.md#26261-bounded-context-domain-layer-class-diagrams)
        - [2.6.2.6.2. Bounded Context Database Design Diagram](02-chapter.md#26262-bounded-context-database-design-diagram)
    - [2.6.3. Bounded Context: Subscriptions](02-chapter.md#263-bounded-context-subscriptions)
      - [2.6.3.1. Domain Layer](02-chapter.md#2631-domain-layer)
      - [2.6.3.2. Interface Layer](02-chapter.md#2632-interface-layer)
      - [2.6.3.3. Application Layer](02-chapter.md#2633-application-layer)
      - [2.6.3.4. Infrastructure Layer](02-chapter.md#2634-infrastructure-layer)
      - [2.6.3.5. Bounded Context Software Architecture Component Level Diagrams](02-chapter.md#2635-bounded-context-software-architecture-component-level-diagrams)
      - [2.6.3.6. Bounded Context Software Architecture Code Level Diagrams](02-chapter.md#2636-bounded-context-software-architecture-code-level-diagrams)
        - [2.6.3.6.1. Bounded Context Domain Layer Class Diagrams](02-chapter.md#26361-bounded-context-domain-layer-class-diagrams)
        - [2.6.3.6.2. Bounded Context Database Design Diagram](02-chapter.md#26362-bounded-context-database-design-diagram)
    - [2.6.4. Bounded Context: Profile](02-chapter.md#264-bounded-context-profile)
      - [2.6.4.1. Domain Layer](02-chapter.md#2641-domain-layer)
      - [2.6.4.2. Interface Layer](02-chapter.md#2642-interface-layer)
      - [2.6.4.3. Application Layer](02-chapter.md#2643-application-layer)
      - [2.6.4.4. Infrastructure Layer](02-chapter.md#2644-infrastructure-layer)
      - [2.6.4.5. Bounded Context Software Architecture Component Level Diagrams](02-chapter.md#2645-bounded-context-software-architecture-component-level-diagrams)
      - [2.6.4.6. Bounded Context Software Architecture Code Level Diagrams](02-chapter.md#2646-bounded-context-software-architecture-code-level-diagrams)
        - [2.6.4.6.1. Bounded Context Domain Layer Class Diagrams](02-chapter.md#26461-bounded-context-domain-layer-class-diagrams)
        - [2.6.4.6.2. Bounded Context Database Design Diagram](02-chapter.md#26462-bounded-context-database-design-diagram)
    - [2.6.5. Bounded Context: Care Routines & Wellness](02-chapter.md#265-bounded-context-care-routines--wellness)
      - [2.6.5.1. Domain Layer](02-chapter.md#2651-domain-layer)
      - [2.6.5.2. Interface Layer](02-chapter.md#2652-interface-layer)
      - [2.6.5.3. Application Layer](02-chapter.md#2653-application-layer)
      - [2.6.5.4. Infrastructure Layer](02-chapter.md#2654-infrastructure-layer)
      - [2.6.5.5. Bounded Context Software Architecture Component Level Diagrams](02-chapter.md#2655-bounded-context-software-architecture-component-level-diagrams)
      - [2.6.5.6. Bounded Context Software Architecture Code Level Diagrams](02-chapter.md#2656-bounded-context-software-architecture-code-level-diagrams)
        - [2.6.5.6.1. Bounded Context Domain Layer Class Diagrams](02-chapter.md#26561-bounded-context-domain-layer-class-diagrams)
        - [2.6.5.6.2. Bounded Context Database Design Diagram](02-chapter.md#26562-bounded-context-database-design-diagram)
    - [2.6.6. Bounded Context: Mobility & Geofencing](02-chapter.md#266-bounded-context-mobility--geofencing)
      - [2.6.6.1. Domain Layer](02-chapter.md#2661-domain-layer)
      - [2.6.6.2. Interface Layer](02-chapter.md#2662-interface-layer)
      - [2.6.6.3. Application Layer](02-chapter.md#2663-application-layer)
      - [2.6.6.4. Infrastructure Layer](02-chapter.md#2664-infrastructure-layer)
      - [2.6.6.5. Bounded Context Software Architecture Component Level Diagrams](02-chapter.md#2665-bounded-context-software-architecture-component-level-diagrams)
      - [2.6.6.6. Bounded Context Software Architecture Code Level Diagrams](02-chapter.md#2666-bounded-context-software-architecture-code-level-diagrams)
        - [2.6.6.6.1. Bounded Context Domain Layer Class Diagrams](02-chapter.md#26661-bounded-context-domain-layer-class-diagrams)
        - [2.6.6.6.2. Bounded Context Database Design Diagram](02-chapter.md#26662-bounded-context-database-design-diagram)
    - [2.6.7. Bounded Context: IAM](02-chapter.md#267-bounded-context-iam)
      - [2.6.7.1. Domain Layer](02-chapter.md#2671-domain-layer)
      - [2.6.7.2. Interface Layer](02-chapter.md#2672-interface-layer)
      - [2.6.7.3. Application Layer](02-chapter.md#2673-application-layer)
      - [2.6.7.4. Infrastructure Layer](02-chapter.md#2674-infrastructure-layer)
      - [2.6.7.5. Bounded Context Software Architecture Component Level Diagrams](02-chapter.md#2675-bounded-context-software-architecture-component-level-diagrams)
      - [2.6.7.6. Bounded Context Software Architecture Code Level Diagrams](02-chapter.md#2676-bounded-context-software-architecture-code-level-diagrams)
        - [2.6.7.6.1. Bounded Context Domain Layer Class Diagrams](02-chapter.md#26761-bounded-context-domain-layer-class-diagrams)
        - [2.6.7.6.2. Bounded Context Database Design Diagram](02-chapter.md#26762-bounded-context-database-design-diagram)
- [Capítulo III: Solution UI/UX Design](03-chapter.md#capítulo-iii-solution-uiux-design)
  - [3.1. Product design](03-chapter.md#31-product-design)
    - [3.1.1. Style Guidelines](03-chapter.md#311-style-guidelines)
      - [3.1.1.1. General Style Guidelines](03-chapter.md#3111-general-style-guidelines)
    - [3.1.2. Information Architecture](03-chapter.md#312-information-architecture)
      - [3.1.2.1. Organization Systems](03-chapter.md#3121-organization-systems)
      - [3.1.2.2. Labelling Systems](03-chapter.md#3122-labelling-systems)
      - [3.1.2.3. SEO Tags and Meta Tags](03-chapter.md#3123-seo-tags-and-meta-tags)
      - [3.1.2.4. Searching Systems](03-chapter.md#3124-searching-systems)
      - [3.1.2.5. Navigation Systems](03-chapter.md#3125-navigation-systems)
    - [3.1.3. Landing Page UI Design](03-chapter.md#313-landing-page-ui-design)
      - [3.1.3.1. Landing Page Wireframe](03-chapter.md#3131-landing-page-wireframe)
      - [3.1.3.2. Landing Page Mock-up](03-chapter.md#3132-landing-page-mock-up)
    - [3.1.4. Mobile Applications UX/UI Design](03-chapter.md#314-mobile-applications-uxui-design)
      - [3.1.4.1. Mobile Applications Wireframes](03-chapter.md#3141-mobile-applications-wireframes)
      - [3.1.4.2. Mobile Applications Wireflow Diagrams](03-chapter.md#3142-mobile-applications-wireflow-diagrams)
      - [3.1.4.3. Mobile Applications Mock-ups](03-chapter.md#3143-mobile-applications-mock-ups)
      - [3.1.4.4. Mobile Applications User Flow Diagrams](03-chapter.md#3144-mobile-applications-user-flow-diagrams)
      - [3.1.4.5. Mobile Applications Prototyping](03-chapter.md#3145-mobile-applications-prototyping)
- [Capítulo IV: Product Implementation & Validation](04-chapter.md#capítulo-iv-product-implementation--validation)
  - [4.1. Software Configuration Management](04-chapter.md#41-software-configuration-management)
    - [4.1.1. Software Development Environment Configuration](04-chapter.md#411-software-development-environment-configuration)
    - [4.1.2. Source Code Management](04-chapter.md#412-source-code-management)
      - [4.1.2.1. GitFlow & Branching Strategy](04-chapter.md#4121-gitflow--branching-strategy)
    - [4.1.3. Source Code Style Guide & Conventions](04-chapter.md#413-source-code-style-guide--conventions)
    - [4.1.4. Software Deployment Configuration](04-chapter.md#414-software-deployment-configuration)
  - [4.2. Landing Page & Mobile Application Implementation](04-chapter.md#42-landing-page--mobile-application-implementation)
    - [4.2.1. Sprint 1](04-chapter.md#421-sprint-1)
      - [4.2.1.1. Sprint Planning 1](04-chapter.md#4211-sprint-planning-1)
      - [4.2.1.2. Aspect Leaders and Collaborators](04-chapter.md#4212-aspect-leaders-and-collaborators)
      - [4.2.1.3. Sprint Backlog 1](04-chapter.md#4213-sprint-backlog-1)
      - [4.2.1.4. Development Evidence for Sprint Review](04-chapter.md#4214-development-evidence-for-sprint-review)
      - [4.2.1.5. Testing Suite Evidence for Sprint Review](04-chapter.md#4215-testing-suite-evidence-for-sprint-review)
      - [4.2.1.6. Execution Evidence for Sprint Review](04-chapter.md#4216-execution-evidence-for-sprint-review)
      - [4.2.1.7. Services Documentation Evidence for Sprint Review](04-chapter.md#4217-services-documentation-evidence-for-sprint-review)
      - [4.2.1.8. Software Deployment Evidence for Sprint Review](04-chapter.md#4218-software-deployment-evidence-for-sprint-review)
      - [4.2.1.9. Team Collaboration Insights during Sprint](04-chapter.md#4219-team-collaboration-insights-during-sprint)
  - [4.3. Validation Interviews](04-chapter.md#43-validation-interviews)
    - [4.3.1. Diseño de Entrevistas](04-chapter.md#431-diseño-de-entrevistas)
    - [4.3.2. Registro de Entrevistas](04-chapter.md#432-registro-de-entrevistas)
    - [4.3.3. Evaluaciones según heurísticas](04-chapter.md#433-evaluaciones-según-heurísticas)
- [Conclusiones y recomendaciones](../README.md#conclusiones-y-recomendaciones)
- [Bibliografía](../README.md#bibliografía)

<div style="page-break-before: always; break-before: page;"></div>

# Índice de tablas

**Capítulo I: Presentación**

- [Tabla 1.1. Perfiles de los integrantes del equipo Healthify](01-chapter.md#tabla-1-1)

**Capítulo II: Requirements Development and Software Solution Design**

- [Tabla 2.1. Competitive Analysis Landscape de Guardian+ frente a sus competidores](02-chapter.md#tabla-2-1)
- [Tabla 2.2. Datos de la entrevista a Rocío Miranda Alvarado Silva](02-chapter.md#tabla-2-2)
- [Tabla 2.3. Datos de la entrevista a Lucía Infante](02-chapter.md#tabla-2-3)
- [Tabla 2.4. Datos de la entrevista a Junio Antenor Ayala](02-chapter.md#tabla-2-4)
- [Tabla 2.5. Datos de la entrevista a Roxana Paola Diana](02-chapter.md#tabla-2-5)
- [Tabla 2.6. Datos de la entrevista a Piero Segura](02-chapter.md#tabla-2-6)
- [Tabla 2.7. Datos de la entrevista a Fernanda Llanos](02-chapter.md#tabla-2-7)
- [Tabla 2.8. Datos de la entrevista a Gabriela Cuadros Curihuaman](02-chapter.md#tabla-2-8)
- [Tabla 2.9. Características identificadas en el segmento de familiares](02-chapter.md#tabla-2-9)
- [Tabla 2.10. Características identificadas en el segmento de cuidadores](02-chapter.md#tabla-2-10)
- [Tabla 2.11. Elementos para la construcción de los arquetipos de usuario](02-chapter.md#tabla-2-11)
- [Tabla 2.12. User Task Matrix de los segmentos de familiares y cuidadores](02-chapter.md#tabla-2-12)
- [Tabla 2.13. User Story US01: Visualización de ritmo cardíaco en tiempo real](02-chapter.md#tabla-2-13)
- [Tabla 2.14. User Story US02: Visualización de presión arterial estimada](02-chapter.md#tabla-2-14)
- [Tabla 2.15. User Story US03: Visualización de saturación de oxígeno periférico (SpO₂)](02-chapter.md#tabla-2-15)
- [Tabla 2.16. User Story US04: Supervisión de temperatura corporal continua](02-chapter.md#tabla-2-16)
- [Tabla 2.17. User Story US05: Visualización de frecuencia respiratoria estimada](02-chapter.md#tabla-2-17)
- [Tabla 2.18. User Story US06: Emisión y confirmación de recordatorios de medicación](02-chapter.md#tabla-2-18)
- [Tabla 2.19. User Story US07: Análisis comparativo y tendencias históricas de signos vitales](02-chapter.md#tabla-2-19)
- [Tabla 2.20. User Story US08: Detección automática de caídas y despacho de emergencia](02-chapter.md#tabla-2-20)
- [Tabla 2.21. User Story US09: Generación de alertas por transgresión de umbrales biomédicos](02-chapter.md#tabla-2-21)
- [Tabla 2.22. User Story US10: Confirmación manual de estado de bienestar tras incidente](02-chapter.md#tabla-2-22)
- [Tabla 2.23. User Story US11: Escalamiento automatizado de alertas críticas no atendidas](02-chapter.md#tabla-2-23)
- [Tabla 2.24. User Story US12: Configuración y parametrización de niveles de alerta](02-chapter.md#tabla-2-24)
- [Tabla 2.25. User Story US13: Programación y notificación de consultas médicas](02-chapter.md#tabla-2-25)
- [Tabla 2.26. User Story US14: Recordatorios programados para actividad física ligera](02-chapter.md#tabla-2-26)
- [Tabla 2.27. User Story US15: Activación de auxilio mediante botón SOS en pulsera](02-chapter.md#tabla-2-27)
- [Tabla 2.28. User Story US16: Administración de agenda de contactos de auxilio](02-chapter.md#tabla-2-28)
- [Tabla 2.29. User Story US17: Estimación y registro de fases de sueño](02-chapter.md#tabla-2-29)
- [Tabla 2.30. User Story US18: Telemetría de geolocalización en tiempo real](02-chapter.md#tabla-2-30)
- [Tabla 2.31. User Story US19: Exportación de reporte cronológico de telemetría médica](02-chapter.md#tabla-2-31)
- [Tabla 2.32. User Story US20: Notificación de nivel crítico de batería en wearable](02-chapter.md#tabla-2-32)
- [Tabla 2.33. User Story US21: Sincronización y persistencia resiliente de telemetría (Offline Sync)](02-chapter.md#tabla-2-33)
- [Tabla 2.34. User Story US22: Silenciamiento de alertas no críticas en el Care Circle](02-chapter.md#tabla-2-34)
- [Tabla 2.35. User Story US23: Establecimiento de canal de comunicación directa](02-chapter.md#tabla-2-35)
- [Tabla 2.36. User Story US24: Consolidación y despacho de reporte semanal de salud](02-chapter.md#tabla-2-36)
- [Tabla 2.37. User Story US25: Despacho simultáneo a múltiples contactos de auxilio](02-chapter.md#tabla-2-37)
- [Tabla 2.38. User Story US26: Recordatorios periódicos de hidratación y pausas activas](02-chapter.md#tabla-2-38)
- [Tabla 2.39. User Story US27: Detección de inactividad física prolongada](02-chapter.md#tabla-2-39)
- [Tabla 2.40. User Story US28: Delimitación y monitoreo perimetral mediante geocercas múltiples](02-chapter.md#tabla-2-40)
- [Tabla 2.41. User Story US29: Previsión de agotamiento de stock y pedidos de medicinas](02-chapter.md#tabla-2-41)
- [Tabla 2.42. User Story US30: Navegación entre secciones informativas de la Landing Page](02-chapter.md#tabla-2-42)
- [Tabla 2.43. User Story US31: Presentación de características y beneficios clave del sistema](02-chapter.md#tabla-2-43)
- [Tabla 2.44. User Story US32: Captura y procesamiento de solicitudes de contacto institucional](02-chapter.md#tabla-2-44)
- [Tabla 2.45. User Story US33: Visualización comparativa de planes de suscripción Guardian+](02-chapter.md#tabla-2-45)
- [Tabla 2.46. Technical Story TS01: Endpoint RESTful para consulta y filtrado de incidentes y alertas](02-chapter.md#tabla-2-46)
- [Tabla 2.47. Technical Story TS02: Endpoint RESTful para ingesta de telemetría biomédica por lotes](02-chapter.md#tabla-2-47)
- [Tabla 2.48. Spike SP01: Investigación de protocolos de transporte ligero y telemetría MQTT sobre ESP32-S3](02-chapter.md#tabla-2-48)
- [Tabla 2.49. Spike SP02: Investigación de pasarela de pagos y cobro recurrente de suscripciones con Stripe](02-chapter.md#tabla-2-49)
- [Tabla 2.50. Product Backlog de Guardian+](02-chapter.md#tabla-2-50)
- [Tabla 2.51. Alternativas de Context Mapping evaluadas](02-chapter.md#tabla-2-51)
- [Tabla 2.52. Leyenda de patrones del Context Map](02-chapter.md#tabla-2-52)
- [Tabla 2.53. Catálogo de relaciones del Context Map](02-chapter.md#tabla-2-53)
- [Tabla 2.54. Command Handlers de Subscriptions](02-chapter.md#tabla-2-54)
- [Tabla 2.55. Query Handlers de Subscriptions](02-chapter.md#tabla-2-55)
- [Tabla 2.56. Event Handlers de Subscriptions](02-chapter.md#tabla-2-56)

**Capítulo III: Solution UI/UX Design**

- [Tabla 3.1. Paleta de colores de Guardian+](03-chapter.md#tabla-3-1)
- [Tabla 3.2. Escala tipográfica de Guardian+](03-chapter.md#tabla-3-2)
- [Tabla 3.3. Criterios de etiquetado](03-chapter.md#tabla-3-3)
- [Tabla 3.4. Correspondencia entre el Ubiquitous Language y las etiquetas de interfaz](03-chapter.md#tabla-3-4)
- [Tabla 3.5. Etiquetas del Landing Page](03-chapter.md#tabla-3-5)
- [Tabla 3.6. Funcionalidades del Landing Page y sección asociada en la aplicación](03-chapter.md#tabla-3-6)
- [Tabla 3.7. Etiquetas de la navegación principal de la aplicación](03-chapter.md#tabla-3-7)
- [Tabla 3.8. Etiquetas dentro de cada sección de la aplicación](03-chapter.md#tabla-3-8)
- [Tabla 3.9. Etiquetas de estado](03-chapter.md#tabla-3-9)
- [Tabla 3.10. Etiquetas de la pulsera](03-chapter.md#tabla-3-10)
- [Tabla 3.11. Elementos SEO del Landing Page](03-chapter.md#tabla-3-11)
- [Tabla 3.12. Etiquetas HTML de SEO del Landing Page](03-chapter.md#tabla-3-12)
- [Tabla 3.13. Elementos ASO de la aplicación móvil](03-chapter.md#tabla-3-13)
- [Tabla 3.14. Anatomía del desplegable con búsqueda](03-chapter.md#tabla-3-14)
- [Tabla 3.15. Elementos del filtrado por etiquetas](03-chapter.md#tabla-3-15)
- [Tabla 3.16. Aplicación de los mecanismos de búsqueda por sección](03-chapter.md#tabla-3-16)
- [Tabla 3.17. Mecanismos de navegación del Landing Page](03-chapter.md#tabla-3-17)
- [Tabla 3.18. Tipos de navegación de la aplicación móvil](03-chapter.md#tabla-3-18)
- [Tabla 3.19. Reglas de navegación de la aplicación móvil](03-chapter.md#tabla-3-19)
- [Tabla 3.20. Ruta de emergencia](03-chapter.md#tabla-3-20)
- [Tabla 3.21. Pantallas de los wireframes de Health Monitoring](03-chapter.md#tabla-3-21)
- [Tabla 3.22. Pantallas de los wireframes de Profile, IAM y Subscriptions](03-chapter.md#tabla-3-22)
- [Tabla 3.23. Pantallas de los mock-ups de Health Monitoring](03-chapter.md#tabla-3-23)
- [Tabla 3.24. Pantallas de los mock-ups de Extras](03-chapter.md#tabla-3-24)
- [Tabla 3.25. Criterios de interacción del prototipo](03-chapter.md#tabla-3-25)
- [Tabla 3.26. Flujos cubiertos por el prototipo](03-chapter.md#tabla-3-26)
- [Tabla 3.27. Enlaces al prototipo y al video del recorrido](03-chapter.md#tabla-3-27)

**Capítulo IV: Product Implementation & Validation**

- [Tabla 4.1. Herramientas de Project Management](04-chapter.md#tabla-4-1)
- [Tabla 4.2. Herramientas de Requirements Management](04-chapter.md#tabla-4-2)
- [Tabla 4.3. Herramientas de Product UX/UI Design](04-chapter.md#tabla-4-3)
- [Tabla 4.4. Herramientas de Software Architecture & Modeling](04-chapter.md#tabla-4-4)
- [Tabla 4.5. Herramientas de Software Development](04-chapter.md#tabla-4-5)
- [Tabla 4.6. Herramientas de Software Testing](04-chapter.md#tabla-4-6)
- [Tabla 4.7. Herramientas de Software Deployment](04-chapter.md#tabla-4-7)
- [Tabla 4.8. Herramientas de Software Documentation](04-chapter.md#tabla-4-8)
- [Tabla 4.9. Technology Stack de Guardian+](04-chapter.md#tabla-4-9)
- [Tabla 4.10. Repositorios de Guardian+](04-chapter.md#tabla-4-10)
- [Tabla 4.11. Ramas del workflow GitFlow](04-chapter.md#tabla-4-11)
- [Tabla 4.12. Convenciones de nombres de ramas](04-chapter.md#tabla-4-12)
- [Tabla 4.13. Tipos de Conventional Commits](04-chapter.md#tabla-4-13)
- [Tabla 4.14. Lenguajes y tecnologías por producto](04-chapter.md#tabla-4-14)
- [Tabla 4.15. Resumen de convenciones de nombres](04-chapter.md#tabla-4-15)
- [Tabla 4.16. Deployment Overview de Guardian+](04-chapter.md#tabla-4-16)
- [Tabla 4.17. Entornos de despliegue](04-chapter.md#tabla-4-17)
- [Tabla 4.18. Pasos del despliegue del Landing Page](04-chapter.md#tabla-4-18)
- [Tabla 4.19. Recursos de Azure de los Web Services](04-chapter.md#tabla-4-19)
- [Tabla 4.20. Preparación del repositorio de los Web Services](04-chapter.md#tabla-4-20)
- [Tabla 4.21. Aprovisionamiento de los Web Services en Azure](04-chapter.md#tabla-4-21)
- [Tabla 4.22. Variables de entorno de los Web Services](04-chapter.md#tabla-4-22)
- [Tabla 4.23. Pasos del despliegue de la aplicación móvil](04-chapter.md#tabla-4-23)
- [Tabla 4.24. Recursos aprovisionados para el IoT Simulator](04-chapter.md#tabla-4-24)
- [Tabla 4.25. Preparación y despliegue del IoT Simulator](04-chapter.md#tabla-4-25)
- [Tabla 4.26. Variables de Terraform del IoT Simulator](04-chapter.md#tabla-4-26)
- [Tabla 4.27. Variables de entorno del IoT Simulator](04-chapter.md#tabla-4-27)
- [Tabla 4.28. Consideraciones de despliegue](04-chapter.md#tabla-4-28)
- [Tabla 4.29. Sprint Planning del Sprint 1](04-chapter.md#tabla-4-29)
- [Tabla 4.30. User Stories comprometidas en el Sprint 1](04-chapter.md#tabla-4-30)
- [Tabla 4.31. Leadership-and-Collaboration Matrix del Sprint 1](04-chapter.md#tabla-4-31)
- [Tabla 4.32. Sprint Backlog 1](04-chapter.md#tabla-4-32)
- [Tabla 4.33. Commits del Landing Page](04-chapter.md#tabla-4-33)
- [Tabla 4.34. Commits de Web Services: Emergency & Alerting](04-chapter.md#tabla-4-34)
- [Tabla 4.35. Commits de Web Services: Care Routines & Wellness](04-chapter.md#tabla-4-35)
- [Tabla 4.36. Commits de Web Services: Health Monitoring](04-chapter.md#tabla-4-36)
- [Tabla 4.37. Commits de Web Services: Mobility & Geofencing](04-chapter.md#tabla-4-37)
- [Tabla 4.38. Commits de Web Services: Profile](04-chapter.md#tabla-4-38)
- [Tabla 4.39. Commits de Mobile App: Emergency & Alerting](04-chapter.md#tabla-4-39)
- [Tabla 4.40. Commits de Mobile App: Health Monitoring](04-chapter.md#tabla-4-40)
- [Tabla 4.41. Commits de IoT Simulator](04-chapter.md#tabla-4-41)
- [Tabla 4.42. Unit Tests del Bounded Context Profile](04-chapter.md#tabla-4-42)
- [Tabla 4.43. Commit de los Unit Tests de Profile](04-chapter.md#tabla-4-43)
- [Tabla 4.44. Video de ejecución del Landing Page](04-chapter.md#tabla-4-44)
- [Tabla 4.45. Video de ejecución de la aplicación móvil](04-chapter.md#tabla-4-45)
- [Tabla 4.46. Video de ejecución de los Web Services](04-chapter.md#tabla-4-46)
- [Tabla 4.47. Endpoints de Emergency & Alerting](04-chapter.md#tabla-4-47)
- [Tabla 4.48. Endpoints de Health Monitoring](04-chapter.md#tabla-4-48)
- [Tabla 4.49. Endpoints de Care Routines & Wellness](04-chapter.md#tabla-4-49)
- [Tabla 4.50. Procesos de Care Routines & Wellness disparados por el sistema](04-chapter.md#tabla-4-50)
- [Tabla 4.51. Endpoints de Mobility & Geofencing](04-chapter.md#tabla-4-51)
- [Tabla 4.52. Endpoints de Profile](04-chapter.md#tabla-4-52)
- [Tabla 4.53. Despliegue del Landing Page en el Sprint 1](04-chapter.md#tabla-4-53)
- [Tabla 4.54. Pasos del despliegue del Landing Page en el Sprint 1](04-chapter.md#tabla-4-54)
- [Tabla 4.55. Resultados de Lighthouse del Landing Page](04-chapter.md#tabla-4-55)
- [Tabla 4.56. Despliegue de los Web Services en el Sprint 1](04-chapter.md#tabla-4-56)
- [Tabla 4.57. Pasos del despliegue de los Web Services en el Sprint 1](04-chapter.md#tabla-4-57)
- [Tabla 4.58. Despliegue del IoT Simulator en el Sprint 1](04-chapter.md#tabla-4-58)
- [Tabla 4.59. Pasos del despliegue del IoT Simulator en el Sprint 1](04-chapter.md#tabla-4-59)
- [Tabla 4.60. Video de las entrevistas de validación](04-chapter.md#tabla-4-60)
- [Tabla 4.61. Datos de la entrevista de validación a Rocio Alvarado](04-chapter.md#tabla-4-61)
- [Tabla 4.62. Datos de la entrevista de validación a Junior Antenor](04-chapter.md#tabla-4-62)
- [Tabla 4.63. Datos de la entrevista de validación a Roxana Paola Diana](04-chapter.md#tabla-4-63)
- [Tabla 4.64. Datos de la entrevista de validación a Piero Segurda Cardenas](04-chapter.md#tabla-4-64)
- [Tabla 4.65. Datos de la entrevista de validación a Gabriela Cuadros](04-chapter.md#tabla-4-65)
- [Tabla 4.66. Datos generales de la evaluación heurística](04-chapter.md#tabla-4-66)
- [Tabla 4.67. Escala de severidad de la evaluación heurística](04-chapter.md#tabla-4-67)
- [Tabla 4.68. Resumen de problemas de la evaluación heurística](04-chapter.md#tabla-4-68)

<div style="page-break-before: always; break-before: page;"></div>

# Índice de figuras

**Capítulo I: Presentación**

- [Figura 1.1. Análisis 5W2H de la problemática](01-chapter.md#figura-1-1)
- [Figura 1.2. Lean UX Canvas de Guardian+](01-chapter.md#figura-1-2)

**Capítulo II: Requirements Development and Software Solution Design**

- [Figura 2.1. Captura de la entrevista a Rocío Miranda Alvarado Silva](02-chapter.md#figura-2-1)
- [Figura 2.2. Captura de la entrevista a Lucía Infante](02-chapter.md#figura-2-2)
- [Figura 2.3. Captura de la entrevista a Junio Antenor Ayala](02-chapter.md#figura-2-3)
- [Figura 2.4. Captura de la entrevista a Roxana Paola Diana](02-chapter.md#figura-2-4)
- [Figura 2.5. Captura de la entrevista a Piero Segura](02-chapter.md#figura-2-5)
- [Figura 2.6. Captura de la entrevista a Fernanda Llanos](02-chapter.md#figura-2-6)
- [Figura 2.7. Captura de la entrevista a Gabriela Cuadros Curihuaman](02-chapter.md#figura-2-7)
- [Figura 2.8. User Persona del segmento de familiares](02-chapter.md#figura-2-8)
- [Figura 2.9. User Persona del segmento de cuidadores](02-chapter.md#figura-2-9)
- [Figura 2.10. User Journey Map del segmento de familiares](02-chapter.md#figura-2-10)
- [Figura 2.11. User Journey Map del segmento de cuidadores](02-chapter.md#figura-2-11)
- [Figura 2.12. Empathy Map del segmento de familiares](02-chapter.md#figura-2-12)
- [Figura 2.13. Empathy Map del segmento de cuidadores](02-chapter.md#figura-2-13)
- [Figura 2.14. Big Picture EventStorming de Guardian+](02-chapter.md#figura-2-14)
- [Figura 2.15. Impact Mapping de Guardian+](02-chapter.md#figura-2-15)
- [Figura 2.16. Eventos del Big Picture EventStorming usados como punto de partida](02-chapter.md#figura-2-16)
- [Figura 2.17. EventStorming del Bounded Context Emergency & Alerting](02-chapter.md#figura-2-17)
- [Figura 2.18. EventStorming del Bounded Context Health Monitoring](02-chapter.md#figura-2-18)
- [Figura 2.19. EventStorming del Bounded Context Care Routines & Wellness](02-chapter.md#figura-2-19)
- [Figura 2.20. EventStorming del Bounded Context Mobility & Geofencing](02-chapter.md#figura-2-20)
- [Figura 2.21. EventStorming del Bounded Context IAM](02-chapter.md#figura-2-21)
- [Figura 2.22. EventStorming del Bounded Context Profile](02-chapter.md#figura-2-22)
- [Figura 2.23. EventStorming del Bounded Context Subscriptions](02-chapter.md#figura-2-23)
- [Figura 2.24. Domain message flow del flujo de caída confirmada](02-chapter.md#figura-2-24)
- [Figura 2.25. Domain message flow del flujo de SOS manual](02-chapter.md#figura-2-25)
- [Figura 2.26. Domain message flow del flujo de anomalía biométrica reconocida a tiempo](02-chapter.md#figura-2-26)
- [Figura 2.27. Domain message flow del flujo de anomalía biométrica escalada](02-chapter.md#figura-2-27)
- [Figura 2.28. Domain message flow del flujo de recordatorio de medicación reemitido](02-chapter.md#figura-2-28)
- [Figura 2.29. Domain message flow del flujo de inactividad prolongada](02-chapter.md#figura-2-29)
- [Figura 2.30. Bounded Context Canvas de Emergency & Alerting](02-chapter.md#figura-2-30)
- [Figura 2.31. Bounded Context Canvas de Health Monitoring](02-chapter.md#figura-2-31)
- [Figura 2.32. Bounded Context Canvas de Care Routines & Wellness](02-chapter.md#figura-2-32)
- [Figura 2.33. Bounded Context Canvas de Subscriptions](02-chapter.md#figura-2-33)
- [Figura 2.34. Bounded Context Canvas de Profile](02-chapter.md#figura-2-34)
- [Figura 2.35. Bounded Context Canvas de Mobility & Geofencing](02-chapter.md#figura-2-35)
- [Figura 2.36. Bounded Context Canvas de IAM](02-chapter.md#figura-2-36)
- [Figura 2.37. Context Map global de Guardian+](02-chapter.md#figura-2-37)
- [Figura 2.38. Context Map de las señales que disparan alertas](02-chapter.md#figura-2-38)
- [Figura 2.39. Context Map de identidad y sistemas externos](02-chapter.md#figura-2-39)
- [Figura 2.40. Diagrama de contexto de Guardian+](02-chapter.md#figura-2-40)
- [Figura 2.41. Diagrama de contenedores de Guardian+](02-chapter.md#figura-2-41)
- [Figura 2.42. Diagrama de componentes de la Guardian+ REST API](02-chapter.md#figura-2-42)
- [Figura 2.43. Diagrama de despliegue de Guardian+](02-chapter.md#figura-2-43)
- [Figura 2.44. Diagrama de componentes del Bounded Context Emergency & Alerting](02-chapter.md#figura-2-44)
- [Figura 2.45. Diagrama de clases de la Domain Layer de Emergency & Alerting](02-chapter.md#figura-2-45)
- [Figura 2.46. Diagrama de base de datos de Emergency & Alerting](02-chapter.md#figura-2-46)
- [Figura 2.47. Diagrama de componentes del Bounded Context Health Monitoring](02-chapter.md#figura-2-47)
- [Figura 2.48. Diagrama de clases de la Domain Layer de Health Monitoring](02-chapter.md#figura-2-48)
- [Figura 2.49. Diagrama de base de datos de Health Monitoring](02-chapter.md#figura-2-49)
- [Figura 2.50. Diagrama de componentes del Bounded Context Subscriptions](02-chapter.md#figura-2-50)
- [Figura 2.51. Diagrama de clases de la Domain Layer de Subscriptions](02-chapter.md#figura-2-51)
- [Figura 2.52. Diagrama de base de datos de Subscriptions](02-chapter.md#figura-2-52)
- [Figura 2.53. Diagrama de componentes del Bounded Context Profile](02-chapter.md#figura-2-53)
- [Figura 2.54. Diagrama de clases de la Domain Layer de Profile](02-chapter.md#figura-2-54)
- [Figura 2.55. Diagrama de base de datos de Profile](02-chapter.md#figura-2-55)
- [Figura 2.56. Diagrama de componentes del Bounded Context Care Routines & Wellness](02-chapter.md#figura-2-56)
- [Figura 2.57. Diagrama de clases de la Domain Layer de Care Routines & Wellness](02-chapter.md#figura-2-57)
- [Figura 2.58. Diagrama de base de datos de Care Routines & Wellness](02-chapter.md#figura-2-58)
- [Figura 2.59. Diagrama de componentes del Bounded Context Mobility & Geofencing](02-chapter.md#figura-2-59)
- [Figura 2.60. Diagrama de clases de la Domain Layer de Mobility & Geofencing](02-chapter.md#figura-2-60)
- [Figura 2.61. Diagrama de base de datos de Mobility & Geofencing](02-chapter.md#figura-2-61)
- [Figura 2.62. Diagrama de componentes del Bounded Context IAM](02-chapter.md#figura-2-62)
- [Figura 2.63. Diagrama de clases de la Domain Layer de IAM](02-chapter.md#figura-2-63)
- [Figura 2.64. Diagrama de base de datos de IAM](02-chapter.md#figura-2-64)
- [Figura 2.65. Esquema físico consolidado de la base de datos de Guardian+](02-chapter.md#figura-2-65)

**Capítulo III: Solution UI/UX Design**

- [Figura 3.1. Paleta de colores aplicada en el design system](03-chapter.md#figura-3-1)
- [Figura 3.2. Tipografía aplicada en el design system](03-chapter.md#figura-3-2)
- [Figura 3.3. Espaciado, bordes y elevaciones del design system](03-chapter.md#figura-3-3)
- [Figura 3.4. Ejemplo de componentes con los lineamientos de estilo](03-chapter.md#figura-3-4)
- [Figura 3.5. Ejemplo de vista con los lineamientos de estilo](03-chapter.md#figura-3-5)
- [Figura 3.6. Esquemas de organización de la aplicación móvil](03-chapter.md#figura-3-6)
- [Figura 3.7. Navegación del Landing Page](03-chapter.md#figura-3-7)
- [Figura 3.8. Mapa de navegación de la aplicación móvil](03-chapter.md#figura-3-8)
- [Figura 3.9. Wireframe de escritorio del Landing Page: Cómo funciona](03-chapter.md#figura-3-9)
- [Figura 3.10. Wireframe de escritorio del Landing Page: Beneficios](03-chapter.md#figura-3-10)
- [Figura 3.11. Wireframe de escritorio del Landing Page: Por qué Guardian+](03-chapter.md#figura-3-11)
- [Figura 3.12. Wireframe de escritorio del Landing Page: Precios](03-chapter.md#figura-3-12)
- [Figura 3.13. Wireframe de escritorio del Landing Page: Contacto](03-chapter.md#figura-3-13)
- [Figura 3.14. Wireframes móviles del Landing Page](03-chapter.md#figura-3-14)
- [Figura 3.15. Mock-up de escritorio del Landing Page: Cómo funciona](03-chapter.md#figura-3-15)
- [Figura 3.16. Mock-up de escritorio del Landing Page: Beneficios](03-chapter.md#figura-3-16)
- [Figura 3.17. Mock-up de escritorio del Landing Page: Por qué Guardian+](03-chapter.md#figura-3-17)
- [Figura 3.18. Mock-up de escritorio del Landing Page: Precios](03-chapter.md#figura-3-18)
- [Figura 3.19. Mock-up de escritorio del Landing Page: Contacto](03-chapter.md#figura-3-19)
- [Figura 3.20. Mock-ups móviles del Landing Page](03-chapter.md#figura-3-20)
- [Figura 3.21. Wireframes de Health Monitoring](03-chapter.md#figura-3-21)
- [Figura 3.22. Wireframes de Profile, IAM y Subscriptions](03-chapter.md#figura-3-22)
- [Figura 3.23. Wireframes de Emergency & Alerting](03-chapter.md#figura-3-23)
- [Figura 3.24. Wireframes de Care Routines & Wellness](03-chapter.md#figura-3-24)
- [Figura 3.25. Wireflow de Health Monitoring: Consultar ritmo cardíaco (US01)](03-chapter.md#figura-3-25)
- [Figura 3.26. Wireflow de Health Monitoring: Consultar presión arterial (US02)](03-chapter.md#figura-3-26)
- [Figura 3.27. Wireflow de Health Monitoring: Consultar saturación de oxígeno (US03)](03-chapter.md#figura-3-27)
- [Figura 3.28. Wireflow de Health Monitoring: Supervisar temperatura corporal (US04)](03-chapter.md#figura-3-28)
- [Figura 3.29. Wireflow de Health Monitoring: Consultar frecuencia respiratoria (US05)](03-chapter.md#figura-3-29)
- [Figura 3.30. Wireflow de Health Monitoring: Analizar tendencias históricas (US07)](03-chapter.md#figura-3-30)
- [Figura 3.31. Wireflow de Health Monitoring: Exportar historial de telemetría (US19)](03-chapter.md#figura-3-31)
- [Figura 3.32. Wireflow de Health Monitoring: Sincronizar telemetría sin conexión (US21)](03-chapter.md#figura-3-32)
- [Figura 3.33. Wireflow de Health Monitoring: Revisar reporte semanal de salud (US24)](03-chapter.md#figura-3-33)
- [Figura 3.34. Wireflow de Extras: Gestionar información personal](03-chapter.md#figura-3-34)
- [Figura 3.35. Wireflow de Extras: Consultar entorno de cuidado (persona bajo cuidado)](03-chapter.md#figura-3-35)
- [Figura 3.36. Wireflow de Extras: Consultar entorno de cuidado (círculo de cuidado)](03-chapter.md#figura-3-36)
- [Figura 3.37. Wireflow de Extras: Consultar entorno de cuidado (pulsera)](03-chapter.md#figura-3-37)
- [Figura 3.38. Wireflow de Extras: Consultar suscripción actual](03-chapter.md#figura-3-38)
- [Figura 3.39. Wireflow de Extras: Configurar preferencias de la aplicación (idioma)](03-chapter.md#figura-3-39)
- [Figura 3.40. Wireflow de Extras: Configurar preferencias de la aplicación (accesibilidad)](03-chapter.md#figura-3-40)
- [Figura 3.41. Wireflow de Extras: Cerrar sesión de forma segura](03-chapter.md#figura-3-41)
- [Figura 3.42. Wireflow de Emergency & Alerting: Atender una alerta de caída (US08, US11)](03-chapter.md#figura-3-42)
- [Figura 3.43. Wireflow de Emergency & Alerting: Responder a un SOS (US15)](03-chapter.md#figura-3-43)
- [Figura 3.44. Wireflow de Emergency & Alerting: Seguir una alerta de signos vitales (US09, US10)](03-chapter.md#figura-3-44)
- [Figura 3.45. Wireflow de Care Routines & Wellness: Programar una toma de medicación (US06)](03-chapter.md#figura-3-45)
- [Figura 3.46. Wireflow de Care Routines & Wellness: Agendar una cita médica (US13)](03-chapter.md#figura-3-46)
- [Figura 3.47. Mock-ups de Health Monitoring](03-chapter.md#figura-3-47)
- [Figura 3.48. Mock-ups de Extras](03-chapter.md#figura-3-48)
- [Figura 3.49. Mock-ups de Emergency & Alerting](03-chapter.md#figura-3-49)
- [Figura 3.50. Mock-ups de Care Routines & Wellness](03-chapter.md#figura-3-50)
- [Figura 3.51. User flow de Mobility & Geofencing: Consultar la ubicación en tiempo real](03-chapter.md#figura-3-51)
- [Figura 3.52. User flow de Mobility & Geofencing: Comunicarse directamente con la persona bajo cuidado](03-chapter.md#figura-3-52)
- [Figura 3.53. User flow de Mobility & Geofencing: Configurar y monitorear zonas seguras](03-chapter.md#figura-3-53)
- [Figura 3.54. User flow de Health Monitoring: Consultar ritmo cardíaco (US01)](03-chapter.md#figura-3-54)
- [Figura 3.55. User flow de Health Monitoring: Consultar presión arterial (US02)](03-chapter.md#figura-3-55)
- [Figura 3.56. User flow de Health Monitoring: Consultar saturación de oxígeno (US03)](03-chapter.md#figura-3-56)
- [Figura 3.57. User flow de Health Monitoring: Supervisar temperatura corporal (US04)](03-chapter.md#figura-3-57)
- [Figura 3.58. User flow de Health Monitoring: Consultar frecuencia respiratoria (US05)](03-chapter.md#figura-3-58)
- [Figura 3.59. User flow de Health Monitoring: Analizar tendencias históricas (US07)](03-chapter.md#figura-3-59)
- [Figura 3.60. User flow de Health Monitoring: Exportar historial de telemetría (US19)](03-chapter.md#figura-3-60)
- [Figura 3.61. User flow de Health Monitoring: Sincronizar telemetría sin conexión (US21)](03-chapter.md#figura-3-61)
- [Figura 3.62. User flow de Health Monitoring: Revisar reporte semanal de salud (US24)](03-chapter.md#figura-3-62)
- [Figura 3.63. User flow de Extras: Gestionar información personal](03-chapter.md#figura-3-63)
- [Figura 3.64. User flow de Extras: Consultar entorno de cuidado](03-chapter.md#figura-3-64)
- [Figura 3.65. User flow de Extras: Consultar suscripción actual](03-chapter.md#figura-3-65)
- [Figura 3.66. User flow de Extras: Configurar preferencias de la aplicación](03-chapter.md#figura-3-66)
- [Figura 3.67. User flow de Emergency & Alerting: Atender una alerta de caída (US08, US11)](03-chapter.md#figura-3-67)
- [Figura 3.68. User flow de Emergency & Alerting: Responder a un SOS (US15, US25)](03-chapter.md#figura-3-68)
- [Figura 3.69. User flow de Emergency & Alerting: Seguir una alerta de signos vitales (US09, US10)](03-chapter.md#figura-3-69)
- [Figura 3.70. Conexiones del prototipo de Guardian+](03-chapter.md#figura-3-70)
- [Figura 3.71. Conexiones de la sección Salud en el prototipo](03-chapter.md#figura-3-71)
- [Figura 3.72. Ejecución del prototipo desde la pantalla de Inicio](03-chapter.md#figura-3-72)

**Capítulo IV: Product Implementation & Validation**

- [Figura 4.1. Diagrama de despliegue de Guardian+](04-chapter.md#figura-4-1)
- [Figura 4.2. Tablero del Sprint 1 en ClickUp (parte 1)](04-chapter.md#figura-4-2)
- [Figura 4.3. Tablero del Sprint 1 en ClickUp (parte 2)](04-chapter.md#figura-4-3)
- [Figura 4.4. Ejecución de los Unit Tests de Profile](04-chapter.md#figura-4-4)
- [Figura 4.5. Landing Page en ejecución](04-chapter.md#figura-4-5)
- [Figura 4.6. Aplicación móvil en ejecución en el emulador](04-chapter.md#figura-4-6)
- [Figura 4.7. Web Services en ejecución en Swagger UI](04-chapter.md#figura-4-7)
- [Figura 4.8. Landing Page publicado en Cloudflare Pages](04-chapter.md#figura-4-8)
- [Figura 4.9. Grupo de recursos guardian-plus-rg en Azure](04-chapter.md#figura-4-9)
- [Figura 4.10. Máquina virtual guardian-plus-vm en Azure](04-chapter.md#figura-4-10)
- [Figura 4.11. Servidor de Azure Database for PostgreSQL](04-chapter.md#figura-4-11)
- [Figura 4.12. Ejecuciones de los workflows de GitHub Actions](04-chapter.md#figura-4-12)
- [Figura 4.13. Documentación de los Web Services en Swagger UI](04-chapter.md#figura-4-13)
- [Figura 4.14. Insights del repositorio de los Web Services](04-chapter.md#figura-4-14)
- [Figura 4.15. Insights del repositorio de la aplicación móvil](04-chapter.md#figura-4-15)
- [Figura 4.16. Insights del repositorio del Landing Page](04-chapter.md#figura-4-16)
- [Figura 4.17. Insights del repositorio del IoT Simulator](04-chapter.md#figura-4-17)
- [Figura 4.18. Video de las entrevistas de validación del Landing Page](04-chapter.md#figura-4-18)
- [Figura 4.19. Captura de la entrevista de validación a Rocio Alvarado](04-chapter.md#figura-4-19)
- [Figura 4.20. Captura de la entrevista de validación a Junior Antenor](04-chapter.md#figura-4-20)
- [Figura 4.21. Captura de la entrevista de validación a Roxana Paola Diana](04-chapter.md#figura-4-21)
- [Figura 4.22. Captura de la entrevista de validación a Piero Segurda Cardenas](04-chapter.md#figura-4-22)
- [Figura 4.23. Captura de la entrevista de validación a Gabriela Cuadros](04-chapter.md#figura-4-23)
- [Figura 4.24. Pantalla Nueva toma del módulo de Rutinas](04-chapter.md#figura-4-24)
- [Figura 4.25. Pantalla Nueva cita del módulo de Rutinas](04-chapter.md#figura-4-25)
- [Figura 4.26. Pantalla Nueva actividad del módulo de Rutinas](04-chapter.md#figura-4-26)
- [Figura 4.27. Pantalla Contactos de emergencia](04-chapter.md#figura-4-27)
- [Figura 4.28. Panel Buscar y filtrar del módulo de Salud](04-chapter.md#figura-4-28)
- [Figura 4.29. Pantalla Exportar expediente](04-chapter.md#figura-4-29)
- [Figura 4.30. Pantalla Sueño del módulo de Rutinas](04-chapter.md#figura-4-30)

<div style="page-break-before: always; break-before: page;"></div>

# Student Outcome

**ABET - EAC - Student Outcome 7**

Criterio: *La capacidad de adquirir y aplicar nuevos conocimientos según sea necesario, utilizando estrategias de aprendizaje apropiadas.*

En el siguiente cuadro se describen las acciones realizadas y enunciados de conclusiones por parte del grupo, que permiten sustentar el haber alcanzado el logro del ABET – EAC - Student Outcome 7.

<table>
<thead>
<tr>
<th>Criterio específico</th>
<th>Acciones realizadas</th>
<th>Conclusiones</th>
</tr>
</thead>
<tbody>
<tr>
<td>Actualiza conceptos y conocimientos necesarios para su desarrollo profesional y en especial para su proyecto en soluciones de software.</td>
<td>
<strong>Azama Fukuda, Juan Pablo</strong><br>
<em>AV1:</em> Investigué y apliqué el patrón Bounded Context Canvas (Nick Tune V1) y el enfoque táctico de Domain-Driven Design (agregados, value objects, domain services y repositorios) para diseñar desde cero el Bounded Context IAM: registro y verificación de credenciales, autenticación con segundo factor (OTP) y recuperación de contraseña. También diseñé y documenté el Bounded Context Health Monitoring, contrastando mi propio modelo de dominio contra el diagrama de clases que ya habíamos elaborado como equipo para asegurarme de que ambos coincidieran. Redacté y prioricé las User Stories del proyecto, documenté el User Task Matrix y elaboré el análisis competitivo con las estrategias frente a nuestros competidores. Para terminar de documentar IAM aprendí por mi cuenta dos notaciones que no vimos en clase, Structurizr DSL para el diagrama de componentes C4 y PlantUML para el diagrama de clases, y las apliqué directamente sobre mi propio diseño.<br>
<em>TB1:</em> Elaboré la guía de estilos general y los Searching Systems de la arquitectura de información, y diseñé los flujos, wireframes y mock-ups del Bounded Context Health Monitoring en la aplicación móvil. Como líder de UX/UI Design, Health Monitoring e IAM, implementé Health Monitoring en los Web Services con Spring Boot y desarrollé las pantallas de inicio de sesión y de monitoreo de salud en Kotlin con Jetpack Compose. También construí en Python el simulador IoT que reproduce los datos de la pulsera para probar el sistema sin el dispositivo físico. Por último, preparé el Sprint Planning, el Sprint Backlog y la matriz de líderes y colaboradores del Sprint 1 en ClickUp.
<br><br>
<strong>Mechan Montenegro, Luciana Carolina</strong><br>
<em>AV1:</em> Reforcé el concepto de Análisis Competitivo como herramienta estratégica para contrastar la propuesta de valor de una solución frente al mercado, aplicándolo dentro del contexto específico de este proyecto. Amplié y actualicé mis conocimientos sobre User Personas dentro del proceso de Needfinding, afinando la forma en que sintetizo información cualitativa en arquetipos de usuario. Profundicé en Domain-Driven Design (DDD) a nivel estratégico, reforzando el uso de Event Storming como técnica colaborativa para el descubrimiento del dominio, así como el Bounded Context Canvas para delimitar responsabilidades entre subdominios. De igual forma, actualicé mi manejo del C4 Model para la representación de arquitectura de software en distintos niveles de abstracción, y reforcé el concepto de Ubiquitous Language como práctica para establecer un vocabulario común entre el equipo técnico y los stakeholders del negocio.<br>
<em>TB1:</em> Actualicé y apliqué conceptos de diseño de interfaces móviles al elaborar en Figma las pantallas principales del bounded context de Care Routines & Wellness, cuidando la consistencia visual con las Style Guidelines del proyecto, la usabilidad y los principios de diseño inclusivo para usuarios como familiares y cuidadores. Además, amplié mi manejo de Domain-Driven Design a nivel táctico al implementar el backend con Java y Spring Boot, llevando el modelo de dominio diseñado en la entrega anterior a código organizado en capas (Domain, Application, Interface e Infrastructure).
<br><br>
<strong>Luis Miranda, Diego Andres</strong><br>
<em>AV1:</em> Identifiqué al público objetivo al que va dirigido el producto: cuidadores y familiares. Las entrevistas que realicé me permitieron transformar sus necesidades en requerimientos funcionales. Además, elaboré la descripción de la startup y diseñé un bounded context de Mobility & Geofencing, complementado con sesiones de event storming, canvas estratégico y la aplicación de Tactical Domain Driven Design dividido en capas (interface, domain, application, infrastructure). Finalmente, desarrollé diagramas de base de datos y modelos arquitectónicos C4, lo que me exigió investigar y aplicar herramientas de modelado avanzadas. Estas actividades reflejan mi capacidad de aprender de manera autónoma y aplicar ese aprendizaje en la práctica.<br>
<em>TB1:</em> Me encargué de diseñar la interfaz (wireframes, mock-ups y flujos) del Bounded Context Mobility & Geofencing, teniendo en cuenta la arquitectura de información, nuestras User Stories y sus criterios de aceptación para cumplir cada user goal. Además, participé en la implementación de este contexto en el backend, integrado con la arquitectura por capas definida con DDD. También apoyé en el apartado Development Evidence for Sprint Review, documentando las evidencias del avance del proyecto (Web Services, Landing Page y aplicación móvil).
<br><br>
<strong>López Monroy, Rodrigo Alfredo</strong><br>
<em>AV1:</em> Apliqué Domain-Driven Design en sus dos niveles para diseñar el Bounded Context Emergency & Alerting, que es el Core Domain de Guardian+. En lo estratégico partí del EventStorming para delimitar el contexto y armar su Bounded Context Canvas, y en lo táctico definí sus agregados, value objects y eventos de dominio sobre una arquitectura de cuatro capas. Modelé el recorrido completo de una emergencia, desde la señal de riesgo hasta la respuesta del cuidador, con sus reglas de despacho y escalamiento. Para documentarlo aprendí por mi cuenta Mermaid y Graphviz, que no vimos en clase, y me permitieron mantener los diagramas como código versionado junto al informe.<br>
<em>TB1:</em> Desarrollé los Labelling Systems y Navigation Systems de la arquitectura de información. Para ello investigué los tipos de navegación y las recomendaciones de Material Design para la bottom navigation bar, que limitan los destinos principales a cinco, lo que me llevó a reubicar Perfil en la barra superior. Implementé el Bounded Context Emergency & Alerting en los Web Services con Spring Boot y sus pantallas en la aplicación móvil con Kotlin y Jetpack Compose, además de construir el Landing Page con React. Para publicar el backend aprendí a desplegarlo en una máquina virtual de Azure con Docker Compose, Caddy y Azure Database for PostgreSQL, y a automatizar ese despliegue con GitHub Actions. También conecté el prototipo navegable en Figma y rehíce el Context Map con la notación de DDD Crew usando Context Mapper.
<br><br>
<strong>Sanchez Cuadrado, Juan Antonio</strong><br>
<em>AV1:</em> Durante el desarrollo de Guardian+ profundicé y apliqué conceptos de Domain-Driven Design y arquitectura de software para diseñar y documentar los Bounded Contexts Subscriptions y Profile. Trabajé desde el EventStorming y los Bounded Context Canvases hasta el diseño táctico, definiendo Aggregate Roots, Entities, Value Objects, Domain Policies, Repository Interfaces y las capas Interface, Application, Domain e Infrastructure. Además, aprendí y apliqué Structurizr DSL para elaborar los diagramas de componentes C4 y reforcé el modelado UML en Lucidchart para mantener los Code Level Diagrams alineados con el modelo de persistencia. Durante la revisión también identifiqué y corregí inconsistencias entre los modelos de dominio, los diagramas de componentes y el ERD, manteniendo coherencia entre las reglas de negocio, la arquitectura y la base de datos.<br>
<em>TB1:</em> Actualicé y apliqué mis conocimientos de Domain-Driven Design y arquitectura por capas durante la implementación del Bounded Context Profile de Guardian+. Pasé del diseño conceptual a una implementación funcional mediante aggregates como UserProfile, CareRecipientProfile, CareRelationship y UserPreferences, incorporando commands, queries, domain events, repositories, servicios de aplicación, persistencia con JPA y endpoints REST. También reforcé mis conocimientos de pruebas automatizadas utilizando JUnit Jupiter, Mockito y el patrón AAA, implementando una suite de 18 Unit Tests que validan el comportamiento del dominio y los servicios de aplicación. Asimismo, apliqué conocimientos de Git y GitFlow para integrar la rama de Profile con develop, resolver conflictos en recursos compartidos y mantener la compatibilidad con los demás bounded contexts. Finalmente, reforcé el prototipado interactivo en Figma conectando el Dashboard con Perfil y sus pantallas de Persona bajo cuidado, Círculo de cuidado, Configuración, Idioma y Accesibilidad.
</td>
<td><em>AV1:</em> Como equipo notamos que avanzar con Guardian+ nos obligó a reforzar conceptos que no dominábamos del todo, sobre todo en Domain-Driven Design estratégico y táctico, y en notaciones de arquitectura (C4, Structurizr, PlantUML) que terminamos aplicando directamente sobre nuestro propio backend en vez de quedarnos solo con la teoría vista en clase.<br><br>
<em>TB1:</em> Como equipo pasamos del diseño a la implementación y eso nos llevó a actualizar conocimientos en frentes muy distintos: arquitectura de información, guía de estilos y prototipado en Figma para la aplicación móvil; Spring Boot, JPA y pruebas con JUnit y Mockito para los Web Services; Kotlin con Jetpack Compose para la app; y un simulador IoT en Python para reemplazar la pulsera física. Aplicar el modelo táctico de DDD en código real nos mostró que el diseño del AV1 necesitaba ajustes, por lo que tuvimos que volver a la documentación y alinearla con lo implementado en cada Bounded Context.</td>
</tr>
<tr>
<td>Reconoce la necesidad del aprendizaje permanente para el desempeño profesional y el desarrollo de proyectos en soluciones de software.</td>
<td>
<strong>Azama Fukuda, Juan Pablo</strong><br>
<em>AV1:</em> Como team leader revisé la coherencia entre los artefactos de DDD que ya teníamos (EventStorming, Bounded Context Canvases y diseño táctico) y esto me forzó a aprender nuevos conceptos relacionados a DDD. De la misma manera, al diseñar los bounded context de IAM, tuve que investigar sobre los conceptos de OTP y servicios de envío de correos electrónicos, actualmente es una primera iteración de diseño pero con el tiempo todo se irá refinando poco a poco. Esto me da a comprender que, obviamente, a lo largo de mi carrera siempre tendré que aprender conocimientos técnicos nuevos, al igual que mejorar mis habilidades blandas.<br>
<em>TB1:</em> Pasar del diseño a la implementación me mostró que el modelo de Health Monitoring del AV1 no coincidía del todo con lo que realmente necesitaba el código, por lo que tuve que volver a la documentación y alinear cada capa con lo implementado. Además, trabajar por primera vez con Jetpack Compose y con un simulador IoT me obligó a aprender sobre la marcha, y coordinar el Sprint en ClickUp me enseñó a planificar considerando la capacidad real del equipo y no solo el alcance deseado.
<br><br>
<strong>Mechan Montenegro, Luciana Carolina</strong><br>
<em>AV1:</em> Reconocí que, pese a haber aplicado antes Event Storming, Bounded Context Canvas y C4 Model, cada nuevo dominio de negocio me exige volver a estudiar y adaptar estas técnicas, ya que su correcta aplicación depende de la comprensión particular del proyecto y no de un conocimiento memorizado. También identifiqué que un artefacto como el Ubiquitous Language necesita revisión y actualización constante a medida que el proyecto avanza, lo que confirma que el aprendizaje no se detiene una vez que se domina una herramienta por primera vez.<br>
<em>TB1:</em> Reconocí que pasar del diseño a la implementación exige seguir aprendiendo ya que al convertir el modelo de dominio en un backend funcional con Spring Boot tuve que revisar y reforzar conceptos de DDD táctico que en el diseño inicial se veían correctos, pero que en el código requerían decisiones adicionales. De igual forma, al diseñar las pantallas de Figma comprendí que el diseño de interfaces debe contrastarse constantemente con las necesidades reales de los usuarios identificadas en las entrevistas, lo que me llevó a revisar y ajustar mis decisiones de diseño.
<br><br>
<strong>Luis Miranda, Diego Andres</strong><br>
<em>AV1:</em> Desde la perspectiva de identificación del público objetivo y la realización de entrevistas con cuidadores y familiares, hasta la elaboración de la propuesta de la startup y el diseño del bounded context de Mobility & Geofencing, tuve que incorporar metodologías de análisis de usuarios, técnicas de Domain Driven Design y herramientas de modelado arquitectónico como diagramas de base de datos y C4. Este proceso evidenció que el desempeño en soluciones de software requiere una actitud constante de aprendizaje, exploración de nuevas prácticas y adaptación a contextos cambiantes, lo cual fortalece mi capacidad de crecer profesionalmente.<br>
<em>TB1:</em> Amplié y apliqué mis conocimientos en diseño de interfaces, arquitectura de información, user stories y criterios de aceptación para desarrollar los mockups, wireframes y flujos correspondientes al bounded context de Mobility & Geofencing. Asimismo, reforcé mis conocimientos sobre Domain-Driven Design (DDD) y arquitectura por capas mediante mi participación en la implementación del backend de este contexto y su integración con la arquitectura definida para el proyecto. Complementariamente, participé en la documentación de las evidencias de desarrollo para el Sprint Review, recopilando y organizando los avances relacionados con los web services, landing page y aplicación móvil. Estas actividades me permitieron aprender y adaptarme a diferentes aspectos del desarrollo de software, demostrando que la actualización constante de conocimientos es necesaria para responder a los requerimientos del proyecto y mejorar la calidad de las soluciones desarrolladas.
<br><br>
<strong>López Monroy, Rodrigo Alfredo</strong><br>
<em>AV1:</em> Modelar reglas de temporización y escalamiento me tomó varias iteraciones y discusiones con el equipo hasta llegar a un modelo que representara el negocio y no solo mis supuestos. También aprendí que mantener alineados los distintos diagramas no es algo que ocurra solo: si cada uno avanza por su lado, terminan describiendo cosas distintas del mismo dominio. Hacia adelante quiero especializarme en sistemas embebidos, que tiene estándares y restricciones bastante distintos a los del desarrollo web, así que doy por hecho que voy a seguir aprendiendo por mi cuenta después de la carrera.<br>
<em>TB1:</em> Al definir la navegación de la app antes de que existieran sus wireframes, entendí que las decisiones de arquitectura de información condicionan el trabajo de diseño que viene después, por lo que deben documentarse y comunicarse al equipo. Pasar del diseño de Emergency & Alerting a su implementación me obligó a ajustar el modelo que había planteado en el AV1, porque varias reglas de escalamiento solo se entendieron bien al programarlas. El despliegue en Azure tampoco salió a la primera: tuve que aprender sobre la marcha a leer los registros de un pipeline y a trabajar con los límites de memoria de la máquina virtual. Esto me confirma que cada entrega me va a exigir herramientas que todavía no conozco.
<br><br>
<strong>Sanchez Cuadrado, Juan Antonio</strong><br>
<em>AV1:</em> El desarrollo de Guardian+ me permitió reconocer que los conocimientos aprendidos en clase necesitan complementarse continuamente con investigación y práctica autónoma. Para completar mis responsabilidades tuve que aprender a relacionar artefactos de distintos niveles, como EventStorming, Bounded Context Canvas, C4, UML y modelos relacionales, entendiendo cómo un cambio en el dominio puede afectar también la arquitectura y la persistencia. Asimismo, investigué por mi cuenta el uso de Structurizr DSL y conceptos de integración y desacoplamiento entre Bounded Contexts. Esta experiencia me permitió comprender que, en el desarrollo profesional de software, las herramientas, tecnologías y decisiones de diseño evolucionan constantemente, por lo que será necesario continuar actualizando mis conocimientos técnicos durante toda mi carrera.<br>
<em>TB1:</em> Durante el desarrollo de Guardian+ reconocí que implementar una solución real exige seguir aprendiendo y adaptando conocimientos incluso después de haber realizado el diseño inicial. La implementación de Profile me llevó a revisar y profundizar conceptos de DDD, persistencia con JPA, diseño de servicios REST, validaciones, internacionalización y pruebas unitarias. Además, al integrar mi trabajo con develop tuve que aprender a resolver conflictos de Git sin afectar los cambios realizados por otros integrantes y verificar nuevamente el funcionamiento mediante pruebas automatizadas. Del mismo modo, el desarrollo del prototipo en Figma me permitió aprender a definir flujos de navegación coherentes entre pantallas sin depender únicamente del Bottom Navigation. Estas actividades me permitieron reconocer que las tecnologías, herramientas y buenas prácticas evolucionan constantemente y que mantener un aprendizaje continuo será necesario para desarrollar soluciones de software de manera profesional.
</td>
<td><em>AV1:</em> Como equipo reconocimos que, incluso contando con experiencia previa en DDD y en herramientas de arquitectura, cada nuevo dominio de negocio nos exige volver a investigar, adaptar y refinar esos conceptos en lugar de aplicarlos de forma mecánica, ya sea al diseñar bounded contexts desde cero, al mantener coherencia entre los artefactos elaborados como equipo o al actualizar el Ubiquitous Language conforme avanza el proyecto. Esto nos confirma que el aprendizaje técnico no termina al dominar una herramienta por primera vez, sino que es un proceso continuo que se repite en cada proyecto, y que a lo largo de nuestra carrera profesional deberemos seguir actualizando tanto nuestros conocimientos técnicos como nuestras habilidades blandas.<br><br>
<em>TB1:</em> Como equipo comprobamos que implementar una solución real exige seguir aprendiendo después de haber terminado el diseño: tecnologías nuevas para varios de nosotros, como Jetpack Compose o el despliegue en la nube, la integración de ramas con GitFlow sin afectar el trabajo de los demás y la planificación del Sprint según la capacidad real del equipo. También notamos que las versiones de frameworks y las condiciones de los servicios en la nube cambian con rapidez, por lo que cada decisión técnica deberá volver a investigarse en futuros proyectos. Esto confirma que el aprendizaje continuo es parte del trabajo profesional y no una etapa que termina con el curso.</td>
</tr>
</tbody>
</table>


# Objetivos SMART

## Azama Fukuda, Juan Pablo

**Objetivo SMART 1:**
Dentro de los 3 años posteriores a mi graduación, alcanzaré el rol de Ingeniero de Software Semi Senior, liderando el diseño arquitectónico de al menos 2 aplicaciones web en producción (definición de arquitectura, ADRs y patrones de diseño), evidenciado por la propiedad técnica de al menos un módulo crítico en cada proyecto y la aprobación formal de mis decisiones de diseño en revisiones de arquitectura.
- *Specific:* Rol + entregable concreto (ownership arquitectónico de 2 apps).
- *Measurable:* Se verifica con el cambio de título/rol y el conteo de ADRs/módulos bajo mi propiedad.
- *Achievable:* Alcanzable en 3 años dado el ciclo típico junior a mid senior.
- *Relevant:* Aplica directamente arquitectura de software y diseño de software, áreas que me interesan.
- *Time-bound:* 3 años desde la graduación.

**Objetivo SMART 2:**
Dentro de los primeros 2 años de carrera, entregaré al menos 3 mejoras medibles (rendimiento, reducción de deuda técnica o automatización) en los productos web de las empresas donde trabaje, cada una respaldada por una métrica de impacto (p. ej. ≥20% de reducción en tiempo de carga o ≥15% de reducción de bugs en producción).
- *Specific:* Tipo y cantidad de contribuciones definidas (3, medibles).
- *Measurable:* Métricas numéricas concretas por contribución.
- *Achievable:* Realista para un ingeniero que busca responsabilidad propia activamente desde el inicio.
- *Relevant:* Responde directamente a "crear valor" y "contribuciones significativas", algo que considero que es importante para mi crecimiento.
- *Time-bound:* 2 años desde el inicio de la carrera profesional.

## Mechan Montenegro, Luciana Carolina

**Objetivo SMART 1:**
Durante los primeros 18 meses después de graduarme, me desempeñaré como desarrolladora backend en una empresa de tecnología, consolidando experiencia práctica en el diseño e implementación de servicios backend y arquitecturas escalables en proyectos reales de producción. Para ello, comenzaré desde ahora a prepararme para obtener una certificación relacionada a arquitectura de software en la nube (por ejemplo, AWS Certified Solutions Architect – Associate o equivalente), la cual buscaré tener lista como máximo dentro de los primeros meses tras egresar.
- *Specific:* Desempeñarme como desarrolladora backend consolidando experiencia en diseño de servicios y arquitecturas escalables, y obtener una certificación en arquitectura cloud.
- *Measurable:* Un puesto laboral formal como backend developer y una certificación obtenida.
- *Achievable:* Cuento con base técnica previa en desarrollo backend y arquitectura de software desarrollada durante la carrera, y ya puedo empezar a prepararme para la certificación desde ahora.
- *Relevant:* Sienta las bases técnicas necesarias para avanzar hacia roles de mayor responsabilidad en arquitectura de software.
- *Time-bound:* Certificación lista a más tardar en los primeros meses tras la graduación; consolidación en el rol backend dentro de los 18 meses posteriores.

**Objetivo SMART 2:**
En un plazo de 4 años tras graduarme, asumiré un rol de mayor responsabilidad técnica (Senior Backend Developer o Software Architect Jr.) en el que participe activamente en la toma de decisiones de arquitectura de software, como definición de bounded contexts, patrones de integración entre servicios y selección de tecnologías, habiendo liderado o co-liderado al menos dos proyectos de diseño o migración de arquitectura de software dentro de ese periodo.
- *Specific:* Asumir un rol donde participe en decisiones de arquitectura de software, con al menos dos proyectos liderados o co-liderados en ese ámbito.
- *Measurable:* Cargo formal alcanzado y número de proyectos de arquitectura en los que haya participado activamente.
- *Achievable:* Es una progresión natural desde un rol de desarrollo backend, apoyada en la experiencia técnica acumulada desde la universidad.
- *Relevant:* Está directamente alineado con mi interés profesional a largo plazo en arquitectura de software y desarrollo backend.
- *Time-bound:* 4 años después de la graduación.

## Luis Miranda, Diego Andres

**Objetivo SMART 1:**
Dentro de los 2 años posteriores a mi graduación, alcanzaré el rol de AI Engineer o Full Stack Developer, liderando la integración de modelos de Inteligencia Artificial (modelos predictivos), asumiré roles de liderazgo técnico en al menos 2 proyectos de software, aplicando principios de arquitectura y documentando resultados, con el fin de consolidar mi perfil como arquitecto de software.
- *Specific:* Desarrollar habilidades en diseño de arquitecturas de software y liderazgo técnico en proyectos colaborativos.
- *Measurable:* Participar en al menos 2 proyectos académicos o personales donde asuma el rol de arquitecto o líder técnico, documentando las decisiones de diseño y resultados.
- *Achievable:* Aprovechar cursos de la carrera y proyectos extracurriculares para aplicar patrones de arquitectura y buenas prácticas.
- *Relevant:* Fortalecer mi perfil profesional AI Engineer para roles de liderazgo en desarrollo de software.
- *Time-bound:* Antes de 2 años posteriores a mi graduación.

**Objetivo SMART 2:**
En los próximos 2 años después de graduarme, contribuiré con al menos 5 funcionalidades clave en proyectos de software (académicos, open source o laborales), asegurando que generen valor medible para usuarios o equipos, consolidando mi especialización en AI Engineer o full stack developer.
- *Specific:* Generar impacto directo en proyectos de desarrollo mediante aportes técnicos en AI, full stack o Dev.
- *Measurable:* Contribuir con al menos 5 funcionalidades clave en proyectos académicos, open source o laborales, que sean utilizadas por otros usuarios o equipos.
- *Achievable:* Usar mis conocimientos adquiridos en .NET, Spring Boot, Node.js y bases de datos para implementar soluciones completas.
- *Relevant:* Alinear mi crecimiento profesional con la especialización en AI Engineer o full stack developer.
- *Time-bound:* Alcanzar este objetivo dentro de los 2 años posteriores a mi graduación.

## López Monroy, Rodrigo Alfredo

**Objetivo SMART 1:**
Dentro de los primeros 18 meses posteriores a mi graduación, me incorporaré como ingeniero de software embebido o de firmware, programando en C y C++ sobre sistemas operativos de tiempo real, y consolidaré esa base con al menos 3 proyectos propios documentados en un repositorio público y un curso o certificación formal en sistemas embebidos.
- *Specific:* Incorporarme a un rol de software embebido o firmware con C/C++ y RTOS, con 3 proyectos documentados y una certificación del área.
- *Measurable:* Un puesto formal en el rubro, 3 repositorios públicos con su documentación y el certificado obtenido.
- *Achievable:* Parte de la base en programación de bajo nivel y protocolos de comunicación la trabajé durante la carrera, y los proyectos propios puedo iniciarlos desde ahora sin depender de un empleador.
- *Relevant:* Es la puerta de entrada al diseño de software de bajo nivel, que es el campo en el que quiero especializarme.
- *Time-bound:* 18 meses desde la graduación, con la certificación lista durante el primer año.

**Objetivo SMART 2:**
En un plazo de 4 años tras graduarme, cursaré una especialización de posgrado en sistemas embebidos o software automotriz en el extranjero y daré el paso a la industria automotriz, habiendo postulado a al menos 4 programas con financiamiento o beca, obtenido admisión en uno de ellos, y acreditado formación en los estándares del sector, como AUTOSAR para la arquitectura de software automotriz, MISRA C como estándar de codificación e ISO 26262 de seguridad funcional, para contribuir en al menos un proyecto de software vehicular en desarrollo o en producción.
- *Specific:* Cursar un posgrado en el extranjero en sistemas embebidos o software automotriz y entrar a la industria automotriz con formación acreditada en AUTOSAR, MISRA C e ISO 26262.
- *Measurable:* 4 postulaciones enviadas, una carta de admisión, los certificados de los tres estándares y la participación verificable en un proyecto de software vehicular.
- *Achievable:* Los 18 meses previos de experiencia en firmware y el portafolio del primer objetivo sostienen tanto la postulación al posgrado como el cambio de industria.
- *Relevant:* Reúne mis tres metas profesionales: especializarme en el extranjero, trabajar en software de bajo nivel y hacerlo en el sector automotriz.
- *Time-bound:* 4 años desde la graduación, con las postulaciones enviadas antes del segundo año.

## Sanchez Cuadrado, Juan Antonio

**Objetivo SMART 1:**
Dentro de los primeros 2 años posteriores a mi graduación, participaré en el desarrollo y publicación de al menos 2 aplicaciones móviles Android en producción utilizando Kotlin e integración con servicios backend, asumiendo responsabilidad directa sobre al menos un módulo funcional completo en cada proyecto y alcanzando una cobertura mínima de pruebas automatizadas del 70% en dichos módulos.
- *Specific:* Desarrollar aplicaciones Android reales y asumir responsabilidad completa sobre módulos funcionales.
- *Measurable:* 2 aplicaciones en producción, al menos 1 módulo funcional bajo mi responsabilidad por aplicación y una cobertura mínima de pruebas del 70% en dichos módulos.
- *Achievable:* Es alcanzable considerando mi formación en Ingeniería de Software y la experiencia que estoy desarrollando actualmente en Android, arquitectura de aplicaciones e integración con APIs.
- *Relevant:* Está alineado con mi interés profesional en desarrollo móvil y en la construcción de soluciones de software completas y mantenibles.
- *Time-bound:* Dentro de los primeros 2 años posteriores a mi graduación.

**Objetivo SMART 2:**
Durante los primeros 3 años de mi carrera profesional, diseñaré e implementaré al menos 3 módulos backend aplicando principios de arquitectura modular o Domain-Driven Design, integrando en cada uno como mínimo una base de datos y un servicio externo, y documentando sus principales decisiones mediante diagramas C4, UML o ADRs antes de su puesta en producción.
- *Specific:* Diseñar e implementar módulos backend con arquitectura modular o DDD, persistencia e integración con servicios externos.
- *Measurable:* Al menos 3 módulos completados, cada uno con base de datos, una integración externa y documentación arquitectónica.
- *Achievable:* Es una meta progresiva y alcanzable a partir de los conocimientos que estoy desarrollando en diseño de Bounded Contexts, APIs, repositories, C4 y modelado de dominio.
- *Relevant:* Complementa mi perfil de desarrollo móvil con capacidades de backend, integración y diseño arquitectónico de soluciones.
- *Time-bound:* Dentro de los primeros 3 años de mi carrera profesional.
