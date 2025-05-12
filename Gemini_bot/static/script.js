document.getElementById('chat-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const userMessage = document.getElementById('message').value;
    const chatHistory = document.getElementById('chat-history');

    // Add user message to chat history
    const userEntry = document.createElement('div');
    userEntry.className = 'chat-message user';
    userEntry.innerHTML = `<strong>You:</strong> ${userMessage}`;
    chatHistory.appendChild(userEntry);

    fetch('/get_response', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMessage })
    })
    .then(response => response.json())
    .then(data => {
        const botEntry = document.createElement('div');
        botEntry.className = 'chat-message bot';
        botEntry.innerHTML = `<strong>Bot:</strong> ${data.reply}`;
        chatHistory.appendChild(botEntry);

        // Scroll to bottom
        chatHistory.scrollTop = chatHistory.scrollHeight;
    })
    .catch(error => {
        console.error('Error:', error);
    });

    // Clear input field
    document.getElementById('message').value = '';
});
