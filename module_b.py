"""
Módulo B - Ejemplo de logging con diferentes niveles
"""
import logging

logger = logging.getLogger(__name__)


def hello_world_b():
    """
    Función principal del módulo B que ejecuta operaciones con logging
    """
    logger.debug("DEBUG: Iniciando función hello_world_b()")
    logger.info("INFO: Módulo B está ejecutándose")
    
    print("=" * 50)
    print("Hello World desde el Módulo B!")
    print("=" * 50)
    
    logger.info("INFO: Procesando datos del módulo B...")
    logger.warning("WARNING: Este es un mensaje de advertencia del módulo B")
    logger.debug("DEBUG: Detalles de depuración del módulo B")
    
    # Simulando alguna operación
    resultado = realizar_operacion_b()
    
    logger.info(f"INFO: Operación completada con resultado: {resultado}")
    logger.debug("DEBUG: Finalizando función hello_world_b()")
    
    return resultado


def realizar_operacion_b():
    """
    Función auxiliar que simula una operación
    """
    logger.debug("DEBUG: Ejecutando operación auxiliar en módulo B")
    logger.info("INFO: Calculando resultado en módulo B...")
    
    try:
        resultado = "Módulo B procesado correctamente"
        logger.debug(f"DEBUG: Resultado generado: {resultado}")
        logger.info("INFO: Operación exitosa en módulo B")
        return resultado
    except Exception as e:
        logger.error(f"ERROR: Ocurrió un error en módulo B: {e}")
        logger.critical(f"CRITICAL: Error crítico en módulo B: {e}")
        raise


if __name__ == "__main__":
    # Configuración básica para pruebas
    logging.basicConfig(level=logging.DEBUG)
    hello_world_b()
