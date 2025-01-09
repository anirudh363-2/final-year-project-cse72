import React from 'react';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Link } from "react-router-dom";
import {
  faHome
} from "@fortawesome/free-solid-svg-icons";

export default function ErrorPage() {
  return (
    <div className="error-page">
        
      <div className="error-content">
        <div className="sad-robot">🤖</div>
        <h1 className='error-heading'>Oops! Something went wrong.</h1>
        <p className='error-text'>Looks like we ran into an error. Please try again later.</p>
        <Link to="/">
          <div className="home-button-error">
            <FontAwesomeIcon icon={faHome} />
          </div>
        </Link>
      </div>
      
    </div>
  );
}
