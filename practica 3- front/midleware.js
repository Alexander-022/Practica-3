// AuthMiddleware.js
import React from 'react';
import { Navigate } from 'react-router-dom';
import Cookies from 'js-cookie';

const AuthMiddleware = ({ children }) => {
  const token = Cookies.get('token');

  if (!token) {
    // Si no hay token, redirigir a la página de sesión
    return <Navigate to="/session" />;
  }

  // Si hay token, renderizar el componente hijo
  return children;
};

export default AuthMiddleware;