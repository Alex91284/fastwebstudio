import { BrowserRouter, Routes, Route } from "react-router-dom"

import Home from "../pages/Home"
import Login from "../pages/Login"
import Dashboard from "../pages/Dashboard"
import AdminPanel from "../pages/AdminPanel"; // <-- si no existe, créala
import Unauthorized from "../pages/Unauthorized"; // <-- opcional
// import Register from "../pages/Register"
// import NotFound from "../pages/NotFound"

import ProtectedRoute from "../components/ProtectedRoute";
import AdminRoute from "../components/AdminRoute";

export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Rutas Publicas */}
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        {/* <Route path="/register" element={<Register />} /> */}

        {/* Rutas Protegidas */}
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>} />
        
        {/* Protegidas (requieren rol "admin") */}
        <Route
          path="/admin"
          element={
            <AdminRoute>
              <AdminPanel />
            </AdminRoute>} />
        
        {/* Ruta para denegar acceso */}
        <Route path="/unauthorized" element={<Unauthorized />} />

        {/* Otras rutas (404) */}
        {/* <Route path="*" element={<NotFound />} /> */}
      </Routes>
    </BrowserRouter>
  )
}