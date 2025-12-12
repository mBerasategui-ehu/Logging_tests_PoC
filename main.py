"""
Script principal para ejecutar los módulos A y B con logging configurable
"""
import os
import sys
import logging
from dotenv import load_dotenv
import module_a
import module_b

# Cargar variables de entorno
load_dotenv()

# Configurar logging básico
logging.basicConfig(
    stream=sys.stdout,
    level=os.getenv("GLOBAL_LOG_LEVEL", "INFO"),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    force=True
)

# Configurar niveles por módulo
logging.getLogger("module_a").setLevel(os.getenv("MODULE_A_LOG_LEVEL", "INFO"))
logging.getLogger("module_b").setLevel(os.getenv("MODULE_B_LOG_LEVEL", "INFO"))


def main():
    """Ejecuta los módulos A y B"""
    print("\n" + "="*50)
    print("PRUEBA DE LOGGING")
    print("="*50 + "\n")
    
    # Ejecutar módulos
    module_a.hello_world_a()
    print()
    module_b.hello_world_b()
    
    print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    main()
