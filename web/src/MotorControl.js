import React, { Component } from "react";
import io from "socket.io-client";
import MotorControlButtons from "./MotorControlButtons.js";

const socket = io("http://raspberrypi:8000");

socket.on("connect", () => {
  console.log("Socket.io Connected!");
});

socket.on("disconnect", () => {
  console.log("Socket.io Disconnected!");
});

class MotorControl extends Component {
  constructor(props) {
    super(props);
    this.state = { motors: [
      {
        motorId: 0,
        speed: 1000,
        dir: 1,
        en: 1
      },
      {
        motorId: 1,
        speed: 1000,
        dir: 1,
        en: 1
      }
    ]};
  }

  render() {

    const motor1KeyMap = {
      dirLeft: "a",
      dirRight: "d",
      enable: "e",
      speedUp: "w",
      speedDown: "s"
    }

    return (
      <div>
        <MotorControlButtons 
          motorId={0} 
          setDirection={this.setDirection(0).bind(this)}
          increaseSpeed={this.increaseSpeed(0).bind(this)}
          decraseSpeed={this.decraseSpeed(0).bind(this)}
          toggleEnable={this.toggleEnable(0).bind(this)}
          motorState={this.state.motors[0]}/>
        <MotorControlButtons 
          motorId={1} 
          setDirection={this.setDirection(1).bind(this)}
          increaseSpeed={this.increaseSpeed(1).bind(this)}
          decraseSpeed={this.decraseSpeed(1).bind(this)}
          toggleEnable={this.toggleEnable(1).bind(this)}
          motorState={this.state.motors[1]}
          keymap={motor1KeyMap}/>
      </div>
    );
  }

  componentWillUnmount() {
    document.removeEventListener(
      "keydown",
      this.handleKeyDown.bind(this),
      false
    );
  }

  setMotorState = (motorId, key, value) => {
    const motors = this.state.motors.slice();
    motors[motorId][key] = value;
    this.setState({ motors });
  };

  setDirection = motorId => dir => e => {
    this.setMotorState(motorId, "dir", dir);
    socket.emit("motor", {motorId, dir});
  };

  toggleEnable = motorId => () => {
    console.log("toggleEnable");
    const enable = !this.state.motors[motorId].enable;
    this.setMotorState(motorId, "enable", enable);
    socket.emit("motor", {motorId, enable})

  };

  setSpeed = motorId => speed => {
    this.setMotorState(motorId, "speed", speed);
    socket.emit("motor", {motorId, speed})
  };

  increaseSpeed = motorId => () => {
    const speed = this.state.motors[motorId].speed + 100;
    this.setSpeed(motorId)(speed);
  };

  decraseSpeed = motorId => () => {
    const speed = this.state.motors[motorId].speed - 100;
    this.setSpeed(motorId)(speed);
  };
}

export default MotorControl;
