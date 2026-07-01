# SysAdmin-RateLimiter-con-Middleware
este repositorio presenta el antiguo sistema de RateLimiter con una nueva implementación de Middleware.

Esta implementación utiliza un patrón de diseño Middleware para interceptar las peticiones HTTP antes de llegar a la lógica de negocio. Esto desacopla la capa de seguridad (Rate Limiter) de la capa de aplicación, permitiendo una arquitectura escalable y de baja latencia.