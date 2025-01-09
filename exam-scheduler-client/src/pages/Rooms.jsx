import React, { useState, useEffect } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faTrash,
  faPen,
  faPlus,
  faArrowLeft,
  faHome
} from "@fortawesome/free-solid-svg-icons";
import { Link } from "react-router-dom";
import AddRoomForm from "../components/AddRoomForm";
import EditRoomForm from "../components/EditRoomForm";
import ErrorPage from "../components/ErrorPage";
import LoadingScreen from "../components/LoadingScreen";

const Rooms = () => {
  const [rooms, setRooms] = useState([]);
  const [showForm, setShowForm] = useState(false); // Toggle form visibility
  const [showEditForm, setShowEditForm] = useState(false);
  const [showDeletePopup, setShowDeletePopup] = useState(false); // Delete popup visibility
  const [selectedRoom, setSelectedRoom] = useState(null); // Store room to delete
  const [error, setError] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    getRooms();
  }, []);

  const getRooms = async () => {
    setIsLoading(true);

    try {
      const response = await fetch("/api/rooms");
      const data = await response.json();
      setRooms(data);
      setTimeout(() => {
        setIsLoading(false);
      }, 800);
    } catch (error) {
      console.error("Error fetching rooms:", error);
      setError(true);

    }
  };

  const addRoom = async (roomData) => {
    setIsLoading(true);

    try {
      const response = await fetch("/api/rooms", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(roomData),
      });

      if (response.ok) {
        getRooms(); // Refresh rooms after adding
        setShowForm(false); // Hide form after successful addition
        setTimeout(() => {
          setIsLoading(false);
        }, 800);
      } else {
        console.error("Failed to add room");
        setError(true);
      }
    } catch (error) {
      console.error("Error adding room:", error);
      setError(true);

    }
  };

  const editRoom = async (updatedRoom) => {
    setIsLoading(true);

    try {
      const response = await fetch(`/api/rooms/${updatedRoom._id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(updatedRoom),
      });

      if (response.ok) {
        getRooms();
        setShowEditForm(false);
        setSelectedRoom(null);
        setTimeout(() => {
          setIsLoading(false);
        }, 800);
      } else {
        console.error("Failed to update room");
        setError(true);
      }
    } catch (error) {
      console.error("Error updating room:", error);
      setError(true);

    }
  };



  const confirmDeleteRoom = (room) => {
    setSelectedRoom(room);
    setShowDeletePopup(true);
  };

  const deleteRoom = async () => {
    setIsLoading(true);

    try {
      const response = await fetch(`/api/rooms/${selectedRoom._id}`, {
        method: "DELETE",
      });

      if (response.ok) {
        getRooms(); // Refresh rooms after deletion
        setTimeout(() => {
          setIsLoading(false);
        }, 800);
      } else {
        console.error("Failed to delete room");
        setError(true);
      }
    } catch (error) {
      console.error("Error deleting room:", error);
      setError(true);

    } finally {
      setShowDeletePopup(false); // Hide popup
      setSelectedRoom(null);
    }
  };

  return (
    <div className="table-container">
      <div className="sidebar">
        <Link to="/data">
          <div className="back-arrow">
            <FontAwesomeIcon icon={faArrowLeft} />
          </div>
        </Link>
        <Link to="/">
                  <div className="home-button">
                    <FontAwesomeIcon icon={faHome} />
                  </div>
                </Link>
      </div>
      <h2 className="table-heading">ROOMS</h2>
      <table className="table">
        <thead>
          <tr>
            <th>S.No.</th>
            <th>Room</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {rooms.map((room, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{room.name}</td>
              <td className="icon-group">
                <span className="warning-icon" onClick={() => {setSelectedRoom(room); setShowEditForm(true);}}>
                  <FontAwesomeIcon icon={faPen} />
                </span>
                <span
                  className="delete-icon"
                  onClick={() => confirmDeleteRoom(room)}
                >
                  <FontAwesomeIcon icon={faTrash} />
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Add Button */}
      <button className="add-button" onClick={() => setShowForm(!showForm)}>
        <FontAwesomeIcon icon={faPlus} />
      </button>

      {/* Conditional Form Rendering */}
      {showForm && (
        <div className="form-overlay">
          <AddRoomForm onAddRoom={addRoom} setShowForm={setShowForm} />
        </div>
      )}

      {/* Render Edit Form */}
      {showEditForm && selectedRoom && (
        <div className="form-overlay">
          <EditRoomForm
            onEditRoom={editRoom}
            setShowForm={setShowEditForm}
            currentRoom={selectedRoom}
          />
        </div>
      )}

      {/* Delete Confirmation Popup */}
      {showDeletePopup && (
        <div className="deletePopup">
          <div className="popup-content">
            <h3>Are you sure you want to delete "<span style={{color: "red"}}>{selectedRoom.name}</span>"?</h3>
            <div className="popup-buttons">
              <button className="confirm-button" onClick={deleteRoom}>
                Yes, Delete
              </button>
              <button
                className="cancel-button"
                onClick={() => setShowDeletePopup(false)}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}

      <div className="table-blue-circle"></div>
      <div className="table-diagonal-square"></div>

      {error && <ErrorPage />}
      {isLoading && <LoadingScreen />}
    </div>
  );
};

export default Rooms;
