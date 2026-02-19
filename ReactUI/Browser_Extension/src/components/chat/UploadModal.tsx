import React, { useState } from "react";
import { uploadDocument } from "../../api/apiClient";

interface Props {
  department: string;
  onClose: () => void;
}

const UploadModal: React.FC<Props> = ({
  department,
  onClose,
}) => {
  const [selectedFile, setSelectedFile] =
    useState<File | null>(null);

  const handleUpload = async () => {
    if (!department) {
      alert("Please select department first");
      return;
    }

    if (!selectedFile) {
      alert("Please choose a file");
      return;
    }

    try {
      await uploadDocument(selectedFile, department);
      alert("File uploaded successfully");
      onClose();
    } catch (error: any) {
      alert(error.message || "Upload failed");
    }
  };

  return (
    <div className="upload-overlay">
      <div className="upload-modal">

        <div className="upload-title">
          Upload Document
        </div>

        <input
          type="file"
          onChange={(e) =>
            setSelectedFile(
              e.target.files ? e.target.files[0] : null
            )
          }
        />

        <div className="upload-actions">
          <button onClick={handleUpload}>
            Upload
          </button>

          <button
            className="cancel-btn"
            onClick={onClose}
          >
            Cancel
          </button>
        </div>

      </div>
    </div>
  );
};

export default UploadModal;
