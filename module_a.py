"""
Módulo A - Ejemplo de logging con diferentes niveles
"""
import logging

logger = logging.getLogger(__name__)


def hello_world_a():
    """
    Función principal del módulo A que ejecuta operaciones con logging
    """
    logger.debug("DEBUG: Iniciando función hello_world_a()")
    logger.info("INFO: Módulo A está ejecutándose")
    
    print("=" * 50)
    print("Hello World desde el Módulo A!")
    print("=" * 50)
    
    logger.info("INFO: Procesando datos del módulo A...")
    logger.warning("WARNING: Este es un mensaje de advertencia del módulo A")
    logger.debug("DEBUG: Detalles de depuración del módulo A")
    
    # Simulando alguna operación
    resultado = realizar_operacion_a()
    
    logger.info(f"INFO: Operación completada con resultado: {resultado}")
    logger.debug("DEBUG: Finalizando función hello_world_a()")
    
    return resultado


def realizar_operacion_a():
    """
    Función auxiliar que simula una operación
    """
    logger.debug("DEBUG: Ejecutando operación auxiliar en módulo A")
    logger.info("INFO: Calculando resultado en módulo A...")
    
    try:
        resultado = sum([1, 2, 3, 4, 5])
        logger.debug(f"DEBUG: Suma calculada: {resultado}")
        logger.info("INFO: Operación exitosa en módulo A")
        return resultado
    except Exception as e:
        logger.error(f"ERROR: Ocurrió un error en módulo A: {e}")
        logger.critical(f"CRITICAL: Error crítico en módulo A: {e}")
        raise


if __name__ == "__main__":
    # Configuración básica para pruebas
    logging.basicConfig(level=logging.DEBUG)
    hello_world_a()
