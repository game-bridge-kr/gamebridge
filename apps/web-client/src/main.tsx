import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom"
import './index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <BrowserRouter>
      <div className='container'>
        <Routes>
          <Route path='/' element={<App />} />
        </Routes>
      </div>
    </BrowserRouter>
  </React.StrictMode>,
)
