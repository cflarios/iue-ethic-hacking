const express = require('express');
const app = express();
const port = 3000;

// Middleware para parsear JSON en las solicitudes
app.use(express.json());

// Datos de ejemplo (simulación de una base de datos)
let data = [];

// Ruta para obtener data los elementos
app.get('/data', (req, res) => {
  res.json(data);
});

// Ruta para agregar un elemento
app.post('/data', (req, res) => {
  const newTodo = req.body;
  data.push(newTodo);
  res.status(201).json(newTodo);
});

// Ruta para eliminar un elemento por su índice
app.delete('/data/:index', (req, res) => {
  const index = req.params.index;
  if (index >= 0 && index < data.length) {
    data.splice(index, 1);
    res.status(204).send();
  } else {
    res.status(404).json({ message: 'Índice no válido' });
  }
});

// Iniciar el servidor
app.listen(port, () => {
  console.log(`Servidor en funcionamiento en http://localhost:${port}/data`);
});
