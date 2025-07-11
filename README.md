🎾🏀 Analítica de Apuestas Deportivas: Extracción y Estructuración de Datos con Python 📊
Este proyecto presenta una solución integral para la extracción, procesamiento y estructuración de datos de diversas casas de apuestas online en los deportes de tenis y baloncesto. Desarrollado íntegramente en Python, su objetivo principal es recopilar información crucial para su posterior análisis, permitiendo la identificación de tendencias, patrones y oportunidades. Lo más destacado es que esta extracción se realiza de forma automática y recurrente cada 30 segundos, asegurando que los datos para el análisis estén siempre actualizados y reflejen las cuotas más recientes del mercado.

La arquitectura del sistema se basa en principios sólidos de la Programación Orientada a Objetos (POO) y el patrón Modelo-Vista-Controlador (MVC), garantizando una base de código modular, escalable y de fácil mantenimiento. El corazón del proceso reside en el Web Scraping, utilizando librerías de Python para navegar y extraer datos de las plataformas de apuestas. Una vez obtenidos, los datos se someten a un proceso de descomposición de objetos JSON, transformando la información cruda en un formato estructurado y manejable. Es importante destacar que todos los datos extraídos se guardan de forma persistente en una base de datos SQLite3, proporcionando un almacenamiento eficiente y accesible para el análisis posterior.

El diseño bajo POO se evidencia en clases clave que gestionan la información esencial:

📈 apuesta.py: Este programa funcional maneja la lógica central de las apuestas, incluyendo la extracción de datos de cuotas y eventos.

⏳ apuesta_tiempo.py: Se encarga de la gestión de apuestas basadas en el tiempo o de eventos en vivo, un aspecto crítico para los datos dinámicos.

🏷️ categoria.py: Este módulo clasifica y organiza la información extraída, asegurando que los datos de diferentes deportes o tipos de apuesta se manejen correctamente.

🔗 conexion.py: Gestiona la conectividad y la interacción con las fuentes de datos, siendo el punto de enlace para el web scraping y la gestión de la base de datos SQLite3.

El resultado es un conjunto de datos limpios y organizados, almacenados de forma robusta, listos para ser alimentados a herramientas de análisis estadístico o de Machine Learning, brindando una base sólida para la toma de decisiones informadas en el ámbito de las apuestas deportivas.
