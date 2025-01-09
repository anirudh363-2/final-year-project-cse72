import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import "./App.css";
import Home from "./pages/Home";
import Data from "./pages/Data";
import Generate from "./pages/Generate";
import Courses from "./pages/Courses";
import Rooms from "./pages/Rooms";
import Faculty from "./pages/Faculty";
import OtherDetails from "./pages/OtherDetails";
import Students from "./pages/Students";
import Timetables from "./pages/Timetables";
import Methods from "./pages/Methods";


function App() {

  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/data" element={<Data />} />
          <Route path="/generate" element={<Generate />} />
          <Route path="/courses" element={<Courses /> } />
          <Route path="/rooms" element={<Rooms />} />
          <Route path="/faculty" element={<Faculty />} />
          <Route path="/other-details" element={<OtherDetails />} />
          <Route path="/students" element={<Students />} />
          <Route path="/timetables" element={<Timetables />} />
          <Route path="/methods/:id" element={<Methods />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
