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
import AddFacultyForm from "../components/AddFacultyForm";
import EditFacultyForm from "../components/EditFacultyForm";
import ErrorPage from "../components/ErrorPage";
import LoadingScreen from "../components/LoadingScreen";

const Faculty = () => {
  const [faculty, setFaculty] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [showEditForm, setShowEditForm] = useState(false);
  const [showDeletePopup, setShowDeletePopup] = useState(false);
  const [selectedFaculty, setSelectedFaculty] = useState(null);
  const [timeSlots, setTimeSlots] = useState([]);
  const [error, setError] = useState(false);
  const [isLoading, setIsLoading] = useState(false);


  useEffect(() => {
    getFaculty();
    getDetails();
  }, []);

  const getFaculty = async () => {
    setIsLoading(true);

    try {
      const response = await fetch("/api/faculty");
      const data = await response.json();
      setFaculty(data);
      setTimeout(() => {
        setIsLoading(false);
      }, 800);
    } catch (error) {
      console.error("Error fetching faculty:", error);
      setError(true);

    }
  };

  const getDetails = async () => {
    try {
        const response = await fetch("/api/other-details");
        const data = await response.json();
        setTimeSlots(data[0].timeSlots);
        setTimeout(() => {
          setIsLoading(false);
        }, 800);
        } catch (error) {
        console.error("Error fetching time slots:", error);
        setError(true);
    }
  }

  const addFaculty = async (facultyData) => {
    setIsLoading(true);
    try {
      const response = await fetch("/api/faculty", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(facultyData),
      });

      if (response.ok) {
        getFaculty();
        setShowForm(false);
        setTimeout(() => {
          setIsLoading(false);
        }, 800);
      } else {
        console.error("Failed to add faculty");
        setError(true);

      }
    } catch (error) {
      console.error("Error adding faculty:", error);
      setError(true);

    }
  };

  const editFaculty = async (updatedFaculty) => {
    setIsLoading(true);
    try {
      const response = await fetch(`/api/faculty/${updatedFaculty._id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(updatedFaculty),
      });

      if (response.ok) {
        getFaculty();
        setShowEditForm(false);
        setSelectedFaculty(null);
        setTimeout(() => {
          setIsLoading(false);
        }, 800);
      } else {
        console.error("Failed to update faculty");
        setError(true);

      }
    } catch (error) {
      console.error("Error updating faculty:", error);
      setError(true);

    }
  };

  const confirmDeleteFaculty = (facultyMember) => {
    setSelectedFaculty(facultyMember);
    setShowDeletePopup(true);
  };

  const deleteFaculty = async () => {
    setIsLoading(true);

    try {
      const response = await fetch(`/api/faculty/${selectedFaculty._id}`, {
        method: "DELETE",
      });

      if (response.ok) {
        getFaculty();
        setTimeout(() => {
          setIsLoading(false);
        }, 800);
      } else {
        console.error("Failed to delete faculty");
        setError(true);

      }
    } catch (error) {
      console.error("Error deleting faculty:", error);
      setError(true);

    } finally {
      setShowDeletePopup(false);
      setSelectedFaculty(null);
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
      <h2 className="table-heading">FACULTY</h2>
      <table className="table">
        <thead>
          <tr>
            <th>S.No.</th>
            <th>Faculty Name</th>
            <th>Availability</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {faculty.map((member, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{member.name}</td>
              <td>
                {[...member.availability]
                  .sort((a, b) => {
                    const order = { "9AM": 1, "12PM": 2, "3PM": 3 };
                    return order[a] - order[b];
                  })
                  .map((slot, index) => (
                    <span key={index} className="availability-slot">
                      <ul className="styled-list">
                        <li>{slot}</li>
                      </ul>
                    </span>
                  ))}
              </td>
              <td className="icon-group">
                <span
                  className="warning-icon"
                  onClick={() => {
                    setSelectedFaculty(member);
                    setShowEditForm(true);
                  }}
                >
                  <FontAwesomeIcon icon={faPen} />
                </span>
                <span
                  className="delete-icon"
                  onClick={() => confirmDeleteFaculty(member)}
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
          <AddFacultyForm onAddFaculty={addFaculty} setShowForm={setShowForm} timeSlots={timeSlots} />
        </div>
      )}

      {/* Render Edit Form */}
      {showEditForm && selectedFaculty && (
        <div className="form-overlay">
          <EditFacultyForm
            onEditFaculty={editFaculty}
            setShowForm={setShowEditForm}
            currentFaculty={selectedFaculty}
            timeSlots={timeSlots}
          />
        </div>
      )}

      {/* Delete Confirmation Popup */}
      {showDeletePopup && (
        <div className="deletePopup">
          <div className="popup-content">
            <h3>
              Are you sure you want to delete "
              <span style={{ color: "red" }}>{selectedFaculty.name}</span>"?
            </h3>
            <div className="popup-buttons">
              <button className="confirm-button" onClick={deleteFaculty}>
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

export default Faculty;
