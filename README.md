# SysAdmin-RateLimiter-con-Middleware
este repositorio presenta el antiguo sistema de RateLimiter con una nueva implementación de Middleware.
___
Esta implementación utiliza un patrón de diseño Middleware para interceptar las peticiones HTTP antes de llegar a la lógica de negocio. Esto desacopla la capa de seguridad (Rate Limiter) de la capa de aplicación, permitiendo una arquitectura escalable y de baja latencia.
___
# GuardianRate: Sistema de Rate Limiting

## Descripción
Sistema de limitación de tasa (Rate Limiter) diseñado para proteger servicios web contra ataques de saturación. Actúa como middleware de seguridad interceptando el tráfico.

## Arquitectura
- Estructura de Datos: HashMap (diccionario Python) para acceso O(1).
- Patrón: Middleware desacoplado de la lógica de negocio.
- Estándar: Cumplimiento de código HTTP 429 (Too Many Requests).

## Tecnologías
- Python 3.x
- Flask

## Demostración
[👉 Ver video de demostración aquí]https://youtu.be/sCBahPqp8CA?si=ZuofkMNEJ9GA2YOJ

## Instalación
1. git clone https://github.com/tu-usuario/nombre-del-repo.git
2. pip install flask
3. python servidor.py

## Roadmap
- [x] Implementación de HashMap
- [x] Middleware Flask
- [ ] Persistencia con Redis
- [ ] Auth Bearer Tokens

---
Desarrollado para el Laboratorio de Arquitectura de Sistemas.
Licencia: MIT