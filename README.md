# 📝 Flask Notes App

Aplicación web sencilla de notas desarrollada con **Flask** y **SQLAlchemy**, pensada como proyecto de aprendizaje y base para futuras mejoras (CRUD, autenticación, despliegue, etc.).

---

## 🚀 Características

- Framework **Flask**
- Motor de plantillas **Jinja2**
- Base de datos **SQLite**
- ORM **SQLAlchemy**
- Estructura básica lista para escalar
- Separación de entornos con **venv**
- Control de versiones con **Git y GitHub**

---

## 🛠️ Tecnologías utilizadas

- Python 3.12+
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML5 / Jinja2

---

## 📂 Estructura del proyecto

```
notes_app/
│
├── app.py
├── requirements.txt
├── notes.sqlite
├── .gitignore
├── templates/
│   ├── home.html
│   └── note_form.html
└── venv/
```

---

## ⚙️ Instalación y ejecución local

### 1️⃣ Clonar el repositorio
```bash
git clone git@github.com:ZapataLuisH/notes_app.git
cd notes_app
```

### 2️⃣ Crear y activar entorno virtual

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / Mac**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

---

### 4️⃣ Ejecutar la aplicación
```bash
flask run
```

La app estará disponible en:
```
http://127.0.0.1:5000
```

---

## 🧪 Endpoints disponibles

| Ruta | Método | Descripción |
|-----|-------|-------------|
| `/` | GET | Página principal |
| `/crear_nota` | GET / POST | Formulario para crear notas |
| `/acerca_de` | GET | Información de la app |
| `/api/info` | GET | API con datos de la app |

---

## 📌 Estado del proyecto

🚧 En desarrollo  

Próximas mejoras:
- CRUD completo de notas
- Persistencia real en base de datos
- Autenticación de usuarios
- Despliegue en la nube

---

## 👨‍💻 Autor

**Luis Zapata**  
Ingeniero de Telecomunicaciones | Desarrollador de Software  
GitHub: https://github.com/ZapataLuisH

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT.
