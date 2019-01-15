import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import MotorControl from './MotorControl.js'
class App extends Component {

  render() {

    return (
      <div className="App">
        <MotorControl/>
      </div>
    );
  }
}

export default App;
