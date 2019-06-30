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
        {JSON.stringify(this.state)}
      </div>
    );
  }

  componentDidMount = () => {
    document.addEventListener("keydown", this.handleKeyDown.bind(this), false);
  };

  handleKeyDown = event => {
    const defaultKeymap = {
      dirLeft: "ArrowLeft",
      dirRight: "ArrowRight",
      enable: " ",
      speedUp: "ArrowUp",
      speedDown: "ArrowDown"
    }
    const {
      keymap = defaultKeymap
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
