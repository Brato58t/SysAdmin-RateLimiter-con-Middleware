from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Nuestra lógica de Rate Limiter (El "cerebro" que ya construiste)
rate_limiter = {}
WINDOW_SIZE = 60
MAX_REQUESTS = 3 # Bajito para que puedas probar el bloqueo rápido

def es_permitido(ip):
    current_time = time.time()
    if ip not in rate_limiter:
        rate_limiter[ip] = {'count': 1, 'last_reset': current_time}
        return True
    
    user_data = rate_limiter[ip]
    if current_time - user_data['last_reset'] > WINDOW_SIZE:
        user_data['count'] = 1
        user_data['last_reset'] = current_time
        return True
    
    if user_data['count'] < MAX_REQUESTS:
        user_data['count'] += 1
        return True
    
    return False

# Esta es nuestra "Ruta" protegida
@app.route('/')
def home():
    user_ip = request.remote_addr # Obtenemos la IP de quien nos visita
    
    if es_permitido(user_ip):
        return jsonify({"mensaje": "¡Bienvenido, ingeniero! Acceso concedido."}), 200
    else:
        # Aquí es donde ocurre la magia de la seguridad
        return jsonify({"error": "Demasiadas peticiones. ¡Vete a estudiar un poco y vuelve luego!"}), 429

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)