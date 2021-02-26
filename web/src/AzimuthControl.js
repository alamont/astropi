/* eslint no-undef: 0 */

import React, { Component } from "react";
import 'joypad.js'; 

class AzimuthControl extends Component {
  constructor(props) {
    super(props);
    this.state = { azimuth: { 
        speed: 1000,
        dir: 1,
        en: 0
      }};
  }

  render() {
    return (
      <div>
        <h2>Azimuth</h2>
        <h4>Controls</h4>
          <pre>
            {JSON.stringify(this.defaultKeymap, null, 2)}
          </pre>
        <h4>State</h4>
          <pre>
            {JSON.stringify(this.state, null, 2)}
          </pre>
      </div>
    );
  }

  componentDidMount = () => {
    document.addEventListener("keydown", this.handleKeyDown.bind(this), false);
    joypad.on('button_press', e => {
      const { buttonName } = e.detail; 
      console.log(`${buttonName} was pressed!`);
      if (buttonName === "button_12") {
        this.toggleDirection();
      } else if (buttonName === "button_13") {
        this.toggleEnable();
      } else if (buttonName === "button_15") {
        this.increaseSpeed();
      } else if (buttonName === "button_14") {
        this.decraseSpeed();
      }
    });
  };

  defaultKeymap = {
    dirLeft: "a",
    dirRight: "d",
    enable: "q",
    speedUp: "w",
    speedDown: "s"
  }

  handleKeyDown = event => {
    const {
      keymap = this.defaultKeymap
    } = this.props;

    if (event.key === keymap.dirLeft) {
      this.setDirection(0)();
    } else if (event.key === keymap.dirRight) {
      this.setDirection(1)();
    } else if (event.key === keymap.enable) {
      this.toggleEnable();
    } else if (event.key === keymap.speedUp) {
      this.increaseSpeed();
    } else if (event.key === keymap.speedDown) {
      this.decraseSpeed();
    }
  };

  setAzimuthState = (key, value) => {
    console.log(this.state);
    // const azimuth = this.state.azimuth.slice();
    const azimuth = Object.assign(this.state.azimuth);
    azimuth[key] = value;
    this.setState({ azimuth });
  };

  setDirection = dir => e => {
    this.setAzimuthState("dir", dir);
    this.props.socket.emit("azimuth", {dir});
  };

  toggleDirection = () => {
    const dir = 1 - this.state.azimuth.dir;
    this.setAzimuthState("dir", dir)
    this.props.socket.emit("azimuth", {dir})
  }

  toggleEnable = () => {
    console.log("toggleEnable");
    const enable = !this.state.azimuth.enable;
    this.setAzimuthState("enable", enable);
    this.props.socket.emit("azimuth", {enable})

  };

  setSpeed = speed => {
    this.setAzimuthState("speed", speed);
    this.props.socket.emit("azimuth", {speed})
  };

  increaseSpeed = () => {
    const speed = this.state.azimuth.speed + 25;
    this.setSpeed(speed);
  };

  decraseSpeed = () => {
    let speed = this.state.azimuth.speed - 25;
    if (speed < 1) {
      speed = 1;
    }
    this.setSpeed(speed);
  };
}

export default AzimuthControl;
