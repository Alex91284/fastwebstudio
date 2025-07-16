# 🚀 FastWebStudio Backend

FastWebStudio es un generador de sitios web dinámicos, desarrollado con **FastAPI**. Este backend gestiona usuarios, proyectos, páginas, componentes, plantillas, autenticación y más, usando una arquitectura limpia y escalable.

La plataforma backend construida con **FastAPI**, pensada para permitir a los usuarios crear sitios web dinámicamente usando proyectos, páginas, plantillas, componentes y más.

---

## 📦 Estructura del Proyecto

```
app/
├── core/          # Configuración global y .env
├── crud/          # Lógica de base de datos
├── db/            # Conexión y sesión de la base de datos
├── models/        # Modelos SQLAlchemy
├── routes/        # Endpoints del API
├── schemas/       # Esquemas Pydantic
└── main.py        # Punto de entrada de la app

```

# 🚀 Instalación y uso local
1. Clona el repositorio

git clone https://github.com/tu-usuario/fastwebstudio.git
cd fastwebstudio/backend

2. Crea y activa un entorno virtual

python3 -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows

3. Instala dependencias

pip install -r requirements.txt

4. Configura tus variables de entorno
Crea un archivo .env basado en .env.example:

cp .env.example .env

5. Levanta el servidor

uvicorn app.main:app --reload
Abre en navegador: http://localhost:8000/docs

# 🔐 Autenticación
Usamos JWT para proteger las rutas. Para probar:

Crea un usuario vía POST /users/

Inicia sesión vía POST /auth/login

Copia el token y úsalo como Bearer Token para acceder a rutas protegidas (/users/me, etc.)

🧪 Pruebas
A través de Swagger UI:

bash
Copiar código
http://localhost:8000/docs

# 📘 Documentación API
FastAPI genera documentación automáticamente en:

Swagger UI: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

# 🧾Licencia
Este proyecto está bajo la licencia MIT.

# 🤝 Autor
Desarrollado por Alex Bolaños Muñoz 
