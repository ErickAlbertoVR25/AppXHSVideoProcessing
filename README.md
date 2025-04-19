# XHS Video Processor
Microservicio Flask que:

1. Busca el video más reciente en la carpeta de descarga de su preferencia
2. Renombra el archivo según la nomeclatura que usted le asigne.
3. Convierte cualquier formato a ".mp4" y remueve el audio.
4. Elimina el archivo original al finalizar.

# Parametros basicos del archivo
- download_folder: Carpeta local en la que el script buscará el video descargado y donde guardará el resultado. Puedes cambiarla para apuntar a cualquier otro directorio de tu sistema. Por defecto esta preestablecida en
` download_folder = r"C:\Users\erick\XHS-Downloader\Download" `
- new_filename: Construcción del nombre de salida. Patrón de nomenclatura para el archivo procesado. Puedes modificar el string para cambiar prefijo, sufijo, formato, etc, pero no cambies la variable "video_id". Por defecto, este parametro es
` new_filename = f"XiaoHongShuVideo({video_id}).mp4" `

# Parámetros para usuarios avanzados (recomendamos no modificarlos si la aplicación funciona adecuadamente)
- video_id: Campo del JSON de entrada. Identificador único del video (campo “作品ID”) que el usuario debe enviar en el payload. Se utiliza para generar el nombre final del archivo. este parametro esta establecido en:
`video_id = data.get('video_id')`
- Host y puerto de Flask
host: IP o nombre de interfaz donde Flask escucha (0.0.0.0 para todas)
port: puerto TCP (cámbialo si ya tienes otro servicio en el 5000)
debug: activa el modo debug (log detallado y auto‑reload). Puedes poner "False" en producción
Estos parametros estan establecidos en
`app.run(host='0.0.0.0', port=5000, debug=True)`