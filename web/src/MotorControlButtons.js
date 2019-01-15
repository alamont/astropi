import React, { Component } from "react";

class MotorControlButtons extends Component {

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
      keymap = defaultKeymap, 
      setDirection,
      toggleEnable,
      increaseSpeed,
      decraseSpeed
    } = this.props;

    if (event.key === keymap.dirLeft) {
      setDirection(0)();
    } else if (event.key === keymap.dirRight) {
      setDirection(1)();
    } else if (event.key === keymap.enable) {
      toggleEnable();
    } else if (event.key === keymap.speedUp) {
      increaseSpeed();
    } else if (event.key === keymap.speedDown) {
      decraseSpeed();
    }
  };

  render () {
    const {
      motorId, 
      motorState,
      setDirection,
      toggleEnable,
      increaseSpeed,
      decraseSpeed
    } = this.props;
    return (
      <div>
        <p>Motor Controls Motor {motorId}</p>
        {JSON.stringify(motorState)}
        <div>
          <button onClick={setDirection(0)}>CW</button>
          <button onClick={setDirection(1)}>CCW</button>
          <button onClick={increaseSpeed}>Speed+</button>
          <button onClick={decraseSpeed}>Speed-</button>
          <button onClick={toggleEnable}>Enable/Disable</button>
        </div>
        {/* {stateTable} */}
      </div>
    )
  }

}

MotorControlButtons.componentDidMount = () => {
  document.addEventListener("keydown", this.handleKeyDown.bind(this), false);
};

export default MotorControlButtons;