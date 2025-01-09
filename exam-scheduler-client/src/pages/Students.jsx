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
import AddStudentForm from "../components/AddStudentForm";
import EditStudentForm from "../components/EditStudentForm";
import ErrorPage from "../components/ErrorPage";
import LoadingScreen from "../components/LoadingScreen";

const Students = () => {
  const [students, setStudents] = useState([]);
  const [showForm, setShowForm] = useState(false);
  const [showEditForm, setShowEditForm] = useState(false);
  const [showDeletePopup, setShowDeletePopup] = useState(false);
  const [selectedStudent, setSelectedStudent] = useState(null);
  const [courses, setCourses] = useState([]);
  const [error, setError] = useState(false);
  const [isLoading, setIsLoading] = useState(false);


  useEffect(() => {
    getStudents();
    getCourses();
  }, []);

  const getStudents = async () => {
    setIsLoading(true);
    try {
      const response = await fetch("/api/students");
      const data = await response.json();
      setStudents(data);
      setTimeout(() => {
        setIsLoading(false);
      }, 800);
    } catch (error) {
      console.error("Error fetching students:", error);
    }
  };

  const getCourses = async () => {
    try {
        const response = await fetch("/api/courses");
        const data = await response.json();
        const courses = data.map(course => course.name);
        setCourses(courses);
        } catch (error) {
        console.error("Error fetching courses:", error);
        setError(true);
    }
  }

  const addStudent = async (studentData) => {
    setIsLoading(true);
    try {
      const response = await fetch("/api/students", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(studentData),
      });

      if (response.ok) {
        getStudents();
        setShowForm(false);
        setTimeout(() => {
          setIsLoading(false);
        }, 800);
      } else {
        console.error("Failed to add student");
        setError(true);

      }
    } catch (error) {
      console.error("Error adding student:", error);
      setError(true);

    }
  };

  const editStudent = async (updatedStudent) => {
    setIsLoading(true);

    try {
      const response = await fetch(`/api/students/${updatedStudent._id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(updatedStudent),
      });

      if (response.ok) {
        getStudents();
        setShowEditForm(false);
        setSelectedStudent(null);
        setTimeout(() => {
          setIsLoading(false);
        }, 800);
      } else {
        console.error("Failed to update student");
        setError(true);

      }
    } catch (error) {
      console.error("Error updating student:", error);
      setError(true);

    }
  };

  const confirmDeleteStudent = (student) => {
    setSelectedStudent(student);
    setShowDeletePopup(true);
  };

  const deleteStudent = async () => {
    setIsLoading(true);

    try {
      const response = await fetch(`/api/students/${selectedStudent._id}`, {
        method: "DELETE",
      });

      if (response.ok) {
        getStudents();
        setTimeout(() => {
          setIsLoading(false);
        }, 800);
      } else {
        console.error("Failed to delete student");
        setError(true);

      }
    } catch (error) {
      console.error("Error deleting student:", error);
      setError(true);

    } finally {
      setShowDeletePopup(false);
      setSelectedStudent(null);
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
      <h2 className="table-heading">STUDENTS</h2>
      <table className="table">
        <thead>
          <tr>
            <th>S.No.</th>
            <th>Student Roll Number</th>
            <th>Student Name</th>
            <th>Courses</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {students.map((student, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{student.rollNumber}</td>
              <td>{student.name}</td>
              <td>
                {student.courses.map((course, index) => (
                  <span key={index} className="course-tag">
                    <ul className="styled-list">
                      <li>{course}</li>
                    </ul>
                  </span>
                ))}
              </td>
              <td className="icon-group">
                <span
                  className="warning-icon"
                  onClick={() => {
                    setSelectedStudent(student);
                    setShowEditForm(true);
                  }}
                >
                  <FontAwesomeIcon icon={faPen} />
                </span>
                <span
                  className="delete-icon"
                  onClick={() => confirmDeleteStudent(student)}
                >
                  <FontAwesomeIcon icon={faTrash} />
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <br />
      <br />
      

      <h1 style={{color: "white"}} >HAR HAR MAHADEV</h1>

      {/* Add Button */}
      <button className="add-button" onClick={() => setShowForm(!showForm)}>
        <FontAwesomeIcon icon={faPlus} />
      </button>

      {/* Conditional Form Rendering */}
      {showForm && (
        <div className="form-overlay">
          <AddStudentForm onAddStudent={addStudent} setShowForm={setShowForm} courses={courses} />
        </div>
      )}

      {/* Render Edit Form */}
      {showEditForm && selectedStudent && (
        <div className="form-overlay">
          <EditStudentForm
            onEditStudent={editStudent}
            setShowForm={setShowEditForm}
            currentStudent={selectedStudent}
            courses={courses}
          />
        </div>
      )}

      {/* Delete Confirmation Popup */}
      {showDeletePopup && (
        <div className="deletePopup">
          <div className="popup-content">
            <h3>
              Are you sure you want to delete "
              <span style={{ color: "red" }}>{selectedStudent.name}</span>"?
            </h3>
            <div className="popup-buttons">
              <button className="confirm-button" onClick={deleteStudent}>
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

export default Students;
