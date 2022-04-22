'use strict';

const express = require('express');

const PORT = 8080;
const HOST = '0.0.0.0';

const app = express();
app.get('/', (req, res) => {
  res.send('Supa easy Hello World!');
});

app.get('/foo', (req, res) => {
  res.send('See your foo and respond with bar!');
});

app.get('/bar', (req, res) => {
  res.send('See your bar and respond with foo!');
});

app.listen(PORT, HOST, () => {
  console.log(`Running on http://${HOST}:${PORT}`);
});
