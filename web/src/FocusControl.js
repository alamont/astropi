import React, { Component } from "react";

class FocusControl extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        Focus
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
    }
    const {
      keymap = defaultKeymap
    } = this.props;

    if (event.key === keymap.dirLeft) {
      this.setStepLeft();
    } else if (event.key === keymap.dirRight) {
      this.setStepRight();
    }
  };


  setStepLeft = () => {
    this.props.socket.emit("focus", {step: "left"});
  };

  setStepRight = () => {
    this.props.socket.emit("focus", {step: "right"});
  };
}

export default FocusControl;
