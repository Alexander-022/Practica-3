'use client'

// Importar los módulos necesarios
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './dashboard.css';
import Cookies from 'js-cookie';

// Importar componentes de las páginas
import Listar from '../dashboard/productos/listar/page';
import ListarPAC from '../dashboard/productos/listarPAC/page';
import GuardarP from '../dashboard/productos/guardarP/page';

import Session from '../session/page';

// Componente Dashboard
function Dashboard() {
  const handleLogout = () => {
    Cookies.remove('token');
    window.location.href = '/session'; // Redirige a /session después de cerrar sesión
  };

  return (
    <div className="dashboard">
      <div className="sidebar">
        <div className="logo">
          <h2>Facturas</h2>
        </div>
        <nav className="nav-menu">
          <Link to="productos/listar" className="nav-item">Productos</Link>
          <Link to="productos/listarPAC" className="nav-item">Productos Al caducar</Link>
          <Link to="productos/guardarP" className="nav-item">Guardar Productos</Link>
         
        </nav>
      </div>
      <div className="content">
        <header className="header">
          <div className="header-left">
            <button>🌐 Español</button>
          </div>
          <div className="header-right">
            <span>Buenos días, Alexander</span>
            <div className="profile-icon">A</div>
            <button onClick={handleLogout} className="logout-button">Cerrar Sesión</button>
          </div>
        </header>
        <main className="main-content">
          <Routes>
            <Route path="productos/listar" element={<Listar />} />
            <Route path="productos/listarPAC" element={<ListarPAC />} />
            <Route path="productos/guardarP" element={<GuardarP />} />
           
            <Route path="*" element={<h2>Bienvenidos</h2>} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

// Componente principal App
export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/session" element={<Session />} />
        <Route path="/dashboard/*" element={<Dashboard />} />
      </Routes>
    </Router>
  );
}