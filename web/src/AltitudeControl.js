import React, { Component } from "react";

class AltitudeControl extends Component {
  constructor(props) {
    super(props);
    this.state = { altitude: { 
        speed: 1000,
        dir: 1,
        en: 1
      }};
  }

  render() {
    return (
      <div>
        <h3>Altitude</h3>
        <h4>Controls</h4>
          {JSON.stringify(this.defaultKeymap)}
        <h4>State</h4>
        {JSON.stringify(this.state)}
      </div>
    );
  }

  componentDidMount = () => {
    document.addEventListener("keydown", this.handleKeyDown.bind(this), false);
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
    const speed = this.state.altitude.speed + 100;
    this.setSpeed(speed);
  };

  decraseSpeed = () => {
    const speed = this.state.altitude.speed - 100;
    this.setSpeed(speed);
  };
}

export default AltitudeControl;
