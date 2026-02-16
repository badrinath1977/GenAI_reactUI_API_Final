import React from "react";

interface Props {
  question: string;
  setQuestion: (q: string) => void;
  onSend: () => void;
  onUploadClick: () => void;
}

const ChatInput: React.FC<Props> = ({
  question,
  setQuestion,
  onSend,
  onUploadClick,
}) => {

  return (
    <div className="input-area">
      <button
        className="plus-btn"
        onClick={onUploadClick}
      >
        +
      </button>

      <input
        type="text"
        placeholder="Ask something..."
        value={question}
        onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
          setQuestion(e.target.value)
        }
        onKeyDown={(e) =>
          e.key === "Enter" && onSend()
        }
      />

      <button onClick={onSend}>Send</button>
    </div>
  );
};

export default ChatInput;
