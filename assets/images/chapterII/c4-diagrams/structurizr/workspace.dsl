workspace "Guardian+" "C4 model of the Guardian+ platform." {

    model {
        familyMember = person "Family Member" "A family member of an elderly, disabled, or dependent person who supervises their wellbeing without being permanently present."
        personUnderCare = person "Person Under Care" "Elderly person, person with disability, or person in a dependency situation who wears the Guardian+ bracelet."
        caregiver = person "Caregiver" "A person in charge of the frequent or permanent care of an elderly, disabled, or dependent person, either privately or as part of a specialized institution."

        stripe = softwareSystem "Stripe" "External payment gateway that processes subscription payments." "External"
        notificationService = softwareSystem "Push/SMS Notification Service" "External service that dispatches push notifications and SMS messages for alerts and reminders." "External"
        videoCallService = softwareSystem "Video Call Service" "External real-time communication service used for direct video calls between family/caregiver and the person under care." "External"
        googleMaps = softwareSystem "Google Maps" "External mapping and geolocation service used for location visualization, geocoding, and geofence calculations." "External"

        guardianPlus = softwareSystem "Guardian+" "Container view of the Guardian+ platform." {
            landingPage = container "Guardian+ Landing Page" "Public landing page where visitors learn about the value proposition, subscription plans, and can contact the team." "React, HTML, CSS, JavaScript" "Web"
            mobileApp = container "Guardian+ Mobile Application" "Provides the experience for family members and caregivers: health monitoring, routine management, alerts, and location tracking." "Native Android, Kotlin" "Mobile"
            wearableFirmware = container "Guardian+ Wearable Firmware" "Embedded firmware running on the IoT bracelet that captures vital signs, detects falls, obtains GPS location, and allows the SOS button to be triggered." "Embedded, C/C++ on ESP32-S3" "Embedded"
            restApi = container "Guardian+ REST API" "Provides the backend REST APIs for health monitoring, alerting, routines, location, identity, and subscriptions." "Java and Spring Boot" "API"
            database = container "Guardian+ Database" "Stores all domain data: identity, profiles, vital signs, routines, alerts, location, and subscriptions." "PostgreSQL Server" "Database"
        }

        familyMember -> landingPage "Visits" "HTTPS"
        familyMember -> mobileApp "Uses" "HTTPS"
        caregiver -> landingPage "Visits" "HTTPS"
        caregiver -> mobileApp "Uses" "HTTPS"
        personUnderCare -> wearableFirmware "Wears and uses (SOS button, sensors)"

        wearableFirmware -> restApi "Sends vital-sign telemetry, location, and events" "MQTT/HTTPS"
        mobileApp -> restApi "Consumes" "RESTful API/JSON-HTTPS"
        restApi -> database "Reads and writes" "JDBC"
        restApi -> stripe "Processes payments and subscriptions" "HTTPS"
        restApi -> notificationService "Sends push notifications and SMS" "HTTPS"
        restApi -> videoCallService "Orchestrates video call sessions" "HTTPS"
        restApi -> googleMaps "Queries geocoding and address resolution" "HTTPS"
        mobileApp -> videoCallService "Establishes the video call directly" "HTTPS/WebRTC"
        mobileApp -> googleMaps "Renders maps and real-time location" "HTTPS"

        production = deploymentEnvironment "Production" {
            deploymentNode "Vercel" "Hosting platform for static and frontend web applications." "Vercel Platform" {
                deploymentNode "Edge Network" "" "Global CDN" {
                    landingPageInstance = containerInstance landingPage
                }
            }

            deploymentNode "User Smartphone" "Smartphone of the family member or caregiver." "Android 7.0+ (API 24+)" {
                mobileAppInstance = containerInstance mobileApp
            }

            deploymentNode "Guardian+ Bracelet" "IoT bracelet worn by the person under care. Replaced by the IoT simulator during development." "ESP32-S3" {
                wearableFirmwareInstance = containerInstance wearableFirmware
            }

            deploymentNode "Render" "Cloud application platform." "Render (Virginia, US East)" {
                deploymentNode "Web Service" "" "Docker container" {
                    deploymentNode "Java Runtime" "" "JRE 27" {
                        restApiInstance = containerInstance restApi
                    }
                }
            }

            deploymentNode "Neon" "Managed serverless PostgreSQL service." "Neon (AWS us-east-1)" {
                deploymentNode "guardian-plus project" "" "PostgreSQL" {
                    databaseInstance = containerInstance database
                }
            }

            deploymentNode "Google Firebase" "" "Firebase" {
                appDistribution = infrastructureNode "Firebase App Distribution" "Distributes release builds of the mobile application to testers." "Firebase"
                softwareSystemInstance notificationService
            }

            deploymentNode "Stripe Cloud" "" "Stripe (test mode)" {
                softwareSystemInstance stripe
            }

            deploymentNode "Google Cloud" "" "Google Maps Platform" {
                softwareSystemInstance googleMaps
            }

            deploymentNode "Video Call Provider" "" "SaaS" {
                softwareSystemInstance videoCallService
            }

            appDistribution -> mobileAppInstance "Delivers release builds to" "HTTPS"
        }
    }

    views {
        container guardianPlus "Containers" "Container view of the Guardian+ platform." {
            include *
            autoLayout lr 300 150
        }

        deployment guardianPlus production "Deployment" "Deployment view of the Guardian+ platform in the production environment." {
            include *
            autoLayout lr 300 150
        }

        styles {
            element "Element" {
                background #ffffff
                color #1168bd
                stroke #d9d9d9
            }
            element "Person" {
                shape Person
            }
            element "Database" {
                shape Cylinder
            }
            element "External" {
                background #999999
                color #ffffff
            }
        }
    }
}
