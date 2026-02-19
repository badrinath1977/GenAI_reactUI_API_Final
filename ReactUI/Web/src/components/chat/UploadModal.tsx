import React, { useState } from "react";
import {
  uploadDocument,
  sendChatMessage,
} from "../../api/apiClient";
import { Message } from "../../models/ChatTypes";

interface Props {
  userId: string;
  department: string;
  onClose: () => void;
  onSummaryGenerated: (msg: Message) => void;
}

const UploadModal: React.FC<Props> = ({
  userId,
  department,
  onClose,
  onSummaryGenerated,
}) => {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [showDuplicatePopup, setShowDuplicatePopup] = useState(false);

  const simulateProgress = () => {
    return new Promise<void>((resolve) => {
      let value = 0;
      const interval = setInterval(() => {
        value += 10;
        setProgress(value);
        if (value >= 100) {
          clearInterval(interval);
          resolve();
        }
      }, 200);
    });
  };

  const summarizeFile = async () => {
    if (!file) return;

    const response = await sendChatMessage(
      userId,
      `Summarize the document ${file.name} in bullet points`,
      department
    );

    const summaryMessage: Message = {
      id: crypto.randomUUID(),
      type: "bot",
      text: response.answer,
      timestamp: new Date().toISOString(),
      department,
    };

    onSummaryGenerated(summaryMessage);
  };

  const finishProcess = () => {
    setLoading(false);
    setProgress(0);

    setTimeout(() => {
      onClose();
    }, 300);
  };

  // const processUpload = async () => {
  //   if (!file || !department) return;

  //   setLoading(true);
  //   setProgress(0);

  //   try {
  //     // Try normal upload
  //     await uploadDocument(file, department);

  //     await simulateProgress();
  //     await summarizeFile();
  //     finishProcess();
  //   } catch (error: any) {
  //     // Duplicate file detected
  //     if (error?.status === 400) {
  //       setShowDuplicatePopup(true);
  //     } else {
  //       console.error(error);
  //       finishProcess();
  //     }
  //   }
  // };

  const processUpload = async () => {
  if (!file || !department) return;

  setLoading(true);
  setProgress(0);

  try {
    await uploadDocument(file, department);

    await simulateProgress();
    await summarizeFile();
    finishProcess();
  } catch (error: any) {
    if (error?.status === 400) {
      // Do NOT console.error
      setShowDuplicatePopup(true);
    } else {
      // Only log unexpected errors
      console.warn("Unexpected upload error:", error);
      finishProcess();
    }
  }
};


  const handleOverwrite = async () => {
    setShowDuplicatePopup(false);

    // No second upload call (backend does not support overwrite)
    await simulateProgress();
    await summarizeFile();
    finishProcess();
  };

  const handleCancelDuplicate = async () => {
    setShowDuplicatePopup(false);

    await simulateProgress();
    await summarizeFile();
    finishProcess();
  };

  return (
    <div className="upload-overlay">
      <div className="upload-modal">

        {!showDuplicatePopup ? (
          <>
            <div className="upload-title">
              Upload File
            </div>

            <input
              type="file"
              disabled={loading}
              onChange={(e) =>
                setFile(
                  e.target.files
                    ? e.target.files[0]
                    : null
                )
              }
            />

            {loading && (
              <div className="progress-bar">
                <div
                  className="progress-fill"
                  style={{ width: `${progress}%` }}
                />
                <span>{progress}%</span>
              </div>
            )}

            <div className="upload-actions">
              <button
                disabled={loading}
                onClick={processUpload}
              >
                {loading ? "Processing..." : "Upload"}
              </button>

              <button
                disabled={loading}
                className="cancel-btn"
                onClick={onClose}
              >
                Cancel
              </button>
            </div>
          </>
        ) : (
          <>
            <div className="upload-title">
              File already exists
            </div>

            <p>
              This file was already uploaded.
              What would you like to do?
            </p>

            <div className="upload-actions">
              <button onClick={handleOverwrite}>
                Overwrite
              </button>
              <button
                className="cancel-btn"
                onClick={handleCancelDuplicate}
              >
                Cancel
              </button>
            </div>
          </>
        )}

      </div>
    </div>
  );
};

export default UploadModal;
