import React, { useState, useEffect } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faArrowLeft,
  faArrowRight,
  faHome,
  faEye,
  faDatabase,
} from "@fortawesome/free-solid-svg-icons";
import { Link, useLocation } from "react-router-dom";
import ErrorPage from "../components/ErrorPage";
import LoadingScreen from "../components/LoadingScreen";
import TimetableDisplay from "../components/TimetableDisplay";

export default function Methods() {
  const [rotation, setRotation] = useState(0);
  const [methods, setMethods] = useState({});
  const [isPopupOpen, setIsPopupOpen] = useState(false); // Popup visibility state
  const [selectedMethodData, setSelectedMethodData] = useState(null); // Data to be passed to the popup
  const [selectedMethodName, setSelectedMethodName] = useState(null);
  const location = useLocation();
  const { timetableName, id } = location.state || {}; // Destructure examName and id from state
  const [error, setError] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const formattedMethods = {
    ConstraintSatisfactionProblem: "Constraint Satisfaction Problem",
    GeneticAlgorithm: "Genetic Algorithm",
    SimulatedAnnealing: "Simulated Annealing",
    OpenAI: "OpenAI",
  };

  // Fetch the timetables on component mount
  useEffect(() => {
    getTimetable();
  }, [id]);

  const getTimetable = async () => {
    setIsLoading(true);
    try {
      const response = await fetch(`/api/timetables/${id}`);
      const data = await response.json();
      console.log("Fetched data:", data); // Log the fetched data to confirm the structure
      setMethods(data.methods); // Store the methods object
      setTimeout(() => {
        setIsLoading(false);
      }, 800);
    } catch (error) {
      console.error("Error fetching timetables:", error);
      setError(true);
    }
  };

  const handlePrevClick = () => {
    setRotation((prev) => prev + 90);
  };

  const handleNextClick = () => {
    setRotation((prev) => prev - 90);
  };

  const handleViewClick = (methodName, methodDetails) => {
    setSelectedMethodData(methodDetails); // Set the data to be passed to the popup
    setSelectedMethodName(methodName)
    setIsPopupOpen(true); // Open the popup
  };

  const closePopup = () => {
    setIsPopupOpen(false); // Close the popup
  };

  return (
    <div className="methods-container">
      <div className="table-diagonal-square"></div>
      <div className="table-blue-circle"></div>

      <div className="sidebar">
        <Link to="/timetables">
          <div className="back-arrow">
            <FontAwesomeIcon icon={faArrowLeft} />
          </div>
        </Link>
        <Link to="/">
          <div className="home-button">
            <FontAwesomeIcon icon={faHome} />
          </div>
        </Link>
        <Link to="/data">
          <div className="db-button">
            <FontAwesomeIcon icon={faDatabase} />
          </div>
        </Link>
      </div>
      <div className="method-page">
        <h1 className="generate-heading">{timetableName}</h1>
        <br />
        <br />
        <div
          className="method-card-container"
          style={{ transform: `perspective(1000px) rotateY(${rotation}deg)` }}
        >
          {Object.entries(methods).map(([methodName, methodDetails], index) => (
            <span key={index} style={{ "--i": index + 1 }}>
              <div className="method-card">
                <div className="method-card-content">
                  <h3 className="method-name">
                    {formattedMethods[methodName]}
                  </h3>
                  {methodName === "OpenAI" && <p className="recommendation">Most Recommended</p>}
                  {methodName === "GeneticAlgorithm" && <p className="recommendation">Recommended</p>}
                  <br />
                  <button
                    className="view-button"
                    onClick={() => handleViewClick(methodName, methodDetails)} // Pass the data to the popup
                  >
                    <FontAwesomeIcon icon={faEye} />
                    View
                  </button>
                </div>
              </div>
            </span>
          ))}
        </div>
        <div className="btn-container">
          <button className="method-btn" id="prev" onClick={handlePrevClick}>
            <FontAwesomeIcon icon={faArrowLeft} />
          </button>
          <button className="method-btn" id="next" onClick={handleNextClick}>
            <FontAwesomeIcon icon={faArrowRight} />
          </button>
        </div>
      </div>

      {error && <ErrorPage />}
      {isLoading && <LoadingScreen />}

      {isPopupOpen && selectedMethodData && (
        <TimetableDisplay name={selectedMethodName} data={selectedMethodData} closePopup={closePopup} />
      )}
    </div>
  );
}
