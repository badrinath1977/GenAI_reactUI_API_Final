import React from "react";

interface Props {
  message: string;
}

const Toast: React.FC<Props> = ({
  message,
}) => {
  return (
    <div className="toast">
      {message}
    </div>
  );
};

export default Toast;
