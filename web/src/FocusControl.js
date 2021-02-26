/* eslint no-undef: 0 */

import React, { Component } from "react";
import 'joypad.js'; 

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
        <h2>Focus</h2>
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
      if (buttonName === "button_4") {
        this.setStepLeft();
      } else if (buttonName === "button_5") {
        this.setStepRight();
      } else if (buttonName === "button_9") {
        this.speedUp();
      } else if (buttonName === "button_8") {
        this.speedDown();
      }
    });
  };

  defaultKeymap = {
    dirLeft: "z",
    dirRight: "x", 
    speedUp: "v",
    speedDown: "c" 
  }

  handleKeyDown = event => {
    const {
      keymap = this. defaultKeymap
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
    this.state.focus.speed = this.state.focus.speed + 50;
    this.props.socket.emit("focus", {speed: this.state.focus.speed});
  }

  speedDown = () => {
    this.state.focus.speed = this.state.focus.speed - 50;
    if (this.state.focus.speed < 1) {
      this.state.focus.speed = 1;
    }
    this.props.socket.emit("focus", {speed: this.state.focus.speed});
  }
}

export default FocusControl;
