import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faCalendarAlt, faArrowLeft } from "@fortawesome/free-solid-svg-icons";
import ErrorPage from "../components/ErrorPage";
import LoadingScreen from "../components/LoadingScreen";

export default function Timetables() {
  const [timetables, setTimetables] = useState([]);
  const [error, setError] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const getTimetables = async () => {
    setIsLoading(true);
    try {
      const response = await fetch("/api/timetables");
      const data = await response.json();
      setTimetables(data);
      setTimeout(() => {
        setIsLoading(false);
      }, 800);
    } catch (error) {
      console.error("Error fetching timetables:", error);
      setError(true);
    }
  };

  useEffect(() => {
    getTimetables();
  }, []);

  return (
    <>

      <div className="timetable-generate-container">

      <div className="nav-bar">
        <Link to="/data">
          <div className="back-arrow">
            <FontAwesomeIcon icon={faArrowLeft} />
          </div>
        </Link>
      </div>

      <div className="generate-diagonal-square"></div>
      <div className="generate-blue-circle"></div>

        <h1 className="generate-heading">Exam Names</h1>

        <div className="timetable-card-container">
        {timetables.map((timetable) => (
            <Link
              to={`/methods/${timetable.name}`}
              state={{ timetableName: timetable.name, id: timetable._id }} 
            >
              <div key={timetable._id} className="timetable-card">
                <div className="timetable-card-content">
                  <h2 className="timetable-name-display">{timetable.name}</h2>
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>
      {error && <ErrorPage />}
        {isLoading && <LoadingScreen />}    
    </>
  );
}
