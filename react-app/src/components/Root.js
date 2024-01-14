import React from 'react';
import { Outlet } from "react-router-dom";
import './Root.css'
function Root() {
  return (
    <header>
        <h1> CHAT </h1>
        <Outlet />
    </header>
);
}

export default Root;
