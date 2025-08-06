const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const axios = require('axios');

const app = express();
const PORT = 5000;

app.use(cors());
app.use(bodyParser.json());

// Chat endpoint
app.post('/chat', async (req, res) => {
  const userPrompt = req.body.prompt;

  try {
    const ollamaResponse = await axios.post('http://localhost:11434/api/generate', {
      model: "mistral", // or your model like llama3
      prompt: userPrompt,
      stream: false
    });

    const responseText = ollamaResponse.data.response;
    res.json({ response: responseText });
  } catch (error) {
    console.error('❌ Error communicating with Ollama:', error.message);
    res.status(500).json({ error: 'Failed to connect to AI model.' });
  }
});

app.listen(PORT, () => {
  console.log(`🚀 Server running at http://localhost:${PORT}`);
});