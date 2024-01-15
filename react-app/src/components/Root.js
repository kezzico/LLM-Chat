import React from 'react';
import { Outlet } from "react-router-dom";
import './Root.css'

function Root() {
  return (
    <>
      <Outlet />
    </>
  );
}

export default Root;
