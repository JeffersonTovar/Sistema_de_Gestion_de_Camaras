# Sistema de Gestión de Cámaras - Grupo Verytel

Aplicación full-stack para la gestión de cámaras de videovigilancia y tickets de mantenimiento en Bogotá.

## Tecnologías utilizadas

### Backend
- FastAPI
- SQLAlchemy
- MySQL
- Pydantic (validaciones)
- Docker

### Frontend
- React + Vite
- Material UI (MUI)
- Axios
- React Router
- React Query

### Infraestructura
- Docker
- Docker Compose

---

## Requisitos

- Docker
- Docker Compose

## Instalación
Clonar el repositorio:

```bash
git clone git@github.com:JeffersonTovar/Sistema_de_Gestion_de_Camaras.git
cd Sistema_de_Gestion_de_Camaras.git
```

---

## Ejecución del proyecto

```bash
docker-compose up --build
```

## Accesos

* Servicio	URL
* Frontend	http://localhost:5173
* Backend API	http://localhost:8000
* Docs API	http://localhost:8000/docs


## Funcionalidades implementadas

### CRUD de Cámaras
* Listado paginado
* Búsqueda por texto (ID, modelo, ubicación)
* Filtros por:
  * Estado (Activa, Inactiva, En Mantenimiento)
  * Localidad
* Creación con validaciones:
  * ID único
  * Latitud y longitud dentro de Bogotá
* Edición (ID no editable)
* Eliminación lógica (soft delete)
* Vista de detalle con tickets asociados


## CRUD de Tickets

* Listado paginado
* Filtros por:
  * Estado
  * Tipo
  * Prioridad
  * Rango de fechas
* Creación:
  * Estado inicial automático: Nuevo
  * Fecha de apertura automática
* Flujo de estados controlado:
  * Nuevo → En curso → Resuelto
  * No permite retrocesos
* Al resolver:
  * Se asigna fecha de cierre automáticamente
* Validación de cámara existente

## Dashboard

* KPI Cards:
  * Total cámaras activas
  * Tickets abiertos
  * Tiempo promedio de resolución
  * % tickets críticos/altos
* Gráfica de dona:
  * Distribución de cámaras por estado
* Gráfica de barras:
  * Tickets por prioridad

## Mapa interactivo

* Implementado con Leaflet
* Marcadores geolocalizados
* Colores por estado:
  * 🟢 Activa
  * 🟠 En mantenimiento
  * 🔴 Inactiva
* Popup con:
  * ID
  * Modelo
  * Ubicación
  * Estado
  * Tickets abiertos

## Estructura del proyecto

```bash
backend/
  app/
    api/
    models/
    schemas/
    services/
    db/

frontend/
  src/
    api/
    components/
    pages/
```

## Consideraciones

* Se implementó soft delete en cámaras y tickets
* El sistema evita mostrar registros eliminados
* Manejo de errores detallado (ej: duplicados, validaciones)
