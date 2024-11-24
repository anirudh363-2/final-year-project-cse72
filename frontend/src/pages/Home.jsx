import React from "react";
import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div classNameName="home">
      <div class="background">
        <div class="logo">
          <h1 class="title">CHRONO</h1>
        </div>
        <div class="glass-panel">
          <p class="subtitle">
            Effortlessly create fair, efficient, and personalized examination
            timetables
          </p>
          <h2 class="main-text">
            CHRONO creates fla  wless timetables
            <br /> with just a few clicks
          </h2>
          <div class="buttons">
            <button class="btn generate-button">
              <a href="/HTML/faculty.html">
                <svg
                  class="sparkle"
                  id="Layer_1"
                  data-name="Layer 1"
                  viewBox="0 0 24 24"
                  fill="#FFFFFF"
                  width="24"
                  height="24"
                >
                  <path
                    clip-rule="evenodd"
                    d="M12 14a3 3 0 0 1 3-3h4a2 2 0 0 1 2 2v2a2 2 0 0 1-2 2h-4a3 3 0 0 1-3-3Zm3-1a1 1 0 1 0 0 2h4v-2h-4Z"
                    fill-rule="evenodd"
                  ></path>
                  <path
                    clip-rule="evenodd"
                    d="M12.293 3.293a1 1 0 0 1 1.414 0L16.414 6h-2.828l-1.293-1.293a1 1 0 0 1 0-1.414ZM12.414 6 9.707 3.293a1 1 0 0 0-1.414 0L5.586 6h6.828ZM4.586 7l-.056.055A2 2 0 0 0 3 9v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2h-4a5 5 0 0 1 0-10h4a2 2 0 0 0-1.53-1.945L17.414 7H4.586Z"
                    fill-rule="evenodd"
                  ></path>
                </svg>

                <span class="text">Edit Database</span>
              </a>
            </button>
            <button class="btn edit-botton">
              <a href="/HTML/generate_timetable.html">
                <svg
                  height="24"
                  width="24"
                  fill="#FFFFFF"
                  viewBox="0 0 24 24"
                  data-name="Layer 1"
                  id="Layer_1"
                  class="sparkle"
                >
                  <path d="M10,21.236,6.755,14.745.264,11.5,6.755,8.255,10,1.764l3.245,6.491L19.736,11.5l-6.491,3.245ZM18,21l1.5,3L21,21l3-1.5L21,18l-1.5-3L18,18l-3,1.5ZM19.333,4.667,20.5,7l1.167-2.333L24,3.5,21.667,2.333,20.5,0,19.333,2.333,17,3.5Z"></path>
                </svg>

                <span class="text">Generate</span>
              </a>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
