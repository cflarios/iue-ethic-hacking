# ¿Cómo probarlo?

## Curl

Método POST

curl -X POST -H "Content-Type: application/json" -d '{"ValorA": 5, "ValorB": 3}' http://localhost:5000/api/cristian/larios/suma

Método GET

curl http://localhost:5000/api/cristian/larios/resta\?ValorA\=5\&ValorB\=3