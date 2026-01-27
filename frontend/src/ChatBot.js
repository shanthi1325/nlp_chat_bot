import React, { useState } from "react";
import "./ChatBot.css";

const BOT_IMG = "https://cdn-icons-png.flaticon.com/512/4712/4712035.png";
const PERSON_IMG = "https://cdn-icons-png.flaticon.com/512/847/847969.png";

export default function ChatBot() {
  const [messages, setMessages] = useState([
    {
      name: "ChatBot",
      img: BOT_IMG,
      side: "left",
      text: "Hi, welcome to ChatBot! Go ahead and send me a message 😄",
      time: getTime()
    }
  ]);

  const [input, setInput] = useState("");

  async function sendMessage(e) {
    e.preventDefault();
    if (!input.trim()) return;

    // User message
    const userMsg = {
      name: "You",
      img: PERSON_IMG,
      side: "right",
      text: input,
      time: getTime()
    };

    setMessages(prev => [...prev, userMsg]);
    setInput("");

    try {
      const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          user: "usha",
          message: input
        })
      });

      const data = await res.json();

      const botMsg = {
        name: "ChatBot",
        img: BOT_IMG,
        side: "left",
        text: data.reply,
        time: getTime()
      };

      setMessages(prev => [...prev, botMsg]);

    } catch (err) {
      console.error("Backend error:", err);
    }
  }

  return (
    <section className="msger">
      <header className="msger-header">
        <div className="msger-header-title">🤖 ChatBot 🤖</div>
      </header>

      <main className="msger-chat">
        {messages.map((msg, i) => (
          <div key={i} className={`msg ${msg.side}-msg`}>
            <div
              className="msg-img"
              style={{ backgroundImage: `url(${msg.img})` }}
            ></div>

            <div className="msg-bubble">
              <div className="msg-info">
                <div className="msg-info-name">{msg.name}</div>
                <div className="msg-info-time">{msg.time}</div>
              </div>

              <div className="msg-text">{msg.text}</div>
            </div>
          </div>
        ))}
      </main>

      <form className="msger-inputarea" onSubmit={sendMessage}>
        <input
          type="text"
          className="msger-input"
          placeholder="Enter your message..."
          value={input}
          onChange={e => setInput(e.target.value)}
        />
        <button type="submit" className="msger-send-btn">Send</button>
      </form>
    </section>
  );
}

function getTime() {
  const date = new Date();
  const h = "0" + date.getHours();
  const m = "0" + date.getMinutes();
  return `${h.slice(-2)}:${m.slice(-2)}`;
}