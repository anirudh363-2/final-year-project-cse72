import React, { useState } from "react";

const AddRoomForm = ({ onAddRoom, setShowForm }) => {
    const [roomData, setRoomData] = useState({ name: "" });


    const handleSubmit = (e) => {
        e.preventDefault();
        if (roomData.name.trim()) {
          onAddRoom(roomData); // Pass the entire object
          setRoomData({ name: "" }); // Reset the form field
        } else {
          alert("Room name cannot be empty!");
        }
      };

      return (
        <div className="add-edit-form-container">
          <h2 className="form-heading">Add Room</h2>
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
                  setRoomData({ ...roomData, name: e.target.value }) // Update the name property
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
                Add Room
              </button>
            </div>
          </form>
        </div>
      );
};

export default AddRoomForm;
