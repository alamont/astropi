import React, { Component } from "react";
import io from "socket.io-client";
// const socket = io("http://raspberrypi:8000");
// const socket = io("http://192.168.2.22:8000");
const socket = io("http://raspberrypi:8000");

socket.on("connect", () => {
  console.log("Socket.io Connected!");
});

socket.on("disconnect", () => {
  console.log("Socket.io Disconnected!");
});


class MotorControls extends Component {
  constructor(props) {
    super(props);
    this.state = { enable: 0, speed: 1000, dir: 0 };
  }

  render() {
    let stateRows = Object.keys(this.state).map(k => (
      <tr>
        <td>{k}</td>
        <td>{this.state[k]}</td>
      </tr>
    ));

    let stateTable = (
      <table>
        <thead>
          <tr>
            <th>Control</th>
            <th>Value</th>
          </tr>
        </thead>
        {stateRows}
      </table>
    );

    return (
      <div>
        <p>Motor Controls</p>
        <div>
          <button onClick={this.setDirection(0)}>CW</button>
          <button onClick={this.setDirection(1)}>CCW</button>
          <button onClick={this.increaseSpeed}>Speed+</button>
          <button onClick={this.decraseSpeed}>Speed-</button>
          <button onClick={this.toggleEnable}>Enable/Disable</button>
        </div>
        {stateTable}
      </div>
    );
  }

  componentDidMount() {
    document.addEventListener("keydown", this.handleKeyDown.bind(this), false);
    
    socket.on("direction", data => {
      console.log("direction", data);
      this.setState({dir: data})
    });
    socket.on("speed", data => this.setState({speed: data}));
    socket.on("enable", data => this.setState({enable: data}));
  }

  componentWillUnmount() {
    document.removeEventListener(
      "keydown",
      this.handleKeyDown.bind(this),
      false
    );
  }

  setDirection = dir => e => {
    this.setState({ dir: dir });
    socket.emit("direction", dir);
  };

  toggleEnable = () => {
    console.log("toggleEnable");
    this.setState({ enable: + !this.state.enable });
    socket.emit("enable", this.state.enable);
  };

  setSpeed = speed => {
    socket.emit("speed", speed);
  };

  increaseSpeed = e => {
    this.setState({ speed: this.state.speed - 10 });
    this.setSpeed(this.state.speed);
  };

  decraseSpeed = e => {
    this.setState({ speed: this.state.speed + 10 });
    this.setSpeed(this.state.speed);
  };

  handleKeyDown = event => {
    if (event.key === "ArrowLeft") {
      this.setDirection(0)();
    } else if (event.key === "ArrowRight") {
      this.setDirection(1)();
    } else if (event.code === "Space") {
      this.toggleEnable();
    } else if (event.key === "ArrowUp") {
      this.increaseSpeed();
    } else if (event.key === "ArrowDown") {
      this.decraseSpeed();
    }
  };
}

export default MotorControls;
