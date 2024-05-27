import requests # type: ignore

# URL de la API Rest
base_url = "http://api-rest-productos.onrender.com"

# Función para realizar una solicitud GET
def get_products():
    response = requests.get(f"{base_url}/productos")
    if response.status_code == 200:
        products = response.json()
        print("Productos obtenidos:")
        for product in products:
            print(product)
    else:
        print(f"Error al obtener productos: {response.status_code}")

# Función para realizar una solicitud POST
def create_product(name, price, stock):
    product_data = {
        "nombre": name,
        "precio": price,
        "stock": stock
    }
    response = requests.post(f"{base_url}/productos", json=product_data)
    if response.status_code == 201:
        print("Producto creado exitosamente:")
        print(response.json())
    else:
        print(f"Error al crear producto: {response.status_code}")

if __name__ == "__main__":
    # Espera de 30 segundos para asegurar que la API esté activa
    import time
    time.sleep(30)

    # Realizar una solicitud GET para obtener productos
    get_products()

    # Realizar una solicitud POST para crear un nuevo producto
    create_product("Producto de prueba", 123.45, 10)
