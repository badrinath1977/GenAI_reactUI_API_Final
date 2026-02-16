import React, { useState } from "react";
import { uploadDocumentAPI } from "../../api/apiClient";

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

  const handleUpload = async (): Promise<void> => {

    if (!selectedFile) {
      alert("Please select a file.");
      return;
    }

    const formData = new FormData();
    formData.append("department", department);
    formData.append("file", selectedFile);

    try {
      await uploadDocumentAPI(formData);
      alert("File uploaded successfully.");
      onClose();
    } catch (error) {
      console.error(error);
      alert("Upload failed.");
    }
  };

  return (
    <div className="popup-overlay">
      <div className="popup-box">
        <h3>Upload Document</h3>

        <p>
          <strong>Department:</strong> {department}
        </p>

        <input
          type="file"
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setSelectedFile(
              e.target.files?.[0] || null
            )
          }
        />

        <div className="popup-actions">
          <button onClick={handleUpload}>
            Upload
          </button>

          <button onClick={onClose}>
            Cancel
          </button>
        </div>
      </div>
    </div>
  );
};

export default UploadModal;
