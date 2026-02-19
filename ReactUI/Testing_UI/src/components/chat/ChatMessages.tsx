// import React, {
//   useEffect,
//   useRef,
// } from "react";
// import ReactMarkdown from "react-markdown";
// import { Message } from "../../models/ChatTypes";

// interface Props {
//   messages: Message[];
// }

// const ChatMessages: React.FC<Props> = ({
//   messages,
// }) => {
//   const bottomRef =
//     useRef<HTMLDivElement | null>(
//       null
//     );

//   useEffect(() => {
//     bottomRef.current?.scrollIntoView(
//       { behavior: "smooth" }
//     );
//   }, [messages]);

//   return (
//     <div className="chat-area">
//       {messages.map((msg) => (
//         <div
//           key={msg.id}
//           className={
//             msg.type === "user"
//               ? "user-msg"
//               : "bot-msg"
//           }
//         >
//           <ReactMarkdown>
//             {msg.text}
//           </ReactMarkdown>
//         </div>
//       ))}
//       <div ref={bottomRef} />
//     </div>
//   );
// };

// export default ChatMessages;

import React, { useEffect, useRef } from "react";
import ReactMarkdown from "react-markdown";
import { Message } from "../../models/ChatTypes";

interface Props {
  messages: Message[];
}

const ChatMessages: React.FC<Props> = ({ messages }) => {
  const bottomRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  return (
    <div className="chat-area">
      {messages.map((msg) => (
        <div
          key={msg.id}
          className={
            msg.type === "user"
              ? "user-msg"
              : "bot-msg"
          }
        >
          {msg.type === "bot" ? (
            <ReactMarkdown>
              {msg.text}
            </ReactMarkdown>
          ) : (
            msg.text
          )}
        </div>
      ))}

      <div ref={bottomRef} />
    </div>
  );
};

export default ChatMessages;
