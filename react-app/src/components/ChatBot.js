import React, { useState, useEffect } from 'react';

function ChatBot() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const eventSource = new EventSource('/chat');

    eventSource.onmessage = (event) => {
        console.log(event.data)
        setMessages((prevMessages) => [...prevMessages, event.data]);
    };

    eventSource.onerror = (error) => {
      console.error('EventSource failed:', error);
      eventSource.close();
    };

    return () => {
      eventSource.close();
    };
  }, []);

  return (
    <div>
      {messages.join("").split("xxx").map((msg, index) => {
        <p>{msg}▊</p>
      })}
      <p>{messages.join("")}▊</p>
    </div>
  );
}

export default ChatBot;
