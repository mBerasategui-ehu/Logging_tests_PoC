# Logging Tests PoC

Proyecto de prueba de concepto para testing de logging en Python con múltiples módulos y configuración mediante variables de entorno.

## 📋 Descripción

Este proyecto simula dos módulos independientes (A y B) con diferentes niveles de logging que pueden ser configurados dinámicamente mediante variables de entorno. Es útil para aprender y probar diferentes configuraciones de logging sin modificar código.

## 📁 Estructura del Proyecto

```
Logging_tests_PoC/
├── main.py              # Script principal con configuración de logging
├── module_a.py          # Módulo A con operaciones de ejemplo
├── module_b.py          # Módulo B con operaciones de ejemplo
├── .env                 # Variables de entorno (configuración)
├── requirements.txt     # Dependencias Python
└── README.md            # Este archivo
```

## 🚀 Instalación

1. **Clonar o descargar el proyecto**

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuración

La configuración se realiza mediante el archivo `.env`. Existen dos tipos de configuración:

### 1. Nivel Global
Define el nivel de logging por defecto para todos los módulos:
```env
GLOBAL_LOG_LEVEL=INFO
```

### 2. Niveles por Módulo
Puedes configurar cada módulo de forma independiente:
```env
MODULE_A_LOG_LEVEL=DEBUG
MODULE_B_LOG_LEVEL=ERROR
```

### Niveles de Logging Disponibles

| Nivel | Descripción |
|-------|-------------|
| `DEBUG` | Información detallada para diagnóstico |
| `INFO` | Confirmación de que las cosas funcionan como se espera |
| `WARNING` | Indicación de algo inesperado o un problema futuro |
| `ERROR` | Error más serio, el software no ha podido realizar una función |
| `CRITICAL` | Error muy grave, el programa puede no continuar ejecutándose |

## 📝 Ejemplos de Uso

### Ejemplo 1: Ambos módulos en DEBUG
Edita el archivo `.env`:
```env
GLOBAL_LOG_LEVEL=DEBUG
MODULE_A_LOG_LEVEL=DEBUG
MODULE_B_LOG_LEVEL=DEBUG
```

Ejecuta:
```bash
python main.py
```

### Ejemplo 2: Solo módulo A activo con INFO
```env
GLOBAL_LOG_LEVEL=CRITICAL
MODULE_A_LOG_LEVEL=INFO
MODULE_B_LOG_LEVEL=CRITICAL
```

### Ejemplo 3: A en DEBUG, B en ERROR
```env
GLOBAL_LOG_LEVEL=INFO
MODULE_A_LOG_LEVEL=DEBUG
MODULE_B_LOG_LEVEL=ERROR
```

### Ejemplo 4: Usar solo el nivel global
```env
GLOBAL_LOG_LEVEL=WARNING
# No definir MODULE_A_LOG_LEVEL ni MODULE_B_LOG_LEVEL
```



## 🎯 Características

- ✅ Configuración simple mediante variables de entorno
- ✅ Nivel global y niveles específicos por módulo
- ✅ Salida formateada con timestamp y nivel
- ✅ Solo ~25 líneas de configuración
- ✅ Sin dependencias circulares

## 🔍 Cómo Funciona

Es muy simple:

1. [main.py](main.py) carga el archivo `.env` con `python-dotenv`
2. Configura el nivel global con `logging.basicConfig()`
3. Configura cada módulo con `logging.getLogger().setLevel()`
4. Los módulos usan `logging.getLogger(__name__)` normalmente

## 📚 Recursos Adicionales

- [Documentación oficial de logging en Python](https://docs.python.org/3/library/logging.html)
- [Logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
