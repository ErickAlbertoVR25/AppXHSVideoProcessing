from flask import Flask, request, jsonify
import os
import glob
from moviepy import VideoFileClip

app = Flask(__name__)

@app.route('/process-video', methods=['POST'])
def process_video():
    """
    Procesa el video descargado realizando los siguientes pasos:
      1. Se recibe un JSON con el campo 'video_id' (作品ID).
      2. Se busca en la carpeta de descarga el archivo más reciente.
      3. Se convierte el video al formato .mp4, se remueve el audio y se le asigna el nombre:
         'XiaoHongShuVideo(作品ID).mp4'.
      4. Se elimina el archivo original.
      
    Retorna en JSON la ruta del archivo procesado.
    """
    data = request.get_json()
    video_id = data.get('video_id')
    
    if not video_id:
        return jsonify({"error": "El campo 'video_id' es obligatorio."}), 400

    # Carpeta donde se descargan los videos
    download_folder = r"C:\Users\erick\XHS-Downloader\Download"
    
    # Define el nombre de archivo estandarizado
    new_filename = f"XiaoHongShuVideo({video_id}).mp4"
    new_filepath = os.path.join(download_folder, new_filename)
    
    # Busca todos los archivos en la carpeta
    files = glob.glob(os.path.join(download_folder, "*"))
    if not files:
        return jsonify({"error": "No se encontró ningún archivo en la carpeta de descarga."}), 404

    # Se asume que el archivo recién descargado es el de fecha de creación más reciente.
    latest_file = max(files, key=os.path.getctime)
    
    try:
        # Carga el video sin importar su formato original
        clip = VideoFileClip(latest_file)
        # Crea una versión del clip sin audio
        clip_no_audio = clip.without_audio()
        # Convierte y escribe el archivo sin audio, forzando el formato mp4 con los codecs indicados
        clip_no_audio.write_videofile(new_filepath, codec='libx264', audio_codec='aac')
        # Cerramos ambos clips para liberar recursos
        clip_no_audio.close()
        clip.close()
        # Eliminamos el archivo original
        os.remove(latest_file)
    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

    return jsonify({"output_path": new_filepath}), 200

if __name__ == '__main__':
    # Ejecuta el servidor en todas las interfaces en el puerto 5000
    app.run(host='0.0.0.0', port=5000, debug=True)