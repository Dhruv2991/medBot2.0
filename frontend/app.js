function addMessage(sender, text, isEmergency = false) {
    const chatbox = document.getElementById("chatbox");
    
    // Determine if it is the user or the bot for styling classes
    const isUser = sender === "You";
    const alignClass = isUser ? "user" : "bot";
    const emergencyClass = isEmergency ? "emergency" : "";

    // Create the HTML structure for the message
    const messageHTML = `
        <div class="message ${alignClass} ${emergencyClass}">
            <div class="sender-name">${sender}</div>
            <div class="bubble">${text.replace(/\n/g, '<br>')}</div>
        </div>
    `;

    chatbox.insertAdjacentHTML('beforeend', messageHTML);
    chatbox.scrollTop = chatbox.scrollHeight;
}

function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();

    if (!message) return;

    addMessage("You", message);
    input.value = ""; // Clear input immediately for better UX

    // Visual loading state could be added here
    
    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    })
    .then(res => res.json())
    .then(data => {
        const reply =
            `<strong>${data.response}</strong><br><br>` +
            `<small>Risk Level: ${data.risk} (Confidence: ${data.confidence}%)</small>`;

        addMessage("medBot", reply, data.emergency);

        if (data.emergency) {
            // Optional: Add a sound effect here
            alert("⚠️ EMERGENCY DETECTED!\nPlease seek immediate medical help.");
        }
    })
    .catch(err => {
        addMessage("medBot", "Sorry, I'm having trouble connecting to the server.");
        console.error(err);
    });
}

// Voice input
function startVoice() {
    if (!('webkitSpeechRecognition' in window)) {
        alert("Voice recognition is not supported in this browser.");
        return;
    }

    const recognition = new webkitSpeechRecognition();
    const voiceBtn = document.querySelector('.voice-btn');
    
    recognition.lang = "en-IN";
    
    // Visual feedback for listening
    recognition.onstart = () => {
        voiceBtn.classList.add('voice-active');
    };

    recognition.onend = () => {
        voiceBtn.classList.remove('voice-active');
    };

    recognition.onresult = (event) => {
        document.getElementById("userInput").value =
            event.results[0][0].transcript;
    };
    
    recognition.start();
}