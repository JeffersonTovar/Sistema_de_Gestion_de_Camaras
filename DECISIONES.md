# DECISIONES TÉCNICAS

## 1. Stack elegido

### Backend
- **FastAPI**
- **SQLAlchemy**
- **MySQL**

**Justificación:**
Se eligió FastAPI por su alto rendimiento, tipado fuerte con Pydantic y facilidad para construir APIs REST robustas con validaciones claras.
SQLAlchemy permite una separación limpia entre modelos y lógica de negocio.
MySQL fue seleccionado por alinearse con el stack mencionado en la prueba tecnica.

---

### Frontend
- **React + Vite**
- **Material UI (MUI)**
- **Axios**
- **React Router**
- **React Query**

**Justificación:**
React es un estándar de la industria para aplicaciones SPA.
Vite permite un entorno rápido de desarrollo.
Material UI acelera la construcción de interfaces limpias y consistentes.
React Query simplifica el manejo de estado asincrónico y caché de datos.

---

### Infraestructura
- **Docker + Docker Compose**

**Justificación:**
Permite ejecutar todo el sistema con un solo comando, asegurando reproducibilidad y facilitando la evaluación.

---

## 2. Desarrollo de la solución

### Arquitectura

Se implementó una arquitectura en capas en el backend:

* Routes → Services → Models → DB

- **Routes:** Manejo de endpoints
- **Services:** Lógica de negocio
- **Models:** Definición ORM
- **Schemas:** Validación de datos (Pydantic)

**Motivación:**
Separar responsabilidades para mantener el código escalable y mantenible.

---

### Frontend

Estructura modular:

pages/
components/
api/


- **pages:** vistas principales
- **components:** componentes reutilizables
- **api:** capa de comunicación con backend

---

## 3. Uso de herramientas de IA

Se utilizó **ChatGPT** como asistente en:

- Generación inicial de estructura del backend
- Definición de validaciones con Pydantic
- Implementación de filtros y paginación
- Estructuración del frontend
- Configuración de Docker

### Ajustes realizados manualmente:

- Corrección de errores en validaciones (422)
- Manejo de errores HTTP personalizados
- Ajuste de relaciones entre modelos
- Corrección de problemas de renderizado en MUI
- Optimización de consultas y filtros
- Control del flujo de estados en tickets

**Conclusión:**
La IA fue utilizada como acelerador, pero se requirió criterio técnico para ajustar y validar la solución.

---

## 4. Decisiones de diseño

### 🔹 Soft Delete
Se implementó `deleted_at` en lugar de eliminación física.

**Ventajas:**
- Permite auditoría
- Evita pérdida de información

---

### 🔹 Flujo de estados en tickets

Se definió una máquina de estados:

* Nuevo → En curso → Resuelto


**Restricciones:**
- No se permite retroceder estados
- Se valida en backend

---

### 🔹 Validaciones fuertes en backend

- Latitud/longitud dentro de Bogotá
- Estados permitidos
- ID único
- Integridad de relaciones

**Motivación:**
Evitar inconsistencias independientemente del frontend.

---

### 🔹 Manejo de errores

Se implementaron errores HTTP claros:

- 404 → recurso no encontrado
- 400 → validaciones de negocio
- 409 → duplicados

Esto mejora la experiencia de usuario y debugging.

---

### 🔹 Dashboard dinámico

Los datos se calculan desde backend:

- KPIs
- Distribuciones
- Métricas

**Motivación:**
Evitar lógica duplicada en frontend.

---

### 🔹 Mapa interactivo

Se utilizó Leaflet por ser:
- Liviano
- Fácil de integrar
- Ideal para geolocalización

---

## 5. Trade-offs

### No implementado (por tiempo)

- Autenticación de usuarios
- Tests automatizados
- Cache avanzado
- WebSockets en tiempo real

---

### Decisiones tomadas

- Priorizar funcionalidad completa sobre UI avanzada
- Implementar validaciones backend antes que optimizaciones
- Usar React Query en lugar de estado global complejo

---

## 6. ¿Qué haría diferente con más tiempo?

- Implementar pruebas unitarias (pytest)
- Agregar autenticación (JWT)
- Optimizar queries con índices en MySQL
- Implementar caching (Redis)
- Mejorar UX/UI (feedback visual, loaders, etc.)
- Agregar tests e2e

---

## 7. Tiempo invertido

| Módulo | Tiempo |
|--------|--------|
| Planeación | 30 min |
| Backend | 3.5 h |
| Frontend | 3 h |
| Docker | 1 h |
| Documentación | 30 min |

---

## 8. Conclusión

Se desarrolló una solución funcional, escalable y alineada con buenas prácticas, priorizando:

- Separación de responsabilidades
- Validaciones robustas
- Facilidad de despliegue
