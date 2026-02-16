import React from "react";

interface HeaderProps {
  department: string;
  setDepartment: (dept: string) => void;
}

const Header: React.FC<HeaderProps> = ({
  department,
  setDepartment,
}) => {

  return (
    <div className="header">
      <h2>Enterprise Copilot</h2>

      <select
        value={department}
        onChange={(e: React.ChangeEvent<HTMLSelectElement>) =>
          setDepartment(e.target.value)
        }
      >
        <option value="IT">IT</option>
        <option value="HR">HR</option>
        <option value="Finance">Finance</option>
      </select>
    </div>
  );
};

export default Header;
