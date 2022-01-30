import './App.css';
import {Home} from './Home';
import {Employee} from './Employee';
import {Jobs} from './Jobs';
import {BrowserRouter, Route, Routes, NavLink} from 'react-router-dom';



function App() {
  return (
  <BrowserRouter>
    <div className="App">
      <h3 className='d-flex justify-content-center m-3'>
        react
      </h3>
      <nav className='navbar navbar-expand-sm justify-content-center bg-light navbar-dark'>
        <ul className='navbar-nav'>
          <li className='nav-item m-1'>
            <NavLink className='btn btn-light btn-outline-primary' to="/home">
              Home
            </NavLink>
          </li>

          <li className='nav-item m-1'>
            <NavLink className='btn btn-light btn-outline-primary' to="/job">
              Jobs
            </NavLink>
          </li>

          <li className='nav-item m-1'>
            <NavLink className='btn btn-light btn-outline-primary' to="/employee">
              Employees
            </NavLink>
          </li>
        </ul>
      </nav>
      <Routes>
          <Route path="/home" element={<Home />}></Route>
          <Route path="/job" element={<Jobs />}></Route>
          <Route path="/employee" element={<Employee />}></Route>
      </Routes>
    </div>
    </BrowserRouter>
  );
}

export default App;
