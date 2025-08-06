document.getElementById('sendButton').addEventListener('click', sendMessage);
document.getElementById('userInput').addEventListener('keypress', function(event) {
  if (event.key === 'Enter') {
    sendMessage();
  }
});

async function sendMessage() {
  const userInput = document.getElementById('userInput');
  const chatContainer = document.getElementById('chat');
  const userMessage = userInput.value.trim();

  if (userMessage === '') return;

  // Add user message to chat
  const userMessageElement = document.createElement('div');
  userMessageElement.classList.add('message', 'user');
  userMessageElement.textContent = userMessage;
  chatContainer.appendChild(userMessageElement);
  userInput.value = '';

  // Placeholder bot message
  const botMessageElement = document.createElement('div');
  botMessageElement.classList.add('message', 'bot');
  botMessageElement.textContent = '⏳ Typing...';
  chatContainer.appendChild(botMessageElement);
  chatContainer.scrollTop = chatContainer.scrollHeight;

  try {
    const response = await fetch('http://localhost:5000/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ prompt: userMessage })
    });

    // Check if server returned a successful response
    if (!response.ok) {
      throw new Error(`Server responded with status ${response.status}`);
    }

    const data = await response.json();
    botMessageElement.textContent = data.response || "⚠️ No response from bot.";
  } catch (error) {
    console.error("Error talking to backend:", error);
    botMessageElement.textContent = "❌ Failed to fetch response from server.";
  }

  chatContainer.scrollTop = chatContainer.scrollHeight;
}