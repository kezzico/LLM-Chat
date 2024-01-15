import React, { useState, useEffect } from 'react';
import './Chat.css'

function Chat() {
  const [messages, setMessages] = useState([]);

  // useEffect(() => {
  //   const eventSource = new EventSource('/chat');

  //   console.log('😅😅😅')

  //   eventSource.onmessage = (event) => {
  //     console.log('😊')
  //       console.log(event.data)
  //       setMessages((prevMessages) => [...prevMessages, event.data]);
  //   };

  //   eventSource.onerror = (error) => {
  //     console.error('EventSource failed:', error);
  //     eventSource.close();
  //   };

  //   return () => {
  //     console.log('close!')
  //     // eventSource.close();
  //   };
  // }, []);

  return (
    <main class="chat">
      {messages.length === 0 && (
        <article class="chat empty">
          <h2> How can I help you today? </h2>
          <img class="icon" src="./gpu.svg" />
          <div class="suggestion">
            <p>Show me a code snippet</p>
            <p>of a website sticky header</p>
          </div>

          <div class="suggestion">
            <p>Design a database schema</p>
            <p>for an online merch store</p>
          </div>
        </article>
      )}

      {messages.length > 0 && (
        <article>
          {messages.join("").split("xxx").map((msg, index) => {
            <p>{msg}▊</p>
          })}
        </article>
      )}

      <form>
        <textarea type="text" placeholder="Message LLM"></textarea>
      </form>
    </main>
  );
}

export default Chat;
