const input = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const chatBox = document.getElementById("chat-box");


// ==========================================
// CONVERSATION HISTORY
// ==========================================

let conversationHistory = [];


// ==========================================
// ADD MESSAGE TO CHAT
// ==========================================

function addMessage(message, sender) {

    const messageDiv = document.createElement("div");

    messageDiv.classList.add("message");

    if (sender === "user") {

        messageDiv.classList.add("user-message");

        messageDiv.innerHTML = `
            <strong>You</strong>
            <p>${escapeHTML(message)}</p>
        `;

    } else {

        messageDiv.classList.add("bot-message");

        messageDiv.innerHTML = `
            <strong>TrustCare AI</strong>
            <p>${escapeHTML(message)}</p>
        `;
    }

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}


// ==========================================
// ESCAPE HTML
// ==========================================

function escapeHTML(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}


// ==========================================
// SHOW CUSTOMER ANALYSIS
// ==========================================

function showAnalysis(
    frustration,
    knowledge,
    trust
) {

    const analysisDiv =
        document.createElement("div");

    analysisDiv.classList.add(
        "analysis-box"
    );


    // ======================================
    // FRUSTRATION REASONS
    // ======================================

    let reasonsHTML = "";

    if (
        frustration &&
        frustration.reasons &&
        frustration.reasons.length > 0
    ) {

        reasonsHTML =
            frustration.reasons
                .map(
                    reason =>
                        `<li>${escapeHTML(reason)}</li>`
                )
                .join("");

    } else {

        reasonsHTML =
            "<li>No strong frustration indicators detected</li>";
    }


    // ======================================
    // TRUST INFORMATION
    // ======================================

    let trustHTML = "";

    if (trust) {

        trustHTML = `
            <p>
                <b>Trust Score:</b>
                ${trust.trust_score}
            </p>

            <p>
                <b>Trust Level:</b>
                ${escapeHTML(trust.trust_level || "UNKNOWN")}
            </p>
        `;

    } else {

        trustHTML = `
            <p>
                <b>Trust Score:</b>
                Not available
            </p>

            <p>
                <b>Trust Level:</b>
                Not available
            </p>
        `;
    }


    // ======================================
    // ANALYSIS BOX
    // ======================================

    analysisDiv.innerHTML = `

        <strong>Customer Analysis</strong>

        <p>
            <b>Frustration Score:</b>
            ${frustration.frustration_score}
        </p>

        <p>
            <b>Frustration Level:</b>
            ${escapeHTML(frustration.level || "UNKNOWN")}
        </p>

        ${trustHTML}

        <p>
            <b>Category:</b>
            ${escapeHTML(knowledge.category || "Unknown")}
        </p>

        <p>
            <b>Knowledge Confidence:</b>
            ${knowledge.confidence || 0}
        </p>

        <p>
            <b>Frustration Reasons:</b>
        </p>

        <ul>
            ${reasonsHTML}
        </ul>

    `;


    chatBox.appendChild(
        analysisDiv
    );

    chatBox.scrollTop =
        chatBox.scrollHeight;
}


// ==========================================
// SHOW ESCALATION
// ==========================================

function showEscalation(trust) {

    if (
        trust &&
        trust.escalation_required === true
    ) {

        const escalationDiv =
            document.createElement("div");

        escalationDiv.classList.add(
            "escalation-box"
        );

        escalationDiv.innerHTML = `

            <strong>
                🚨 Human Support Recommended
            </strong>

            <p>
                ${escapeHTML(
                    trust.escalation_reason ||
                    "Human support is recommended."
                )}
            </p>

            <p>
                A human support representative
                should assist with this conversation.
            </p>

        `;

        chatBox.appendChild(
            escalationDiv
        );

        chatBox.scrollTop =
            chatBox.scrollHeight;
    }
}


// ==========================================
// SAVE CONVERSATION
// ==========================================

function saveConversation() {

    localStorage.setItem(
        "trustcare_conversation",
        JSON.stringify(
            conversationHistory
        )
    );
}


// ==========================================
// LOAD CONVERSATION
// ==========================================

function loadConversation() {

    const savedConversation =
        localStorage.getItem(
            "trustcare_conversation"
        );


    if (!savedConversation) {

        return;
    }


    try {

        conversationHistory =
            JSON.parse(
                savedConversation
            );


        conversationHistory.forEach(
            message => {

                addMessage(
                    message.text,
                    message.sender
                );

            }
        );

    }
    catch (error) {

        console.error(
            "Could not load conversation:",
            error
        );

        conversationHistory = [];
    }
}


// ==========================================
// ADD TO CONVERSATION HISTORY
// ==========================================

function addToHistory(
    text,
    sender
) {

    conversationHistory.push({

        text: text,

        sender: sender,

        time: new Date().toISOString()

    });


    saveConversation();
}


// ==========================================
// CLEAR CONVERSATION
// ==========================================

function clearConversation() {

    const confirmed =
        confirm(
            "Are you sure you want to clear this conversation?"
        );


    if (!confirmed) {

        return;
    }


    conversationHistory = [];


    localStorage.removeItem(
        "trustcare_conversation"
    );


    chatBox.innerHTML = "";


    addMessage(
        "Hello! How can I help you today?",
        "bot"
    );
}


// ==========================================
// SEND CUSTOMER MESSAGE
// ==========================================

async function sendMessage() {

    const message =
        input.value.trim();


    // ======================================
    // CHECK EMPTY MESSAGE
    // ======================================

    if (message === "") {

        return;
    }


    // ======================================
    // DISABLE BUTTON
    // ======================================

    sendButton.disabled = true;


    // ======================================
    // SHOW CUSTOMER MESSAGE
    // ======================================

    addMessage(
        message,
        "user"
    );


    addToHistory(
        message,
        "user"
    );


    // ======================================
    // CLEAR INPUT
    // ======================================

    input.value = "";


    // ======================================
    // SHOW THINKING
    // ======================================

    addMessage(
        "Thinking...",
        "bot"
    );


    try {

        // ==================================
        // SEND MESSAGE TO FLASK
        // ==================================

        const response =
            await fetch(
                "http://127.0.0.1:5000/chat",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        message: message

                    })

                }
            );


        // ==================================
        // CHECK RESPONSE
        // ==================================

        if (!response.ok) {

            throw new Error(
                "Server returned HTTP " +
                response.status
            );
        }


        // ==================================
        // CONVERT TO JSON
        // ==================================

        const data =
            await response.json();


        // ==================================
        // REMOVE THINKING MESSAGE
        // ==================================

        const messages =
            chatBox.querySelectorAll(
                ".bot-message"
            );


        if (messages.length > 0) {

            messages[
                messages.length - 1
            ].remove();
        }


        // ==================================
        // CHECK BACKEND ERROR
        // ==================================

        if (data.error) {

            addMessage(

                "Sorry, something went wrong: " +
                data.error,

                "bot"

            );

            addToHistory(

                "Sorry, something went wrong: " +
                data.error,

                "bot"

            );

            return;
        }


        // ==================================
        // SHOW CUSTOMER ANALYSIS
        // ==================================

        if (
            data.frustration &&
            data.knowledge
        ) {

            showAnalysis(

                data.frustration,

                data.knowledge,

                data.trust

            );
        }


        // ==================================
        // SHOW ESCALATION
        // ==================================

        showEscalation(
            data.trust
        );


        // ==================================
        // SHOW AI RESPONSE
        // ==================================

        if (data.response) {

            addMessage(
                data.response,
                "bot"
            );


            addToHistory(
                data.response,
                "bot"
            );

        } else {

            const errorMessage =
                "The support system did not return a response.";

            addMessage(
                errorMessage,
                "bot"
            );


            addToHistory(
                errorMessage,
                "bot"
            );
        }


        // ==================================
        // DEBUG INFORMATION
        // ==================================

        console.log(
            "Frustration:",
            data.frustration
        );


        console.log(
            "Knowledge:",
            data.knowledge
        );


        console.log(
            "Trust:",
            data.trust
        );

    }
    catch (error) {

        // ==================================
        // CONNECTION ERROR
        // ==================================

        console.error(
            "Connection error:",
            error
        );


        const errorMessage =
            "Sorry, I cannot connect to the support server.";


        addMessage(
            errorMessage,
            "bot"
        );


        addToHistory(
            errorMessage,
            "bot"
        );

    }
    finally {

        // ==================================
        // ENABLE BUTTON AGAIN
        // ==================================

        sendButton.disabled = false;


        input.focus();
    }
}


// ==========================================
// SEND BUTTON
// ==========================================

sendButton.addEventListener(
    "click",
    sendMessage
);


// ==========================================
// ENTER KEY
// ==========================================

input.addEventListener(
    "keypress",
    function(event) {

        if (
            event.key === "Enter"
        ) {

            sendMessage();

        }

    }
);


// ==========================================
// LOAD SAVED CONVERSATION
// ==========================================

loadConversation();

