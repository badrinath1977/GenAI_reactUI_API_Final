import React from "react";
import { FiPaperclip } from "react-icons/fi";
import { IoSend } from "react-icons/io5";

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
  onUploadClick
}) => {

  return (
    <div className="input-area">

      <button className="icon-btn" onClick={onUploadClick}>
        <FiPaperclip size={18} />
      </button>

      <input
        type="text"
        placeholder="Ask something..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && onSend()}
      />

      <button className="icon-btn" onClick={onSend}>
        <IoSend size={18} />
      </button>

    </div>
  );
};

export default ChatInput;
