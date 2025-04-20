import json

# Nota: corrijamos primero tu JSON (faltaban algunas llaves y corchetes):
json_string = """
{
  "customerId": "c12345",
  "orderDate": "2025-04-19T14:30:00Z",
  "items": [
    {
      "productId": "p987",
      "quantity": 2
    },
    {
      "productId": "p654",
      "quantity": 1
    }
  ]
}
"""

# Parsear la cadena a un dict de Python
data = json.loads(json_string)

# Acceder a valores
print("Customer ID:", data["customerId"])
print("Order Date:", data["orderDate"])

# Recorrer los ítems
for item in data["items"]:
    print(f"- Producto {item['productId']}, cantidad {item['quantity']}")
