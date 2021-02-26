/* eslint no-undef: 0 */

import React, { Component } from "react";
import 'joypad.js'; 

class AltitudeControl extends Component {
  constructor(props) {
    super(props);
    this.state = { altitude: { 
        speed: 1000,
        dir: 1,
        en: 0
      }};
  }

  render() {
    return (
      <div>
        <h2>Altitude</h2>
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
      if (buttonName === "button_3") {
        this.toggleDirection();
      } else if (buttonName === "button_0") {
        this.toggleEnable();
      } else if (buttonName === "button_1") {
        this.increaseSpeed();
      } else if (buttonName === "button_2") {
        this.decraseSpeed();
      }
    });
  };

  defaultKeymap = {
    dirLeft: "ArrowLeft",
    dirRight: "ArrowRight",
    enable: " ",
    speedUp: "ArrowUp",
    speedDown: "ArrowDown"
  }

  handleKeyDown = event => {
    // const defaultKeymap = {
    //   dirLeft: "ArrowLeft",
    //   dirRight: "ArrowRight",
    //   enable: " ",
    //   speedUp: "ArrowUp",
    //   speedDown: "ArrowDown"
    // }
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

  setAltitudeState = (key, value) => {
    console.log(this.state);
    // const altitude = this.state.altitude.slice();
    const altitude = Object.assign(this.state.altitude);
    altitude[key] = value;
    this.setState({ altitude });
  };

  setDirection = dir => e => {
    this.setAltitudeState("dir", dir);
    this.props.socket.emit("altitude", {dir});
  };

  toggleDirection = () => {
    const dir = 1 - this.state.altitude.dir;
    this.setAltitudeState("dir", dir)
    this.props.socket.emit("altitude", {dir})
  }

  toggleEnable = () => {
    console.log("toggleEnable");
    const enable = !this.state.altitude.enable;
    this.setAltitudeState("enable", enable);
    this.props.socket.emit("altitude", {enable})

  };

  setSpeed = speed => {
    this.setAltitudeState("speed", speed);
    this.props.socket.emit("altitude", {speed})
  };

  increaseSpeed = () => {
    const speed = this.state.altitude.speed + 25;
    this.setSpeed(speed);
  };

  decraseSpeed = () => {
    let speed = this.state.altitude.speed - 25;
    if (speed < 1) {
      speed = 1;
    }
    this.setSpeed(speed);
  };
}

export default AltitudeControl;
