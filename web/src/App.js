import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import MotorControls from './motorControls.js'

class App extends Component {
  render() {
    return (
      <div className="App">
        <MotorControls/>
      </div>
    );
  }
}

export default App;
