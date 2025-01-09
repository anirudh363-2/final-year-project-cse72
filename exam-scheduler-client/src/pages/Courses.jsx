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
import AddCourseForm from "../components/AddCourseForm";
import EditCourseForm from "../components/EditCourseForm";
import ErrorPage from "../components/ErrorPage";
import LoadingScreen from "../components/LoadingScreen";

const Courses = () => {
  const [courses, setCourses] = useState([]);
  const [showForm, setShowForm] = useState(false); // Toggle form visibility
  const [showEditForm, setShowEditForm] = useState(false);
  const [showDeletePopup, setShowDeletePopup] = useState(false); // Delete popup visibility
  const [selectedCourse, setSelectedCourse] = useState(null); // Store course to delete
  const [error, setError] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    getCourses();
  }, []);

  const getCourses = async () => {
    setIsLoading(true);
    try {
      const response = await fetch("/api/courses");
      const data = await response.json();
      setCourses(data);
      setTimeout(() => {
        setIsLoading(false);
      }, 800);
    } catch (error) {
      console.error("Error fetching courses:", error);
      setError(true);
    }
  };

  const addCourse = async (courseData) => {
    setIsLoading(true);
    try {
      const response = await fetch("/api/courses", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(courseData),
      });

      if (response.ok) {
        getCourses(); // Refresh courses after adding
        setShowForm(false); // Hide form after successful addition
        setTimeout(() => {
          setIsLoading(false);
        }, 800);
      } else {
        console.error("Failed to add course");
        setError(true);
      }
    } catch (error) {
      console.error("Error adding course:", error);
      setError(true);

    }
  };

  const editCourse = async (updatedCourse) => {
    setIsLoading(true);
    try {
      const response = await fetch(`/api/courses/${updatedCourse._id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(updatedCourse),
      });

      if (response.ok) {
        getCourses();
        setShowEditForm(false);
        setSelectedCourse(null);
        setTimeout(() => {
          setIsLoading(false);
        }, 800);
      } else {
        console.error("Failed to update course");
        setError(true);

      }
    } catch (error) {
      console.error("Error updating course:", error);
      setError(true);

    }
  };



  const confirmDeleteCourse = (course) => {
    setSelectedCourse(course);
    setShowDeletePopup(true);
  };

  const deleteCourse = async () => {
    setIsLoading(true);
    try {
      const response = await fetch(`/api/courses/${selectedCourse._id}`, {
        method: "DELETE",
      });

      if (response.ok) {
        getCourses(); // Refresh courses after deletion
        setTimeout(() => {
          setIsLoading(false);
        }, 800);
      } else {
        console.error("Failed to delete course");
        setError(true);

      }
    } catch (error) {
      console.error("Error deleting course:", error);
      setError(true);

    } finally {
      setShowDeletePopup(false); // Hide popup
      setSelectedCourse(null);
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
      <h2 className="table-heading">COURSES</h2>
      <table className="table">
        <thead>
          <tr>
            <th>S.No.</th>
            <th>Course</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {courses.map((course, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{course.name}</td>
              <td className="icon-group">
                <span className="warning-icon" onClick={() => {setSelectedCourse(course); setShowEditForm(true);}}>
                  <FontAwesomeIcon icon={faPen} />
                </span>
                <span
                  className="delete-icon"
                  onClick={() => confirmDeleteCourse(course)}
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
          <AddCourseForm onAddCourse={addCourse} setShowForm={setShowForm} />
        </div>
      )}

      {/* Render Edit Form */}
      {showEditForm && selectedCourse && (
        <div className="form-overlay">
          <EditCourseForm
            onEditCourse={editCourse}
            setShowForm={setShowEditForm}
            currentCourse={selectedCourse}
          />
        </div>
      )}

      {/* Delete Confirmation Popup */}
      {showDeletePopup && (
        <div className="deletePopup">
          <div className="popup-content">
            <h3>Are you sure you want to delete "<span style={{color: "red"}}>{selectedCourse.name}</span>"?</h3>
            <div className="popup-buttons">
              <button className="confirm-button" onClick={deleteCourse}>
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

export default Courses;