import React, { useState } from "react";

const EditRoomForm = ({ onEditRoom, setShowForm, currentRoom }) => {
  // Initialize state with the current room data
  const [roomData, setRoomData] = useState(currentRoom);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (roomData.name.trim()) {
      onEditRoom(roomData); // Pass the updated room object
    } else {
      alert("Room name cannot be empty!");
    }
  };

  return (
    <div className="add-edit-form-container">
      <h2 className="form-heading">Edit Room</h2>
      <form onSubmit={handleSubmit} className="add-edit-form">
        <div className="input-group">
          <label htmlFor="roomName" className="form-label">
            Room Name:
          </label>
          <input
            type="text"
            id="roomName"
            placeholder="Enter room name"
            value={roomData.name}
            onChange={(e) =>
              setRoomData({ ...roomData, name: e.target.value }) // Update name property
            }
            className="form-input"
          />
        </div>
        <div className="form-buttons">
          <button
            type="button"
            className="cancel"
            onClick={() => setShowForm(false)}
          >
            Cancel
          </button>
          <button type="submit" className="create-button">
            Save Changes
          </button>
        </div>
      </form>
    </div>
  );
};

export default EditRoomForm;
