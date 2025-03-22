document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');

    chatForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const message = userInput.value.trim();
        if (!message) return;

        // Add user message to chat
        appendMessage('user', message);
        userInput.value = '';

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();
            
            if (data.error) {
                throw new Error(data.error);
            }

            // Handle the response based on whether it's code or regular text
            appendMessage('assistant', data.response, data.isCode);

        } catch (error) {
            appendMessage('error', 'Error: ' + error.message);
        }
    });

    function appendMessage(role, content, isCode = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}-message`;

        if (isCode) {
            // Create a pre and code element for code formatting
            const pre = document.createElement('pre');
            const code = document.createElement('code');
            code.className = 'python'; // Add syntax highlighting class
            code.textContent = content;
            pre.appendChild(code);
            messageDiv.appendChild(pre);
        } else {
            // Regular text message
            messageDiv.textContent = content;
        }

        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});