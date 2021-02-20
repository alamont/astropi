import React, { Component } from "react";

class FocusControl extends Component {
  constructor(props) {
    super(props);
    this.state = { focus: { 
      speed: 100      
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
      dirLeft: "z",
      dirRight: "x", 
      speedUp: "v",
      speedDown: "c" 
    }
    const {
      keymap = defaultKeymap
    } = this.props;

    if (event.key === keymap.dirLeft) {
      this.setStepLeft();
    } else if (event.key === keymap.dirRight) {
      this.setStepRight();
    } else if (event.key === keymap.speedUp) {
      this.speedUp();
    } else if (event.key === keymap.speedDown) {
      this.speedDown();
    }
  };


  setStepLeft = () => {
    this.props.socket.emit("focus", {step: "left"});
  };

  setStepRight = () => {
    this.props.socket.emit("focus", {step: "right"});
  };

  speedUp = () => {
    this.state.focus.speed = this.state.focus.speed + 100;
    this.props.socket.emit("focus", {speed: this.state.focus.speed});
  }

  speedDown = () => {
    this.state.focus.speed = this.state.focus.speed - 100;
    this.props.socket.emit("focus", {speed: this.state.focus.speed});
  }
}

export default FocusControl;
