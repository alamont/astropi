import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import MotorControl from './MotorControl.js'
import AltitudeControl from './AltitudeControl.js'

import io from "socket.io-client";

const socket = io("http://raspberrypi:8000");

socket.on("connect", () => {
  console.log("Socket.io Connected!");
});

socket.on("disconnect", () => {
  console.log("Socket.io Disconnected!");
});
class App extends Component {

  render() {

    return (
      <div className="App">
        {/* <MotorControl socket={socket}/> */}
        <AltitudeControl socket={socket}/>
      </div>
    );
  }
}

export default App;
