import { Routes, Route } from "react-router-dom";
import Cameras from "../pages/Cameras";
import Tickets from "../pages/Tickets";
import Dashboard from "../pages/Dashboard";

export default function AppRouter() {
  return (
    <Routes>
      <Route path="/" element={<Dashboard />} />
      <Route path="/cameras" element={<Cameras />} />
      <Route path="/tickets" element={<Tickets />} />
    </Routes>
  );
}
