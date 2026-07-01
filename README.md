# SysAdmin-RateLimiter-con-Middleware
este repositorio presenta el antiguo sistema de RateLimiter con una nueva implementación de Middleware.
___
Esta implementación utiliza un patrón de diseño Middleware para interceptar las peticiones HTTP antes de llegar a la lógica de negocio. Esto desacopla la capa de seguridad (Rate Limiter) de la capa de aplicación, permitiendo una arquitectura escalable y de baja latencia.
___
# GuardianRate: Sistema de Rate Limiting con Arquitectura Middleware

## Resumen Ejecutivo
Este proyecto implementa un sistema de limitación de tasa (Rate Limiter) diseñado para proteger la infraestructura web contra ataques de saturación de peticiones (DDoS) y fuerza bruta. El sistema actúa como un **Middleware** de seguridad, interceptando el tráfico antes de que llegue a la lógica de negocio.

## Decisión de Arquitectura
Para garantizar un rendimiento óptimo bajo alta carga, se han tomado las siguientes decisiones técnicas:

1.  **Estructura de Datos de Alta Eficiencia:** Se utiliza un **HashMap** (diccionario en Python) para almacenar el estado de las peticiones. Esto permite una complejidad temporal de **$O(1)$** para la búsqueda y actualización de usuarios, garantizando latencia mínima incluso al escalar el número de usuarios.
2.  **Patrón Middleware:** La lógica de validación está desacoplada del servidor web principal. Esto permite que el componente de seguridad sea agnóstico, facilitando una migración futura a soluciones de persistencia en memoria (como Redis o Memcached) sin reescribir la lógica de negocio.
3.  **Estado de Respuesta:** El sistema implementa correctamente el código de estado HTTP **429 (Too Many Requests)**, siguiendo los estándares de RFC 6585.

## Tecnologías Utilizadas
*   **Lenguaje:** Python 3.x
*   **Framework Web:** Flask (Micro-framework para el despliegue del servidor)
*   **Entorno de Ejecución:** Testeado y validado en entornos Unix-like (incluyendo Termux).

## Demostración (Proof of Concept)
Para validar la efectividad del sistema, se ha realizado una prueba de carga donde se superan los límites configurados. 

[👉 Ver video de demostración en YouTube](PRÓXIMAMENTE)

## Instrucciones de Instalación
1. Clona el repositorio:
   ```bash
   git clone [https://github.com/tu-usuario/nombre-del-repo.git](https://github.com/tu-usuario/nombre-del-repo.git)

*cabe aclarar que esté repositorio tiene licencia MIT*