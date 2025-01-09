import React from "react";
import home from "../assets/home.jpg";
import { Link } from "react-router-dom";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faDatabase, faCalendarCheck } from '@fortawesome/free-solid-svg-icons'; 

const Home = () => {
  return (
    <div className="home-container">
      <div className="home-left">
        <div className="logo">
          <h1>Examination Timetable Generator</h1>
        </div>
        <div className="home-content">
          <h2>Create flawless timetables with just a few clicks</h2>
          <p>
            Effortlessly create fair, efficient, and personalized examination
            timetables
          </p>
          <div className="buttons">
            <Link to='/data'> <button className="btn btn-green"> <FontAwesomeIcon icon={faDatabase} style={{ marginRight: '10px' }} /> Edit your database</button> </Link>
            <Link to='/generate'> <button className="btn btn-blue"> <FontAwesomeIcon icon={faCalendarCheck} style={{ marginRight: '10px' }} /> Generate timetable</button> </Link>
          </div>
        </div>
      </div>

      {/* Green Diagonal Square */}
      <div className="diagonal-square"></div>

      {/* Blue Circle */}
      <div className="blue-circle"></div>

      {/* Right Section with Black Glass Overlay */}
      <div className="home-right">
      <p className="creators-text">Creators</p>

        {/* Hidden Creator Names */}
        <div className="creators-container">
          <p>Manur Yashas Sreevatsa - 20211CSE0275</p>
          <p>Priya K R - 20211CSE0340</p>
          <p>Perepi Bhanu Vaishnavi - 20211CSE0393</p>
          <p>Anirudh Manjunath Sandilya - 20211CSE0362</p>
        </div>

        <div className="home-overlay"></div>
        <img src={home} alt="Workspace" className="home-image" />
      </div>
    </div>
  );
};

export default Home;