# 🚀 API de Recursos Humanos (Backend)

Este es el backend de un sistema de gestión de Recursos Humanos, construido como una API RESTful. Proporciona los endpoints necesarios para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los registros de empleados.

Actualmente, esta API está conectada a una base de datos en la nube y se encuentra desplegada en producción.

## 🛠️ Tecnologías Utilizadas

* **Framework:** Django & Django REST Framework (DRF)
* **Base de Datos:** MySQL (Alojada en Aiven Cloud)
* **Servidor Web (Producción):** Gunicorn
* **Gestión de Archivos Estáticos:** WhiteNoise
* **Despliegue:** Render

## 🌍 URL Base (Producción)

La API está viva y accesible en:
`https://backend-rh-django.onrender.com`

## 📖 Endpoints Principales

Todos los endpoints tienen el prefijo `/api/`. 

| Método | Endpoint | Descripción |
| :--- | :--- | :--- |
| `GET` | `/api/empleados/` | Obtiene la lista de todos los empleados. |
| `POST` | `/api/empleados/` | Crea un nuevo registro de empleado. |
| `GET` | `/api/empleados/<id>/` | Obtiene los detalles de un empleado específico. |
| `PUT` | `/api/empleados/<id>/` | Actualiza todos los datos de un empleado. |
| `DELETE` | `/api/empleados/<id>/` | Elimina un empleado de la base de datos. |

## 💻 Instalación y Uso Local

Si deseas correr este proyecto en tu propia máquina para desarrollo, sigue estos pasos:

**1. Clonar el repositorio**
```bash
git clone https://github.com/Valduz-Jose/Backend-RH-Django.git
cd rh_django
```

**2. Crear y activar un entorno virtual**

```Bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
```

**3. Instalar las dependencias**

```Bash
pip install -r requirements.txt
```

**4. Configurar las Variables de Entorno**

Crea un archivo .env en la raíz del proyecto (al mismo nivel que manage.py) y agrega las siguientes variables. (Nota: Deberás proveer tu propia URL de base de datos MySQL para desarrollo local o usar la de producción si tienes los permisos).

```Bash
DEBUG=True
SECRET_KEY=tu_clave_secreta_aqui
DATABASE_URL=mysql://usuario:password@host:puerto/nombre_db
```

**5. Aplicar migraciones**

```Bash
python manage.py migrate
```

**6. Correr el servidor local**

```Bash
python manage.py runserver
```

**👨‍💻 Autor**
Jose Alejandro Valduz Contreras- Desarrollador Fullstack
